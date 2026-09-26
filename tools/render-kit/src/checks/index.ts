import type { CheckContext, CheckResult } from '../model.ts';
import { CHECK_IDS } from '../model.ts';
import * as resources from './resources.ts'; import * as consoleCheck from './console.ts';
import * as fonts from './fonts.ts'; import * as overflow from './overflow.ts'; import * as collision from './collision.ts';
import * as contrast from './contrast.ts'; import * as cvd from './cvd.ts'; import * as fidelity from './fidelity.ts';
import * as a11y from './a11y.ts'; import * as value from './value.ts'; import * as pdfFonts from './pdf-fonts.ts';
const runners=[resources,consoleCheck,fonts,overflow,collision,contrast,cvd,fidelity,a11y,value,pdfFonts];

export async function runChecks(ctx:CheckContext,selected?:string[]):Promise<CheckResult[]>{
 const ids=selected??CHECK_IDS, out:CheckResult[]=[];
 for(const id of ids){const runner=runners[CHECK_IDS.indexOf(id)];if(!runner)throw new Error(`Unknown check: ${id}`);process.stderr.write(`  ${id}\n`);out.push(await runner.run(ctx));}
 return out;
}
