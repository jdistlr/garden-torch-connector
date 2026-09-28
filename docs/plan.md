# Projektplan

## 1. Quellenbasis — abgeschlossen

- 16 vorhandene JPEG-Dateien visuell als Übersicht gesichtet.
- Prüfsummen ermittelt; 07 entspricht 02 und 12 entspricht 03.
- 14 Vorschauen, Quellenzuordnung und Original-Prüfsummen im Repository.
- Sichtbar: hohles Metallrohr, vom Ende offener Längsschlitz mit gerundetem Ende und seitlicher Aussparung; separater spitzer Einsatz mit zylindrischem Kopf und radialem Stift.
- Materialgüte, Belastbarkeit und genaue Maße sind aus den Bildern nicht belegt.

## 2. Maßaufnahme und Funktionsklärung — nächster Schritt

Maßtabelle gemeinsam vervollständigen. Erst Gesamtmaße, danach Schlitz und Gegenstück. Fotoablesungen als Schätzung kennzeichnen und direkt am Bauteil bestätigen. Klären, ob eine Kopie oder eine geänderte Ausführung gewünscht ist und wie die Fackel am anderen Rohrende befestigt wird.

Ergebnis: bestätigte Parameter mit Quelle, Messmethode und Datum.

## 3. Parametrisches Modell — geplant

CadQuery-Modell des Rohres mit getrennten Merkmalen für Grundkörper, Längsschlitz und seitliche Aussparung. Referenzkörper für den Erdspieß optional. Maße zentral aus parameters/connector.json lesen. Keine parallelen, unabhängig gepflegten OpenSCAD- und CadQuery-Geometrien.

Prüfen: positiver Wandquerschnitt, Ausschnitte nur in beabsichtigter Wand, gültiger Volumenkörper, richtige Endlage und Kollisionsfreiheit entlang der bestätigten Montagebewegung. Ein Kollisionscheck allein belegt weder Spiel noch Festigkeit.

## 4. Zeichnung und Review — geplant

STEP-Export; FreeCAD/TechDraw für Ansichten, Schnitt und Schlitzdetail. Ansichten aus dem Modell ableiten. Maßtext nicht unabhängig von den Modellparametern eintippen. Beim Import eines STEP-Modells entsteht nicht automatisch der originale parametrische Modellbaum; CadQuery bleibt die Modellquelle.

Gemeinsam prüfen: Öffnungsrichtung, Drehrichtung, Gegenstück, Maßbezüge, Material, Oberfläche, Kanten und erforderliches Spiel. Toleranzen mit dem Fertiger abstimmen.

## 5. Auftragspaket — geplant

PDF, STEP, optional STL für einen Anschauungsprototyp, Renderansichten und Auftragsbeschreibung. Paket mit Revision, Commit, Erstellungsdatum und Freigabestatus versehen. Noch offene Werte verhindern die Kennzeichnung als fertigungsfreigegeben.

## 6. Automatisierung und Präsentation — optional

Nach erfolgreichem lokalem Modellaufbau Abhängigkeiten versionieren und GitHub Actions zur regenerierbaren Erstellung der Exporte ergänzen. Browseransicht mit Drehen/Zoomen und Downloads; Veröffentlichung separat umsetzen. Nicht jeder Push erzeugt eine Fertigungsfreigabe.

## Abnahmekriterien

- Alle produktionsrelevanten Maße und Anforderungen geklärt.
- CAD-Volumenkörper gültig und STEP wieder einlesbar.
- Zeichnung und Modell stimmen überein.
- Montagefunktion am Gegenstück geprüft; nötigenfalls Musterteil.
- Versioniertes Auftragspaket durch Auftraggeber freigegeben.
