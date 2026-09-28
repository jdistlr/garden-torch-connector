import * as THREE from 'three';
import {OrbitControls} from 'three/addons/OrbitControls.js';
export async function createViewer(host,thickness){
 const renderer=new THREE.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0xf1f0ed);host.replaceChildren(renderer.domElement);
 const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(35,1,.1,2000);camera.up.set(0,0,1);
 const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=false;controls.minDistance=80;controls.maxDistance=850;
 scene.add(new THREE.HemisphereLight(0xffffff,0x747474,2.6));const key=new THREE.DirectionalLight(0xfff6ee,3);key.position.set(-120,80,300);scene.add(key);
 const group=new THREE.Group();scene.add(group);let objects=[],view='assembly',active=false,seq=0;
 function geometry(m){const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.Float32BufferAttribute(m.positions.flat(),3));g.setIndex(m.triangles.flat());g.computeVertexNormals();return g;}
 function size(){const r=host.getBoundingClientRect();if(r.width&&r.height){renderer.setSize(r.width,r.height);camera.aspect=r.width/r.height;camera.updateProjectionMatrix();}}
 function reset(){controls.target.set(0,0,view==='exploded'?110:85);camera.position.set(285,view==='section'?-425:425,300);controls.update();}
 function setView(v){view=v;for(const o of objects){o.mesh.geometry=v==='section'?o.half:o.full;o.mesh.position.set(0,v==='exploded'?(o.explode_y||0)*.62:0,v==='exploded'?o.explode*.62:0);}reset();}
 async function load(t){const n=++seq;const response=await fetch(`assets/sockel-d/model-${t}.json?rev=3`);if(!response.ok)throw Error('Model unavailable');const d=await response.json();if(n!==seq)return;if(d.revision!=='D-V03'||d.parts.map(p=>p.id).sort().join(',')!=='adapter,pin,plate,screw,tube')throw Error('Unexpected model');for(const o of objects){group.remove(o.mesh);o.full.dispose();o.half.dispose();o.mesh.material.dispose();}objects=d.parts.map(p=>{const full=geometry(p.full),half=geometry(p.section),mesh=new THREE.Mesh(full,new THREE.MeshStandardMaterial({color:p.color,metalness:.22,roughness:.48,side:THREE.DoubleSide}));group.add(mesh);return {...p,full,half,mesh};});setView(view);}
 const observer=new ResizeObserver(size);observer.observe(host);await load(thickness);reset();
 return {load,setView,reset,zoom(factor){const offset=camera.position.clone().sub(controls.target);offset.setLength(Math.max(80,Math.min(850,offset.length()*factor)));camera.position.copy(controls.target).add(offset);controls.update();},start(){active=true;size();renderer.setAnimationLoop(()=>{if(active)renderer.render(scene,camera);});},stop(){active=false;renderer.setAnimationLoop(null);},setTransparent(on){for(const o of objects){o.mesh.material.transparent=on;o.mesh.material.opacity=on?.35:1;o.mesh.material.depthWrite=!on;}},turn(direction){const offset=camera.position.clone().sub(controls.target);offset.applyAxisAngle(new THREE.Vector3(0,0,1),direction*Math.PI/6);camera.position.copy(controls.target).add(offset);controls.update();}};
}
