# Aktueller Einstieg D-V03

Root `index.html` führt zu `web/variants.html`. Lokal: `python3 -m http.server 8765 --directory web`, dann `/variants.html` öffnen. `/index.html` innerhalb web zeigt weiterhin die Originalreferenz D02.

D-V03: `python3 model/check_motion_d.py` prüft den nominalen Rohrweg aus STEP und schreibt `motion-checks.json`. `python3 model/cost_d.py` erzeugt die Kostenszenarien. `node model/render_docs.cjs` (Node mit Paket `marked`) erzeugt druckbare HTML-Seiten aus den vier neuen Markdown-Dokumenten. Für diese Erweiterung wurden CAD/STEP/A3-Dateien nicht verändert.

Die Montageanimation in `web/montage-d.js` verwendet dieselben CAD-Teile. 50° ist eine Demonstrationsposition vor dem Anschlag, nicht eine bestätigte Endlage. STEP und freie Ansicht starten weiterhin bei0°. Automatisches Abspielen nur nach Betätigung; Tabwechsel pausiert; reduzierte Bewegung wählt langsames Tempo. Schnitt/Transparenz bleiben benutzbar. Keine Handsimulation, keine Gewinde-/Kontaktkraftsimulation.

## Historisches D02-Runbook

# Viewer D02

Statische Three.js-Anwendung unter `web/`. Alle Browserabhängigkeiten liegen lokal unter `web/vendor` (Three.js 0.180.0, MIT-Lizenz beigefügt). Keine CDN-Abhängigkeit, kein Backend.

## Lokal ansehen

Im Repository `python3 -m http.server 8765 --directory web` ausführen und http://localhost:8765 öffnen. Nicht index.html per file:// starten, da JSON-Daten geladen werden.

## Modell neu erzeugen

CadQuery 2.7.0 installieren: `python3 -m pip install -r model/requirements.txt`. Danach `python3 model/build.py` ausführen. Das Skript liest ausschließlich `parameters/photo-draft.json` und erzeugt STEP, Browsermesh und Metadaten unter web/assets. `parameters/connector.json` bleibt der unveränderte Platz für bestätigte Maße.

D02 ist ein ausdrücklich unbestätigter Foto-Entwurf. Geschätzte Werte und ihre Bildquellen sind in der separaten Parameterdatei gespeichert. Der seitliche Ausschnitt ist geometrisch vereinfacht. Mesh und STEP werden aus denselben zwei CAD-Körpern erzeugt. Dieser erste Viewer nutzt ein Mesh-JSON mit Millimeterkoordinaten; GLB ist nicht nötig. Keine Umrechnung in Meter findet statt.

Parameter-, Generator-, STEP- und Mesh-Prüfsummen sind in metadata.json festgehalten. Modellgeometrie und STEP-Rückimport werden beim Erzeugen geprüft. CAD-Volumen und Oberfläche sind Kennwerte des Entwurfs, keine Messungen am Original.

## GitHub Pages

Der vorhandene Pages-Dienst veröffentlicht den main-Branch aus dem Repository-Stamm. index.html führt nach web/. Es wird kein zweiter eigener Deployment-Workflow benötigt.

Öffentlicher Einstieg: https://jdistlr.github.io/garden-torch-connector/

Direkter Viewer: https://jdistlr.github.io/garden-torch-connector/web/

Den Lauf „pages build and deployment“ unter Actions prüfen. Der erste eigene Deploy-Lauf war erfolgreich; für weitere Änderungen wird ausschließlich die bestehende Branch-Veröffentlichung genutzt.

## Korrektur D02

Das schwarze Gegenstück gehört zum Modellumfang. Kopf, Schaft, konische Spitze und radialer Stift bilden einen eigenen Solid. Die gemeinsame STEP-Datei enthält zwei getrennte Solids in illustrativer Montagelage; Einzeldateien behalten dasselbe Bezugssystem. Der Viewer startet getrennt und kann beide Teile zusammensetzen oder ausblenden. Diese Anzeigeverschiebung verändert die CAD-Kennwerte nicht.

## Technische Zeichnungen

Nach `python3 model/build.py` erzeugt `python3 model/drawings.py` die drei A3-Prüfzeichnungen. Anleitung und Darstellungsgrenzen: [drawings.md](drawings.md). Der PDF-Download ist im Viewer neben STEP eingebunden.

## Gesamten schematischen Montageweg prüfen

`node model/export_assembly_poses.mjs /tmp/torch-poses.json`, dann `python3 model/check_assembly_d.py /tmp/torch-poses.json`. Je71Posen für5/8/9mm prüfen alle Körperpaare und die Bodenebene. Das ergänzt die feinere Rohrprüfung; Stiftpressung und Schraubengewindeflanken werden nicht simuliert. Ergebnis `assembly-motion-checks.json`. Ohne äußere Schraubendrehung sind die Außenhülle und Schnittvolumina gleich; nur der Antrieb rotiert in der Ansicht.
