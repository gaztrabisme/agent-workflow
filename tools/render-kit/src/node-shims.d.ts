declare const process: { argv:string[]; env:Record<string,string|undefined>; versions:{node:string}; stdout:{write:(s:string)=>void}; stderr:{write:(s:string)=>void}; exitCode?:number; cwd:()=>string };
declare const Buffer: { from:(value:any,encoding?:string)=>any; byteLength:(value:string,encoding?:string)=>number };
declare module 'node:fs/promises' { export const access:any, mkdir:any, readFile:any, writeFile:any, mkdtemp:any, stat:any, readdir:any; }
declare module 'node:path' { export const dirname:any, extname:any, resolve:any, join:any, sep:string; }
declare module 'node:os' { export const tmpdir:any; }
declare module 'node:http' { export const createServer:any; }
declare module 'node:net' { export const createServer:any; export type AddressInfo={port:number}; }
declare module 'node:child_process' { export const execFile:any, spawn:any; }
declare module 'node:util' { export const parseArgs:any, promisify:any; }
declare module 'node:test' { export const test:any; }
declare module 'node:assert/strict' { const assert:any; export default assert; export = assert; }
