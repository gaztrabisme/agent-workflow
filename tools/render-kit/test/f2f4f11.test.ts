import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { report, rk, temp } from './helpers.ts';

test('F2 an expected failed request matches URL pattern and status only', { timeout: 90000 }, async () => {
  const d=await temp(),page=join(d,'error.html');
  await writeFile(page,'<!doctype html><html><body><main>Missing record</main><script>fetch("/missing.json").catch(()=>{});</script></body></html>');
  const expected=await report(['check',page,'--checks','resources','--expect-request','*/missing.json=404','--out-dir',join(d,'expected')]);
  assert.equal(expected.code,0,expected.stderr);assert.equal(expected.data.checks[0].status,'pass');
  assert.deepEqual(expected.data.checks[0].items.map((item:any)=>item.status),['expected']);
  assert.equal(expected.data.checks[0].items[0].expected_status,404);
  const wrongStatus=await report(['check',page,'--checks','resources','--expect-request','*/missing.json=503','--out-dir',join(d,'wrong-status')]);
  assert.equal(wrongStatus.code,1,wrongStatus.stderr);assert.equal(wrongStatus.data.checks[0].items[0].status,'unexpected');
  const wrongPattern=await report(['check',page,'--checks','resources','--expect-request','*/other.json=404','--out-dir',join(d,'wrong-pattern')]);
  assert.equal(wrongPattern.code,1,wrongPattern.stderr);
  assert.equal((await rk(['check',page,'--expect-request','missing-status'])).code,2);
});

test('F4 visual checks skip closed details, offscreen skip links, and visually hidden text while retaining scroll content', { timeout: 90000 }, async () => {
  const d=await temp(),page=join(d,'visibility.html');
  await writeFile(page,`<!doctype html><html><head><style>
    .skip{position:absolute;left:-10000px;top:0}.skip:focus{left:0}
    .modern{position:absolute;width:1px;height:1px;clip-path:inset(50%);overflow:hidden}
    .legacy{position:absolute;width:1px;height:1px;clip:rect(0,0,0,0);overflow:hidden;white-space:nowrap}
    .scroll{width:250px;overflow-x:auto}.wide{width:900px;white-space:nowrap}
  </style></head><body>
    <a class="skip" href="#main" style="font-family:'Render Kit Hidden Missing Font'">Skip navigation</a>
    <h2 class="modern" style="font-family:'Render Kit Hidden Missing Font'">Visually hidden heading</h2>
    <span class="legacy" style="font-family:'Render Kit Hidden Missing Font'">Visually hidden status</span>
    <details><summary>Options</summary><p style="font-family:'Render Kit Hidden Missing Font'">Closed details content</p></details>
    <div class="scroll"><p class="wide">A wide table cell with enough content to extend well past its horizontal scroll area</p></div>
    <main id="main">Visible content</main>
  </body></html>`);
  const result=await report(['check',page,'--width','400','--checks','fonts,overflow,collision','--out-dir',join(d,'checked')]);
  assert.equal(result.code,0,result.stderr);assert.deepEqual(result.data.checks.map((check:any)=>check.status),['pass','pass','pass']);
});

test('F11 and F12 one brief includes labelled states and per-state answer slots', { timeout: 120000 }, async () => {
  const d=await temp(),out=join(d,'review'),questions=join(d,'questions.md'),ready=join(d,'ready.html'),empty=join(d,'empty.html');
  await mkdir(out,{recursive:true});
  await writeFile(questions,'# State clarity\n- Is the state clear?\n- Is the content complete?\n');
  await writeFile(ready,'<!doctype html><html><body><main><h1>Ready</h1></main></body></html>');
  await writeFile(empty,'<!doctype html><html><body><main><h1>Nothing to review</h1></main></body></html>');
  const result=await rk(['brief','--state',`Ready=${ready}`,'--state',`Empty=${empty}`,'--questions',questions,'--out-dir',out,'--checks','resources,overflow']);
  assert.equal(result.code,0,result.stderr);
  const brief=await readFile(join(out,'brief.md'),'utf8');
  assert.match(brief,/### Ready/);assert.match(brief,/### Empty/);assert.match(brief,/ready\.html/);assert.match(brief,/empty\.html/);
  assert.doesNotMatch(brief,/PDF and page images show the print output/);
  const template=JSON.parse(await readFile(join(out,'answers.template.json'),'utf8'));
  assert.deepEqual(template.answers.map((answer:any)=>[answer.id,answer.state]),[
    ['Q1','Ready'],['Q2','Ready'],['Q1','Empty'],['Q2','Empty']
  ]);
  for(const folder of ['state-1-ready','state-2-empty']){
    assert.ok(await readFile(join(out,folder,'render.png')));
    assert.ok(await readFile(join(out,folder,'report.json')));
  }
  assert.deepEqual(JSON.parse(result.stdout).states.map((state:any)=>state.label),['Ready','Empty']);

  const answers=template.answers.map((answer:any)=>({...answer,answer:'yes',where:'main content',reason:'The reviewed content is clear.'}));
  const answersPath=join(out,'answers.json');
  await writeFile(answersPath,JSON.stringify({reviewer:'reviewer',answers}));
  assert.equal((await rk(['brief','--verify',answersPath])).code,0);

  answers[3].answer='no';
  await writeFile(answersPath,JSON.stringify({reviewer:'reviewer',answers}));
  const no=await rk(['brief','--verify',answersPath]);
  assert.equal(no.code,1,`${no.stderr}${no.stdout}`);assert.match(no.stdout,/Empty/);assert.match(no.stdout,/Q2/);

  await writeFile(answersPath,JSON.stringify({reviewer:'reviewer',answers:answers.slice(0,3)}));
  const missing=await rk(['brief','--verify',answersPath]);
  assert.equal(missing.code,2,missing.stderr);assert.match(missing.stdout,/state\/question/i);
});
