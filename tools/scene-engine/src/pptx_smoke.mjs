import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';

function appleScriptString(value) {
  return String(value).replaceAll('\\', '\\\\').replaceAll('"', '\\"');
}

export function exportWithKeynote(inputPptx, outputPdf) {
  fs.mkdirSync(path.dirname(outputPdf), { recursive: true });
  fs.rmSync(outputPdf, { force: true });
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
