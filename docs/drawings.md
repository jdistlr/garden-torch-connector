> Historische Originalreferenz, kein aktueller D-V03-Nachweis. Aktuell: [Entscheidungskette](entscheidungen-d.md) und [D-V03](sockel-d.md).

# Klassische technische Prüfzeichnungen D02

Die PDF unter `web/assets/werkstattzeichnungen-D02.pdf` enthält drei A3-Querformatblätter. Ziel ist eine gut lesbare Werkstattdarstellung in vertrauter Zeichenpraxis, keine dekorative Retro-Grafik.

## Darstellungsregeln

- Schwarze Vektorlinien; sichtbare Kanten 0,5 mm, Maßlinien 0,25 mm, Achsen und verdeckte Kanten 0,18 mm.
- Millimeter, geschlossene Maßpfeile, Durchmesserzeichen, Maßhilfslinien, Achsen als Strichpunktlinie, verdeckte Kanten gestrichelt.
- Hauptansichten 1:1; lokale Details ausdrücklich 3:1 bzw. 2:1. Separate Blickrichtungen sind beschriftet. Beim Rohr steht die Ansicht vom linken Ende rechts (Projektionsmethode 1).
- Rahmen, Schriftfeld, Zeichnungsnummern, Revision, Blattzählung, Werkstoff- und Prüfstatus; Zusammenbau mit Stückliste.
- Sämtliche Maße unterliegen dem deutlich sichtbaren Hinweis „unbestätigter Foto-Entwurf“. Keine Maßtoleranz, Passung oder Oberflächenanforderung ist stillschweigend ergänzt.

Historischer Bezug: ISO 128:1982 beschreibt allgemeine Darstellungsgrundsätze technischer Zeichnungen. Die DIN-Media-Ersatzhistorie nennt DIN 406-1:1977-04 und DIN 406-2:1981-08 als Vorgänger der späteren DIN 406-10. Die vollständigen historischen Normtexte wurden nicht für eine Konformitätsprüfung herangezogen. Deshalb wird ausdrücklich keine vollständige Normkonformität nach einer bestimmten Ausgabe behauptet.

Quellen:
- https://www.iso.org/standard/3938.html
- https://www.dinmedia.de/de/norm/din-406-10/1990706

## Neu erzeugen

```sh
python3 -m pip install -r model/requirements.txt
python3 model/build.py
python3 model/drawings.py
```

Der Zeichnungsgenerator nutzt dieselben STEP-Solids und dieselbe Parameterdatei wie der Viewer. Vor dem Zeichnen prüft er Parameter- und Gesamt-STEP-Prüfsummen gegen die Metadaten. Orthogonale Kantenprojektionen stammen aus OCCT mit verdeckter-Kanten-Ermittlung (HLR); Kurven werden für die PDF als fein abgetastete Vektorzüge ausgegeben. Kein Nachzeichnen aus Screenshots.

Die PDF-Erzeugung benötigt zusätzlich DejaVu Sans unter `/usr/share/fonts/truetype/dejavu/`. Der Blattaufbau ist auf die Proportionen D02 abgestimmt. Nach Maßänderungen alle Blätter erneut auf Layout und Maßzuordnung prüfen.

## Prüfung und Grenzen

Drei A3-Seiten, eingebettete Schrift, sichtbare Revisions- und Prüfkennzeichnung, Druckkontrollstrecke 50 mm. Alle Seiten gerendert und visuell geprüft. Einzelteilmaße aus D02; abgeleitete Gesamtlänge 130 als Hilfsmaß geklammert. Der vorläufige Schlitzradius R2,5 ist explizit eine Modellannahme. Die gemeinsame STEP-Datei bleibt unverändert.

Vor Verwendung zur Fertigung sind direkte Messungen, Material, Passungen, Toleranzen, Rauheit, Kanten und Herstellverfahren zu klären. Die Zeichnungen dienen jetzt der gemeinsamen Papierprüfung.

## Direkte Webansicht

Der Viewer enthält eine Werkstattansicht mit drei Blatt-Schaltflächen, Zoom (1 bis 4-fach), Einpassen und einer verschiebbaren Vorschau. Die PNGs sind aus derselben PDF gerendert; zum Drucken die Vektor-PDF nutzen. Nach Neuerzeugung der PDF Vorschauen aktualisieren:

```sh
pdftoppm -scale-to 2200 -png web/assets/werkstattzeichnungen-D02.pdf web/assets/zeichnung-D02
```
