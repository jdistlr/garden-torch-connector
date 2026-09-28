"""Raster previews from the existing D-V03 meshes, no new CAD geometry.
Camera projection and lighting only. Poses are supplied from montage-d.js.
"""
from pathlib import Path
import json, math, hashlib
import numpy as np
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[1]; O=R/'web/assets/ux'; O.mkdir(exist_ok=True)
poses=json.loads((O/'poses.json').read_text())
W,H,S=800,720,2
# Orthonormal orthographic camera basis: view from +X/+Y, Z up.
eye=np.array([1.05,1.65,1.05]);eye/=np.linalg.norm(eye)
right=np.cross([0,0,1],eye);right/=np.linalg.norm(right)
up=np.cross(eye,right);light=np.array([-.4,.2,1.]);light/=np.linalg.norm(light)
def render(parts,mode,pose=None):
 eye=np.array([1.05,-1.65 if mode=="section" or (pose and 2<=pose["q"]<=3) else 1.65,1.05]);eye/=np.linalg.norm(eye)
 right=np.cross([0,0,1],eye);right/=np.linalg.norm(right);up=np.cross(eye,right)
 triangles=[];all_points=[]
 for p in parts:
  m=p['section'] if mode=='section' or (pose and 2<=pose['q']<=3 and p['id']!='tube') else p['full']
  v=np.array(m['positions'],float); t=np.array(m['triangles'],int)
  if mode=='exploded':v[:,2]+=p.get('explode',0)*.62;v[:,1]+=p.get('explode_y',0)*.62
  if pose:
   a=math.radians(pose['angle']) if p['id']=='tube' else pose.get('screwAngle',0) if p['id']=='screw' else 0
   v=v@np.array([[math.cos(a),math.sin(a),0],[-math.sin(a),math.cos(a),0],[0,0,1]])
   v[:,2]+=pose[p['id']]
   if p['id']=='pin':v[:,1]+=pose['pinY']
  proj=np.stack([v@right,-v@up,v@eye],axis=1);all_points.extend(proj[:,:2])
  color=np.array([int(p['color'][i:i+2],16) for i in (1,3,5)])
  for f in t:
   pts=v[f];normal=np.cross(pts[1]-pts[0],pts[2]-pts[0]);n=np.linalg.norm(normal)
   if n<1e-10:continue
   normal/=n
   # Include back faces: cut surfaces and hollow interiors remain visible with painter sorting.
   shade=.70+.30*abs(np.dot(normal,light));rgb=tuple(np.clip(color*shade,0,255).astype(int))
   triangles.append((proj[f,2].mean(),proj[f],rgb))
 bounds=np.array(all_points);mn=bounds.min(axis=0);mx=bounds.max(axis=0)
 # A consistent framing across assembly steps avoids perceived part scaling.
 if pose:mn=np.minimum(mn,[-115,-310]);mx=np.maximum(mx,[115,70])
 scale=min((W-100)/(mx[0]-mn[0]),(H-90)/(mx[1]-mn[1]));center=(mn+mx)/2
 pixels=np.empty((H*S,W*S,3),dtype=np.uint8);pixels[:]=[241,240,237]
 depth=np.full((H*S,W*S),-np.inf)
 for _,pts,c in triangles:
  xy=((pts[:,:2]-center)*scale+[W/2,H/2])*S
  lo=np.maximum(np.floor(xy.min(axis=0)).astype(int),0);hi=np.minimum(np.ceil(xy.max(axis=0)).astype(int),[W*S-1,H*S-1])
  if np.any(hi<lo):continue
  (x0,y0),(x1,y1),(x2,y2)=xy;den=(y1-y2)*(x0-x2)+(x2-x1)*(y0-y2)
  if abs(den)<1e-8:continue
  yy,xx=np.mgrid[lo[1]:hi[1]+1,lo[0]:hi[0]+1];xx=xx+.5;yy=yy+.5
  a=((y1-y2)*(xx-x2)+(x2-x1)*(yy-y2))/den
  b=((y2-y0)*(xx-x2)+(x0-x2)*(yy-y2))/den;cweight=1-a-b
  z=a*pts[0,2]+b*pts[1,2]+cweight*pts[2,2]
  region=depth[lo[1]:hi[1]+1,lo[0]:hi[0]+1];valid=(a>=-1e-7)&(b>=-1e-7)&(cweight>=-1e-7)&(z>region)
  region[valid]=z[valid];pixels[lo[1]:hi[1]+1,lo[0]:hi[0]+1][valid]=c
 return Image.fromarray(pixels).resize((W,H),Image.Resampling.LANCZOS)
manifest={'source':'D-V03 existing model JSON and montage-d.js; orthographic preview, no physical simulation','models':{},'images':[]}
for thick in [5,8,9]:
 path=R/f'web/assets/sockel-d/model-{thick}.json';data=json.loads(path.read_text());manifest['models'][str(thick)]=hashlib.sha256(path.read_bytes()).hexdigest()
 for mode in ['assembly','section','exploded']:
  name=f'{mode}-{thick}.png';render(data['parts'],mode).save(O/name,optimize=True);manifest['images'].append(name)
 for q,pose in enumerate(poses[str(thick)]):
  pose['q']=q;name=f'step-{q}-{thick}.png';render(data['parts'],'assembly',pose).save(O/name,optimize=True);manifest['images'].append(name)
(O/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Generated',len(manifest['images']),'CAD-derived preview images.')
