# Projektplan: kleine Schritte, sichtbare Ergebnisse

Stand: 28.09.2026. Dieser Ablauf ersetzt die bisherige große Umsetzungsreihenfolge. Die ausführliche Viewer-Spezifikation bleibt das spätere Zielbild.

## Bereits vorhanden

16 Quelldateien gesichtet, 14 verschiedene Bildvorschauen und Duplikatzuordnung im Repository. Maßliste und Werkzeugentscheidung liegen vor. CAD-Fotoentwurf D02, STEP und eine erste Viewer-Version sind inzwischen erstellt. Direkte Maße und Fertigungsauftrag stehen noch aus. Siehe viewer-runbook.md.

## Nächste Etappen

| Etappe | Sichtbares Ergebnis | Was wir daran prüfen |
|---|---|---|
| 1. Formabgleich | Ein Blatt mit ausgewählten Fotos und nummerierten Merkmalen; einfache Skizze ohne Maßstabsanspruch | Rohr, offener Längsschlitz, Rundung, seitliche Aussparung und Montagebewegung richtig verstanden? |
| 2. Grober CAD-Entwurf | Drei Modellansichten plus STEP-Entwurf | Stimmen Form, Ausschnittrichtung und grobe Proportionen? |
| 3. Minimaler Web-Viewer | Ein drehbares Modell, Ansicht zurücksetzen, eine Infobox mit Maßen und deren Status | Dasselbe Modell im Browser verständlich und maßstäblich korrekt dargestellt? |
| 4. Gezielte Korrektur | Überarbeiteter Entwurf, markierte Änderungen; Schnittbild bei Bedarf | Nur noch die für Form und Passung entscheidenden offenen Maße nachmessen |
| 5. Fertigungsunterlagen | Bemaßte PDF-Zeichnung, STEP und kurze Auftragsbeschreibung | Maße, Passung, Material, Oberfläche, Stückzahl und Toleranzen geklärt? |

## Startregel

Zuerst vorhandene Linealfotos im Detail auswerten. Ablesbare Werte als Foto-Schätzung samt Quelle und Unsicherheit festhalten. Keine scheinpräzisen Zahlen. Für ein erstes Größenmodell bevorzugt Rohrlänge sowie Außen- und Innendurchmesser bestätigen lassen; weitere Maße nur anfordern, wenn sie den nächsten Entwurf tatsächlich blockieren.

Ein früher Entwurf darf ausdrücklich gekennzeichnete Foto-Schätzungen verwenden. Unbekannte Werte bleiben offen. Frei gewählte Beispielwerte sind keine Rekonstruktion und dürfen nicht unbemerkt ergänzt werden. Bestätigte Werte werden getrennt geführt. Jede Entwurfsansicht trägt ihren Status.

## Kurze Rückkopplung

Pro Runde ein sichtbares Ergebnis und höchstens drei konkrete Fragen. Der Nutzer korrigiert Form, Richtung oder Maße direkt am gezeigten Merkmal. Danach neue Revision erzeugen. Kein vollständiger Fragebogen vor dem ersten Formabgleich.

## Minimaler technischer Umfang

CadQuery-Modell und Parameterdatei; ein Exportweg für STEP und Browsermesh. Der erste Viewer zeigt beide Teile, Drehen/Zoomen/Reset und ein kompaktes Maß-/Statuspanel. Bestehende Standards für Einheiten, gültiges Solid und gemeinsame Revision gelten bereits.

Schnitte, weitere Panels und Montageanimation werden nach Bedarf ergänzt. Backend, Browser-CAD-Kern, freie Messwerkzeuge und CI-Automatisierung bleiben vorerst zurückgestellt. FreeCAD/TechDraw kommt zur Zeichnungsableitung hinzu.

## Wiederverwendung

Den Ablauf in [workflow.md](workflow.md) für ähnliche Teile übernehmen. Quellen, Parameter, Modell und Exporte getrennt halten. Das Repository bleibt beim konkreten Verbindungsrohr; weder Umbenennung noch Plattformumbau nötig. Gemeinsamen Code erst auslagern, wenn ein zweites reales Bauteil denselben Ablauf nutzt.

## Abschluss

Ein früher Entwurf ist erreicht, sobald die Form gemeinsam prüfbar ist. Ein Fertigungsstand erfordert zusätzlich bestätigte Maße und Anforderungen, gültige CAD-Geometrie, konsistente Exporte und eine Prüfung der Verbindung am Gegenstück.

## Neue verbindliche Ausbaustufen

[Standardteile, Beschaffung, Gesamtkosten, Funktionsprüfung, Montageanleitung und Produktanimation](next-features.md). Diese Reihenfolge hat Vorrang vor früheren offenen Ausbaustufen.
