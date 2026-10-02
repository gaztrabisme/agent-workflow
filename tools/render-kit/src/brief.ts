import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { jsonWrite } from './util.ts';

export function parseQuestions(source:string){
 const headings:string[]=[],questions:string[]=[];
 for(const line of source.split(/\r?\n/)){if(line.startsWith('#'))headings.push(line);else if(/^(?:- |\d+\. )/.test(line))questions.push(line.replace(/^(?:- |\d+\. )/,''));}
 return {headings,questions};
}

export async function writeBrief(dir:string,questionPath:string,purpose:string,report:any,simulations:string[],pdfPages:string[]=[]){
 await mkdir(dir,{recursive:true});const {headings,questions}=parseQuestions(await readFile(questionPath,'utf8'));
 if(!questions.length)throw new Error('Questions file has no questions');
 const images=['render.png',...simulations.map(t=>`render-${t}.png`),...(report.outputs?.pdf?['render.pdf',...pdfPages]:[])];
 const checks=report.checks.map((c:any)=>`- **${c.id}: ${c.status}**${c.reason?` — ${c.reason}`:''}`).join('\n');
 const qs=questions.map((q,i)=>`Q${i+1}. ${q}`).join('\n');
 const md=`# Visual review brief\n\n**Purpose:** ${purpose||'Review the rendered artifact.'}\n\n## Review files\n\n${images.map(p=>`- ${join(dir,p)}`).join('\n')}\n\n## Code checks\n\n${checks}\n\nThese checks report mechanical findings. Review the images for visual qualities the code cannot judge. The PDF and page images show the print output.\n\n## How to answer\n\nFor each question, answer yes, no, unsure, or not-judged. Use not-judged if you cannot see the image. Give one sentence explaining the answer. Set where to the region or element for yes and no. A yes means the artifact passes the question.\n\n${headings.join('\n')}\n\n${qs}\n`;
 await writeFile(join(dir,'brief.md'),md);await jsonWrite(join(dir,'answers.template.json'),{reviewer:null,answers:questions.map((question,i)=>({id:`Q${i+1}`,question,answer:null,where:null,reason:null}))});
 return {questions,images};
}

export async function verifyAnswers(path:string,strict=false){
 const data=JSON.parse(await readFile(path,'utf8')),brief=await readFile(join(dirname(path),'brief.md'),'utf8');
 if(!Array.isArray(data.answers))throw new Error('answers must be an array');
 const count=[...brief.matchAll(/^Q\d+\./gm)].length,expected=Array.from({length:count},(_,i)=>`Q${i+1}`),rows=data.answers;
 if(rows.length!==expected.length||rows.some((r:any,i:number)=>r.id!==expected[i]))throw new Error('answers have missing, extra, or out-of-order questions');
 const valid=new Set(['yes','no','unsure','not-judged']);
 for(const row of rows){if(!valid.has(row.answer))throw new Error(`${row.id} has an invalid answer`);if(typeof row.reason!=='string'||!row.reason.trim())throw new Error(`${row.id} has an empty reason`);if(['yes','no'].includes(row.answer)&&(!row.where||!String(row.where).trim()))throw new Error(`${row.id} needs where for ${row.answer}`);}
 const no=rows.filter((r:any)=>r.answer==='no').map((r:any)=>r.id),unsure=rows.filter((r:any)=>r.answer==='unsure').map((r:any)=>r.id),not_judged=rows.filter((r:any)=>r.answer==='not-judged').map((r:any)=>r.id);
 return {value:{no,unsure,not_judged},code:no.length||strict&&(unsure.length||not_judged.length)?1:0};
}
