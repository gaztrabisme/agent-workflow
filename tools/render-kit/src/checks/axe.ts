import type { Page } from 'playwright';
import type { Session } from '../model.ts';

export async function withAxePage<T>(session:Session,run:(page:Page)=>Promise<T>):Promise<T>{
 const context=await session.browser.newContext({viewport:{width:session.width,height:session.height},deviceScaleFactor:session.scale,locale:'en-US',timezoneId:'UTC'}),page=await context.newPage(),origin=new URL(session.url).origin;
 await page.route('**/*',async route=>{if(!session.allowNetwork&&new URL(route.request().url()).origin!==origin)await route.abort('blockedbyclient');else await route.continue();});
 try{await page.goto(session.url,{waitUntil:'load',timeout:30000});await page.evaluate(()=>document.fonts.ready);return await run(page);}
 finally{await context.close();}
}
