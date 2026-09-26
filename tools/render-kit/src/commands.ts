import { resolve, extname, join } from 'node:path';
import { writeBrief, verifyAnswers } from './brief.ts';
import { runOptions, validateChecks } from './args.ts';
import { prepare, capture } from './render.ts';
import { checkInput } from './runner.ts';
import { selftest } from './selftest.ts';
import { textCommand } from './text-command.ts';
import { jsonWrite } from './util.ts';

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
 if(!input||!v.questions||!v['out-dir'])throw new Error('brief requires <input>, --questions and --out-dir');
 const simulations=String(v.simulate??'').split(',').filter(Boolean);for(const t of simulations)if(!visions.includes(t))throw new Error(`Unknown simulation: ${t}`);
 const options=await runOptions(input,v,false);validateChecks(options.checks);const dir=resolve(v['out-dir']);options.outDir=dir;
 const {report}=await checkInput(options);
 for(const type of simulations){const session=await prepare({...options,simulate:type});try{await capture(session,{...options,simulate:type},join(dir,`render-${type}.png`),'png');}finally{await session.stop();}}
 const written=await writeBrief(dir,resolve(v.questions),String(v.purpose??''),report,simulations);return {value:{out_dir:dir,images:written.images.map(x=>join(dir,x)),questions:written.questions.length},code:0};
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
