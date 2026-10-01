import * as THREE from './vendor/three.module.js';
export const revision='XR-DEMO / 02 · Vectron-nahe Designstudie';
// Invented display geometry. Not a product design, manufacturing plan or radiation model.
export const parts=[
 {id:'base',name:'Montagefuß',material:'Aluminiumoptik',size:'360 × 12 × 190',color:'#718ba0',offset:[0,-110,0],price:38,source:'POC Metallatelier',task:'Der Fuß bildet den visuellen Bezug. Keine geprüfte Tragstruktur.'},
 {id:'carrier',name:'Innenrahmen',material:'Metalloptik',size:'280 × 86 × 120',color:'#a5b7c4',offset:[0,0,-210],price:54,source:'POC Formwerk',task:'Der Innenrahmen wird als Träger eingesetzt. Befestigungen und Toleranzen sind nicht ausgelegt.'},
 {id:'anode',name:'Anoden-/Rotormodul',material:'Kupfer- und Stahloptik',size:'120 × Ø80',color:'#bc8056',offset:[-210,30,0],price:210,source:'POC Komponentenlabor',task:'Ein geometrischer Platzhalter für die Anodenseite. Kein funktionaler Rotor, kein berechnetes Target.'},
 {id:'cathode',name:'Kathodenmodul',material:'Keramik- und Metalloptik',size:'70 × Ø46',color:'#d4dedf',offset:[220,30,0],price:140,source:'POC Komponentenlabor',task:'Die Gegenseite wird ergänzt. Emission, Fokussierung und elektrische Anschlüsse sind bewusst nicht ausgelegt.'},
 {id:'envelope',name:'Röhrenhülle',material:'Transparente Demo-Hülle',size:'280 × Ø120',color:'#79b2c6',offset:[0,230,0],price:165,source:'POC Glasmodellbau',task:'Die transparente Hülle macht die Baugruppenbeziehung sichtbar. Das Überstülpen ist eine Erklärbewegung, kein Vakuum-Fertigungsprozess.'},
 {id:'cooler',name:'Kühlmodul',material:'Dunkle Aluminiumoptik',size:'190 × 34 × 82',color:'#355366',offset:[0,160,-180],price:85,source:'POC Thermoattrappen',task:'Ein Kühlmodul ergänzt die Silhouette. Keine thermische Auslegung oder realer Kühlkreislauf.'},
 {id:'housing',name:'Gehäuseschale',material:'Lackierte Metalloptik',size:'450 × 170 × 220',color:'#d1dce3',offset:[0,0,-300],price:110,source:'POC Formwerk',task:'Die äußere Schale umgibt das Modell. Ihre Dicke ist rein grafisch und kein Strahlenschutznachweis.'},
 {id:'window',name:'Fenstermodul',material:'Kontrastfarbene Attrappe',size:'76 × 54 × 28',color:'#538d9f',offset:[0,0,200],price:32,source:'POC Optikattrappen',task:'Das Fenstermodul markiert eine gedachte Austrittsseite. Es gibt keinen Strahl, keine Filter- oder Dosisberechnung.'},
 {id:'cover',name:'Servicehaube',material:'Helle Gehäuseoptik',size:'450 × 16 × 220',color:'#e2e8eb',offset:[0,290,0],price:62,source:'POC Formwerk',task:'Die Servicehaube schließt die Darstellung. Zugänglichkeit und Montagekollisionen sind nicht geprüft.'},
 {id:'endcap',name:'Enddeckel',material:'Dunkle Gehäuseoptik',size:'16 × 170 × 220',color:'#294658',offset:[250,0,0],price:44,source:'POC Formwerk',task:'Der Enddeckel vervollständigt das Anschauungsmodell. Keine Inbetriebnahme – nur eine vollständige Darstellung.'}
];
parts[2].name='Anodenteller mit Rotor';
parts.splice(3,0,{id:'bearing',name:'Flüssigmetalllager (Symbol)',material:'Türkise Lagerfilm-Symbolik',size:'50 × Ø64',color:'#4caaa4',offset:[-180,120,140],price:125,source:'POC Lagerattrappen',task:'Die Ringe symbolisieren einen Flüssigmetall-Lagerfilm zwischen rotierender und stationärer Struktur. Keine reale Lagergeometrie, Legierung, Spaltweite oder Betriebsbedingung.'});
for(const [id,changes] of Object.entries({base:{name:'Silberner Montagerahmen',offset:[0,-210,-90]},carrier:{name:'Trägerstruktur (Schema)'},anode:{task:'Anodenteller und Rotor als vereinfachte Innenbaugruppe. Keine originalen Vectron-Maße oder Targetauslegung.'},cooler:{name:'Leitungen & Anschlüsse (Attrappe)',material:'Silber- und Messingoptik',offset:[-250,70,0],task:'Seitliche Leitungen und Anschlussattrappen prägen die Vectron-nahe Silhouette. Kein funktionsfähiger Kühlkreis oder elektrischer Anschluss.'},housing:{name:'Zylindrischer Röhrenkörper',material:'Dunkle Metalloptik'},cover:{name:'Bronzefarbene Formhaube',material:'Bronze- / Messingoptik',offset:[0,70,270],task:'Konturierte Formhaube und umlaufender Schraubflansch nach öffentlicher Erscheinungsreferenz. Keine originale Form-, Material- oder Abschirmungsauslegung.'},endcap:{name:'Runder Seitendeckel'},window:{offset:[0,100,350]}}))Object.assign(parts.find(p=>p.id===id),changes);
export const steps=[{name:'Alle Teile kennenlernen',text:'Elf schematische Baugruppen einer Vectron-nahen Designstudie. Keine Original-Montagefolge oder Herstellungsanweisung.'},...parts.map(p=>({name:p.name,text:p.task}))];
export function activeStep(progress){return Math.max(0,Math.min(parts.length,Math.ceil(Math.max(0,progress)-1e-8)));}
export function pose(index,progress){const t=Math.min(1,Math.max(0,progress-index));const eased=t*t*(3-2*t);return parts[index].offset.map(x=>x*(1-eased));}
export function buildParts(){
 const output=parts.map(p=>{const group=new THREE.Group();group.userData.partId=p.id;return {...p,group,meshes:[]};});
 const byId=Object.fromEntries(output.map(p=>[p.id,p]));
 function add(id,geometry,pos,color,axis='z',opacity=1){const p=byId[id],mat=new THREE.MeshStandardMaterial({color:color||p.color,metalness:id==='cover'?.72:.48,roughness:.38,transparent:opacity<1,opacity,side:THREE.DoubleSide,depthWrite:opacity===1});mat.userData.baseOpacity=opacity;const m=new THREE.Mesh(geometry,mat);m.position.set(...pos);if(axis==='x')m.rotation.y=Math.PI/2;if(axis==='y')m.rotation.x=-Math.PI/2;m.userData.partId=id;p.group.add(m);p.meshes.push(m);return m;}
 const box=(id,w,h,d,pos,color)=>add(id,new THREE.BoxGeometry(w,h,d),pos,color);
 const cyl=(id,r,len,pos,color,axis='x',segments=24)=>{const g=new THREE.CylinderGeometry(r,r,len,segments);g.rotateX(Math.PI/2);return add(id,g,pos,color,axis);};
 function outline(points){const s=new THREE.Shape();points.forEach(([x,y],i)=>i?s.lineTo(x,y):s.moveTo(x,y));s.closePath();return s;}
 function form(id,points,depth,pos,color,bevel=5){const g=new THREE.ExtrudeGeometry(outline(points),{depth,bevelEnabled:bevel>0,bevelThickness:bevel,bevelSize:bevel,bevelSegments:2,curveSegments:4,steps:1});g.translate(0,0,-depth/2);return add(id,g,pos,color);}
 const profile=[[-102,-131],[65,-131],[99,-110],[105,-57],[145,-25],[147,77],[116,122],[78,138],[-78,138],[-105,111]];
 // Rear silver casting and feet: visual interpretation of the public product silhouette.
 form('base',[[-161,-143],[-117,-143],[-99,-117],[-100,108],[-125,135],[-161,135]],15,[0,0,-95],'#b4bdc1',4);
 for(const y of [-135,129])box('base',270,16,185,[-20,y,-11],'#b8c0c3');
 for(const x of [-135,116])box('base',44,12,174,[x,-151,-4],'#6d777a');
 cyl('carrier',97,18,[-134,0,-5],'#727e80');cyl('carrier',70,23,[133,0,-5],'#9ca5a5');
 for(const x of [-95,105])box('carrier',20,90,42,[x,-94,-3],'#79878b');
 cyl('anode',25,92,[-66,0,-5],'#717d81');cyl('anode',58,10,[-13,0,-5],'#ab7856');cyl('anode',45,3,[-5,0,-5],'#474b4a');cyl('anode',17,20,[7,0,-5],'#c39670');
 cyl('cathode',24,58,[81,0,-5],'#e0dad0');cyl('cathode',29,12,[115,0,-5],'#929e9f');box('cathode',24,25,22,[44,0,-5],'#b89070');
 for(const x of [-103,-88,-73,-58])add('bearing',new THREE.TorusGeometry(28,2,6,18),[x,0,-5],'#559d98','x');
 const sleeve=new THREE.CylinderGeometry(69,69,280,32,1,true);sleeve.rotateX(Math.PI/2);add('envelope',sleeve,[0,0,-5],'#9bc5ce','x',.18);
 for(const x of [-140,140])add('envelope',new THREE.RingGeometry(63,69,24),[x,0,-5],'#6f8f96','x');
 // No real channels or electrical connection geometry: capped visual connectors.
 for(const [y,z,r] of [[72,52,19],[-54,59,13],[113,18,11]]){
  cyl('cooler',r+4,24,[-165,y,z],'#788381');cyl('cooler',r,47,[-196,y,z],y===113?'#ac9257':'#929d9e');
  cyl('cooler',r*.64,2,[-220,y,z],'#26343a');cyl('cooler',r*.36,3,[-222,y,z],'#576769');
 }
 const path=new THREE.CatmullRomCurve3([[-165,-123,74],[-184,-110,76],[-187,86,76],[-174,112,73],[-121,123,65]].map(p=>new THREE.Vector3(...p)));
 add('cooler',new THREE.TubeGeometry(path,20,6,8,false),[0,0,0],'#b3bbbf');
 cyl('cooler',5,119,[-125,-94,95],'#9a844e');
 const barrel=new THREE.CylinderGeometry(105,105,255,32,1,true);barrel.rotateX(Math.PI/2);add('housing',barrel,[-2,0,-5],'#555e58','x');
 for(const x of [-130,127])add('housing',new THREE.RingGeometry(94,105,32),[x,0,-5],'#6b7165','x');
 box('window',66,23,12,[58,68,157],'#494837');box('window',54,8,3,[58,68,164],'#242f32');
 // Bronze formed cover: contoured silhouette, stepped flange, contrasting fasteners.
 form('cover',[[-138,-147],[164,-147],[164,147],[-138,147]],8,[0,0,94],'#7f754f',3);
 form('cover',profile,39,[0,0,117],'#a79561',12);
 for(const y of [-132,-88,-44,0,44,88,132])for(const x of [-130,156]){
  cyl('cover',5,4,[x,y,102],'#c7cdcb','z',8);cyl('cover',2.4,5,[x,y,104],'#29383e','z',6);
 }
 for(const y of [83,88,93])box('cover',61,2,2,[58,y,150],'#7b6e47');
 cyl('endcap',101,12,[144,0,-5],'#858d83');
 for(let i=0;i<10;i++){const a=i*Math.PI/5;cyl('endcap',4,5,[153,85*Math.cos(a),-5+85*Math.sin(a)],'#cad0cf','x',6);}
 return output;
}
// All reported sizes are rounded bounds of the invented display meshes, not product dimensions.
const measuringParts=buildParts(),assemblyBounds=new THREE.Box3();
for(const o of measuringParts){const b=new THREE.Box3().setFromObject(o.group);assemblyBounds.union(b);parts.find(p=>p.id===o.id).size=b.getSize(new THREE.Vector3()).toArray().map(n=>Math.round(n*10)/10).join(' × ');}
export const displayDimensions=assemblyBounds.getSize(new THREE.Vector3()).toArray().map(n=>Math.round(n*10)/10).join(' × ');
measuringParts.forEach(o=>o.meshes.forEach(m=>{m.geometry.dispose();m.material.dispose();}));
export function applyPose(objects,{mode='assembly',progress=parts.length,explode=0,hidden=[],selected='',solo=false,transparent=false,cut=false}={}){
 objects.forEach((o,i)=>{const xyz=mode==='montage'?pose(i,progress):o.offset.map(v=>v*explode);o.group.position.set(...xyz);o.group.visible=!hidden.includes(o.id)&&(!solo||!selected||o.id===selected);const focus=mode==='montage'?activeStep(progress)-1===i:o.id===selected;o.meshes.forEach(m=>{let alpha=m.material.userData.baseOpacity??1;if(transparent&&['housing','cover','endcap'].includes(o.id))alpha=.18;m.material.opacity=alpha;m.material.transparent=alpha<1;m.material.depthWrite=alpha===1;m.material.emissive?.set(focus?'#35220f':'#000000');});o.group.updateMatrixWorld(true);});
}
export function cameraPose(view='iso') {return {iso:[-650,310,760],front:[0,70,900],side:[-900,100,0],top:[1,900,1]}[view]||[-650,310,760];}
// CPU projection of the SAME meshes: usable when WebGL is unavailable, not a substitute image.
// Depth-sorted faces are approximate (not a GPU depth buffer); deliberately marked in UI.
export function vectorScene(objects,camera,width=900,height=550,{cut=false,selected='',dimensions=false}={}){
 camera.aspect=width/height;camera.updateProjectionMatrix();camera.updateMatrixWorld();const faces=[];
 const project=v=>{const q=v.clone().project(camera);return [(q.x+1)*width/2,(1-q.y)*height/2,q.z];};
 for(const o of objects){if(!o.group.visible)continue;for(const mesh of o.meshes){mesh.updateWorldMatrix(true,false);const bounds=new THREE.Box3().setFromObject(mesh);const nearDepth=Math.min(...[bounds.min.x,bounds.max.x].flatMap(x=>[bounds.min.y,bounds.max.y].flatMap(y=>[bounds.min.z,bounds.max.z].map(z=>new THREE.Vector3(x,y,z).project(camera).z))));const meshDepth=o.id==='cover'&&camera.position.y>bounds.max.y?nearDepth:bounds.getCenter(new THREE.Vector3()).project(camera).z;const g=mesh.geometry,pos=g.attributes.position,idx=g.index,n=idx?idx.count:pos.count;
 for(let j=0;j<n;j+=3){let poly=[0,1,2].map(k=>new THREE.Vector3().fromBufferAttribute(pos,idx?idx.getX(j+k):j+k).applyMatrix4(mesh.matrixWorld));if(cut){const out=[];for(let k=0;k<poly.length;k++){const a=poly[k],b=poly[(k+1)%poly.length],ina=a.z<=0,inb=b.z<=0;if(ina)out.push(a);if(ina!==inb)out.push(a.clone().lerp(b,(0-a.z)/(b.z-a.z)));}poly=out;}if(poly.length<3)continue;
 const normal=poly[1].clone().sub(poly[0]).cross(poly[2].clone().sub(poly[0])).normalize(),light=Math.min(1,Math.max(.38,.72+normal.dot(new THREE.Vector3(.4,.8,.5).normalize())*.25));if(mesh.material.opacity===1&&normal.dot(camera.position.clone().sub(poly[0]))<=0)continue;const color=mesh.material.color.clone().multiplyScalar(light);if(o.id===selected)color.lerp(new THREE.Color('#d6a271'),.2);const ps=poly.map(project);if(ps.some(p=>Math.abs(p[2])>1))continue;faces.push({meshDepth,z:ps.reduce((s,p)=>s+p[2],0)/ps.length,svg:`<polygon points="${ps.map(p=>p.slice(0,2).map(n=>n.toFixed(1)).join(',')).join(' ')}" fill="#${color.getHexString()}" stroke="#${color.getHexString()}" stroke-width=".3" stroke-opacity="${mesh.material.opacity}" fill-opacity="${mesh.material.opacity}"/>`});
 }}}
 faces.sort((a,b)=>b.z-a.z);let result=faces.map(f=>f.svg).join('');
 if(dimensions)result+=`<text x="24" y="${height-24}" fill="#48667b" font-family="sans-serif" font-size="14">Gesamt ${displayDimensions} Demo-mm · frei erfunden</text>`;
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" role="img" aria-label="Fiktives Röntgenstrahler-Anschauungsmodell"><rect width="100%" height="100%" fill="#edf2f5"/>${result}</svg>`;
}
