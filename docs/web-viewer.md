# Engineering-Web-Viewer: Zielbild und Abnahme

Stand 28.09.2026. Anforderung aufgenommen; noch nicht implementiert. Der Viewer ist nun fester Bestandteil des Zielumfangs.

## Ziel

Das Verbindungsrohr im Browser räumlich untersuchen, Innenraum und Wandstärke verstehen und zugehörige Maße, Quellen und Modellkennwerte anzeigen. Desktop und Smartphone berücksichtigen. Die Oberfläche soll ohne CAD-Vorkenntnisse nutzbar sein.

## Architektur

Eine Modellrevision liefert aus CadQuery/OCCT:
- das CAD-Volumenmodell (B-Rep: Flächen, Kanten, Topologie; Berechnung mit numerischen Toleranzen),
- STEP für Austausch,
- ein daraus trianguliertes GLB für Three.js,
- Metadaten zu Parametern, Merkmalen, Kennwerten und Herkunft,
- bei Bedarf im CAD-Kern berechnete Schnittkonturen.

Three.js übernimmt Darstellung und Interaktion. Ein GLB-Dreiecksnetz ist kein exaktes CAD-Volumenmodell. Die exakte Modellquelle bleibt im CAD-Kern. Kennwerte werden dort berechnet und zusammen mit derselben Modellrevision angezeigt. Keine unabhängig nachgezeichnete Browsergeometrie.

## Erste Viewer-Version

| Bereich | Geplante Funktion |
|---|---|
| Hauptansicht | Drehen, zoomen, verschieben, Ansicht zurücksetzen |
| Technische Ansichten | Orthografisch vorn/seitlich/oben, Isometrie; Perspektive umschaltbar |
| Darstellung | Schattierte Flächen mit echten CAD-Kanten, Transparenz, Teile ein-/ausblenden |
| Schnitt | Verschiebbare Schnittebene zur visuellen Untersuchung; Schnittmaterial geschlossen darstellen, Hohlraum offen lassen |
| Bauteile | Rohr auswählen; Referenz-Erdspieß gesondert, sofern modelliert |
| Maße | Definierte CAD-Maße am passenden Merkmal einblenden |
| Downloads | STEP, PDF und Darstellung aus derselben Revision, sobald verfügbar |

Grafisches Clipping schneidet nur die Anzeige. Es ändert weder das gespeicherte CAD-Modell noch dessen Gesamtvolumen. Für genaue Schnittkonturen und Flächenkennwerte muss der CAD-Kern rechnen. Grafische Schnittkappen allein sind keine CAD-Schnittfläche.

## Informationspanels

| Panel | Inhalt |
|---|---|
| Bauteil | Name, Bauteil-ID, Modellrevision, Status |
| Maße | Länge, Durchmesser, Wandstärke, Schlitzmaße; Einheit und Bestätigungsstatus |
| Kennwerte | Materialvolumen, Oberfläche und Schwerpunkt aus CAD; Masse nur mit dokumentiertem Material und Dichte |
| Quellen | Bildnummer und Quelle des gewählten Parameters; geschätzt/gemessen/entschieden |
| Prüfung | Durchgeführte Geometrieprüfungen, offene Werte und Warnungen aus tatsächlichen Prüfergebnissen |
| Ausgabe | Passende STEP-/PDF-Dateien und Versionsangaben |

Beim Rohr bedeutet Materialvolumen das tatsächlich vorhandene Material ohne Innenraum und Ausschnitte. Unbekanntes Material erzeugt keine erfundene Masse. Prüfstatus sagt nicht automatisch etwas über Festigkeit, Wärmeeignung oder Fertigungsfreigabe aus.

## Messfunktionen und Ausbau

Zunächst definierte Maße aus dem CAD-Modell. Freies Anklicken beliebiger Mesh-Punkte liefert lediglich angenäherte Werte und müsste so gekennzeichnet werden. Exakte freie Messungen zwischen CAD-Flächen, Achsen oder Kanten benötigen CAD-Geometriezugriff und stabile Zuordnung.

Später möglich: Explosionsansicht, Montagebewegung, Parameteränderungen mit Neuberechnung, Revisionsvergleich. Physikalische Festigkeitsanalyse ist nicht Teil des Viewers.

Für echte interaktive Solid-Operationen (Boolesche Schnitte, exakte freie Messung, Regeneration) ist ein CAD-Kern im Backend oder als WebAssembly erforderlich. Das wäre ein eigener Ausbauschritt; Three.js allein reicht dafür nicht.

## Qualitätsanforderungen

- Parameter, STEP, GLB und Kennwerte tragen denselben Quell-Commit und Parameter-Hash.
- CAD in mm; GLB in Metern. Umrechnung von Länge, Fläche und Volumen explizit prüfen. UI zeigt mm, mm² und mm³.
- Tessellierungsparameter dokumentieren. Vorläufiges Exportziel: lineare Abweichung höchstens 0,05 mm, Winkelparameter 0,1 rad; nach bestätigten kleinsten Details überprüfen. Exportparameter allein belegen noch keine gemessene maximale Abweichung.
- Darstellungsgenauigkeit und Fertigungstoleranz getrennt behandeln.
- Geometrieprüfung vor Export: gültiger Volumenkörper, erwartete Anzahl von Solids, positives Materialvolumen.
- Mesh-Prüfung: geschlossene Materialoberfläche einschließlich Rohrstirnringen und Ausschnittwänden, korrekte Normalen, keine unbeabsichtigten offenen Kanten.
- Bounding Box und Materialvolumen von Mesh und CAD vergleichen; Akzeptanzgrenzen vor Release passend zur Geometrie festlegen. Volumenvergleich allein reicht nicht zur Qualitätsbewertung.
- Merkmal-IDs semantisch vergeben; nicht auf dauerhaft stabile OCCT-Flächenindizes vertrauen.
- Auswahl und Bemaßung müssen auf das richtige Merkmal zeigen; CAD-Kanten nicht durch Dreieckskanten ersetzen.
- Ungültige oder fehlende Daten deutlich anzeigen; keine Platzhalterwerte als Messung ausgeben.
- Schnittansicht gegen CAD-Querschnitt an mehreren Positionen prüfen.
- Desktop und iPhone prüfen: Touch-Bedienung, lesbare Panels, Lade-/Fehlerzustände und Leistung.
- Keine pauschale Behauptung einer Normkonformität; konkrete Prüfungen dokumentieren.

## Umsetzung

1. Maße und Montagefunktion bestätigen; CAD-Modell erstellen.
2. Gemeinsamen Export von Modell, Kennwerten und Metadaten aufbauen.
3. Viewer mit Standardansichten, Auswahl und Informationspanels umsetzen.
4. Schnittdarstellung und definierte Maße ergänzen, visuell und numerisch prüfen.
5. Hosting festlegen und veröffentlichen. GitHub Pages bleibt ein Kandidat für statische Darstellung; Live-CAD-Neuberechnung erfordert zusätzliche Infrastruktur oder einen Browser-CAD-Kern.

## Offizielle technische Referenzen

- https://threejs.org/docs/pages/GLTFLoader.html
- https://threejs.org/docs/pages/Material.html
- https://cadquery.readthedocs.io/en/latest/classreference.html
- https://cadquery.readthedocs.io/en/latest/importexport.html
