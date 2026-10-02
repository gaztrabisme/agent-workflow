import { resolve, extname, join } from 'node:path';
import { writeBrief, verifyAnswers } from './brief.ts';
import { runOptions, validateChecks } from './args.ts';
import { prepare, capture } from './render.ts';
import { checkInput } from './runner.ts';
import { selftest } from './selftest.ts';
import { textCommand } from './text-command.ts';
import { jsonWrite } from './util.ts';
import { renderPdfPages } from './pdf-pages.ts';

const visions=['protanopia','deuteranopia','tritanopia','achromatopsia'];
export async function renderCommand(input:string,v:Record<string,any>){
 if(!v.out)throw new Error('render requires --out');const format=extname(v.out).slice(1).toLowerCase();if(!['png','pdf'].includes(format))throw new Error('--out must end in .png or .pdf');
 const options=await runOptions(input,v),sim=String(v.simulate??'');if(sim&&!visions.includes(sim))throw new Error(`Unknown simulation: ${sim}`);if(sim&&format==='pdf')throw new Error('--simulate is refused for PDF output');options.simulate=sim||undefined;
 const session=await prepare(options);try{const size=await capture(session,options,resolve(v.out),format);return {value:{out:resolve(v.out),format,width:size.width,height:size.height,scale:options.scale,at_ms:options.at==='end'?options.settle:options.at,browser:{version:session.browser.version(),mode:'new-headless'},requests_blocked:session.blocked},code:0};}finally{await session.stop();}
}

export async function checkCommand(input:string,v:Record<string,any>){
 if(v.simulate)throw new Error('--simulate is not a check option');const options=await runOptions(input,v,!!v.pdf);validateChecks(options.checks);
 const {report,dir}=await checkInput(options);return {value:report,code:(await import('./report.ts')).checkExit(report.checks,options.strict),dir};
}

export async function briefCommand(input:string|undefined,v:Record<string,any>){
 if(v.verify){const {value,code}=await verifyAnswers(resolve(v.verify),!!v.strict);return {value,code};}
 if(!v.questions||!v['out-dir'])throw new Error('brief requires --questions and --out-dir');
 const declared=v.state===undefined?[]:Array.isArray(v.state)?v.state:[v.state];
 if(input&&declared.length)throw new Error('Use either <input> or --state, not both');
 if(!input&&!declared.length)throw new Error('brief requires <input> or at least one --state <label>=<input>');
 const states=declared.length?declared.map((entry:string)=>{const split=entry.indexOf('=');if(split<1||split===entry.length-1)throw new Error(`Invalid --state: ${entry} (expected <label>=<input>)`);return {label:entry.slice(0,split).trim(),input:entry.slice(split+1)};}):[{label:'Artifact',input:input!}];
 if(states.some(state=>!state.label||!state.input))throw new Error('--state labels and inputs must not be empty');
 if(new Set(states.map(state=>state.label.toLowerCase())).size!==states.length)throw new Error('--state labels must be unique');
 const simulations=String(v.simulate??'').split(',').filter(Boolean);for(const t of simulations)if(!visions.includes(t))throw new Error(`Unknown simulation: ${t}`);
 const dir=resolve(v['out-dir']),labelled=declared.length>0,reviews=[];
 for(let i=0;i<states.length;i++){
  const state=states[i],options=await runOptions(state.input,v,!!v.pdf);validateChecks(options.checks);
  const slug=state.label.toLowerCase().replace(/[^a-z0-9]+/g,'-').replace(/^-|-$/g,'')||'state';
  const stateDir=labelled?join(dir,`state-${i+1}-${slug}`):dir;options.outDir=stateDir;options.simulate=undefined;
  const {report}=await checkInput(options);
  for(const type of simulations){const session=await prepare({...options,simulate:type});try{await capture(session,{...options,simulate:type},join(stateDir,`render-${type}.png`),'png');}finally{await session.stop();}}
  const pdfPages=options.pdf?await renderPdfPages(join(stateDir,'render.pdf'),stateDir):[];
  const files=['render.png',...simulations.map(type=>`render-${type}.png`),...(options.pdf?['render.pdf',...pdfPages]:[])].map(file=>labelled?`${stateDir.slice(dir.length+1)}/${file}`:file);
  reviews.push({label:state.label,input:state.input,report,files});
 }
 const written=await writeBrief(dir,resolve(v.questions),String(v.purpose??''),reviews);return {value:{out_dir:dir,images:written.images,questions:written.questions.length,states:reviews.map(state=>({label:state.label,input:state.input}))},code:0};
}

export async function selftestCommand(strict:boolean){return selftest(strict);}

export async function textCli(sub:string,v:Record<string,any>){
 const font=v.font,text=v.text;if(!font||text===undefined)throw new Error('text command requires --font and --text');
 if(sub==='measure'){const out=await textCommand('measure',font,text,undefined,{lineHeight:1.2,format:'json',x:0,y:0,fontFile:v['font-file']});return {value:out.value,code:0};}
 if(sub!=='wrap')throw new Error(`Unknown text command: ${sub}`);if(v.width===undefined)throw new Error('text wrap requires --width');
 const width=Number(v.width),lineHeight=Number(v['line-height']??1.2),maxLines=v['max-lines']===undefined?undefined:Number(v['max-lines']),format=v.format??'json';
 if(!Number.isFinite(width)||width<=0)throw new Error('--width must be positive');if(!Number.isFinite(lineHeight)||lineHeight<=0)throw new Error('--line-height must be positive');if(maxLines!==undefined&&(!Number.isInteger(maxLines)||maxLines<1))throw new Error('--max-lines must be a positive integer');if(!['json','svg'].includes(format))throw new Error('--format must be json or svg');
 const out=await textCommand('wrap',font,text,width,{lineHeight,maxLines,format,x:Number(v.x??0),y:Number(v.y??0),fontFile:v['font-file']});return {value:out.value,code:out.code};
}
