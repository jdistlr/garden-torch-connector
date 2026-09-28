import * as THREE from 'three';
import { OrbitControls } from 'three/addons/OrbitControls.js';
const $=s=>document.querySelector(s);
const fmt=(n,d=0)=>n.toLocaleString('de-DE',{maximumFractionDigits:d});
function showPhoto(id){$('#photo').src=`assets/photos/${id}.jpg`;$('#photo-link').href=`assets/photos/${id}.jpg`;$('#photo').alt=`Referenzfoto ${id}: Originalbauteil`;$('#photo-select').value=id;}
$('#photo-select').addEventListener('change',e=>showPhoto(e.target.value));
try {
 const fetchJSON=async path=>{const r=await fetch(path);if(!r.ok)throw new Error(`Datei nicht erreichbar: ${path}`);return r.json();};
 const [mesh,data]=await Promise.all([fetchJSON('assets/mesh.json?rev=D02'),fetchJSON('assets/metadata.json?rev=D02')]);
 for(const [key,p] of Object.entries(data.dimensions)){
  const row=document.createElement('div');row.className='dim';
  const top=document.createElement('div');top.className='dim-top';
  const label=document.createElement('span');label.textContent=p.label;
  const value=document.createElement('b');value.textContent=`≈ ${p.value} ${p.unit}`;top.append(label,value);
  const note=document.createElement('small');note.textContent=`${p.status} · ${p.range}`;
  const a=document.createElement('a');const id=p.source.split(',')[0].trim();a.href=`assets/photos/${id}.jpg`;a.textContent=`Foto ${p.source} ansehen`;a.addEventListener('click',e=>{e.preventDefault();showPhoto(id);$('#photo').scrollIntoView({behavior:'smooth',block:'center'});});
  row.append(top,note,a);$('#dimensions').append(row);
 }
 const g=data.geometry;
 for(const [title,value] of [['CAD-Geometrie',`${g.solids} gültige Körper`],['Materialvolumen',`${fmt(g.volume_mm3/1000,2)} cm³`],['Oberfläche',`${fmt(g.area_mm2/100,1)} cm²`],['STEP wieder eingelesen',g.step_roundtrip?'Geprüft':'Offen']]){const r=document.createElement('div');const dt=document.createElement('dt');dt.textContent=title;const dd=document.createElement('dd');dd.textContent=value;r.append(dt,dd);$('#metrics').append(r);}
 for(const part of g.parts){const row=document.createElement('div');const dt=document.createElement('dt');dt.textContent=part.label;const dd=document.createElement('dd');dd.textContent=`${fmt(part.volume_mm3/1000,2)} cm³`;row.append(dt,dd);$('#metrics').append(row);}
 data.limitations.forEach(t=>{const li=document.createElement('li');li.textContent=t;$('#limitations').append(li);});
 $('#mesh-info').textContent=`${fmt(g.triangles)} Dreiecke · Exportparameter ${g.linear_deflection_mm} mm / ${g.angular_deflection_rad} rad. Keine Aussage zur Fertigungstoleranz.`;
 const host=$('#viewport');const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0xe9eef4);renderer.outputColorSpace=THREE.SRGBColorSpace;host.prepend(renderer.domElement);renderer.domElement.setAttribute('aria-label','Drehbares CAD-Entwurfsmodell der zweiteiligen Gartenfackel-Verbindung');renderer.domElement.tabIndex=0;
 const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(35,1,0.1,2000);camera.up.set(0,0,1);
 const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.minDistance=12;controls.maxDistance=650;
 scene.add(new THREE.HemisphereLight(0xffffff,0x6f839c,2.5));const light=new THREE.DirectionalLight(0xffffff,3);light.position.set(20,120,180);scene.add(light);const fill=new THREE.DirectionalLight(0xa9c7ef,1.8);fill.position.set(-100,-100,20);scene.add(fill);
 const model=new THREE.Group();model.rotation.y=Math.PI/2;model.position.x=-43;scene.add(model);
 const objects=[];
 for(const part of mesh.parts){
  const group=new THREE.Group();model.add(group);
  const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(part.positions.flat(),3));geometry.setIndex(part.triangles.flat());geometry.computeVertexNormals();
  const material=new THREE.MeshStandardMaterial({color:part.id==='spike'?0x282c32:0xa4b5c8,metalness:.25,roughness:.43});
  group.add(new THREE.Mesh(geometry,material));
  const edgeCoords=[];for(const edge of part.edges)for(let i=1;i<edge.length;i++)edgeCoords.push(...edge[i-1],...edge[i]);
  const lines=new THREE.LineSegments(new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(edgeCoords,3)),new THREE.LineBasicMaterial({color:part.id==='spike'?0x697580:0x31465f,transparent:true,opacity:.55}));group.add(lines);
  objects.push({id:part.id,group,material,lines});
 }
 const grid=new THREE.GridHelper(400,40,0xc6d0dc,0xdbe2ea);grid.rotation.x=Math.PI/2;grid.position.z=-85;scene.add(grid);
 let layout='separated';
 function view(kind){const distance=host.clientWidth<500?620:350;controls.target.set(0,0,0);if(kind==='front')camera.position.set(0,distance,0);else if(kind==='end')camera.position.set(-distance*.65,0,0);else if(kind==='detail'){controls.target.set(-28,0,0);camera.position.set(-68,100,60);}else camera.position.set(-110,distance,190);controls.update();}
 function arrangement(){objects.find(p=>p.id==='spike').group.position.set(layout==='separated'?55:0,0,layout==='separated'?100:0);$('#layout-note').textContent=layout==='separated'?'Getrennte Teile · Rohr + schwarzes Gegenstück':'Zusammengesteckt · illustrative Lage, Passung unbestätigt';$('#separated').setAttribute('aria-pressed',layout==='separated');$('#assembled').setAttribute('aria-pressed',layout==='assembled');view('iso');}
 $('#separated').onclick=()=>{layout='separated';arrangement();};$('#assembled').onclick=()=>{layout='assembled';arrangement();};
 for(const id of ['iso','front','end','detail','reset'])$('#'+id).onclick=()=>{if(id==='detail'){layout='assembled';arrangement();}view(id);};
 for(const part of objects)$('#show-'+part.id).onchange=e=>{part.group.visible=e.target.checked;};
 $('#edges').onchange=e=>{objects.forEach(p=>p.lines.visible=e.target.checked);};$('#transparent').onchange=e=>{objects.forEach(p=>{p.material.transparent=e.target.checked;p.material.opacity=e.target.checked?.32:1;p.material.depthWrite=!e.target.checked;});};
 arrangement();
 const resize=()=>{renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();};new ResizeObserver(resize).observe(host);resize();view('iso');
 renderer.setAnimationLoop(()=>{controls.update();renderer.render(scene,camera);});
 $('#render-status').textContent='2 Bauteile · Foto-Schätzungen';document.body.dataset.viewerReady='true';
}catch(e){$('#error').hidden=false;$('#error').textContent='Die 3D-Ansicht konnte nicht geladen werden. Referenzfotos und STEP-Datei stehen weiterhin zur Verfügung. Bitte Seite neu laden oder einen Browser mit WebGL verwenden.';$('#render-status').textContent='3D-Ansicht nicht verfügbar';console.error(e);}
