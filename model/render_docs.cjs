const fs=require('fs');const {header,footer}=require('./site-shell.cjs');
(async()=>{const {marked}=await import(require.resolve('marked'));
for(const name of ['entscheidungen','montage','mechanik','beschaffung','kosten']){
const md=fs.readFileSync(`docs/${name}-d.md`,'utf8').replace(/\[Gemeinsamer Stand, Stückliste und nächste Entscheidungen\]\(entscheidungen-d.md\)\n/,'');
let html=marked(md).replaceAll('entscheidungen-d.md','entscheidungen.html').replaceAll('montage-d.md','montage.html').replaceAll('next-features.md','https://github.com/jdistlr/garden-torch-connector/blob/main/docs/next-features.md').replaceAll('mechanik-d.md','mechanik.html').replaceAll('beschaffung-d.md','beschaffung.html').replaceAll('kosten-d.md','kosten.html').replaceAll('../web/assets/','assets/');
html=html.replace(/<table>/g,'<div class="table-scroll" tabindex="0" role="region" aria-label="Tabelle, bei Bedarf seitlich scrollen"><table>').replace(/<\/table>/g,'</table></div>');
const titles={entscheidungen:'Stand & Entscheidungen',montage:'Montage & Prüfung',mechanik:'Steck-Dreh-Funktion',beschaffung:'Beschaffung',kosten:'Kostenstudie'};
html=html.replace(/<h1>.*?<\/h1>/,`<h1>${titles[name]}</h1>`);
fs.writeFileSync(`web/${name}.html`,`<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${titles[name]} · Gartenfackel</title><link rel="stylesheet" href="design.css?rev=2"></head><body class="document-page">${header(name)}<main class="document"><div class="document-meta"><p data-project-state>D-V03 · Konzept, keine Freigabe</p><button class="print-action" onclick="window.print()">Drucken / PDF</button></div><article>${html}</article>${name==='kosten'?'<p data-cost-state role="status" class="cost-context">Budgetstudie mit abweichenden Teilen, ausschließlich 5 mm.</p>':''}</main>${footer()}<script src="project-state.js?rev=2"></script></body></html>`);
}
const p='web/variants.html';fs.writeFileSync(p,fs.readFileSync(p,'utf8').replace(/<header[\s\S]*?<\/header>/,header('variants')));
})();
