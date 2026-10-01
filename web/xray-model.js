import * as THREE from './vendor/three.module.js';
export const revision='XR-DEMO / 01';
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
export const steps=[{name:'Alle Teile kennenlernen',text:'Elf erfundene Baugruppen in räumlicher Übersicht. Die Folge erklärt Zusammenhänge; sie ist keine Montageanweisung für einen echten Röntgenstrahler.'},...parts.map(p=>({name:p.name,text:p.task}))];
export function activeStep(progress){return Math.max(0,Math.min(parts.length,Math.ceil(Math.max(0,progress)-1e-8)));}
export function pose(index,progress){const t=Math.min(1,Math.max(0,progress-index));const eased=t*t*(3-2*t);return parts[index].offset.map(x=>x*(1-eased));}
export function buildParts(){
 const output=parts.map(p=>{const group=new THREE.Group();group.userData.partId=p.id;return {...p,group,meshes:[]};});
 const slot=i=>i>=3?i+1:i;
 function add(i,geometry,position,color,opacity=1,rotateZ=0){const p=output[slot(i)],mat=new THREE.MeshStandardMaterial({color:color||p.color,metalness:.32,roughness:.48,transparent:opacity<1,opacity,side:THREE.DoubleSide,depthWrite:opacity===1});mat.userData={baseOpacity:opacity};const m=new THREE.Mesh(geometry,mat);m.position.set(...position);m.rotation.z=rotateZ;m.userData.partId=p.id;m.castShadow=true;m.receiveShadow=true;p.group.add(m);p.meshes.push(m);}
 const box=(i,x,y,z,pos,color)=>add(i,new THREE.BoxGeometry(x,y,z),pos,color);
 const cyl=(i,r,len,pos,color,opacity=1)=>add(i,new THREE.CylinderGeometry(r,r,len,24,1,false),pos,color,opacity,Math.PI/2);
 box(0,360,12,190,[0,-114,0]);for(const x of [-145,145])box(0,24,10,150,[x,-125,0],'#253e50');
 for(const x of [-125,125]){box(1,22,80,115,[x,-61,0]);box(1,44,10,120,[x,-18,0]);}box(1,270,6,20,[0,-96,-45]);
 cyl(2,25,90,[-75,0,0],'#657d90');cyl(2,40,9,[-24,0,0]);cyl(2,18,20,[-16,0,0],'#cca987');
 cyl(3,23,55,[85,0,0]);box(3,32,24,24,[51,0,0],'#7b8e9a');
 // Hollow sleeve uses open side + two annuli, rather than a fictional solid glass plug.
 add(4,new THREE.CylinderGeometry(60,60,280,32,1,true),[0,0,0],null,.22,Math.PI/2);
 for(const x of [-140,140]){const r=new THREE.Mesh(new THREE.RingGeometry(54,60,32),new THREE.MeshStandardMaterial({color:'#537b8c',side:THREE.DoubleSide,roughness:.5}));r.position.x=x;r.rotation.y=Math.PI/2;r.userData.partId=parts[slot(4)].id;r.material.userData.baseOpacity=1;output[slot(4)].group.add(r);output[slot(4)].meshes.push(r);}
 box(5,190,8,82,[0,62,-12]);for(let x=-85;x<=85;x+=17)box(5,5,26,82,[x,79,-12]);
 box(6,450,10,220,[0,-94,0]);box(6,450,160,10,[0,-9,-105]);box(6,190,160,10,[-130,-9,105]);box(6,190,160,10,[130,-9,105]);
 box(7,76,54,28,[0,0,118]);box(7,52,30,4,[0,0,134],'#142e42');
 box(8,450,16,220,[0,99,0]);for(const x of [-160,-120,-80,-40,0,40,80,120,160])box(8,18,1,75,[x,107.6,-10],'#91a5b3');
 box(9,16,170,220,[233,-9,0]);box(9,4,74,126,[243,-9,0],'#536f81');
 for(const x of [-110,-100,-90,-80,-70]){const m=new THREE.Mesh(new THREE.TorusGeometry(29,3,8,24),new THREE.MeshStandardMaterial({color:'#4caaa4',metalness:.5,roughness:.35}));m.rotation.y=Math.PI/2;m.position.x=x;m.userData.partId='bearing';m.material.userData.baseOpacity=1;output[3].group.add(m);output[3].meshes.push(m);}
 return output;
}
export function applyPose(objects,{mode='assembly',progress=parts.length,explode=0,hidden=[],selected='',solo=false,transparent=false,cut=false}={}){
 objects.forEach((o,i)=>{const xyz=mode==='montage'?pose(i,progress):o.offset.map(v=>v*explode);o.group.position.set(...xyz);o.group.visible=!hidden.includes(o.id)&&(!solo||!selected||o.id===selected);const focus=mode==='montage'?activeStep(progress)-1===i:o.id===selected;o.meshes.forEach(m=>{let alpha=m.material.userData.baseOpacity??1;if(transparent&&['housing','cover','endcap'].includes(o.id))alpha=.18;m.material.opacity=alpha;m.material.transparent=alpha<1;m.material.depthWrite=alpha===1;m.material.emissive?.set(focus?'#35220f':'#000000');});o.group.updateMatrixWorld(true);});
}
export function cameraPose(view='iso') {return {iso:[650,410,620],front:[0,70,900],side:[900,100,0],top:[1,900,1]}[view]||[650,410,620];}
// CPU projection of the SAME meshes: usable when WebGL is unavailable, not a substitute image.
// Depth-sorted faces are approximate (not a GPU depth buffer); deliberately marked in UI.
export function vectorScene(objects,camera,width=900,height=550,{cut=false,selected='',dimensions=false}={}){
 camera.aspect=width/height;camera.updateProjectionMatrix();camera.updateMatrixWorld();const faces=[];
 const project=v=>{const q=v.clone().project(camera);return [(q.x+1)*width/2,(1-q.y)*height/2,q.z];};
 for(const o of objects){if(!o.group.visible)continue;for(const mesh of o.meshes){mesh.updateWorldMatrix(true,false);const bounds=new THREE.Box3().setFromObject(mesh);const nearDepth=Math.min(...[bounds.min.x,bounds.max.x].flatMap(x=>[bounds.min.y,bounds.max.y].flatMap(y=>[bounds.min.z,bounds.max.z].map(z=>new THREE.Vector3(x,y,z).project(camera).z))));const meshDepth=o.id==='cover'&&camera.position.y>bounds.max.y?nearDepth:bounds.getCenter(new THREE.Vector3()).project(camera).z;const g=mesh.geometry,pos=g.attributes.position,idx=g.index,n=idx?idx.count:pos.count;
 for(let j=0;j<n;j+=3){let poly=[0,1,2].map(k=>new THREE.Vector3().fromBufferAttribute(pos,idx?idx.getX(j+k):j+k).applyMatrix4(mesh.matrixWorld));if(cut){const out=[];for(let k=0;k<poly.length;k++){const a=poly[k],b=poly[(k+1)%poly.length],ina=a.z<=0,inb=b.z<=0;if(ina)out.push(a);if(ina!==inb)out.push(a.clone().lerp(b,(0-a.z)/(b.z-a.z)));}poly=out;}if(poly.length<3)continue;
 const normal=poly[1].clone().sub(poly[0]).cross(poly[2].clone().sub(poly[0])).normalize(),light=Math.min(1,Math.max(.38,.72+normal.dot(new THREE.Vector3(.4,.8,.5).normalize())*.25));if(mesh.material.opacity===1&&normal.dot(camera.position.clone().sub(poly[0]))<=0)continue;const color=mesh.material.color.clone().multiplyScalar(light);if(o.id===selected)color.lerp(new THREE.Color('#d6a271'),.2);const ps=poly.map(project);if(ps.some(p=>Math.abs(p[2])>1))continue;faces.push({meshDepth,z:ps.reduce((s,p)=>s+p[2],0)/ps.length,svg:`<polygon points="${ps.map(p=>p.slice(0,2).map(n=>n.toFixed(1)).join(',')).join(' ')}" fill="#${color.getHexString()}" fill-opacity="${mesh.material.opacity}"/>`});
 }}}
 faces.sort((a,b)=>b.meshDepth-a.meshDepth||b.z-a.z);let result=faces.map(f=>f.svg).join('');
 if(dimensions)result+=`<text x="24" y="${height-24}" fill="#48667b" font-family="sans-serif" font-size="14">Hülle ca. 470 × 238 × 246 Demo-mm · frei erfunden</text>`;
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" role="img" aria-label="Fiktives Röntgenstrahler-Anschauungsmodell"><rect width="100%" height="100%" fill="#edf2f5"/>${result}</svg>`;
}
