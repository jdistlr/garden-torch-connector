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
# The black counterpart is a separate solid, never fused to the tube.
head = cq.Solid.makeCylinder(p['head_diameter']/2,p['head_length'])
shaft = cq.Solid.makeCylinder(p['shaft_diameter']/2,p['shaft_length']-p['tip_length'],cq.Vector(0,0,-p['shaft_length']+p['tip_length']))
point = cq.Solid.makeCone(0,p['shaft_diameter']/2,p['tip_length'],cq.Vector(0,0,-p['shaft_length']))
pin = cq.Solid.makeCylinder(p['pin_diameter']/2,p['head_diameter']/2+p['pin_projection'],cq.Vector(0,0,p['pin_z']),cq.Vector(0,1,0))
spike = head.fuse(shaft,point,pin).clean().translate((0,0,data['assembly']['head_shoulder_z_mm']))
parts = [('tube','Rohr',solid),('spike','Schwarzes Gegenstück',spike)]
out = ROOT/'web'/'assets'
out.mkdir(parents=True,exist_ok=True)
meshes=[]; metrics=[]
for part_id,label,shape in parts:
    assert shape.isValid() and len(shape.Solids())==1 and shape.Volume()>0
    cq.exporters.export(shape,str(out/(part_id+'-draft.step')))
    vertices,triangles=shape.tessellate(0.03,0.1)
    triangles=[t for t in triangles if (vertices[t[1]]-vertices[t[0]]).cross(vertices[t[2]]-vertices[t[0]]).Length > 1e-10]
    edges=[]
    for e in shape.Edges():
        points,_=e.sample(max(2,min(200,math.ceil(e.Length()/0.8))))
        edges.append([[round(v.x,6),round(v.y,6),round(v.z,6)] for v in points])
    meshes.append({'id':part_id,'label':label,'positions':[[round(v.x,6),round(v.y,6),round(v.z,6)] for v in vertices],'triangles':triangles,'edges':edges})
    metrics.append({'id':part_id,'label':label,'solids':1,'valid':True,'volume_mm3':shape.Volume(),'area_mm2':shape.Area(),'triangles':len(triangles)})
assembly=cq.Compound.makeCompound([shape for _,_,shape in parts])
cq.exporters.export(assembly,str(out/'connector-draft.step'))
back=cq.importers.importStep(str(out/'connector-draft.step')).val()
assert back.isValid() and len(back.Solids())==2 and abs(back.Volume()-assembly.Volume())/assembly.Volume()<1e-8
intersection=solid.intersect(spike).Volume()
assert intersection<1e-6, f'Unexpected draft interference: {intersection}'
(out/'mesh.json').write_text(json.dumps({'revision':data['revision'],'parts':meshes},separators=(',',':')))
box=assembly.BoundingBox()
data['geometry']={'valid':True,'solids':2,'parts':metrics,'volume_mm3':assembly.Volume(),'area_mm2':assembly.Area(),'bounds_mm':[box.xlen,box.ylen,box.zlen],'triangles':sum(p['triangles'] for p in metrics),'step_roundtrip':True,'intersection_mm3':intersection,'cadquery_version':cq.__version__,'linear_deflection_mm':0.03,'angular_deflection_rad':0.1}
data['parameter_sha256']=hashlib.sha256(spec.read_bytes()).hexdigest()
data['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
data['mesh_sha256']=hashlib.sha256((out/'mesh.json').read_bytes()).hexdigest()
data['step_sha256']=hashlib.sha256((out/'connector-draft.step').read_bytes()).hexdigest()
(out/'metadata.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(data['geometry'],indent=2))
