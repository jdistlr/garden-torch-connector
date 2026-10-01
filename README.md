# Gartenfackel · gewählter Sockel D-V03

**Arbeitsstand 28.09.2026: prüfbares Konzept, keine Fertigungs- oder Betriebsfreigabe.** Ausschließlich Variante D wird weiterentwickelt: massive schwarze Aufnahme mit direkt eingeschnittenem axialem Gewindesackloch. Fünf Teile, keine Gewindebuchse oder Fügezone.

[Projekt öffnen](https://jdistlr.github.io/garden-torch-connector/web/projekt.html) · [Viewer öffnen](https://jdistlr.github.io/garden-torch-connector/web/variants.html) · [Entscheidungskette](docs/entscheidungen-d.md) · [Montage](docs/montage-d.md)

## Der rote Faden

1. **Verstehen:** [Originalfotos](sources/README.md) und [Steck-Dreh-Prinzip](docs/mechanik-d.md). Der frühere Erdspieß ist Referenz, kein Teil des neuen Sockels.
2. **Ausführung wählen:** 150 × 150 mm Grundplatte mit 5/8/9 mm, massive Aufnahme, radialer Stift, Senkschraube und geschlitztes Rohr. Detailmaße bleiben Konzeptwerte oder Fotoschätzungen.
3. **Nachweise unterscheiden:** Geometrie und nominale Bewegungsstichproben liegen vor. Reale Maße, Sicherungen, Werkzeugzugang, Kaufteilpassung und Standsicherheit sind offen.
4. **Teile abstimmen:** [Beschaffungskandidaten](docs/beschaffung-d.md) müssen gegen die [aktuelle Stückliste](docs/entscheidungen-d.md) freigegeben werden. Andere Rohr-/Stiftmaße sind bisher nicht im CAD übernommen.
5. **Kosten entscheiden:** [Budgetstudie](docs/kosten-d.md) für abweichende Kandidaten, ausschließlich 5 mm; noch kein Gesamtpreis des aktuellen CAD und kein Bestellpaket.
6. **Fertigen, montieren, prüfen:** [Konzeptanleitung und Prüfprotokoll](docs/montage-d.md). Erst nach den dokumentierten Nachweisen entsteht eine freigegebene Ausführung.

## Was vorhanden ist

- D-V03-STEP-Baugruppen und fünf Einzelteile für 5/8/9 mm, CAD-abgeleitete Browsermodelle.
- Je drei A3-Prüfzeichnungen für jede Plattenstärke. Im Viewer folgen PDF, Vorschau und STEP der Auswahl, auch wenn WebGL ausfällt.
- Freie 3D-Ansicht, Schnitt, Transparenz, Teileauswahl, Explosionsansicht, definierte Maße und PNG-Export.
- Geführte Konzeptmontage mit Pause, Schrittwahl, Zeitleiste und erklärenden Sockelschnitten. Die 50°-Demonstration zeigt keine Rastung.
- Regionale und Online-Beschaffungsrecherche, Budgetstudie für 1/5/10 Stück, druckbare Dokumentseiten.

Die gewählte Plattenstärke wird in Seitenlinks mitgeführt. Die Anzeige verändert keine CAD-Geometrie. Geometriebearbeitung im Frontend ist eine [spätere Ausbaustufe](docs/next-features.md).

## Was als Nächstes gebraucht wird

Drei Nachweispakete: (1) Rohr, Schlitz, Kopf und Stift direkt messen; (2) Originalbewegung einschließlich Rückweg filmen und Sicherung klären; (3) vollständige Fackel mit oberem Anschluss, Höhe und Gewicht erfassen. Daraus folgen passende Halbzeuge, Werkstoffe und eine gemeinsame Toleranz-/Sicherungsentscheidung. Verantwortlichkeiten und Abschlusskriterien: [Entscheidungskette](docs/entscheidungen-d.md).

## Dateien und Reproduzierbarkeit

| Bereich | Einstieg |
|---|---|
| Aktuelle Konstruktion / Grenzen | [sockel-d.md](docs/sockel-d.md) |
| Bestätigte Maße und offene Messungen | [measurements.md](docs/measurements.md) |
| CAD / Zeichnungen | `model/sockel_d.py`, `model/drawings_d.py` |
| Konzeptparameter | `parameters/sockel-d-v03.json` |
| Modelle, STEP, PDF, Prüfberichte | `web/assets/sockel-d/` |
| Bauen, prüfen, veröffentlichen | [viewer-runbook.md](docs/viewer-runbook.md) |
| Nächste Sitzung | [HANDOVER.md](docs/HANDOVER.md) |

`null` bedeutet unbekannt. 16 ursprüngliche Fotos entsprechen 14 verschiedenen Motiven; verkleinerte Vorschauen und Originalprüfsummen stehen unter `sources/`. Originaldateien nicht überschreiben.

D02 und V01 sind historische Referenzen. Der aktuelle Einstieg ist D-V03. GitHub Pages veröffentlicht den main-Branch; das Repository bleibt öffentlich.
# One More Thing

Zusätzlicher, Vectron-nah gestalteter, technisch fiktiver [Röntgenstrahler-Demonstrator](https://jdistlr.github.io/garden-torch-connector/web/one-more-thing.html): elf illustrative Baugruppen, schrittweise Erklärmontage, Kathode/Anodenteller/Flüssigmetalllager, schematische Strahlungsentstehung, erfundene Stückliste und zwei A3-Schemablätter. Kein realer Bauplan. [Abgrenzung und Implementierung](docs/xray-demo.md). Gartenfackel D-V03 bleibt ein eigenständiges Projekt.
