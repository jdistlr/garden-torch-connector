# Sockelvarianten V01

Zweite Seite: web/variants.html. Bestand D02 und seine Zeichnungen bleiben unverändert.

## Herkunft

Nutzerschätzung vom 28.09.2026: Grundplatte 150 × 150 mm, vorläufig 5 mm stark, eventuell 8–9 mm. Dargestellt ist nur die 5-mm-Version. Kopf und radialer Stift folgen den unbestätigten D02-Fotomaßen. Alle übrigen Maße sind frei gewählte Konzeptannahmen, in der Webseite aufgelistet und im Generator model/variants.py dokumentiert. Sie sind keine Fertigungsmaße.

A: Original kürzen, axialer Gewindegang als glatte Bohrung. B: breiter Fuß, Zentralverschraubung und Passstift. C: Flansch mit drei Schrauben. D: Hülse und gefügte Gewindebuchse; Fügezone nur schematisch. Schrauben sind vereinfachte Platzhalter, keine normmaßhaltigen Kaufteilmodelle. Das Gewinde selbst ist nicht modelliert. Für die 5-mm-Platte stehen Köpfe unterhalb hervor; Freiraum/Füße oder ein späteres Senkkopfkonzept erforderlich. Keine Füße im Modell.

## Reproduzieren

Nach model/build.py: `python3 model/variants.py`. CadQuery erzeugt volle Solids, echte halbe Schnittkörper, gemeinsame STEP-Konzeptdateien und Meshes je Variante. Schnitt zeigt y >= 0; Explosionsverschiebungen dienen nur der Darstellung. Modelleinheit mm. Alle Teile vor Export auf gültigen einzelnen Solid und positives Volumen geprüft.

## Kostenschätzung

Eigene Rechenannahme: 80–120 €/h netto. Zeit inklusive einfacher Rüst-/Bearbeitungsschritte, Material/Kleinteile zusätzlich; Gesamt brutto = (Stunden × Satz + Material) × 1,19. Einzelstück, bereitgestellte Platte. Anschlussbohrungen inklusive; Plattenbeschaffung, Oberfläche, Versand, Konstruktion und Prüfung nicht enthalten.

| Konzept | Zeit h | Material/Kleinteile netto | Gesamt brutto |
|---|---|---|---|
| A | 0,75–1,5 | 15–35 € | 89–256 € |
| B | 1,5–3 | 30–60 € | 179–500 € |
| C | 2–4 | 40–80 € | 238–666 € |
| D | 2–4 | 30–70 € | 226–655 € |

Kein Angebot, keine behauptete aktuelle Marktpreisliste. Hintergrund zu Kostentreibern: https://instawerk.de/wie-entstehen-die-kosten-bei-der-fraesteilfertigung (Artikel 2021; abgerufen 28.09.2026). Die Projektwerte sind eigene Schätzungen.

## Stabilität

Nur qualitative Konzeptbewertung. B ist der bevorzugte Kompromiss; C hat günstig verteilte Befestigungspunkte. A hängt stark vom unbekannten Original ab. D enthält eine zusätzlich auszulegende Fügezone. Halsquerschnitt, Gewinde, Vorspannung, Auflageflächen und Platte bleiben zu bemessen. Es gibt keine zulässige Last, keine FEM und keine Freigabe. Höhe, Gewicht, Schwerpunkt, Wind-/Stoßlast, Untergrund und freier/fester Stand fehlen.

Beispielgewicht bei angenommener Stahldichte 7.850 kg/m³: volle Platte 150 × 150 × 5 / 8 / 9 mm = 0,883 / 1,413 / 1,590 kg vor Bohrungen. Kein Nachweis gegen Kippen.

Technische Grundlagen: https://www.bossard.com/de-de/wissen/ressourcen/technische-informationen/flaechenpressung/ und https://website-assets.bossard.com/Thread-engagement-length-calculator/thread-engagement-length-calculator-en.html
