# Gewählte Sockelvariante D-V02

Konzeptstand vom 28.09.2026. Grundplatte 150 × 150 mm; 5, 8 oder 9 mm Stärke. Kurze Aufnahme, separate innen befestigte Gewindebuchse, von unten versenkte Schraube. Alle neuen Detailmaße sind Konstruktionsannahmen; ursprüngliche Maße sind unbestätigte Fotoschätzungen.

## Prüfergebnis

| Plattenstärke | Kopf über Bodenebene | Restdicke neben Senkung | Nominale Gewindeüberdeckung |
|---|---|---|---|
| 5 mm | 0,2 mm | 1,3 mm | 15,2 mm |
| 8 mm | 0,2 mm | 4,3 mm | 12,2 mm |
| 9 mm | 0,2 mm | 5,3 mm | 11,2 mm |

Für jeden Stand: sechs gültige Einzelkörper, keine volumetrischen Überschneidungen in Montagelage, kein Körper unter z=0, STEP-Rückimport mit sechs Körpern und übereinstimmendem Volumen. Siehe maschinenlesbare Ergebnisse in `web/assets/sockel-d/checks.json`.

Das beweist die geometrische Montagelage, nicht Festigkeit, Kippsicherheit oder Kollisionsfreiheit während der Montage. Die Gewindeüberdeckung ist geometrisch, nicht wirksame tragende Gewindelänge. Gewinde sind vereinfacht dargestellt. Schraube und Senkung sind ideale Konzeptgeometrie, noch kein maßgetreu verifiziertes Normkaufteil. Die Fügezone der Buchse ist schematisch und muss mit Werkstoff/Fertigungsverfahren ausgelegt werden. Platte und Fackelhöhe, Gewicht und Seitenlasten müssen gemeinsam beurteilt werden.

## Ansichten und Dateien

- `web/variants.html`: ausgewählte D-Version mit Plattenwahl, Schnitt, Explosion, Bodenansicht, Detail, Transparenz, Rohr ein/aus, Maßen und PNG-Export.
- `web/assets/sockel-d/`: STEP-Baugruppen und Einzelteile für jede Stärke, Viewer-Geometrien und Prüfbericht.
- `zeichnungen-D-V02.pdf`: drei A3-Blätter für die 5-mm-Ausführung; Platte/Senkung, Aufnahme/Buchse, Zusammenbau. Klassische Schwarzweißdarstellung mit Schnitten und Schriftfeld, keine Behauptung vollständiger historischer Normkonformität.
- `web/variants-v01.html`: verworfenes Variantenarchiv.

## Reproduzieren

Python mit CadQuery und ReportLab: `python3 model/sockel_d.py`, danach `python3 model/drawings_d.py`. Die dokumentierten Konzeptparameter liegen in `parameters/sockel-d-v02.json`. Bei Maßänderungen Generator, Parameterdatei, Zeichnungen und Prüfwerte gemeinsam aktualisieren; noch keine universelle Parametrik für beliebige Produkte.

## Nächste Schritte

[Arbeitsplan](next-features.md): breite regionale und Online-Beschaffung entlang der Stückliste, Funktionsprüfung des Steck-Dreh-Verschlusses, Gesamtkosten für 1/5/10 Stück, Montageanleitung, anschließend erklärende und ästhetische Montageanimation. Derzeitige Kosten im Viewer sind eigene Schätzwerte, keine Händlerangebote.
