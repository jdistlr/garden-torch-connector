(() => {
 const image=document.querySelector('#drawing-image');
 const scroll=document.querySelector('#drawing-scroll');
 const names=['Rohr','schwarzes Gegenstück','Zusammenbau'];
 let sheet=1,zoom=1;
 function update(){
  image.style.width=`${zoom*100}%`;
  document.querySelector('#drawing-status').textContent=`Blatt ${sheet} / 3 · ${zoom===1?'eingepasst':zoom+'× vergrößert'}`;
  document.querySelector('#drawing-minus').disabled=zoom===1;
  document.querySelector('#drawing-plus').disabled=zoom===4;
 }
 document.querySelectorAll('[data-sheet]').forEach(button=>button.addEventListener('click',()=>{
  sheet=Number(button.dataset.sheet);image.src=`assets/zeichnung-D02-${sheet}.png`;
  image.alt=`Blatt ${sheet}: Bemaßte Prüfzeichnung ${names[sheet-1]}, D02`;
  document.querySelector('#drawing-full').href=image.src;
  document.querySelectorAll('[data-sheet]').forEach(b=>b.setAttribute('aria-pressed',String(Number(b.dataset.sheet)===sheet)));
  scroll.scrollTo(0,0);update();
 }));
 document.querySelector('#drawing-plus').onclick=()=>{zoom=Math.min(4,zoom+.5);update();};
 document.querySelector('#drawing-minus').onclick=()=>{zoom=Math.max(1,zoom-.5);update();};
 document.querySelector('#drawing-fit').onclick=()=>{zoom=1;scroll.scrollTo(0,0);update();};
 image.addEventListener('error',()=>{document.querySelector('#drawing-status').textContent='Vorschau nicht geladen. Bitte den PDF-Link darunter verwenden.';});
 update();
})();
