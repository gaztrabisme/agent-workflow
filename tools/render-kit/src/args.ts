import { parseArgs } from 'node:util';
import { stat } from 'node:fs/promises';
import { resolve, sep } from 'node:path';
import { CHECK_IDS, type RunOptions } from './model.ts';
import { DEFAULT_THRESHOLDS } from './thresholds.ts';
import { isUrl } from './util.ts';

export const definitions={out:{type:'string'},root:{type:'string'},width:{type:'string'},height:{type:'string'},scale:{type:'string'},at:{type:'string'},settle:{type:'string'},boot:{type:'string'},media:{type:'string'},'wait-for':{type:'string'},timeout:{type:'string'},'allow-network':{type:'boolean'},'expect-request':{type:'string',multiple:true},state:{type:'string',multiple:true},simulate:{type:'string'},pdf:{type:'boolean'},'out-dir':{type:'string'},checks:{type:'string'},threshold:{type:'string',multiple:true},strict:{type:'boolean'},questions:{type:'string'},purpose:{type:'string'},verify:{type:'string'},font:{type:'string'},text:{type:'string'},'font-file':{type:'string'},'line-height':{type:'string'},'max-lines':{type:'string'},format:{type:'string'},x:{type:'string'},y:{type:'string'}} as const;

export function parseOptions(args:string[]){return parseArgs({args,options:definitions,allowPositionals:true,strict:true});}
const number=(v:string|undefined,label:string,fallback:number)=>{const n=v===undefined?fallback:Number(v);if(!Number.isFinite(n))throw new Error(`${label} must be a number`);return n;};
const positive=(n:number,label:string)=>{if(n<=0)throw new Error(`${label} must be positive`);return n;};

export async function runOptions(input:string,v:Record<string,any>,pdf=false):Promise<RunOptions>{
 const url=isUrl(input);if(url){const u=new URL(input);if(u.protocol!=='http:'||!['localhost','127.0.0.1'].includes(u.hostname))throw new Error('URL input must use http://localhost or http://127.0.0.1');if(v.root)throw new Error('--root cannot be used with a URL');if(u.pathname.toLowerCase().endsWith('.svg'))throw new Error('URL input must serve an HTML page');}
 else{const path=resolve(input);if(!['.html','.svg'].includes(path.slice(path.lastIndexOf('.')).toLowerCase()))throw new Error('Input must be an .html or .svg file');if(!(await stat(path).catch(()=>null))?.isFile())throw new Error(`Input file does not exist: ${path}`);input=path;}
 const root=v.root?resolve(v.root):undefined;if(root&&!(await stat(root).catch(()=>null))?.isDirectory())throw new Error(`Root directory does not exist: ${root}`);if(root&&!url&&!resolve(input).startsWith(root+sep))throw new Error('Input file must be inside --root');
 const at=v.at??'end',time=at==='end'?'end':number(at,'--at',0);if(time!=='end'&&time<0)throw new Error('--at must be non-negative or end');
 const media=v.media??'screen';if(!['screen','print'].includes(media))throw new Error('--media must be screen or print');
 return {input,root,width:v.width?positive(number(v.width,'--width',1),'--width'):undefined,height:v.height?positive(number(v.height,'--height',1),'--height'):undefined,scale:positive(number(v.scale,'--scale',1),'--scale'),at:time,settle:number(v.settle,'--settle',10000),boot:number(v.boot,'--boot',100),media,waitFor:v['wait-for'],timeout:positive(number(v.timeout,'--timeout',30000),'--timeout'),allowNetwork:!!v['allow-network'],simulate:v.simulate,pdf,strict:!!v.strict,outDir:v['out-dir'],checks:v.checks?String(v.checks).split(','):undefined,thresholds:parseThresholds(v.threshold),expectedRequests:parseExpectedRequests(v['expect-request'])};
}

export function parseExpectedRequests(raw?:string|string[]){
 const entries=raw===undefined?[]:Array.isArray(raw)?raw:[raw];
 return entries.map(entry=>{const split=entry.lastIndexOf('='),pattern=entry.slice(0,split),statusText=entry.slice(split+1),status=Number(statusText);if(split<1||!pattern.trim()||!/^\d{3}$/.test(statusText)||status<400||status>599)throw new Error(`Invalid --expect-request: ${entry} (expected <url-pattern>=<4xx-or-5xx-status>)`);return {pattern,status};});
}

export function parseThresholds(raw?:string|string[]){
 const out:Record<string,number>={};for(const entry of raw===undefined?[]:Array.isArray(raw)?raw:[raw]){const m=entry.match(/^([a-z-]+)\.([a-z_]+)=([^=]+)$/);if(!m)throw new Error(`Invalid --threshold: ${entry}`);const key=`${m[1]}.${m[2]}`,n=Number(m[3]);if(!Number.isFinite(n))throw new Error(`Threshold must be numeric: ${entry}`);if(DEFAULT_THRESHOLDS[m[1]]?.[m[2]]===undefined)throw new Error(`Unknown threshold: ${key}`);out[key]=n;}
 return out;
}

export function validateChecks(value:RunOptions['checks']){if(value?.some(id=>!CHECK_IDS.includes(id)))throw new Error(`Unknown check: ${value?.find(id=>!CHECK_IDS.includes(id))}`);if(value&&new Set(value).size!==value.length)throw new Error('--checks contains duplicate ids');}
