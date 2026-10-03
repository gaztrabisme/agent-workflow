import type { CheckResult, RunOptions, Session } from './model.ts';

export function makeReport(input:string,options:RunOptions,session:Session,outputs:{png:string;pdf:string|null},checks:CheckResult[]){
 const summary={pass:0,fail:0,incomplete:0,skipped:0,n_a:0};
 for(const c of checks){if(c.status==='n/a')summary.n_a++;else if(c.status==='pass')summary.pass++;else if(c.status==='fail')summary.fail++;else if(c.status==='incomplete')summary.incomplete++;else summary.skipped++;}
 return {rk_version:'0.1.0',markup_version:1,input,created:new Date().toISOString(),browser:{name:'chromium',version:session.browser.version(),mode:'new-headless'},viewport:{width:session.width,height:session.height,scale:session.scale},at_ms:options.at==='end'?options.settle:options.at,outputs,requests_blocked:session.blocked,checks:checks.map(c=>({id:c.id,status:c.status,thresholds:c.thresholds,items:c.items,reason:c.reason??null})),summary};
}

export function checkExit(checks:CheckResult[],strict:boolean){
 return checks.some(c=>c.status==='fail'||(strict&&(c.status==='skipped'||c.status==='incomplete')))?1:0;
}
