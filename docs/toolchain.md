# Werkzeugentscheidung

## Vorschlag: CadQuery als Modellquelle, FreeCAD/TechDraw für Zeichnungen

CadQuery beschreibt parametrische Volumenkörper in Python und exportiert STEP. Textbasierte Parameter und Modellcode sind in Git gut vergleichbar. Das einfache Rohr mit Ausschnitten eignet sich für diesen Ansatz.

FreeCAD dient zum unabhängigen Öffnen des STEP-Modells und zur Ableitung technischer Zeichnungen mit TechDraw. Der Austausch erfolgt zunächst dateibasiert; ein MCP-Server ist dafür keine Voraussetzung.

OpenSCAD ist eine plausible Alternative für codebasierte Geometrie und Anschauungsmodelle. Für dieses Projekt gibt der direkte STEP-Arbeitsweg von CadQuery den Ausschlag. Es werden nicht mehrere gleichberechtigte Modellquellen gepflegt.

## Geplante Ausgabeformate

| Format | Zweck |
|---|---|
| Python + JSON | Änderbare Modellquelle und Parameter |
| STEP | CAD-Austausch mit Fertiger |
| PDF | Bemaßte Zeichnung und Auftrag |
| PNG/SVG | Ansichten und Erläuterungen |
| STL | Optionaler Anschauungsprototyp |
| GLB | Optionale Webdarstellung |

## Reproduzierbarkeit

Vor dem ersten Modell-Build unterstützte Python-, CadQuery- und FreeCAD-Versionen in der tatsächlichen Umgebung prüfen. Erfolgreiche Versionen anschließend fixieren. Noch sind weder CAD-Abhängigkeiten installiert noch Builds, STEP-Exporte oder Zeichnungsableitungen geprüft.

Offizielle Referenzen:
- https://cadquery.readthedocs.io/en/latest/intro.html
- https://cadquery.readthedocs.io/en/latest/importexport.html
- https://www.freecad.org/features.php
- https://github.com/FreeCAD/FreeCAD-documentation/blob/main/wiki/TechDraw_Workbench.md
