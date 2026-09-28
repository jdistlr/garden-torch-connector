"""V01 concept geometries. All new dimensions are design assumptions, not measurements."""
from pathlib import Path
import json,math
import cadquery as cq
R=Path(__file__).resolve().parents[1];out=R/'web/assets/variants';out.mkdir(exist_ok=True)
p=json.loads((R/'parameters/photo-draft.json').read_text())['dimensions']
def cyl(r,h,z=0,x=0,y=0):return cq.Solid.makeCylinder(r,h,cq.Vector(x,y,z))
def box(w,d,h,z=0):return cq.Solid.makeBox(w,d,h,cq.Vector(-w/2,-d/2,z))
def bore(shape,r,z,h,x=0,y=0):return shape.cut(cyl(r,h,z,x,y))
def bolt(r,hr,hh,top,x=0,y=0):return cyl(hr,hh,0,x,y).fuse(cyl(r,top-hh,hh,x,y)).cut(cq.Workplane('XY').polygon(6,hr).extrude(hh*.65).val().translate((x,y,0)))
head=cyl(p['head_diameter']['value']/2,p['head_length']['value'],32).fuse(cq.Solid.makeCylinder(p['pin_diameter']['value']/2,29,cq.Vector(0,0,32+p['pin_z']['value']),cq.Vector(0,1,0)))
tube=cq.importers.importStep(str(R/'web/assets/tube-draft.step')).val().translate((0,0,26))
cutbox=box(400,200,400,-100).translate((0,100,0)) # keep y >= 0
colors={'plate':'#8fa5bd','adapter':'#30383f','screw':'#c59a49','pin':'#33a49a','insert':'#bd6b3d','weld':'#dd795b','tube':'#c4d2df'}
for key in 'ABCD':
 parts=[]
 def add(id,label,shape,kind,explode):parts.append((id,label,shape.clean(),kind,explode))
 plate=box(150,150,5,7)
 if key=='A':
  adapter=head.fuse(cyl(6,20,12));adapter=bore(adapter,3,12,16)
  plate=bore(plate,3.5,7,5)
  add('screw','Schraube von unten · M6 schematisch',bolt(3,5,6,24).translate((0,0,1)),'screw',-32)
 elif key=='B':
  adapter=head.fuse(cyl(6,12,20),cyl(22,8,12));adapter=bore(adapter,4,12,20);adapter=bore(adapter,2.1,12,4,16)
  plate=bore(plate,4.5,7,5);plate=bore(plate,2.1,8,4,16)
  add('screw','Schraube von unten · M8 schematisch',bolt(4,6.5,8,28).translate((0,0,-1)),'screw',-32)
  add('pin','Passstift gegen Verdrehen · Ø4 Konzept',cyl(2,8,8,16),'pin',15)
 elif key=='C':
  adapter=head.fuse(cyl(6,10,22),cyl(30,10,12))
  for i in range(3):
   ang=2*math.pi*i/3;x,y=22*math.cos(ang),22*math.sin(ang)
   adapter=bore(adapter,3,12,9,x,y);plate=bore(plate,3.5,7,5,x,y)
   add('screw'+str(i+1),'Flanschschraube '+str(i+1)+' · M6 schematisch',bolt(3,5,6,20,x,y).translate((0,0,1)),'screw',-32)
 else:
  adapter=head.fuse(cyl(12,20,12).cut(cyl(9,20,12)))
  plate=bore(plate,4.5,7,5)
  add('insert','Gewindebuchse · M8 schematisch',cyl(8.8,16,12).cut(cyl(4,16,12)),'insert',26)
  add('weld','Fügezone Buchse / Hülse · Schweißkonzept ungeprüft',cyl(9,2,12).cut(cyl(8.8,2,12)),'weld',26)
  add('screw','Schraube von unten · M8 schematisch',bolt(4,6.5,8,26).translate((0,0,-1)),'screw',-32)
 add('plate','Grundplatte · 150 × 150 × 5 · Nutzerschätzung',plate,'plate',0)
 add('adapter','Adapter '+key+' · Konzept',adapter,'adapter',55)
 add('tube','Fackelrohr D02 · Referenz',tube,'tube',85)
 meshes=[]
 for id,label,shape,kind,explode in parts:
  assert shape.isValid() and len(shape.Solids())==1 and shape.Volume()>0,(key,id)
  def mesh(s):
   v,t=s.tessellate(.04,.15)
   return {'positions':[[round(a.x,5),round(a.y,5),round(a.z,5)] for a in v],'triangles':[tri for tri in t if (v[tri[1]]-v[tri[0]]).cross(v[tri[2]]-v[tri[0]]).Length>1e-9]}
  section=shape.intersect(cutbox)
  meshes.append(dict(id=id,label=label,color=colors[kind],kind=kind,explode=explode,full=mesh(shape),section=mesh(section) if section.Volume()>1e-8 else None))
 cq.exporters.export(cq.Compound.makeCompound([s for _,_,s,_,_ in parts]),str(out/f'{key}-concept.step'))
 (out/f'{key}.json').write_text(json.dumps({'revision':'V01','variant':key,'parts':meshes},separators=(',',':')))
 print(key,[(id,len(s.Solids())) for id,_,s,_,_ in parts])
