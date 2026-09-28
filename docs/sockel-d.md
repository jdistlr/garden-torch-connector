# Gewählte Sockelvariante D-V03

Konzeptstand vom 28.09.2026. Grundplatte 150 × 150 mm; 5, 8 oder 9 mm Stärke. Massive Aufnahme mit direkt eingeschnittenem Gewindesackloch, von unten versenkte Schraube. Alle neuen Detailmaße sind Konstruktionsannahmen; ursprüngliche Maße sind unbestätigte Fotoschätzungen.

## Prüfergebnis

| Plattenstärke | Kopf über Bodenebene | Restdicke neben Senkung | Nominale Gewindeüberdeckung |
|---|---|---|---|
| 5 mm | 0,2 mm | 1,3 mm | 15,2 mm |
| 8 mm | 0,2 mm | 4,3 mm | 12,2 mm |
| 9 mm | 0,2 mm | 5,3 mm | 11,2 mm |

Für jeden Stand: fünf gültige Einzelkörper, keine volumetrischen Überschneidungen in Montagelage, kein Körper unter z=0, STEP-Rückimport mit fünf Körpern und übereinstimmendem Volumen. Siehe maschinenlesbare Ergebnisse in `web/assets/sockel-d/checks.json`.

Das beweist die geometrische Montagelage, nicht Festigkeit, Kippsicherheit oder Kollisionsfreiheit während der Montage. Die Gewindeüberdeckung ist geometrisch, nicht wirksame tragende Gewindelänge. Gewinde sind vereinfacht dargestellt. Schraube und Senkung sind ideale Konzeptgeometrie, noch kein maßgetreu verifiziertes Normkaufteil. Die Aufnahme ist Vollmaterial. Querstift und Aufnahme sind separate Körper; Stiftsitz und Sicherung sind auszulegen. Das M8-Gewinde ist als nominale glatte Hülle dargestellt, nicht als Kernloch-Fertigungsmaß. Konzept: Gewinde-Zieltiefe 18 mm, zylindrische Bohrtiefe 20 mm plus 2,4 mm Spitze. Platte und Fackelhöhe, Gewicht und Seitenlasten müssen gemeinsam beurteilt werden.

## Ansichten und Dateien

- `web/variants.html`: ausgewählte D-Version mit Plattenwahl, Schnitt, Explosion, Bodenansicht, Detail, Transparenz, Rohr ein/aus, Maßen und PNG-Export.
- `web/assets/sockel-d/`: STEP-Baugruppen und Einzelteile für jede Stärke, Viewer-Geometrien und Prüfbericht.
- `zeichnungen-D-V03-{5,8,9}mm.pdf`: je drei A3-Blätter pro Plattenstärke; Platte/Senkung, massive Aufnahme/Querstift, Zusammenbau. Klassische Schwarzweißdarstellung mit Schnitten und Schriftfeld, keine Behauptung vollständiger historischer Normkonformität.
- `web/variants-v01.html`: verworfenes Variantenarchiv.

## Reproduzieren

Python mit CadQuery und ReportLab: `python3 model/sockel_d.py`, danach je Stärke `D_PLATE_THICKNESS=5 python3 model/drawings_d.py` (ebenso mit 8 und 9). Die dokumentierten Konzeptparameter liegen in `parameters/sockel-d-v03.json`. Bei Maßänderungen Generator, Parameterdatei, Zeichnungen und Prüfwerte gemeinsam aktualisieren; noch keine universelle Parametrik für beliebige Produkte.

## Nächste Entscheidungen

[Entscheidungskette](entscheidungen-d.md): reale Maße und Funktion, vollständige Fackel, kompatible Stückliste, Sicherung und Belastbarkeit. Recherche, Budgetstudie, Konzeptanleitung und Animation sind vorhanden. Die Budgetstudie verwendet teilweise andere Teile und ist kein Preis des aktuellen CAD.

## Stückliste D-V03

| Pos. | Teil | Menge | Status |
|---|---|---|---|
| 1 | Grundplatte 150 × 150 × 5/8/9 | 1 | Stärke auswählen |
| 2 | Massive Aufnahme Ø24 × 50, direktes M8-Sackloch | 1 | Werkstoff und Detailmaße offen |
| 3 | Radialer Querstift Ø4, Gesamtlänge 21 | 1 | 17 Überstand + 4 Sitz: Konzept, Sicherung offen |
| 4 | Senkschraube M8 × 20 | 1 | Kaufteil auswählen, derzeit idealisierte Hülle |
| 5 | Geschlitztes Fackelrohr | 1 | D02-Fotoschätzung |

Keine Gewindebuchse, Passhülse oder ringförmige Fügezone. D-V02 wurde durch D-V03 ersetzt und bleibt nur in der Git-Historie rekonstruierbar. V01 ist ausdrücklich verworfenes Archiv.

Sacklochabstand zur Schraubenspitze: 4,8 / 7,8 / 8,8 mm für Platte 5 / 8 / 9 mm, gemessen bis zum Beginn der Bohrspitze. Die nominale Überdeckung beträgt weiterhin 15,2 / 12,2 / 11,2 mm; Gewindeauslauf und reale Schraubenspitze sind zusätzlich zu berücksichtigen.

## Montageübersicht

Aufnahme aus Vollmaterial fertigen, direktes Sacklochgewinde herstellen und Querstift sichern. Platte anheben, Aufnahme aufsetzen, Senkschraube von unten einschrauben und mit noch festzulegender Vorspannung sichern. Schraube darf nicht am Sacklochgrund anschlagen. Platte absetzen, Bodenfreiheit prüfen. Rohr erst nach Prüfung des Steck-Dreh-Wegs aufschieben und drehen. Kein bestätigtes Einrasten voraussetzen. Die Explosionsansicht ist eine Teileübersicht, keine geprüfte Bewegungsanimation.

## Ergänzung: Einführlage und geführte Montage

Die bestehende STEP-Baugruppe ist bei0° in **Einführlage**, nicht in verdrehter Endlage. Der nominale Weg bis50° ist abgetastet; ca.55,8° ist der erste geometrische Drehkontakt, obwohl der Nutsektor65° beträgt. Rückdrehen bleibt frei. Siehe [Mechanik](mechanik-d.md), [Montage](montage-d.md), [Beschaffung](beschaffung-d.md) und [Kosten](kosten-d.md). Die geführte Animation ersetzt nicht den Versuch am Original.
