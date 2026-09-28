// Shared document state; deliberately independent of Three.js and WebGL.
(() => {
 const allowed=['5','8','9'], url=new URL(location.href);
 let saved;try{saved=localStorage.getItem('torch-plate');}catch{}
 let thickness=allowed.includes(url.searchParams.get('plate'))?url.searchParams.get('plate'):allowed.includes(saved)?saved:'5';
 const select=document.querySelector('#thickness');
 document.querySelectorAll('[data-view],#reset-d,#section,#edges,#transparent,#dimensions,#ground,#tube,#explode,#snapshot,.montage-panel button,.montage-panel input,.montage-panel select').forEach(e=>e.disabled=true);
 function sync(){
  if(select)select.value=thickness;
  try{localStorage.setItem('torch-plate',thickness);}catch{}
  url.searchParams.set('plate',thickness);history.replaceState(null,'',url);
  document.querySelectorAll('a[href]').forEach(a=>{
   const u=new URL(a.getAttribute('href'),location.href);
   if(u.origin===location.origin&&/\/(projekt|quellen|bauteile|variants|entscheidungen|montage|mechanik|beschaffung|kosten)\.html$/.test(u.pathname)){u.searchParams.set('plate',thickness);a.href=u.href;}
  });
  document.querySelectorAll('[data-project-state]').forEach(e=>e.textContent=`D-V03 · ${thickness} mm Platte · Konzept, keine Fertigungs-/Betriebsfreigabe`);
  document.querySelectorAll('[data-cost-state]').forEach(e=>e.textContent=thickness==='5'?'Für diese CAD-Ausführung gibt es noch keinen vollständigen Preis. Die folgende Budgetstudie betrifft abweichende Kandidatenteile.':`Für die gewählte ${thickness}-mm-Platte liegt keine Gesamtkalkulation vor. Die folgende 5-mm-Budgetstudie betrifft außerdem abweichende Kandidatenteile.`);
  for(const [id,file] of [['step-d','assembly'],['plate-d','plate'],['adapter-d','adapter'],['pin-d','pin'],['screw-d','screw'],['tube-d','tube']]){const a=document.getElementById(id);if(a)a.href=`assets/sockel-d/${file}-${thickness}.step`;}
  document.querySelectorAll('[data-thickness]').forEach(e=>e.textContent=thickness);
  document.querySelectorAll('[data-step-part]').forEach(a=>a.href=`assets/sockel-d/${a.dataset.stepPart}-${thickness}.step`);
  document.querySelectorAll('[data-pdf]').forEach(a=>a.href=`assets/sockel-d/zeichnungen-D-V03-${thickness}mm.pdf`);
  const sheet=document.querySelector('#sheet');if(sheet){sheet.src=`assets/sockel-d/blatt-${thickness}-1.png?rev=5`;sheet.alt=`D-V03 · ${thickness} mm · Prüfzeichnung Blatt 1`;}
  document.querySelectorAll('[data-sheet]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.sheet==='1')));
  const fallback=document.querySelector('#model-fallback');if(fallback)fallback.src=`assets/ux/assembly-${thickness}.png`;
  const label=document.querySelector('#drawing-thickness');if(label)label.textContent=thickness;
  document.dispatchEvent(new CustomEvent('platechange',{detail:Number(thickness)}));
 }
 if(select)select.addEventListener('change',()=>{thickness=select.value;sync();});
 let zoom=1;document.querySelectorAll('[data-sheet]').forEach(b=>b.onclick=()=>{
  const sheet=document.querySelector('#sheet');sheet.src=`assets/sockel-d/blatt-${thickness}-${b.dataset.sheet}.png?rev=5`;sheet.alt=`D-V03 · ${thickness} mm · Prüfzeichnung Blatt ${b.dataset.sheet}`;
  document.querySelectorAll('[data-sheet]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 });
 function sheetZoom(v){zoom=Math.max(1,Math.min(4,v));document.querySelector('#sheet').style.width=zoom*100+'%';}
 const bind=(id,fn)=>{const e=document.getElementById(id);if(e)e.onclick=fn;};
 bind('zoom-in',()=>sheetZoom(zoom+.5));bind('zoom-out',()=>sheetZoom(zoom-.5));bind('fit-sheet',()=>sheetZoom(1));
 const names={plate:'Grundplatte',adapter:'Massive Aufnahme',pin:'Querstift',screw:'Senkschraube',tube:'Fackelrohr'};
 const selected=url.searchParams.get('part');
 const note=document.querySelector('#part-context');
 if(note&&names[selected]){const a=document.createElement('a');a.href=`bauteile.html#${selected}`;a.textContent=`${names[selected]}: Maßherkunft, Kandidat und offene Entscheidung`;note.append(a);}
 document.querySelectorAll('.table-scroll table').forEach(table=>{const labels=[...table.querySelectorAll('th')].map(e=>e.textContent);table.querySelectorAll('tr').forEach(row=>row.querySelectorAll('td').forEach((td,i)=>td.dataset.label=labels[i]||''));});
 sync();
})();
