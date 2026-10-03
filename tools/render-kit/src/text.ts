export type Wrapped = { lines:{text:string;width:number}[]; line_height:number; height:number; overflow:boolean };

export function wrapText(text:string,width:number,measure:(text:string)=>number,fontSize:number,ratio=1.2,maxLines?:number):Wrapped{
 const segments=[...new Intl.Segmenter('en',{granularity:'word'}).segment(text)],units:{text:string;space:boolean}[]=[];let space=false;
 for(const seg of segments){if(/^\s+$/.test(seg.segment)){space=true;continue;}
  const parts=seg.segment.match(/[^-/]+[-/]*|[-/]+/g)??[seg.segment];
  for(let i=0;i<parts.length;i++){units.push({text:parts[i],space:space&&i===0});space=false;}
 }
 const lines:string[]=[];let line='',overflow=false;
 for(const unit of units){if(measure(unit.text)>width)overflow=true;const next=line+(line&&unit.space?' ':'')+unit.text;
  if(line&&measure(next)>width){lines.push(line);line=unit.text;}
  else line=next;
 }
 if(line||!lines.length)lines.push(line);
 const measured=lines.map(text=>({text,width:measure(text)}));
 if(maxLines!==undefined&&measured.length>maxLines)overflow=true;
 return {lines:measured,line_height:fontSize*ratio,height:measured.length*fontSize*ratio,overflow};
}

export function svgWrappedText(w:Wrapped,font:string,x:number,y:number){
 const esc=(s:string)=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('"','&quot;');
 return `<svg xmlns="http://www.w3.org/2000/svg"><text x="${x}" y="${y}" font="${esc(font)}">${w.lines.map((l,i)=>`<tspan x="${x}" dy="${i?w.line_height:0}">${esc(l.text)}</tspan>`).join('')}</text></svg>`;
}
