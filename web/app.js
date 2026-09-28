import * as THREE from 'three';
import { OrbitControls } from 'three/addons/OrbitControls.js';
const $=s=>document.querySelector(s);
const fmt=(n,d=0)=>n.toLocaleString('de-DE',{maximumFractionDigits:d});
function showPhoto(id){$('#photo').src=`assets/photos/${id}.jpg`;$('#photo-link').href=`assets/photos/${id}.jpg`;$('#photo').alt=`Referenzfoto ${id}: Originalbauteil`;$('#photo-select').value=id;}
$('#photo-select').addEventListener('change',e=>showPhoto(e.target.value));
try {
 const fetchJSON=async path=>{const r=await fetch(path);if(!r.ok)throw new Error(`Datei nicht erreichbar: ${path}`);return r.json();};
 const [mesh,data]=await Promise.all([fetchJSON('assets/mesh.json'),fetchJSON('assets/metadata.json')]);
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
 for(const [title,value] of [['CAD-Geometrie',`${g.solids} gültiger Körper`],['Materialvolumen',`${fmt(g.volume_mm3/1000,2)} cm³`],['Oberfläche',`${fmt(g.area_mm2/100,1)} cm²`],['STEP wieder eingelesen',g.step_roundtrip?'Geprüft':'Offen']]){const r=document.createElement('div');const dt=document.createElement('dt');dt.textContent=title;const dd=document.createElement('dd');dd.textContent=value;r.append(dt,dd);$('#metrics').append(r);}
 data.limitations.forEach(t=>{const li=document.createElement('li');li.textContent=t;$('#limitations').append(li);});
 $('#mesh-info').textContent=`${fmt(g.triangles)} Dreiecke · Exportparameter ${g.linear_deflection_mm} mm / ${g.angular_deflection_rad} rad. Keine Aussage zur Fertigungstoleranz.`;
 const host=$('#viewport');const renderer=new THREE.WebGLRenderer({antialias:true,alpha:false});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0xe9eef4);renderer.outputColorSpace=THREE.SRGBColorSpace;host.prepend(renderer.domElement);renderer.domElement.setAttribute('aria-label','Drehbares CAD-Entwurfsmodell des Verbindungsrohrs');renderer.domElement.tabIndex=0;
 const scene=new THREE.Scene();const camera=new THREE.PerspectiveCamera(35,1,0.1,2000);camera.up.set(0,0,1);
 const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.minDistance=12;controls.maxDistance=650;
 scene.add(new THREE.HemisphereLight(0xffffff,0x6f839c,2.5));const light=new THREE.DirectionalLight(0xffffff,3);light.position.set(20,120,180);scene.add(light);const fill=new THREE.DirectionalLight(0xa9c7ef,1.8);fill.position.set(-100,-100,20);scene.add(fill);
 const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(mesh.positions.flat(),3));geometry.setIndex(mesh.triangles.flat());geometry.computeVertexNormals();
 const material=new THREE.MeshStandardMaterial({color:0xa4b5c8,metalness:.35,roughness:.35});
 const body=new THREE.Mesh(geometry,material);const model=new THREE.Group();model.add(body);model.rotation.y=Math.PI/2;model.position.x=-data.dimensions.length.value/2;scene.add(model);
 const edgeCoords=[];for(const edge of mesh.edges)for(let i=1;i<edge.length;i++)edgeCoords.push(...edge[i-1],...edge[i]);
 const lines=new THREE.LineSegments(new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(edgeCoords,3)),new THREE.LineBasicMaterial({color:0x31465f,transparent:true,opacity:.7}));model.add(lines);
 const grid=new THREE.GridHelper(280,28,0xc6d0dc,0xdbe2ea);grid.rotation.x=Math.PI/2;grid.position.z=-23;scene.add(grid);
 function view(kind){const width=host.clientWidth;const distance=width<500?360:290;controls.target.set(0,0,0);if(kind==='front')camera.position.set(0,distance,0);else if(kind==='end')camera.position.set(-distance*.48,0,0);else if(kind==='detail'){controls.target.set(-72,0,0);camera.position.set(-105,87,48);}else camera.position.set(-95,distance,120);controls.update();}
 for(const id of ['iso','front','end','detail','reset'])$('#'+id).onclick=()=>view(id);
 $('#edges').onchange=e=>{lines.visible=e.target.checked;};$('#transparent').onchange=e=>{material.transparent=e.target.checked;material.opacity=e.target.checked?.32:1;material.depthWrite=!e.target.checked;};
 const resize=()=>{renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();};new ResizeObserver(resize).observe(host);resize();view('iso');
 renderer.setAnimationLoop(()=>{controls.update();renderer.render(scene,camera);});
 $('#render-status').textContent='Volumenmodell · Foto-Schätzungen';document.body.dataset.viewerReady='true';
}catch(e){$('#error').hidden=false;$('#error').textContent='Die 3D-Ansicht konnte nicht geladen werden. Referenzfotos und STEP-Datei stehen weiterhin zur Verfügung. Bitte Seite neu laden oder einen Browser mit WebGL verwenden.';$('#render-status').textContent='3D-Ansicht nicht verfügbar';console.error(e);}
