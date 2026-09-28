// D-V03 poses share the exported CAD coordinates; dimensions are concept values.
export const steps = [
 ['Teile vorbereiten', 'Platte auf geeigneten Montageauflagen halten (hier schematisch 35 mm angehoben). Aufnahme, Stift, Schraube und Rohr getrennt. Keine Fertigungsfreigabe.'],
 ['Querstift · Fertigung', 'Stift radial einsetzen. Die Bewegung zeigt nur die Einsetzrichtung; Passung, Einpresskraft und Sicherungsverfahren sind offen. Vor Benutzermontage muss der Stift gesichert sein.'],
 ['Aufnahme aufsetzen', 'Massive Aufnahme auf die saubere, plane Oberseite setzen. Das axiale Sacklochgewinde liegt direkt im Vollmaterial.'],
 ['Von unten verschrauben', 'Senkschraube von unten zuführen und einschrauben. Drehung mit 1,25 mm Konzeptsteigung; glatte Gewindehüllen zeigen keine Gewindeflanken. Anzugsmoment und Losdrehsicherung noch festlegen.'],
 ['Plan absetzen', 'Montageauflagen entfernen und Sockel absetzen. Im idealen Modell liegt die Kopffläche 0,2 mm über der Bodenebene. Am realen Teil mit Richtkante prüfen.'],
 ['Schlitz ausrichten', 'Offenen Längsschlitz auf den radialen Stift ausrichten. Das Rohr steht 40 mm über seiner Einführlage.'],
 ['Rohr aufschieben', 'Axial absenken, bis die Stiftmitte auf der Mitte des seitlichen Ausschnitts liegt. Keine Verdrehung während des Einführens.'],
 ['50° verdrehen · keine Rastung', 'Blick von oben zur Platte: Rohr gegen den Uhrzeigersinn drehen. 50° ist eine geprüfte Darstellungsposition vor dem nominalen Anschlag bei ca. 55,8°. Der Rückweg bleibt frei; keine Rückdrehsicherung nachgewiesen.']
];
// Integer positions are completed target poses; in-between describes the action toward the next pose.
export function stepAt(value) { return Math.min(7,Math.max(0,Math.ceil(value-1e-9))); }
export function poseAt(value, thickness) {
 const q=Math.max(0,Math.min(7,value)),i=Math.min(6,Math.floor(q)),u=q-i,s=u*u*(3-2*u);
 const frames=[
 {plate:35,adapter:75,pin:75,screw:8,tube:120,pinY:25,angle:0},
 {plate:35,adapter:75,pin:75,screw:8,tube:120,pinY:0,angle:0},
 {plate:35,adapter:35,pin:35,screw:8,tube:120,pinY:0,angle:0},
 {plate:35,adapter:35,pin:35,screw:35,tube:120,pinY:0,angle:0},
 {plate:0,adapter:0,pin:0,screw:0,tube:120,pinY:0,angle:0},
 {plate:0,adapter:0,pin:0,screw:0,tube:40,pinY:0,angle:0},
 {plate:0,adapter:0,pin:0,screw:0,tube:0,pinY:0,angle:0},
 {plate:0,adapter:0,pin:0,screw:0,tube:0,pinY:0,angle:50}
 ];
 const out={};for(const k of Object.keys(frames[0]))out[k]=frames[i][k]+(frames[i+1][k]-frames[i][k])*s;
 // Positive Z rotation is clockwise when looking at the head from below.
 const travel=q<2?0:q<3?Math.max(0,out.screw+20.2-(35+thickness)):20.2-thickness;
 out.screwAngle=travel/1.25*Math.PI*2;return out;
}
