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
