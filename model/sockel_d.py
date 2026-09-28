"""Selected D-V03: positive ground-clearance, actual CAD sections, 5/8/9 mm plates."""
from pathlib import Path
import cadquery as cq
import json,hashlib,itertools
R=Path(__file__).resolve().parents[1];O=R/'web/assets/sockel-d';O.mkdir(parents=True,exist_ok=True)
p=json.loads((R/'parameters/sockel-d-v03.json').read_text());photo=json.loads((R/'parameters/photo-draft.json').read_text())['dimensions']
def cyl(r,h,z=0):return cq.Solid.makeCylinder(r,h,cq.Vector(0,0,z))
def mesh(shape):
 v,t=shape.tessellate(.03,.12);edges=[]
 for e in shape.Edges():
  pts,_=e.sample(max(2,min(160,int(e.Length()/.6)+2)));edges.append([[round(a.x,5),round(a.y,5),round(a.z,5)] for a in pts])
 return dict(positions=[[round(a.x,5),round(a.y,5),round(a.z,5)] for a in v],triangles=[q for q in t if (v[q[1]]-v[q[0]]).cross(v[q[2]]-v[q[0]]).Length>1e-9],edges=edges)
cut=cq.Solid.makeBox(400,200,400,cq.Vector(-200,0,-100));allchecks=[]
for thick in p['plate']['thicknesses']:
 plate=cq.Solid.makeBox(150,150,thick,cq.Vector(-75,-75,0)).cut(cyl(4.5,thick)).cut(cq.Solid.makeCone(8.2,4.5,3.7))
 ap=p['adapter'];rad=ap['outer_diameter']/2
 # Nominal thread envelope, not a production core-drill representation.
 bore=cyl(ap['thread_nominal_diameter']/2,ap['bore_cylindrical_depth'],thick)
 tip=cq.Solid.makeCone(4,0,ap['drill_tip_depth'],cq.Vector(0,0,thick+ap['bore_cylindrical_depth']))
 pinz=thick+20+photo['pin_z']['value'];start=rad-ap['pin_seat_depth']
 pin=cq.Solid.makeCylinder(photo['pin_diameter']['value']/2,ap['pin_seat_depth']+photo['pin_projection']['value'],cq.Vector(0,start,pinz),cq.Vector(0,1,0))
 adapter=cyl(rad,ap['height'],thick).cut(bore.fuse(tip)).cut(pin).clean()
 # Ideal 90° head, M8 nominal shank. Flat outer head face 0.2 mm above floor.
 screw=cq.Solid.makeCone(8,4,4,cq.Vector(0,0,.2)).fuse(cyl(4,16,4.2))
 recess=cq.Workplane('XY').polygon(6,5/0.8660254038).extrude(2.5).val().translate((0,0,.2));screw=screw.cut(recess)
 tube=cq.importers.importStep(str(R/'web/assets/tube-draft.step')).val().translate((0,0,thick+14))
 parts=[('plate','1 · Grundplatte',plate,'#869bad',0),('adapter','2 · Vollmaterial-Aufnahme / direktes M8',adapter,'#303b42',46),('pin','3 · Querstift · Passung offen',pin,'#727e87',46),('screw','4 · 90°-Senkschraube · Hüllmodell',screw,'#d2b36b',-32),('tube','5 · Fackelrohr D02 · Referenz',tube,'#bccbd4',82)]
 checks={'thickness_mm':thick,'valid_solids':len(parts),'ground_z_mm':0,'screw_lowest_z_mm':screw.BoundingBox().zmin,'countersink_depth_mm':3.7,'remaining_plate_at_bore_mm':round(thick-3.7,2),'nominal_engagement_mm':round(20.2-thick,2),'bore_end_clearance_mm':round(thick+ap['bore_cylindrical_depth']-20.2,2),'target_thread_depth_mm':ap['thread_target_depth'],'bore_cylindrical_depth_mm':ap['bore_cylindrical_depth'],'max_intersection_mm3':0}
 assert 0<checks['nominal_engagement_mm']<ap['thread_target_depth']<ap['bore_cylindrical_depth']

 output=[]
 for id,name,s,col,exp in parts:
  assert s.isValid() and len(s.Solids())==1 and s.Volume()>0
  assert s.BoundingBox().zmin>=-1e-6,(id,s.BoundingBox().zmin)
  half=s.intersect(cut);assert half.isValid()
  output.append(dict(id=id,label=name,color=col,explode=exp,explode_y=22 if id=='pin' else 0,volume_mm3=s.Volume(),full=mesh(s),section=mesh(half)))
  cq.exporters.export(s,str(O/f'{id}-{thick}.step'))
 for a,b in itertools.combinations(parts,2):
  vol=a[2].intersect(b[2]).Volume();checks['max_intersection_mm3']=max(checks['max_intersection_mm3'],vol);assert vol<1e-5,(thick,a[0],b[0],vol)
 assembly=cq.Compound.makeCompound([s for _,_,s,_,_ in parts]);cq.exporters.export(assembly,str(O/f'assembly-{thick}.step'))
 back=cq.importers.importStep(str(O/f'assembly-{thick}.step')).val();assert back.isValid() and len(back.Solids())==len(parts) and abs(back.Volume()-assembly.Volume())/assembly.Volume()<1e-8
 checks['step_roundtrip']=True;allchecks.append(checks)
 (O/f'model-{thick}.json').write_text(json.dumps({'revision':'D-V03','thickness':thick,'checks':checks,'parts':output},separators=(',',':')))
(O/'checks.json').write_text(json.dumps({'revision':'D-V03','parameter_sha256':hashlib.sha256((R/'parameters/sockel-d-v03.json').read_bytes()).hexdigest(),'results':allchecks},indent=2))
print(json.dumps(allchecks,indent=2))
