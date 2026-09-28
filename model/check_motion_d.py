"""Sample D-V03 STEP motion; no tolerances, loads or real-part certification."""
from pathlib import Path
import cadquery as cq
import json, math, hashlib
R=Path(__file__).resolve().parents[1]; O=R/'web/assets/sockel-d'
results=[]
for t in (5,8,9):
 parts={n:cq.importers.importStep(str(O/f'{n}-{t}.step')).val() for n in ('plate','adapter','pin','screw','tube')}
 tube=parts.pop('tube'); rows=[]
 # 40 mm clear above the reference pose, then insert and turn to 50 degrees.
 for phase,poses in [('insert',[(i*.5,0) for i in range(80,-1,-1)]),('turn',[(0,i*.5) for i in range(101)]),('reverse',[(0,i*.5) for i in range(100,-1,-1)])]:
  peak=0; minimum=1e9
  for dz,a in poses:
   moving=tube.rotate((0,0,0),(0,0,1),a).translate((0,0,dz))
   for n,s in parts.items():
    v=moving.intersect(s).Volume();peak=max(peak,v)
    if n in ('adapter','pin'):minimum=min(minimum,moving.distance(s))
  rows.append(dict(phase=phase,samples=len(poses),max_overlap_mm3=peak,min_clearance_mm=minimum))
  assert peak<1e-5,(t,phase,peak)
 pin=parts['pin'];tests={}
 for name,dz,a in [('wrong_direction',0,-5),('past_stop',0,60),('axial_lift_after_turn',1.1,50),('axial_lower_after_turn',-1.1,50)]:
  tests[name]=tube.rotate((0,0,0),(0,0,1),a).translate((0,0,dz)).intersect(pin).Volume()
  assert tests[name]>1e-5
 results.append(dict(thickness_mm=t,paths=rows,deliberate_collision_mm3=tests))
# Tangential contact at the radial branch end, evaluated at tube inner radius.
angle=65-math.degrees(math.asin(2/12.5))
d=dict(revision='D-V03',date='2026-09-28',status='nominal sampled geometry only',motion=dict(insertion_offset_mm=40,display_rotation_deg=50,branch_sector_deg=65,analytic_first_contact_deg=angle,axial_free_travel_each_direction_mm=1,radial_clearance_mm=.5,slot_side_clearance_mm=.5),results=results,source_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(O.glob('*.step'))},limitations=['No measured dimensions or manufacturing tolerances','Sampling is not a continuous swept-volume proof','No detent or reverse-rotation restraint in this model','No thread, clamp friction, strength or stability simulation'])
(O/'motion-checks.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='source_sha256'},indent=2))
