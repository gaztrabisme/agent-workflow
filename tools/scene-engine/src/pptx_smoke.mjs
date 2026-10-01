import fs from 'node:fs';
import path from 'node:path';
import { homedir } from 'node:os';
import { pathToFileURL } from 'node:url';
import { spawnSync, execFileSync } from 'node:child_process';

const KEYNOTE_OWNER_CHECK = 'owner-check: grant Automation permission (Terminal/Codex → Keynote) and rerun npm run selftest -- --case AT36';

function appleScriptString(value) {
  return String(value).replaceAll('\\', '\\\\').replaceAll('"', '\\"');
}

function runningKeynotePids() {
  const result = spawnSync('pgrep', ['-x', 'Keynote'], { encoding: 'utf8' });
  if (result.error) throw result.error;
  if (result.status === 1) return [];
  if (result.status !== 0) throw new Error(`Could not inspect Keynote processes: ${(result.stderr || '').trim()}`);
  return result.stdout.trim().split(/\s+/).filter(Boolean).map(Number);
}

async function launchKeynote(existingPids) {
  const candidates = [
    '/Applications/Keynote.app/Contents/MacOS/Keynote',
    '/System/Applications/iWork/Keynote.app/Contents/MacOS/Keynote',
    path.join(homedir(), 'Applications/Keynote.app/Contents/MacOS/Keynote')
  ];
  const executable = candidates.find((candidate) => fs.existsSync(candidate));
  if (!executable) throw new Error('Keynote application executable was not found.');
  const application = path.resolve(path.dirname(executable), '../..');
  try {
    execFileSync('/usr/bin/open', ['-a', application], { encoding: 'utf8', timeout: 10000, maxBuffer: 1024 * 1024 });
  } catch (error) {
    throw new Error(`Could not launch Keynote: ${(error.stderr || error.stdout || error.message).toString().trim()}`);
  }
  const baseline = new Set(existingPids);
  const deadline = Date.now() + 10000;
  while (Date.now() < deadline) {
    const launched = runningKeynotePids().filter((pid) => !baseline.has(pid));
    if (launched.length) return launched;
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  throw new Error('Keynote was launched but its process did not appear.');
}

async function waitForKeynoteExit(pids, timeoutMs) {
  const deadline = Date.now() + timeoutMs;
  while (Date.now() < deadline) {
    const current = new Set(runningKeynotePids());
    if (pids.every((pid) => !current.has(pid))) return true;
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
  const current = new Set(runningKeynotePids());
  return pids.every((pid) => !current.has(pid));
}

function signalTrackedKeynotePids(pids, signal) {
  const current = new Set(runningKeynotePids());
  for (const pid of pids) {
    if (!current.has(pid)) continue;
    try { process.kill(pid, signal); }
    catch (error) { if (error.code !== 'ESRCH') throw error; }
  }
}

async function quitTrackedKeynote(pids) {
  if (pids.length === 0) return;
  try {
    execFileSync('osascript', ['-e', 'tell application id "com.apple.iWork.Keynote" to quit'], {
      encoding: 'utf8', timeout: 3000, maxBuffer: 1024 * 1024
    });
  } catch { }
  if (await waitForKeynoteExit(pids, 1000)) return;
  signalTrackedKeynotePids(pids, 'SIGTERM');
  if (await waitForKeynoteExit(pids, 5000)) return;
  signalTrackedKeynotePids(pids, 'SIGKILL');
  if (!await waitForKeynoteExit(pids, 3000)) throw new Error(`Could not stop test-launched Keynote process(es): ${pids.join(', ')}.`);
}

function probeKeynoteAutomation() {
  try {
    const output = execFileSync('osascript', ['-e', 'tell application id "com.apple.iWork.Keynote" to count of documents'], {
      encoding: 'utf8', timeout: 10000, maxBuffer: 1024 * 1024
    });
    if (!output.trim()) throw new Error('Keynote automation probe returned no document count.');
    return { status: 'pass', documentCount: Number(output.trim()) };
  } catch (error) {
    const detail = (error.stderr || error.stdout || error.message).toString().trim();
    if (error.code === 'ETIMEDOUT' || /Not authorized to send Apple events/i.test(detail)) {
      return { status: 'owner-check', manualSteps: [KEYNOTE_OWNER_CHECK], reason: detail || 'Keynote automation probe timed out after 10 seconds.' };
    }
    throw new Error(`Keynote automation probe failed: ${detail}`);
  }
}

export async function exportWithKeynote(inputPptx, outputPdf) {
  fs.mkdirSync(path.dirname(outputPdf), { recursive: true });
  fs.rmSync(outputPdf, { force: true });
  const existingPids = runningKeynotePids();
  const ownedPids = [];
  try {
    if (existingPids.length === 0) ownedPids.push(...await launchKeynote(existingPids));
    const probe = probeKeynoteAutomation();
    if (probe.status === 'owner-check') return probe;

    const source = appleScriptString(path.resolve(inputPptx));
    const destination = appleScriptString(path.resolve(outputPdf));
    const script = [
      'tell application id "com.apple.iWork.Keynote"',
      `set sceneEngineDocument to open POSIX file "${source}"`,
      'set sceneEngineSlideCount to 0',
      'with timeout of 100 seconds',
      'repeat 60 times',
      'try',
      'set sceneEngineSlideCount to count of slides of sceneEngineDocument',
      'if sceneEngineSlideCount > 0 then exit repeat',
      'end try',
      'delay 1',
      'end repeat',
      'end timeout',
      'if sceneEngineSlideCount = 0 then error "Keynote import did not produce any slides."',
      `export sceneEngineDocument to POSIX file "${destination}" as PDF`,
      'close sceneEngineDocument saving no',
      'end tell'
    ].join('\n');
    let output = '';
    try {
      output = execFileSync('osascript', ['-e', script], { encoding: 'utf8', timeout: 120000, maxBuffer: 2 * 1024 * 1024 });
    } catch (error) {
      throw new Error(`Keynote import/PDF export failed: ${(error.stderr || error.stdout || error.message).toString().trim()}`);
    }
    if (!fs.existsSync(outputPdf) || fs.statSync(outputPdf).size === 0) throw new Error('Keynote returned without creating a non-empty PDF.');
    return { status: 'pass', pdf: path.resolve(outputPdf), warnings: output.trim() ? [output.trim()] : [] };
  } finally {
    if (existingPids.length === 0) {
      const owned = new Set(ownedPids);
      for (const pid of runningKeynotePids()) if (!existingPids.includes(pid)) owned.add(pid);
      await quitTrackedKeynote([...owned]);
    }
  }
}

export function renderWithLibreOffice(inputPptx, outputPdf, { soffice = process.env.SCENE_ENGINE_SOFFICE || 'soffice' } = {}) {
  fs.mkdirSync(path.dirname(outputPdf), { recursive: true });
  fs.rmSync(outputPdf, { force: true });
  const profile = path.join(path.dirname(outputPdf), `.lo-profile-${process.pid}-${Date.now()}`);
  const args = [`-env:UserInstallation=${pathToFileURL(profile).href}`, '--headless', '--convert-to', 'pdf:impress_pdf_Export', '--outdir', path.dirname(path.resolve(outputPdf)), path.resolve(inputPptx)];
  let output = '';
  try {
    output = execFileSync(soffice, args, { encoding: 'utf8', timeout: 120000, maxBuffer: 2 * 1024 * 1024 });
  } catch (error) {
    throw new Error(`LibreOffice PDF render failed: ${(error.stderr || error.stdout || error.message).toString().trim()}`);
  } finally {
    fs.rmSync(profile, { recursive: true, force: true });
  }
  const generated = path.join(path.dirname(path.resolve(outputPdf)), `${path.parse(inputPptx).name}.pdf`);
  if (generated !== path.resolve(outputPdf) && fs.existsSync(generated)) fs.renameSync(generated, outputPdf);
  if (!fs.existsSync(outputPdf) || fs.statSync(outputPdf).size === 0) throw new Error('LibreOffice returned without creating a non-empty PDF.');
  return { status: 'pass', pdf: path.resolve(outputPdf), output: output.trim() };
}
