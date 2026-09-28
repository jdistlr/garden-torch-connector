# D-V03 · Bauen, prüfen, veröffentlichen

Öffentlicher Einstieg: https://jdistlr.github.io/garden-torch-connector/ → `web/variants.html`. Historisches Original: `web/index.html`. Aktueller Arbeitsstand: [Entscheidungskette](entscheidungen-d.md).

## Dokumente und Oberfläche

- `npm ci` installiert die fixierte Markdown-Abhängigkeit.
- `npm run docs` erzeugt die fünf Dokumentseiten aus `docs/*-d.md`.
- `python3 -m http.server 8765 --directory web`; lokal `/variants.html?plate=9` öffnen.
- `web/project-state.js` hält Plattenwahl/URL, Dokumentlinks, PDF/STEP und Vorschau unabhängig von Three.js aktuell. Explizite URL gewinnt vor lokaler Merkhilfe. Keine Modell-Neugenerierung.
- `web/montage-d.js` definiert Posen und Aktionszuordnung. Ganzzahlen sind Zielbilder; Übergänge erklären die nächste Handlung. Änderungen an `stepAt` sind keine Änderungen an `poseAt`.
- `node model/test_montage.mjs` prüft die Handlungszuordnung und die nominalen Rohrposen.

## CAD und geometrische Prüfung

Python-Abhängigkeiten: `python3 -m pip install -r model/requirements.txt`. D-V03: `python3 model/sockel_d.py`, dann `D_PLATE_THICKNESS=5 python3 model/drawings_d.py` (auch 8 und 9). PNG-Vorschauen aus den entsprechenden PDFs erzeugen und vollständig dekodieren/visuell prüfen.

`python3 model/check_motion_d.py` prüft den nominalen Rohrweg aus STEP und schreibt `motion-checks.json` mit STEP-Hashes. `node model/export_assembly_poses.mjs /tmp/torch-poses.json`, danach `python3 model/check_assembly_d.py /tmp/torch-poses.json` prüft die Gesamtmontage. Keine Kraft-/Gewindeflanken-/Schwerkraftsimulation; diskrete Prüfung ist kein lückenloser Bewegungsnachweis.

`python3 model/cost_d.py` reproduziert die abweichende 5-mm-Kandidatenstudie. Nicht als CAD-Stücklistenkosten behandeln.

## Freigabe einer Veröffentlichung

1. Geänderte Inhalte prüfen; bei Geometrie/Posenänderungen auch CAD, Zeichnungen und beide Bewegungsprüfungen erneuern. Kopierte Zahlen in Generator/Parametern/Dokumenten bleiben bis zur vollständigen Parametrisierung eine manuelle Prüfpflicht.
2. `npm run docs`; Browserfälle prüfen: 5/8/9, URL/Seitenwechsel, Downloads ohne WebGL, echte 3D-Funktionen, Fehlerzustand, Schritte/Übergänge, reduzierte Bewegung, mobile Ansicht. Nicht erfolgreich prüfbare Fälle im Übergabetext benennen.
3. `python3 model/check_release.py --write` erstellt nach der Prüfung das Dateihash-Manifest. `npm run check` prüft Modellidentität, Aktionszuordnung, aktuelle HTML-Generierung, lokale Links und Manifestgleichheit. Das Manifest verhindert stilles Dateidriften, ist aber kein mechanischer Nachweis.
4. Commit auf main ohne Force-Push. Vorhandenes GitHub Pages aus Branch/root verwenden. Erfolgreichen Lauf zum neuen Commit und live ausgelieferte geänderte Dateien verifizieren.

## Tatsächliche Grenzen

Rohraufschieben und Drehen sind nominal geprüft, Originalfunktion und Rückdrehsicherung bleiben offen. 50° ist keine eingerastete Endlage. Werkzeug-/Handzugang ist nicht modelliert. Download-Auswahl funktioniert auch bei WebGL-Ausfall; bei vollständig deaktiviertem JavaScript gilt die sichtbare statische 5-mm-Vorauswahl. Keine Frontend-Geometriebearbeitung implementiert.
