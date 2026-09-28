"""Rebuild the explicitly unconfirmed photo draft (CadQuery 2.7.0)."""
from pathlib import Path
import json, math, hashlib
import cadquery as cq

ROOT = Path(__file__).resolve().parents[1]
spec = ROOT / 'parameters/photo-draft.json'
data = json.loads(spec.read_text())
p = {k: v['value'] for k, v in data['dimensions'].items()}
L, D, d = p['length'], p['outer_diameter'], p['inner_diameter']
w, depth = p['slot_width'], p['slot_depth']
assert L > depth > w > 0 and D > d > 0
tube = cq.Workplane('XY').circle(D/2).circle(d/2).extrude(L).val()
slot = cq.Solid.makeBox(w,D,depth-w/2+1,cq.Vector(-w/2,0,-1))
tip = cq.Solid.makeCylinder(w/2,D,cq.Vector(0,0,depth-w/2),cq.Vector(0,1,0))
branch = cq.Solid.makeCylinder(D,p['branch_height'],cq.Vector(0,0,p['branch_z']),cq.Vector(0,0,1),p['branch_angle'])
branch = branch.rotate((0,0,0),(0,0,1),90-p['branch_angle'])
solid = tube.cut(slot.fuse(tip)).cut(branch).clean()
assert solid.isValid() and len(solid.Solids()) == 1 and solid.Volume()>0
out = ROOT/'web'/'assets'
out.mkdir(parents=True,exist_ok=True)
cq.exporters.export(solid,str(out/'connector-draft.step'))
back=cq.importers.importStep(str(out/'connector-draft.step')).val()
assert back.isValid() and abs(back.Volume()-solid.Volume())/solid.Volume()<1e-8
vertices,triangles=solid.tessellate(0.03,0.1)
edges=[]
for e in solid.Edges():
    points,_=e.sample(max(2,min(200,math.ceil(e.Length()/0.8))))
    edges.append([[round(v.x,6),round(v.y,6),round(v.z,6)] for v in points])
mesh={'positions':[[round(v.x,6),round(v.y,6),round(v.z,6)] for v in vertices], 'triangles':triangles,'edges':edges}
(out/'mesh.json').write_text(json.dumps(mesh,separators=(',',':')))
box=solid.BoundingBox()
data['geometry']={'valid':True,'solids':1,'volume_mm3':solid.Volume(),'area_mm2':solid.Area(),'bounds_mm':[box.xlen,box.ylen,box.zlen],'triangles':len(triangles),'step_roundtrip':True,'cadquery_version':cq.__version__,'linear_deflection_mm':0.03,'angular_deflection_rad':0.1}
data['parameter_sha256']=hashlib.sha256(spec.read_bytes()).hexdigest()
data['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
data['mesh_sha256']=hashlib.sha256((out/'mesh.json').read_bytes()).hexdigest()
data['step_sha256']=hashlib.sha256((out/'connector-draft.step').read_bytes()).hexdigest()
(out/'metadata.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data['geometry'],indent=2))
