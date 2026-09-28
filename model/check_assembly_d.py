"""Check exported animation poses from montage-d.js, supplied as a JSON path."""
import cadquery as cq,json,itertools,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];O=R/'web/assets/sockel-d';out=[]
for t,poses in json.loads(Path(sys.argv[1]).read_text()).items():
 parts={n:cq.importers.importStep(str(O/f'{n}-{t}.step')).val() for n in ('plate','adapter','pin','screw','tube')};peak=0;floor=1e9
 for pose in poses:
  moved={n:s.rotate((0,0,0),(0,0,1),pose['angle'] if n=='tube' else 0).translate((0,pose['pinY'] if n=='pin' else 0,pose[n])) for n,s in parts.items()}
  for s in moved.values():floor=min(floor,s.BoundingBox().zmin)
  for (a,s),(b,v) in itertools.combinations(moved.items(),2):
   # AABB filter only skips disjoint volumes, never intersecting candidates.
   x=s.BoundingBox();y=v.BoundingBox()
   if any(getattr(x,axis+'max')<=getattr(y,axis+'min')+1e-8 or getattr(y,axis+'max')<=getattr(x,axis+'min')+1e-8 for axis in ('x','y','z')):continue
   ov=s.intersect(v).Volume();peak=max(peak,ov)
   assert ov<1e-5,(t,a,b,ov,pose)
 assert floor>=-1e-6
 out.append(dict(thickness_mm=int(t),pose_samples=len(poses),max_overlap_mm3=peak,min_z_mm=floor))
d={'revision':'D-V03','results':out,'scope':'Sampled translations of all five CAD bodies; tube rotation included. Screw spin ignored because thread is smooth envelope; recess spin does not alter outer envelope. No forces or thread flank contact simulated.'}
(O/'assembly-motion-checks.json').write_text(json.dumps(d,indent=2)+'\n');print(d)
