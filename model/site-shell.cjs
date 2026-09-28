const pages=[['variants','Modell'],['entscheidungen','Stand'],['mechanik','Mechanik'],['montage','Montage'],['beschaffung','Beschaffung'],['kosten','Kosten']];
exports.header=active=>`<header class="site-header"><a class="brand" href="variants.html">Gartenfackel<span>D-V03</span></a><nav aria-label="Hauptnavigation">${pages.map(([slug,label])=>`<a href="${slug}.html"${slug===active?' aria-current="page"':''}>${label}</a>`).join('')}</nav></header>`;
exports.footer=()=>'<footer class="site-footer"><span>Gartenfackel / D-V03</span><a href="variants.html">Zurück zum Modell</a></footer>';
