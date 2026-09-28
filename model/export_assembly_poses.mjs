// Usage: node model/export_assembly_poses.mjs /tmp/torch-poses.json
import fs from 'node:fs';
import {poseAt} from '../web/montage-d.js';
const d={};for(const t of [5,8,9])d[t]=Array.from({length:71},(_,i)=>poseAt(i/10,t));
fs.writeFileSync(process.argv[2],JSON.stringify(d));
