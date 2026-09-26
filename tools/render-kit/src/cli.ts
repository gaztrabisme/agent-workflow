import { parseOptions } from './args.ts';
import { renderCommand, checkCommand, briefCommand, selftestCommand, textCli } from './commands.ts';

const write=(value:unknown)=>process.stdout.write(JSON.stringify(value)+'\n');
const error=(e:unknown)=>{const message=e instanceof Error?e.message:String(e);process.stderr.write(`${message}\n`);write({error:message});process.exitCode=2;};

async function main(){
 const major=Number(process.versions.node.split('.')[0]);if(major<24)throw new Error('render-kit requires Node 24 or later');
 const [command,...args]=process.argv.slice(2);if(!command)throw new Error('Usage: rk <render|check|text|brief|selftest>');
 const {values,positionals}=parseOptions(args);
 if(command==='render'){
  if(positionals.length!==1)throw new Error('render requires one input');process.stderr.write(`Rendering ${positionals[0]}\n`);const out=await renderCommand(positionals[0],values);write(out.value);process.exitCode=out.code;return;
 }
 if(command==='check'){
  if(positionals.length!==1)throw new Error('check requires one input');process.stderr.write(`Checking ${positionals[0]}\n`);const out=await checkCommand(positionals[0],values);write(out.value);process.exitCode=out.code;return;
 }
 if(command==='brief'){
  if(positionals.length>1)throw new Error('brief takes at most one input');const out=await briefCommand(positionals[0],values);write(out.value);process.exitCode=out.code;return;
 }
 if(command==='selftest'){
  if(positionals.length)throw new Error('selftest takes no positional input');const out=await selftestCommand(!!values.strict);write({samples:out.samples,ok:out.ok});process.exitCode=out.code;return;
 }
 if(command==='text'){
  const [sub,...extra]=positionals;if(!sub||extra.length)throw new Error('Usage: rk text <measure|wrap> [options]');const out=await textCli(sub,values);
  if(typeof out.value==='string')process.stdout.write(out.value+'\n');else write(out.value);process.exitCode=out.code;return;
 }
 throw new Error(`Unknown command: ${command}`);
}

main().catch(error);
