import assert from 'node:assert/strict';
import {poseAt,stepAt} from '../web/montage-d.js';
for(const t of [5,8,9]) {
 assert.equal(poseAt(6,t).angle,0);
 assert.equal(poseAt(7,t).angle,50);
 assert.equal(stepAt(6),6);
 assert.equal(stepAt(6.5),7); // rotating, not sliding
 assert.equal(stepAt(2.5),3); // screw feeding, not adapter positioning
 assert.equal(poseAt(6.5,t).tube,0);
 assert.equal(poseAt(6.5,t).angle,25);
}
console.log('Animation: action labels and unchanged insertion/rotation poses verified.');

// Nominal sampled movement was checked on CAD before this UI repair.
// A pose edit must trigger renewed CAD motion checks, not a silent UI-only update.
const {createHash}=await import('node:crypto');
const sampled=[5,8,9].map(t=>Array.from({length:71},(_,i)=>poseAt(i/10,t)));
assert.equal(createHash('sha256').update(JSON.stringify(sampled)).digest('hex'),'9f01a10809fafc4278ff6299f8704ee52782cb25a1798198cb963a3e4f7db7be','Movement changed: repeat CAD assembly checks and review baseline.');
