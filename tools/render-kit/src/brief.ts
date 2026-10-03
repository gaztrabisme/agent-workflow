import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { jsonWrite } from './util.ts';

export function parseQuestions(source:string){
 const groups:{heading?:string;questions:string[]}[]=[];
 let current:{heading?:string;questions:string[]}|undefined;
 for(const line of source.split(/\r?\n/)){
  if(line.startsWith('#')){current={heading:line,questions:[]};groups.push(current);}
  else if(/^(?:- |\d+\. )/.test(line)){
   if(!current){current={questions:[]};groups.push(current);}
   current.questions.push(line.replace(/^(?:- |\d+\. )/,''));
  }
 }
 const populated=groups.filter(group=>group.questions.length>0);
 return {groups:populated,questions:populated.flatMap(group=>group.questions)};
}

export type BriefState={label:string;input:string;report:any;files:string[]};

function stateLabelsFromBrief(brief:string){
 const section=brief.match(/^## Inputs and states\s*\n([\s\S]*?)(?=^## Review files\s*$)/m)?.[1]??'';
 return [...section.matchAll(/^### (.+)$/gm)].map((match)=>match[1].trim());
}

export async function writeBrief(dir:string,questionPath:string,purpose:string,states:BriefState[]){
 await mkdir(dir,{recursive:true});const {groups,questions}=parseQuestions(await readFile(questionPath,'utf8'));
 if(!questions.length)throw new Error('Questions file has no questions');
 if(!states.length)throw new Error('Brief requires at least one labelled input/state');
 const files=states.flatMap(state=>state.files.map(file=>join(dir,file)));
 let questionNumber=0;
 const qs=groups.map(group=>`${group.heading?`${group.heading}\n\n`:''}${group.questions.map(q=>`Q${++questionNumber}. ${q}`).join('\n')}`).join('\n\n');
 const hasPdf=states.some(state=>state.report.outputs?.pdf);
 const stateSections=states.map(state=>{
  const checks=state.report.checks.map((c:any)=>`- **${c.id}: ${c.status}**${c.reason?` — ${c.reason}`:''}`).join('\n');
  const reportPath=join(dirname(join(dir,state.files[0])),'report.json');
  return `### ${state.label}\n\n**Input:** ${state.input}\n\n**Report:** ${reportPath}\n\n**Files:** ${state.files.map(file=>join(dir,file)).join(', ')}\n\n**Code checks:**\n\n${checks}`;
 }).join('\n\n');
 const answerInstructions=states.length>1
  ?'For every state, answer every question once. Use yes, no, unsure, or not-judged. Use not-judged if you cannot see the image. Give one sentence explaining each answer. Set where to the region or element for yes and no. A yes means that state passes the question. Each answer row in answers.template.json includes the question id and state label.'
  :'For each question, answer yes, no, unsure, or not-judged. Use not-judged if you cannot see the image. Give one sentence explaining the answer. Set where to the region or element for yes and no. A yes means the artifact passes the question.';
 const md=`# Visual review brief\n\n**Purpose:** ${purpose||'Review the rendered artifact.'}\n\n## Inputs and states\n\n${stateSections}\n\n## Review files\n\n${files.map(p=>`- ${p}`).join('\n')}\n\nThese checks report mechanical findings. Review the images for visual qualities the code cannot judge.${hasPdf?' The PDF and page images show the print output.':''}\n\n## How to answer\n\n${answerInstructions}\n\n${qs}\n`;
 const answerRows=states.length>1
  ?states.flatMap(state=>questions.map((question,i)=>({id:`Q${i+1}`,state:state.label,question,answer:null,where:null,reason:null})))
  :questions.map((question,i)=>({id:`Q${i+1}`,question,answer:null,where:null,reason:null}));
 await writeFile(join(dir,'brief.md'),md);await jsonWrite(join(dir,'answers.template.json'),{reviewer:null,answers:answerRows});
 return {questions,images:files};
}

export async function verifyAnswers(path:string,strict=false){
 const data=JSON.parse(await readFile(path,'utf8')),brief=await readFile(join(dirname(path),'brief.md'),'utf8');
 if(!Array.isArray(data.answers))throw new Error('answers must be an array');
 const count=[...brief.matchAll(/^Q\d+\./gm)].length,expected=Array.from({length:count},(_,i)=>`Q${i+1}`),rows=data.answers,states=stateLabelsFromBrief(brief),multiState=states.length>1;
 if(multiState){
  const pairs=states.flatMap(state=>expected.map(id=>({id,state})));
  if(rows.length!==pairs.length||rows.some((row:any,i:number)=>row.id!==pairs[i].id||row.state!==pairs[i].state))throw new Error('answers have missing, extra, or out-of-order state/question pairs');
 }else if(rows.length!==expected.length||rows.some((r:any,i:number)=>r.id!==expected[i]))throw new Error('answers have missing, extra, or out-of-order questions');
 const valid=new Set(['yes','no','unsure','not-judged']);
 const answerName=(row:any)=>multiState?`${row.state} ${row.id}`:row.id;
 for(const row of rows){const name=answerName(row);if(!valid.has(row.answer))throw new Error(`${name} has an invalid answer`);if(typeof row.reason!=='string'||!row.reason.trim())throw new Error(`${name} has an empty reason`);if(['yes','no'].includes(row.answer)&&(!row.where||!String(row.where).trim()))throw new Error(`${name} needs where for ${row.answer}`);}
 const resultRows=(answer:string)=>rows.filter((row:any)=>row.answer===answer).map((row:any)=>multiState?{state:row.state,id:row.id}:row.id);
 const no=resultRows('no'),unsure=resultRows('unsure'),not_judged=resultRows('not-judged');
 return {value:{no,unsure,not_judged},code:no.length||strict&&(unsure.length||not_judged.length)?1:0};
}
