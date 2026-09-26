import { mkdtemp, mkdir } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import type { RunOptions } from './model.ts';
import { prepare, capture } from './render.ts';
import { runChecks } from './checks/index.ts';
import { makeReport } from './report.ts';
import { jsonWrite } from './util.ts';

export async function checkInput(options:RunOptions){
 const dir=resolve(options.outDir??await mkdtemp(join(tmpdir(),'rk-check-')));await mkdir(dir,{recursive:true});
 const png=join(dir,'render.png'),pdf=options.pdf?join(dir,'render.pdf'):null,session=await prepare(options);
 try{await capture(session,options,png,'png');if(pdf){await capture(session,{...options,simulate:undefined},pdf,'pdf');await session.page.emulateMedia({media:'screen'});}
  const checks=await runChecks({session,png,pdf:pdf??undefined,options},options.checks);
  const report=makeReport(options.input,options,session,{png,pdf},checks);await jsonWrite(join(dir,'report.json'),report);return {report,dir};
 }finally{await session.stop();}
}
