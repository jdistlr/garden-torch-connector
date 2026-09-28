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
A=ROOT/'web/assets/sockel-d'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
pdfmetrics.registerFont(TTFont('Draw',font));pdfmetrics.registerFont(TTFont('DrawBold',font.replace('Sans.ttf','Sans-Bold.ttf')))
C=canvas.Canvas(str(A/'zeichnungen-D-V02.pdf'),pagesize=(420*mm,297*mm),pageCompression=1)
C.setTitle('Variante D-V02 - Prüfzeichnungen mit versenktem Kopf')
parts={n:cq.importers.importStep(str(A/(n+'-5.step'))).val() for n in ['plate','adapter','insert','screw','weld']}
cut=cq.Solid.makeBox(400,200,300,cq.Vector(-200,0,-50))
def front(s,x,y,scale=1):project(s,x,y,scale,normal=(0,-1,0),right=(1,0,0))
def section(s,x,y,scale=1):
 half=s.intersect(cut)
 for face in half.Faces():
  b=face.BoundingBox()
  if b.ylen>1e-5 or abs(b.ymin)>1e-5:continue
  path=C.beginPath()
  for wire in face.Wires():
   pts,_=wire.sample(max(40,min(1800,int(wire.Length()/.1))))
   path.moveTo(x+pts[0].x*scale,y+pts[0].z*scale)
   for v in pts[1:]:path.lineTo(x+v.x*scale,y+v.z*scale)
   path.close()
  C.saveState();C.clipPath(path,stroke=0,fill=0,fillMode=0)
  for k in range(-400,800,3):line(k,0,k+300,300,.15)
  C.restoreState()
 front(half,x,y,scale)
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
 text(23,269,'D-V02: Konstruktionsannahmen / unbestätigte Maße. Keine Allgemeintoleranz festgelegt.',3.5)
 # Title block, bottom right: 180 x 40 mm.
 C.rect(230,10,180,40);line(230,22,410,22);line(230,34,410,34);line(230,42,410,42)
 line(315,10,315,22);line(357,10,357,22);line(385,10,385,22)
 text(233,45,name,4.5,bold=True);text(233,37,'Werkstoff / Oberfläche: offen',3.2);text(327,37,'Toleranzen / Passung: offen',3)
 text(233,29,'Zeichnungs-Nr.: '+number,3.5);text(365,29,'Rev. D-V02',3.5)
 text(233,17,'Erstellt: 28.09.2026',3);text(233,12,'Prüfung / Freigabe: offen',2.7)
 text(318,17,'Maßstab '+scale,3);text(318,12,'Maße in mm',3)
 text(360,17,'A3 quer',3);text(360,12,'420 × 297',2.7);text(388,17,'Blatt',3);text(388,12,f'{n} / 3',3)
 text(23,43,'Drucken: A3, 100 % / tatsächliche Größe.',3.2)
 text(23,37,'Nicht vom Ausdruck abmessen. Maßzahlen zuerst bestätigen.',3.2)
 text(23,31,'Strichpunkt: Achse · gestrichelt: verdeckte Kante.',3)
 text(23,25,'Klassische Darstellung; keine historische Normfreigabe.',3)
 line(23,17,73,17,.5);line(23,15,23,19);line(73,15,73,19);text(78,16,'Kontrollstrecke 50 mm',3)
def end():C.restoreState();C.showPage()

frame(1,'Grundplatte / bündige Senkung','GF-D-01','1:1 / 4:1')
text(25,252,'Unterseite · Senkung von unten',4,bold=True)
project(parts['plate'],115,162,normal=(0,0,-1),right=(1,0,0));axis(33,162,197,162);axis(115,80,115,244)
dh(40,190,76,87,87,'150');dv(87,237,205,190,190,'150')
leader(123.2,162,149,184,'Ø16,4 × 90° (Annahme)')
text(244,246,'Schnitt / Kopfauflage 4:1',4,bold=True)
local=parts['plate'].intersect(cq.Solid.makeBox(34,34,10,cq.Vector(-17,-17,0)))
section(local,320,177,4);front(parts['screw'].intersect(cut),320,177,4)
line(245,177,401,177,.35,[3,1]);text(245,169,'Bodenebene z = 0',3.5)
dv(177,197,395,388,388,'5')
leader(320-8*4,177+.2*4,250,149,'Kopffläche 0,2 zurückgesetzt')
leader(320+4.5*4,177+3.7*4,341,218,'Ø9 Durchgang')
for i,t in enumerate(['90°-Senkung idealisiert: Tiefe 3,7.', 'Restdicke am Bohrungsrand: 1,3.', 'Kein Teil unter der Auflageebene.', 'Schrauben-Hüllmodell M8 × 20; Kopf Ø16.', 'Kopfrand, Übergänge und Toleranzen fehlen.', 'Reales Kaufteil vor Senkungsauslegung wählen.', '8 / 9 mm: siehe separate STEP-Modelle.']):text(242,134-i*8,t,3.3)
end()
frame(2,'Aufnahme / separate Gewindebuchse','GF-D-02','2:1 / 3:1')
adapter=parts['adapter'].translate((0,0,-5));insert=parts['insert'].translate((0,0,-5))
text(28,252,'Hülse und Kopf · Längsschnitt',4,bold=True)
section(adapter,92,121,2);axis(92,112,92,229)
dv(121,221,45,68,68,'50');dv(121,161,130,116,116,'20');dv(161,221,145,116,116,'30')
dh(68,116,107,121,121,'Ø24');dh(74,110,94,121,121,'Ø18')
leader(96,191,161,212,'Querstift Ø4 / Überstand 17')
text(247,252,'Gewindebuchse · Längsschnitt 3:1',4,bold=True)
section(insert,302,173,3);axis(302,164,302,230)
dh(275.6,328.4,159,173,173,'Ø17,6');dv(173,221,350,328.4,328.4,'16')
leader(314,201,347,231,'M8 · schematisch')
for i,t in enumerate(['Gewinde im CAD glatt mit Nenndurchmesser.', 'Fügezone 1 bis 3 mm über Unterkante.', 'Fügeverfahren und Nahtmaß noch auszulegen.', 'Unterkante nach dem Fügen plan / gratfrei.', 'Material und Schweißbarkeit nicht festgelegt.', 'Die Buchse muss Zug und Drehmoment übertragen.', 'Keine freigegebene Toleranz oder Rauheit.']):text(235,139-i*8,t,3.3)
text(27,73,'Kopf und Querstift: D02-Fotoschätzungen. Hülse und Buchse: neue Konstruktionsannahmen.',3.2)
end()
frame(3,'Variante D / Montage und Prüfung','GF-D-00','2:1 Detail')
text(25,251,'Montageschnitt · Fackelrohr ausgeblendet',4,bold=True)
for name in ['plate','adapter','insert','weld']:
 shape=parts[name]
 if name=='plate':shape=shape.intersect(cq.Solid.makeBox(64,64,8,cq.Vector(-32,-32,0)))
 section(shape,99,125,2)
front(parts['screw'].intersect(cut),99,125,2)
line(25,125,181,125,.5);text(25,115,'Boden / Auflageebene z = 0',3.5)
leader(108,149,155,165,'1 · Gewindebuchse')
leader(104,139,155,146,'2 · Senkschraube')
text(238,246,'GEOMETRISCHE PRÜFUNG',4,bold=True)
for i,t in enumerate(['Platte: 150 × 150 × 5 mm.', 'Kopfunterseite: z = +0,2 mm.', 'Kein Unterstand; kein Kollisionvolumen.', '6 gültige Solids inkl. Rohr; STEP rückgelesen.', 'Nominaler Eingriff: 15,2 mm (vereinfacht).', 'Freiraum bis Buchsenende: 0,8 mm.', 'Gewindeauslauf / Fasen noch nicht enthalten.']):text(238,236-i*8,t,3.3)
text(238,167,'VOR FERTIGUNG',4,bold=True)
for i,t in enumerate(['Kaufteil, Werkstoffe und Standardhalbzeuge wählen.', 'Senkung und Toleranzkette gegen Kopf prüfen.', 'Fügezone, Vorspannung und Losdrehen prüfen.', 'Steck-Dreh-Weg / tatsächliche Rastung prüfen.', 'Standsicherheit der ganzen Fackel prüfen.']):text(238,157-i*8,t,3.3)
text(25,86,'Montage: Buchse sichern → Aufnahme auflegen → Schraube von unten anziehen → Platte absetzen.',3.2)
text(25,78,'Erst danach Fackelrohr aufschieben und erst nach Prüfung der Steck-Dreh-Funktion verbinden.',3.2)
text(25,65,'Senkungs-/Gewindeangaben sind Konzeptwerte. Keine Traglast oder Fertigungsfreigabe.',3.2)
end();C.save()
