# D-V03 – Steck-Dreh-Prüfung

[Gemeinsamer Stand, Stückliste und nächste Entscheidungen](entscheidungen-d.md)


Stand 28.09.2026. Geprüft werden vorhandene STEP-Körper, keine gemessenen Originalteile. Geometrie und Zeichnungsrevision bleiben D-V03.

## Bezug und Bewegung

Boden z=0, Rohrachse +Z, Stift zeigt +Y. Blick **von oben zur Platte**: positive Rohrdrehung gegen den Uhrzeigersinn. Die bisherige STEP-Baugruppe zeigt die **Einführlage** (0°), nicht die verdrehte Endlage. Für die Animation wird ausschließlich das Rohr bewegt; die Sockelaufnahme bleibt fest.

1. Rohr 40 mm oberhalb der bisherigen Einführlage halten, Schlitz mittig auf +Y.
2. Rohr ohne Rotation um 40 mm absenken. Die Unterkante liegt anschließend bei Plattendicke +14 mm, die Stiftmitte bei Plattendicke +35 mm.
3. Rohr um +50° drehen. Diese Darstellungsposition liegt vor dem ersten geometrischen Anschlag, sie ist keine eingerastete Endlage.
4. Zum Lösen um −50° zurückdrehen und axial abziehen. Der Rückweg ist geometrisch ebenso frei.

## Ergebnis am nominalen Konzept

| Merkmal | Ableitung | Bedeutung |
|---|---|---|
| Radiales Spiel | (25−24)/2 = 0,5 mm | Unbelastet konzentrisch; kein Toleranznachweis |
| Schlitzspiel je Seite | (5−4)/2 = 0,5 mm | Ausrichtung beim Einführen erforderlich |
| Axiales Spiel im Abzweig | 6−4 = 2 mm gesamt | Von mittiger Lage je 1 mm bis Kontakt |
| Nutsektor | 65° | Ist nicht der mögliche Drehwinkel des endlichen Stifts |
| Erster Drehkontakt | 65°−asin(2/12,5) ≈ 55,79° | Stift berührt die radiale Endwand am Innenradius des Rohrs |
| Anzeigeweg | 0…50° | Nominale Reserve vor Anschlag; kein Fertigungs-Sicherheitsabstand |
| Rückdrehsicherung | nicht modelliert | Keine Rastung, Feder, Rampe oder Hinterschneidung, die Zurückdrehen blockiert |

`python3 model/check_motion_d.py` prüft jede Plattenstärke in Schritten von 0,5 mm bzw. 0,5° gegen die vier festen Körper. Der JSON-Bericht enthält Stichprobenzahl, Schnittvolumen, Mindestabstand, Gegenproben und STEP-Prüfsummen. Abtastung ist kein mathematisch lückenloser Hüllvolumennachweis. Konzentrische Zylinder und der durchgehende Einführschlitz erklären die freien Zwischenlagen zusätzlich geometrisch.

Absichtliche Gegenproben: −5° in falscher Richtung; +60° über den Anschlag; nach +50° axial um ±1,1 mm verschieben. Diese Lagen überschneiden den Stift. Damit wird insbesondere nicht nur das Ausbleiben einer Fehlermeldung als Prüfung gewertet.

## Kontakt unter Gewicht und Bedienmoment

In der mittigen Darstellungsposition trägt der Stift das Rohr noch nicht: je 1 mm axiale Luft. Unter Eigengewicht sinkt das Rohr bis zur oberen axialen Nutwand ab. Beim Hochziehen liegt die gegenüberliegende Wand am Stift an. Diese Kontaktlagen sind weder Reibungs- noch Festigkeitsnachweise. Die Animation stellt die mittige geometrische Position dar und simuliert keine Schwerkraft.

Drehmoment gelangt über Nutwand/Stift in die massive Aufnahme und über deren Klemmkontakt zur Platte. Bei festgehaltener Schraube mit Rechtsgewinde kann eine Mitdrehung der Aufnahme **gegen den Uhrzeigersinn von oben** die Aufnahme vom Schraubenkopf wegbewegen und die Klemmung lösen; **im Uhrzeigersinn von oben** kann sie sich weiter auf das Gewinde ziehen. Gerade das Eindrehen des Rohres muss deshalb am Muster geprüft werden. Drehrichtung allein ersetzt keine ausreichende Vorspannung oder Losdrehsicherung.

Der idealisierte Schraubenkonus liegt nominal an der Senkfläche: bei z=0,2 besitzt die Senkung Radius 8,0 mm, ebenso der Kopf. Reale Kopfkontur einschließlich Kopfrand ist hiervon nicht abgedeckt. Keine Vorspannung aus dem reinen Schnittvolumen ableiten.

## Toleranzen und Beschichtung

Reale Mindestluft radial = (kleinster Rohrinnendurchmesser − größter fertiger Kopfdurchmesser)/2; Beschichtung auf Kopf und Rohrinnenfläche reduziert das Spiel zusätzlich. Ovalität, Schweißnaht, Grat und Achsversatz berücksichtigen. Entsprechend Nutbreite minus größter fertiger Stiftdurchmesser prüfen. Bei Rohrersatz oder geändertem Stift CAD, Zeichnungen und Bewegungsprüfung gemeinsam neu erzeugen.

## Praktische Abnahme – noch offen

- Kalt und ohne Brennstoff prüfen; Stiftfestigkeit und Verschraubung vorher freigeben.
- Aufnahme/Platte mit gemeinsamem Kontrollstrich markieren, Einstecken und Drehen mehrfach durchführen. Kein Mitdrehen, kein Klemmen; reales Drehmoment erfassen.
- Axialspiel und Endwinkel messen; Stift darf nicht wandern. Gegen Zurückdrehen ist aktuell keine positive Sicherung nachgewiesen.
- Fackelhöhe, Gesamtgewicht, Schwerpunkt, Wind-/Stoßlast und Untergrund für Standprüfung festlegen. Die 150-mm-Platte ist kein Standsicherheitsnachweis.

Drei nächste Rückfragen: (1) Rohrinnen- und Kopfdurchmesser sowie Stiftmaß messen; (2) Originalbewegung bis Anschlag und zurück filmen, insbesondere mögliche Rastung; (3) vollständige Fackel mit Höhe/Gewicht und oberem Anschluss zeigen.

## Gesamte Montagefolge

Zusätzlich wurden je71Posen der vollständigen Animation für5/8/9mm geprüft: alle zehn Körperpaare, einschließlich radialem Stifteinsetzen, axialem Aufsetzen, Schraubenzuführung und Absetzen. Keine Volumenüberschneidung und kein Bodenunterstand an den Abtastpunkten. Bericht `web/assets/sockel-d/assembly-motion-checks.json`. Montageauflagen/Hand/Werkzeug fehlen im CAD; der35-mm-Hub zeigt den erforderlichen Zugang schematisch. Beim Schrauben wird nur die glatte Hülle geprüft, nicht das Gewindeprofil oder Vorspannung.
