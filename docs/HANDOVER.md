# Übergabe: Gartenfackel-Verbindung / Stand 28.09.2026

## Auftrag und Arbeitsweise

Nutzer Johannes/Hannes und ein Freund entwickeln ein Verbinderelement für Gartenfackeln. Repository `jdistlr/garden-torch-connector`, öffentlich. GitHub Pages: https://jdistlr.github.io/garden-torch-connector/ ; ausgewählter Viewer `web/variants.html`. Veröffentlichung und Repository-Arbeit sind beauftragt. Keine Händler kontaktieren oder Bestellungen auslösen ohne separaten Auftrag.

Deutsch, verständlich, kleine sichtbare Schritte. Nutzer war mehrfach wegen scheinbar abgebrochener Streams verunsichert: während laufender Arbeit kurze Statusmeldungen geben; nach Ende nicht behaupten, ein Hintergrundtask laufe weiter. Nutzer war zu Recht enttäuscht über ausgelassenes zweites Teil, überstehende Schraube und unbelegte Hohlteilannahme. Keine neuen Konstruktionsannahmen als gemessen oder bestätigt darstellen.

## Verbindliche Entscheidungen

- Ausschließlich Variante D weiterentwickeln. V01/A–D sind verworfenes Archiv.
- D-V03 ersetzt D-V02: **schwarze Aufnahme aus Vollmaterial, direktes axiales Gewindesackloch**. Keine separate Gewindebuchse, keine Passhülse, keine orange Fügezone.
- Grundplatte 150 × 150 mm; 5 mm, eventuell 8–9 mm. Vage Nutzerschätzungen, keine Festigkeitsvorgabe.
- Platte muss plan auf dem Boden liegen. Von unten eingesetzte Senkschraube darf nicht unterstehen.
- Rohr wird auf den schwarzen Kopf geschoben; Querstift läuft im Schlitz und Rohr wird in den seitlichen Nutabschnitt verdreht. Tatsächliches selbsttätiges Einrasten/Rückdrehsicherung ist NICHT nachgewiesen.
- Gängige Standardhalbzeuge und Normteile, günstig im normalen Fachhandel; keine Sondermaße festschreiben, nur weil der Fotoentwurf sie benutzt.

## Quellen und bisherige Modelle

16 bereitgestellte Fotos, darunter Duplikate. `sources/README.md`, `sources/previews/`, `web/assets/photos/` und Maßdokumentation zuerst lesen. Originaldateien waren zusätzlich im alten Scratch `project_sources/`; neue Session darf deren Verfügbarkeit nicht voraussetzen. Die in Nutzertexten wiederholten Image-read-Fehler ersetzen keine Dateiprüfung. Nicht behaupten, Fotos gesehen zu haben, wenn sie nicht geöffnet wurden.

Original D02: silbernes geschlitztes Rohr und schwarzer Erdspieß mit Kopf und radialem Stift. Fotoentwurf etwa Rohr L180, außen27/innen25; Kopf Ø24 ×30; SchaftØ12 ×100 inkl20 Spitze; StiftØ4, Überstand17. Alles unbestätigte Fotoschätzung, keine Vermessung. Original D02 bleibt als Referenz unter `web/index.html`, nicht mit neuer Sockelvariante verwechseln.

D-V02 hatte unberechtigt eine hohle Aufnahme mit Gewindebuchse. Nutzer hat Vollmaterial festgelegt; dieser Stand ist überholt und über Git-Historie rekonstruierbar.

## D-V03: umgesetzt

- `model/sockel_d.py`: CadQuery, massive Aufnahme mit vereinfachtem direktem Sacklochgewinde, separater Querstift; Grundplatte und idealisierter versenkter Schraubenkopf; Originalrohr als Referenz.
- `parameters/sockel-d-v03.json`: Konzeptparameter; früheres v02-Parameterfile entfernt.
- 5 Körper: Platte, massive Aufnahme, Querstift, Senkschraube, Fackelrohr. Keine Buchse/Fügezone mehr. Querstift wird in Explosion zusätzlich radial versetzt.
- Konzeptannahmen: AufnahmeØ24 ×50; nominal M8, Gewinde-Zieltiefe18; zylindrische Bohrtiefe20 plus2,4 Spitze. Glatte CAD-BohrungØ8 ist **Gewindehüllmodell, kein Kernloch-Fertigungsdurchmesser**. QuerstiftØ4 ×21 (4 Sitz +17 Überstand); Passung/Sicherung noch offen.
- Schraube ideal M8×20 inkl Kopf, 90° KopfØ16, Kopfunterseite0,2 über Boden. SenkungØ16,4, DurchgangØ9, Tiefe3,7. Noch kein gegen konkretes Normkaufteil verifiziertes Modell.
- `web/sockel-d.js`, `web/variants.html`, `web/sockel-d.css`: Plattenwahl5/8/9, alle Teile inkl Rohr initial, Drehen/Zoom, Isometrie/Seite/Unterseite/Senkkopfdetail, echter CAD-Schnitt, Transparenz, Kanten, Maße, Teileauswahl, Explosionsregler, PNG-Export. **Noch keine geführte Montageanimation.**
- STEP-Baugruppen/Einzelteile und Prüf-JSON unter `web/assets/sockel-d/`. Alte Buchsen-/Fügezonen-Downloads entfernt.
- `model/drawings_d.py`: je drei klassische A3-Prüfzeichnungen für jede Plattenstärke; insgesamt drei PDFs/neun Blätter. PDF/Blattwahl im Viewer folgt der Plattenwahl. Platte/Senkung; massive Aufnahme/Querstift; Montageschnitt. Klassische Schwarzweißdarstellung, keine behauptete historische DIN-Vollkonformität.
- Dokumentation, Stückliste, Montageübersicht und README auf Vollmaterial aktualisiert.
- Alte D-V02-Kalkulation226–655 EUR wurde zurückgezogen, weil Buchsenfertigung/Fügen entfallen. Noch keine neue belastbare Kalkulation behaupten.

## Prüfstand

Für5/8/9: fünf gültige Solids, keine volumetrischen Überschneidungen in nominaler Montagelage, kein Teil unterz0; STEP-Rückimport mit gleicher Körperzahl und Volumen geprüft.

| Platte mm | Restdicke Senkung mm | nominale Gewindeüberdeckung mm | Abstand Schraubenspitze bis zyl. Bohrungsende mm |
|---|---|---|---|
|5|1,3|15,2|4,8|
|8|4,3|12,2|7,8|
|9|5,3|11,2|8,8|

Kein Tragfähigkeits-, Losdreh-, Kipp- oder Bewegungsnachweis. Werkstoff, reale Schraube, wirksame Gewindelänge, Toleranzen, Beschichtung und Stiftsicherung offen. CAD-Endlagenprüfung beweist nicht einen kollisionsfreien Steck-Dreh-Montageweg.

Lokaler Playwright-Check: drei Plattenstärken, Schnitt, Explosion, Transparenz, Rohrschalter, Maßansicht, Zeichnungsblätter, mobile Breite390; keine JavaScriptfehler/kein horizontaler Overflow. Vollmaterial-Schnitt visuell gesehen. Zeichnungen gerendert; nach PDF-Export gab es sporadisch abgeschnittene PNGs, durch Einzelblatt-Rerender repariert. Bei Fortsetzung Bilddateien vollständig dekodieren; Browser-naturalWidth allein genügt nicht. PDF-Blätter müssen weiterhin als Prüfzeichnungen ohne Fertigungsfreigabe markiert bleiben.

## Nächste Aufgaben (bereits beauftragt, noch offen)

1. Funktionsprüfung des axialen Aufschiebens und Verdrehens: Geometrie, Einsteckweg, Winkel, Drehrichtung, Kontakt, Spiel, Rückdrehsicherung; reale Maße gezielt erfragen. Bewegung darf die Sockelverschraubung nicht lösen. Keine erfundene Rastung animieren.
2. Breite Beschaffung entlang Stückliste: Erlangen plus Nürnberg, Fürth, Herzogenaurach, Forchheim und Internethändler. Kontakte/Adresse/Telefon/E-Mail oder Kontaktseite, Produkt-/Zuschnittlinks, Legierung, Abmessung, Privatkundenverkauf, Mindestmenge, Abholung/Versand, Preisstand und Verfügbarkeit belegen. Pro Position möglichst zwei Quellen. Standard-Rundvollmaterial statt Buchse/Hohlrohr für die schwarze Aufnahme.
3. Gesamtkosten1/5/10: tatsächliche Kaufmengen, Material/Verschnitt, Schraube/Stift, Platte, Rüsten/Bearbeiten, Schlitz, Oberfläche, Montage, Versand, Werkzeug/Prüfung; Eigenleistung vs Werkstatt, netto/brutto trennen. Recherche ist noch nicht abgeschlossen. Frühe Suchspuren: Herrmann Buntmetall Nürnberg, JERA Metall Nürnberg, Rackl Wendelstein, Würth Erlangen, Hornbach/BAUHAUS. Keine davon als passendes lieferbares Angebot verifiziert. Neu recherchieren.
4. Vollständige Montageanleitung mit Positionsnummern, Werkzeug, Drehmoment erst nach Werkstoff-/Schraubenwahl, Kontrolle und Demontage. Kurze Montageübersicht existiert bereits.
5. Ästhetische Gesamtanimation: erklärende Schrittsteuerung und kurze Produktdemo, Pause/Zeitleiste/Replay, Schnitt/Transparenz zur Erklärung. Platte zum Verschrauben anheben, Schraube von unten, plan absetzen, Rohr aufschieben und drehen. Stiftmontage als Fertigungsschritt trennen. Mechanik vorher prüfen. Keine optischen Tricks/Erfolgsgarantie.
6. Wiederverwendbarkeit: später generischer Ablauf Quelle→Maße/Annahmen→CAD→Zeichnung→Viewer→Stückliste; kein überdimensioniertes Framework.

## Technische Fortsetzung

Vor Änderungen `AGENTS.md`, `README.md`, `docs/sockel-d.md`, `docs/next-features.md`, `docs/measurements.md`, `docs/viewer-runbook.md` lesen. Neues Repo/Remote prüfen, nicht auf alten Scratch vertrauen.

Erzeugung: Python/CadQuery2.7.0/ReportLab; `python3 model/sockel_d.py`; pro Stärke `D_PLATE_THICKNESS=5 python3 model/drawings_d.py` (8/9 analog). Modelle/Parameter/Zeichnungstexte sind noch nicht vollständig universell parametrisiert; alle abhängigen Maße gemeinsam aktualisieren. PNGs per `pdftoppm` einzeln rendern und verifizieren.

GitHub Pages nutzt main-Branch/root. Root index leitet zu `web/variants.html`. Kein zusätzliches Hosting. Alte lokale `.github/` und `tmp/` nicht versehentlich committen. GitHub-Connector-Git-Data-API wurde für Blob/Tree/Commit/Ref verwendet, da kein Shell-Push-Zugang eingerichtet. Schreibzugriff und Veröffentlichung sind autorisiert. Bei API-Upload jeden Blob-Hash gegen lokalen Git-Hash prüfen, binäre/größere Dateien in base64-Lesestücken von240000 Bytes laden; Tooloutput kann sonst abschneiden. Für Löschungen Tree-Eintrag sha:null. Ref niemals force aktualisieren; aktuellen Remotezustand prüfen.

## Zuerst in neuer Session

Aktuellen Commit und Pages-Auslieferung prüfen: sichtbare Revision muss D-V03 sein, Teile müssen `plate, adapter, pin, screw, tube` enthalten, nicht `insert/weld`. Falls Deployment noch läuft, zuerst abschließen. Danach mit Funktionsklärung und Beschaffungsrecherche fortfahren, keine neuen Varianten A–C und keine Rückkehr zur Gewindebuchse.
