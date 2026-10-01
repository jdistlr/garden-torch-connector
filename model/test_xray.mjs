import assert from 'node:assert/strict';
import fs from 'node:fs';
import * as THREE from '../web/vendor/three.module.js';
import {parts,steps,buildParts,pose,activeStep,applyPose,vectorScene,revision,displayDimensions,cameraPose} from '../web/xray-model.js';
assert(revision.includes('/ 02'));assert(revision.includes('Vectron'));
assert.equal(parts.length,11);assert.equal(new Set(parts.map(p=>p.id)).size,11);
for(const id of ['cathode','anode','bearing'])assert(parts.some(p=>p.id===id));
assert.equal(steps.length,12);assert.equal(parts.reduce((s,p)=>s+p.price,0),1065);
for(let i=0;i<parts.length;i++){assert.deepEqual(pose(i,0),parts[i].offset);assert(pose(i,i+1).every(x=>x===0));assert(pose(i,99).every(x=>x===0));}
assert.equal(activeStep(-1),0);assert.equal(activeStep(99),11);
const objects=buildParts();assert.equal(objects.length,11);
for(let p=0;p<=11;p+=.25){applyPose(objects,{mode:'montage',progress:p});for(const o of objects){assert(o.meshes.length>0);const b=new THREE.Box3().setFromObject(o.group);assert([...b.min.toArray(),...b.max.toArray()].every(Number.isFinite));}}
applyPose(objects);assert(objects.every(o=>o.group.position.length()===0));
for(const o of objects){const s=new THREE.Box3().setFromObject(o.group).getSize(new THREE.Vector3()).toArray().map(n=>Math.round(n*10)/10).join(' × ');assert.equal(s,parts.find(p=>p.id===o.id).size);}
assert.equal(displayDimensions,'390.5 × 307 × 275.5');
for(const width of [260,315]){const c=new THREE.PerspectiveCamera(38,width/340,1,6000);c.zoom=Math.min(1,c.aspect/1.05);c.position.set(...cameraPose());c.lookAt(0,0,0);const s=vectorScene(objects,c,width,340);const pts=[...s.matchAll(/points="([^"]+)"/g)].flatMap(m=>m[1].split(' ').map(p=>p.split(',').map(Number)));assert(pts.every(([x,y])=>x>=0&&x<=width&&y>=0&&y<=340),'Mobile default camera crops model');}
applyPose(objects,{selected:'bearing',solo:true});assert.deepEqual(objects.filter(o=>o.group.visible).map(o=>o.id),['bearing']);
applyPose(objects,{hidden:['cathode'],transparent:true});assert(!objects.find(o=>o.id==='cathode').group.visible);assert.equal(objects.find(o=>o.id==='housing').meshes[0].material.opacity,.18);
const c=new THREE.PerspectiveCamera(38,1,1,6000);c.position.set(650,410,620);c.lookAt(0,0,0);
for(const cut of [false,true]){const s=vectorScene(objects,c,900,550,{cut});assert(s.includes('<polygon'));assert(!s.includes('NaN'));}
const html=fs.readFileSync('web/one-more-thing.html','utf8');
for(const p of parts){assert(html.includes(`id="part-${p.id}"`));assert(html.includes(`id="source-${p.id}"`));assert(fs.existsSync(`web/assets/xray-demo/${p.id}.stl`));}
assert(html.includes('id="principle"'));assert(html.includes('id="fx-play"'));
console.log('XR-DEMO: 11 parts, 45 finite poses, selection, transparency, SVG, records and principle checked. No physical validation.');
