# Mobiler Bedienentwurf

Stand: 2026-09-28. Separate Vorschau `ux.html`; bestehender Viewer unverändert. Kein neuer CAD-Stand, keine Fertigungsfreigabe.

## Roter Faden

Modell verstehen → Aufbau nachvollziehen → Teile, Nachweise und Beschaffung beurteilen.
Drei gleichbleibende Bereiche: Modell, Aufbau, Projekt. Unterlagen bleiben aus ihrem sachlichen Zusammenhang erreichbar. Mobile Navigation unten, Desktop oben. Keine zweite globale Navigation.

## Kritik und konkrete Antwort

| Problem | Umsetzung |
|---|---|
| Konkurrierende Navigation und pseudoaktive Links | Drei echte Bereichsschalter mit eindeutigem Aktivzustand |
| Zu kleine mobile Schrift | 16 px Fließtext, 14–15 px ergänzende Texte; kleine Schrift nur für Metadaten |
| Beliebige Karten, Radien und Farbfelder | Offene Flächen, typografische Hierarchie, feine Trennlinien; Radien auf Bedienelemente begrenzt |
| Unruhige Grüntöne | Graphit, warmer neutraler Hintergrund, gezieltes Terrakotta für aktive Navigation und Hauptaktion |
| Unbeabsichtigtes Drehen statt Scrollen | Statische CAD-Vorschau als Einstieg; 3D ausdrücklich aktivieren und beenden |
| Nur Gesten als Steuerung | Drehen, Zoomen und Rücksetzen auch über Schaltflächen |
| Montagebild und Erklärung getrennt | Ein Bild, ein Schritt, ein erklärender Text und direkt anschließende Steuerung |
| Unlesbare Stücklistentabellen | Fünf ausklappbare Bauteilzeilen mit CAD, Kandidat und offener Entscheidung |
| A3-Blatt als kleiner Modellersatz | Eigene Bilder aus bestehenden CAD-Netzen; Zeichnungen separat groß öffnen |
| Unklare Belastbarkeit von Angaben | Konzeptstatus; Kandidatenabweichungen, fehlende Nachweise und Kostenbasis ausdrücklich benannt |

Primäre Touch-Ziele mindestens 48 px hoch. Dialoge verwenden native Fokusführung und Escape. Reduzierte Bewegung erhält manuelle Schritte. Keine automatische 3D-Bewegung. Die CAD-Bildfolge ist keine kontinuierliche Montageanimation und keine Kontakt- oder Kraftsimulation.

## Erweiterungsvertrag für spätere Browseränderungen

Noch nicht implementiert: geometrische Maßänderungen. Heute wählt die Oberfläche nur vorhandene 5-/8-/9-mm-Dateien.

| Zustand/Parameter | Bedeutung | Folge |
|---|---|---|
| sourceRevision | D-V03 mit Quelldatei-Prüfsumme | Ausgangsstand nachvollziehbar |
| plate | 5, 8 oder 9 mm | Modell, Bilder, Zeichnung und Download gemeinsam wechseln |
| view / step / selectedPart | Darstellung, Montageschritt, Bauteil | Reine Anzeigeänderung |
| camera / transparency | Ansicht und Transparenz | Keine Änderung der CAD-Geometrie |
| temporaryDimensions | Spätere temporäre Maßvorschau | Geometrisch veränderte Vorschau ausdrücklich ungeprüft |
| dirty / validationState | Änderung gegenüber Quelle; unbekannt, ungültig oder geprüft | Bestehende Nachweise nicht auf Vorschau übertragen |

Spätere Maßansicht: Ausgangswert, temporärer Wert, Einheit, Herkunft und zulässiger Eingabebereich zusammen anzeigen. Unbekannte Grenzen nicht erfinden. Aktionen: Vorschau anwenden, Ausgangsstand vergleichen, zurücksetzen. Keine STEP-Datei mit unveränderten Ausgangsmaßen als Export der geänderten Vorschau ausgeben. CAD-Neuberechnung bleibt ein eigenständiger späterer Arbeitsschritt.

## Prüfumfang

`ux-review.html` zeigt echte eingebettete Seiten bei 320, 375, 390 und 428 CSS-Pixeln. Dies ersetzt keine Prüfung auf iOS Safari oder Android. Desktop und schmale Browseransichten visuell prüfen; Navigation, Dialoge, Plattenwechsel und Downloads zusätzlich funktional prüfen. Ein grüner Build ist keine ästhetische Abnahme.

Die Modellbilder stammen aus den unveränderten D-V03-Netzen. Der Renderer verändert nur Projektion, Licht und bereits definierte Montagepositionen. Alle fünf Teile bleiben plate, adapter, pin, screw und tube.

### Durchgeführt

Live-Vorschau f00e2a9: Desktop visuell geprüft. Drei echte Browserrahmen mit Außenbreiten 320/375/390/428 px; wegen Rahmen und Desktop-Scrollbalken verfügbare Inhaltsbreite jeweils 17 px kleiner. Kein horizontaler Inhaltsüberlauf in Modell, Aufbau und Projekt. Geprüft: Plattenwechsel auf 9 mm einschließlich PDF-Link, Exportdialog öffnen/schließen, nächster Montageschritt, Abspielen/Pause, Kostenwahl 10 Stück. Screenshot: `ux-mobile-review.jpg`. Noch keine Geräteprüfung auf iOS/Android; 3D-WebGL-Funktion in dieser Cloud-Umgebung nicht visuell nachweisbar. Bestehende Unterseiten verwenden weiterhin ihr bisheriges Layout. Die neue Vorschau ist daher kein abgeschlossener Austausch aller Seiten.
