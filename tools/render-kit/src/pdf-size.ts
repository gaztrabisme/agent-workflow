import { readFile, writeFile } from 'node:fs/promises';

export async function normalizePdfBox(path:string,width:number,height:number){
 const bytes=await readFile(path),text=bytes.toString('latin1'),wanted=(height*.75).toFixed(2);
 const fixed=text.replace(/\/(MediaBox|CropBox|BleedBox|TrimBox|ArtBox)\s*\[\s*0\s+0\s+([-\d.]+)\s+([-\d.]+)(\s*\])/g,(all:string,kind:string,x:string,current:string,end:string)=>{
  if(wanted.length>current.length)return all;const value=wanted.padEnd(current.length,' ');return all.replace(new RegExp(`${current.replaceAll('.','\\.')}(?=${end.replaceAll(']','\\]')})`),value);
 });
 if(Buffer.byteLength(fixed,'latin1')!==bytes.length)throw new Error('PDF page-box normalization changed the PDF byte length');
 await writeFile(path,Buffer.from(fixed,'latin1'));
}
