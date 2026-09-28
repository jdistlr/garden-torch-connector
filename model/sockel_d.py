"""Selected D-V02: positive ground-clearance, actual CAD sections, 5/8/9 mm plates."""
from pathlib import Path
import cadquery as cq
import json,hashlib,itertools
R=Path(__file__).resolve().parents[1];O=R/'web/assets/sockel-d';O.mkdir(parents=True,exist_ok=True)
p=json.loads((R/'parameters/sockel-d-v02.json').read_text());photo=json.loads((R/'parameters/photo-draft.json').read_text())['dimensions']
def cyl(r,h,z=0):return cq.Solid.makeCylinder(r,h,cq.Vector(0,0,z))
def mesh(shape):
 v,t=shape.tessellate(.03,.12);edges=[]
 for e in shape.Edges():
  pts,_=e.sample(max(2,min(160,int(e.Length()/.6)+2)));edges.append([[round(a.x,5),round(a.y,5),round(a.z,5)] for a in pts])
 return dict(positions=[[round(a.x,5),round(a.y,5),round(a.z,5)] for a in v],triangles=[q for q in t if (v[q[1]]-v[q[0]]).cross(v[q[2]]-v[q[0]]).Length>1e-9],edges=edges)
cut=cq.Solid.makeBox(400,200,400,cq.Vector(-200,0,-100));allchecks=[]
for thick in p['plate']['thicknesses']:
 plate=cq.Solid.makeBox(150,150,thick,cq.Vector(-75,-75,0)).cut(cyl(4.5,thick)).cut(cq.Solid.makeCone(8.2,4.5,3.7))
 sleeve=cyl(12,20,thick).cut(cyl(9,20,thick))
 head=cyl(photo['head_diameter']['value']/2,photo['head_length']['value'],thick+20)
 pin=cq.Solid.makeCylinder(photo['pin_diameter']['value']/2,photo['head_diameter']['value']/2+photo['pin_projection']['value'],cq.Vector(0,0,thick+20+photo['pin_z']['value']),cq.Vector(0,1,0))
 adapter=sleeve.fuse(head,pin).clean()
 insert=cyl(8.8,16,thick).cut(cyl(4,16,thick))
 weld=cyl(9,2,thick+1).cut(cyl(8.8,2,thick+1))
 # Ideal 90° head, M8 nominal shank. Flat outer head face 0.2 mm above floor.
 screw=cq.Solid.makeCone(8,4,4,cq.Vector(0,0,.2)).fuse(cyl(4,16,4.2))
 recess=cq.Workplane('XY').polygon(6,5/0.8660254038).extrude(2.5).val().translate((0,0,.2));screw=screw.cut(recess)
 tube=cq.importers.importStep(str(R/'web/assets/tube-draft.step')).val().translate((0,0,thick+14))
 parts=[('plate','Grundplatte',plate,'#869bad',0),('adapter','Hülse / Kopf / Querstift',adapter,'#303b42',46),('insert','Gewindebuchse M8',insert,'#bd7849',22),('weld','Fügezone · schematisch',weld,'#e1b076',22),('screw','90°-Senkschraube · Hüllmodell',screw,'#d2b36b',-32),('tube','Fackelrohr D02 · Referenz',tube,'#bccbd4',82)]
 checks={'thickness_mm':thick,'valid_solids':len(parts),'ground_z_mm':0,'screw_lowest_z_mm':screw.BoundingBox().zmin,'countersink_depth_mm':3.7,'remaining_plate_at_bore_mm':round(thick-3.7,2),'nominal_engagement_mm':round(20.2-thick,2),'insert_end_clearance_mm':round(thick+16-20.2,2),'max_intersection_mm3':0}
 output=[]
 for id,name,s,col,exp in parts:
  assert s.isValid() and len(s.Solids())==1 and s.Volume()>0
  assert s.BoundingBox().zmin>=-1e-6,(id,s.BoundingBox().zmin)
  half=s.intersect(cut);assert half.isValid()
  output.append(dict(id=id,label=name,color=col,explode=exp,volume_mm3=s.Volume(),full=mesh(s),section=mesh(half)))
  cq.exporters.export(s,str(O/f'{id}-{thick}.step'))
 for a,b in itertools.combinations(parts,2):
  vol=a[2].intersect(b[2]).Volume();checks['max_intersection_mm3']=max(checks['max_intersection_mm3'],vol);assert vol<1e-5,(thick,a[0],b[0],vol)
 assembly=cq.Compound.makeCompound([s for _,_,s,_,_ in parts]);cq.exporters.export(assembly,str(O/f'assembly-{thick}.step'))
 back=cq.importers.importStep(str(O/f'assembly-{thick}.step')).val();assert back.isValid() and len(back.Solids())==6 and abs(back.Volume()-assembly.Volume())/assembly.Volume()<1e-8
 checks['step_roundtrip']=True;allchecks.append(checks)
 (O/f'model-{thick}.json').write_text(json.dumps({'revision':'D-V02','thickness':thick,'checks':checks,'parts':output},separators=(',',':')))
(O/'checks.json').write_text(json.dumps({'revision':'D-V02','parameter_sha256':hashlib.sha256((R/'parameters/sockel-d-v02.json').read_bytes()).hexdigest(),'results':allchecks},indent=2))
print(json.dumps(allchecks,indent=2))
