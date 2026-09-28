"""Classical vector review drawings, derived from D02 STEP and parameters.
Run build.py first. No tolerances or material properties are invented.
"""
from pathlib import Path
import json, math, hashlib
import cadquery as cq
from OCP.HLRBRep import HLRBRep_Algo, HLRBRep_HLRToShape
from OCP.HLRAlgo import HLRAlgo_Projector
from OCP.gp import gp_Ax2,gp_Pnt,gp_Dir
from OCP.BRepLib import BRepLib
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'web/assets'; meta=json.loads((A/'metadata.json').read_text());spec=json.loads((ROOT/'parameters/photo-draft.json').read_text())
assert meta['parameter_sha256']==hashlib.sha256((ROOT/'parameters/photo-draft.json').read_bytes()).hexdigest()
assert meta['step_sha256']==hashlib.sha256((A/'connector-draft.step').read_bytes()).hexdigest()
p={k:v['value'] for k,v in spec['dimensions'].items()}
tube=cq.importers.importStep(str(A/'tube-draft.step')).val()
spike=cq.importers.importStep(str(A/'spike-draft.step')).val().translate((0,0,-spec['assembly']['head_shoulder_z_mm']))
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
pdfmetrics.registerFont(TTFont('Draw',font))
pdfmetrics.registerFont(TTFont('DrawBold',font.replace('Sans.ttf','Sans-Bold.ttf')))
C=canvas.Canvas(str(A/'werkstattzeichnungen-D02.pdf'),pagesize=(420*mm,297*mm),pageCompression=1)
C.setTitle('Gartenfackel-Verbindung - Technische Prüfzeichnungen D02')
C.setAuthor('Projekt garden-torch-connector')
def text(x,y,s,size=3.5,bold=False,align='left'):
 C.setFont('DrawBold' if bold else 'Draw',size)
 getattr(C,{'left':'drawString','center':'drawCentredString','right':'drawRightString'}[align])(x,y,str(s))
def line(x1,y1,x2,y2,w=.25,dash=None):
 C.setLineWidth(w);C.setDash(dash or []);C.line(x1,y1,x2,y2);C.setDash([])
def arrow(x,y,dx,dy):
 n=math.hypot(dx,dy);dx,dy=dx/n,dy/n
 q=C.beginPath();q.moveTo(x,y);q.lineTo(x+3*dx+.55*dy,y+3*dy-.55*dx);q.lineTo(x+3*dx-.55*dy,y+3*dy+.55*dx);q.close();C.drawPath(q,fill=1,stroke=0)
def dh(x1,x2,y,obj1,obj2,label):
 for x,o in [(x1,obj1),(x2,obj2)]:line(x,o+(1 if y>o else -1),x,y+(2 if y>o else -2))
 line(x1,y,x2,y);arrow(x1,y,1,0);arrow(x2,y,-1,0);text((x1+x2)/2,y+1.8,label,align='center')
def dv(y1,y2,x,obj1,obj2,label):
 for y,o in [(y1,obj1),(y2,obj2)]:line(o+(1 if x>o else -1),y,x+(2 if x>o else -2),y)
 line(x,y1,x,y2);arrow(x,y1,0,1);arrow(x,y2,0,-1)
 C.saveState();C.translate(x-1.8,(y1+y2)/2);C.rotate(90);text(0,0,label,align='center');C.restoreState()
def leader(x,y,tx,ty,label):
 line(x,y,tx,ty);arrow(x,y,tx-x,ty-y);line(tx,ty,tx+10,ty);text(tx+11,ty-1,label)
def axis(x1,y1,x2,y2):line(x1,y1,x2,y2,.18,[8,1.5,1,1.5])
def project(shape,x,y,scale=1,normal=(0,1,0),right=(0,0,1),hidden=True):
 h=HLRBRep_Algo();h.Add(shape.wrapped);h.Projector(HLRAlgo_Projector(gp_Ax2(gp_Pnt(),gp_Dir(*normal),gp_Dir(*right))));h.Update();h.Hide();hs=HLRBRep_HLRToShape(h)
 for names,dashed in [(['HCompound','OutLineHCompound'],True),(['VCompound','Rg1LineVCompound','OutLineVCompound'],False)]:
  if dashed and not hidden:continue
  C.setLineWidth(.18 if dashed else .5);C.setDash([2,1] if dashed else [])
  for name in names:
   sh=getattr(hs,name)()
   if sh.IsNull():continue
   BRepLib.BuildCurves3d_s(sh,1e-7)
   for e in cq.Shape(sh).Edges():
    if e.Length()<1e-7:continue
    pts,_=e.sample(max(16,min(4000,math.ceil(e.Length()*scale/.15))))
    path=C.beginPath();path.moveTo(x+scale*pts[0].x,y+scale*pts[0].y)
    for v in pts[1:]:path.lineTo(x+scale*v.x,y+scale*v.y)
    C.drawPath(path)
 C.setDash([])
def frame(n,name,number,scale):
 C.saveState();C.scale(mm,mm);C.setLineWidth(.5);C.rect(15,10,395,277)
 text(23,278,'GARTENFACKEL-VERBINDUNG',5,bold=True)
 text(403,278,'PRÜFZEICHNUNG · NICHT ZUR FERTIGUNG',4,bold=True,align='right')
 text(23,269,'Alle Maßzahlen: unbestätigter Foto-Entwurf D02. Keine Allgemeintoleranz festgelegt.',3.5)
 # Title block, bottom right: 180 x 40 mm.
 C.rect(230,10,180,40);line(230,22,410,22);line(230,34,410,34);line(230,42,410,42)
 line(315,10,315,22);line(357,10,357,22);line(385,10,385,22)
 text(233,45,name,4.5,bold=True);text(233,37,'Werkstoff / Oberfläche: offen',3.2);text(327,37,'Toleranzen / Passung: offen',3)
 text(233,29,'Zeichnungs-Nr.: '+number,3.5);text(365,29,'Rev. D02',3.5)
 text(233,17,'Erstellt: 28.09.2026',3);text(233,12,'Prüfung / Freigabe: offen',2.7)
 text(318,17,'Maßstab '+scale,3);text(318,12,'Maße in mm',3)
 text(360,17,'A3 quer',3);text(360,12,'420 × 297',2.7);text(388,17,'Blatt',3);text(388,12,f'{n} / 3',3)
 text(23,43,'Drucken: A3, 100 % / tatsächliche Größe.',3.2)
 text(23,37,'Nicht vom Ausdruck abmessen. Maßzahlen zuerst bestätigen.',3.2)
 text(23,31,'Strichpunkt: Achse · gestrichelt: verdeckte Kante.',3)
 text(23,25,'Klassische Darstellung; keine historische Normfreigabe.',3)
 line(23,17,73,17,.5);line(23,15,23,19);line(73,15,73,19);text(78,16,'Kontrollstrecke 50 mm',3)
def end():C.restoreState();C.showPage()
# 1: tube, main view normal +Y, left end view to its right (first-angle placement).
frame(1,'Rohr mit Steck-Dreh-Ausschnitt','GF-01','1:1 / 3:1')
x,y=45,222;D=p['outer_diameter'];r=D/2
project(tube,x,y);axis(x-7,y,x+p['length']+7,y)
text(45,246,'Vorderansicht (Blick auf Längsschlitz)',3.5)
dh(x,x+p['length'],253,y+r,y+r,str(p['length']))
project(tube,315,y,normal=(0,0,-1),right=(0,1,0));axis(295,y,335,y);axis(315,y-20,315,y+20)
text(277,247,'Stirnansicht vom Schlitzende',3.5)
leader(315+r*.707,y+r*.707,343,244,'Ø'+str(D))
leader(315-p['inner_diameter']/2,y,279,198,'Ø'+str(p['inner_diameter']))
text(245,181,'Ansicht vom linken Ende rechts angeordnet',3)
text(245,176,'(Projektionsmethode 1).',3)
# enlarged CAD crop, clipped after z45. Artificial crop edge labelled.
cut=tube.intersect(cq.Solid.makeBox(80,80,45,cq.Vector(-40,-40,0)))
x,y,s=45,115,3
project(cut,x,y,s);axis(x-6,y,x+142,y)
text(x,166,'DETAIL Z · Schlitzbereich 3:1',4,bold=True)
text(x,160,'Ausschnitt z = 0 ... 45; rechte Schnittkante nur Darstellungsgrenze.',3)
dh(x,x+p['slot_depth']*s,65,y-p['slot_width']*s/2,y-p['slot_width']*s/2,str(p['slot_depth']))
dh(x,x+p['branch_z']*s,80,y-8,y-8,str(p['branch_z']))
dh(x+p['branch_z']*s,x+(p['branch_z']+p['branch_height'])*s,145,y+8,y+8,str(p['branch_height']))
dv(y-p['slot_width']*s/2,y+p['slot_width']*s/2,30,x,x,str(p['slot_width']))
leader(x+(p['slot_depth']-p['slot_width']/2)*s,y-p['slot_width']*s/2,177,87,'R2,5 (Modellannahme)')
text(248,151,'AUSSCHNITT / ABZWEIG',3.5,bold=True)
notes=['Abzweig: z = 18 bis 24 ab Schlitzende.', 'Umfangswinkel im Modell: 65° ab Schlitzmitte', 'zur oben gezeigten Abzweigseite.', 'Gerades Abzweigende geometrisch vereinfacht.', '', 'Wandstärke rechnerisch: (27 - 25) / 2 = 1.', 'Beide Durchmesser separat nachmessen.', '', 'Schlitzradius und Abzweigkontur am Original prüfen.', 'Quellen: Fotos 05, 10, 11, 15.']
for i,t in enumerate(notes):text(248,142-i*6,t,3.2)
end()
# 2: spike unshifted local coordinates. Normal -X, right +Z, up +Y.
frame(2,'Schwarzes Gegenstück mit radialem Stift','GF-02','1:1 / 2:1')
x,y,s=150,215,1
project(spike,x,y,s,normal=(-1,0,0));axis(42,y,190,y)
text(45,256,'Seitenansicht · Kopf, Schaft und Spitze',3.5)
L=p['shaft_length'];T=p['tip_length'];H=p['head_length'];R=p['head_diameter']/2;rs=p['shaft_diameter']/2
# start x50 end180, main dimension chains below.
dh(x-L,x,187,y-rs,y-R,str(L));dh(x,x+H,187,y-R,y-R,str(H))
dh(x-L,x+H,173,y-rs,y-R,f'({L+H})')
dh(x-L,x-L+T,201,y,y-rs,str(T))
dh(x,x+p['pin_z'],252,y+R,y+R+p['pin_projection'],str(p['pin_z']))
dv(y-R,y+R,202,x+H,x+H,'Ø'+str(p['head_diameter']))
dv(y-rs,y+rs,31,x-L+T,x-L+T,'Ø'+str(p['shaft_diameter']))
text(235,253,'Stirnansicht auf Kopf (rechts)',3.5)
# right end viewed from +Z, first-angle on left normally; label isolated instead.
project(spike,306,215,normal=(0,0,1),right=(1,0,0));axis(286,215,326,215);axis(306,195,306,250)
text(239,190,'Separat angeordnete Ansicht; Blickrichtung +Z → -Z.',3)
# enlarged head excluding shaft, show shoulder edge, cut no invented components.
headcrop=spike.intersect(cq.Solid.makeBox(100,100,H,cq.Vector(-50,-50,0)))
x,y,s=95,97,2
project(headcrop,x,y,s,normal=(-1,0,0));axis(88,y,164,y)
text(237,164,'DETAIL K · Kopf und Stift 2:1',4,bold=True)
dh(x,x+H*s,63,y-R*s,y-R*s,str(H))
dh(x,x+p['pin_z']*s,164,y+R*s,y+(R+p['pin_projection'])*s,str(p['pin_z']))
dv(y+R*s,y+(R+p['pin_projection'])*s,183,x+p['pin_z']*s,x+p['pin_z']*s,str(p['pin_projection']))
leader(x+(p['pin_z']+p['pin_diameter']/2)*s,y+(R+8)*s,190,135,'Ø'+str(p['pin_diameter']))
for i,t in enumerate(['Kopf, Schaft und Stift im CAD zu einem Solid vereint.', 'Dies legt kein Herstell- oder Fügeverfahren fest.', 'Stiftüberstand ab Mantelfläche des Kopfes.', 'Stiftmitte ab Kopfschulter bemaßt.', 'Kegelspitze idealisiert; keine Spitzenfase festgelegt.', '(130) = abgeleitetes Hilfsmaß.', 'Schwarz: beobachtete Farbe, Werkstoff unbekannt.', 'Quellen: Fotos 02, 03, 08, 09, 14, 16.']):text(237,148-i*8,t,3.2)
end()
# 3: actual STEP assembly.
frame(3,'Zusammenbau / Teileübersicht','GF-00','1:1')
assembly=cq.importers.importStep(str(A/'connector-draft.step')).val()
project(assembly,145,220,normal=(-1,0,0));axis(42,220,335,220)
text(30,253,'Zusammengesteckt · illustrative Lage, nicht als Verriegelung bestätigt',4,bold=True)
leader(270,233.5,290,251,'1');leader(80,226,55,246,'2')
text(30,185,'STÜCKLISTE DES MODELLS',4,bold=True)
rows=[['Pos.','Anzahl','Benennung','Zeichnung','Werkstoff'],['1','1','Rohr mit Ausschnitt','GF-01','offen'],['2','1','Schwarzes Gegenstück','GF-02','offen']]
xs=[30,48,72,218,268,388];top=179
for j,row in enumerate(rows):
 yy=top-j*11;line(xs[0],yy,xs[-1],yy)
 for k,t in enumerate(row):text(xs[k]+2,yy-7,t,3.5,bold=j==0)
line(xs[0],top-33,xs[-1],top-33)
for xx in xs:line(xx,top,xx,top-33)
text(30,132,'MONTAGEANNAHME IM ENTWURF',3.5,bold=True)
for i,t in enumerate(['Kopfschulter 6 mm hinter dem geschlitzten Rohrende.', 'Abgeleitet: 18 + 6/2 - 15 = 6; Stiftmitte bei z = 21.', 'Stift zeigt zur Längsschlitzmitte; Drehbewegung nicht geprüft.', 'Zwei separate Volumenkörper; im Modell keine Überschneidung.', 'Einstecktiefe, Drehrichtung und Verriegelung am Original klären.']):text(30,123-i*7,t,3.3)
text(230,132,'VOR FERTIGUNGSFREIGABE FESTLEGEN',3.5,bold=True)
for i,t in enumerate(['Maße beider Teile direkt messen und bestätigen.', 'Passung Kopf / Rohr und Stift / Schlitz abstimmen.', 'Material, Oberfläche und Fügeverfahren festlegen.', 'Maßtoleranzen, Kanten und Rauheit festlegen.', 'Funktion und Belastbarkeit praktisch prüfen.']):text(230,123-i*7,t,3.3)
text(30,73,'Geometriequelle: CadQuery / STEP D02. Alle Zeichnungen aus derselben Revision.',3)
text(30,66,'Parameter-SHA256: '+meta['parameter_sha256'][:32]+'…',2.8)
end();C.save()
print(A/'werkstattzeichnungen-D02.pdf')
