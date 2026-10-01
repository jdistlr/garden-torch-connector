# Übergabe · D-V03 nach Konsistenzaudit

## Desktop-Arbeitsoberfläche · 01.10.2026

Neue gemeinsame Layoutschicht `web/workbench.css`: ab 1100 px dauerhafte, nach Tätigkeit gruppierte Projektnavigation. Bildgestützter Projekteinstieg aus vorhandener CAD-Explosionsansicht, nächster realer Messaufgabe und drei Arbeitsphasen. Fachseiten erhalten eine Abschnittsnavigation; Bauteile, Mechanik und Montage nutzen CAD-Abbildungen mit Verweis zum Viewer. Modell: Szene links, zusammenhängender Inspektor rechts, Nachweise darunter. Die bisher unsichtbare Überschrift der geschlossenen Darstellungsoptionen ist wieder bedienbar. Unter 760 px wird gestapelt; keine zweite Kopie der Modellsteuerung. Preview-Bilder folgen der Plattenwahl. Neue Präsentationsbausteine im Generator `model/desktop-layout.cjs`; Dokumentquellen und bestehende Funktions-IDs bleiben erhalten. Keine CAD-, Materialfestlegungs- oder Bewegungsänderung. `python3 model/test_workbench.py` prüft Navigation, IDs und Abschnittsanker aller neun Seiten. Visuelle Browserprüfung zusätzlich erforderlich; WebGL-Fähigkeit getrennt vom HTML-Layout bewerten.

Stand 28.09.2026. Ausgangscommit der Reparatur: `59661168c681c6fc0ee955d2f77ed9527727616c`. Frühere Übergabetexte sind in Git erhalten. Aktueller Einstieg: README und [Entscheidungskette](entscheidungen-d.md).

## Verbindlich

Nur D, Vollmaterial mit direktem axialem Gewindesackloch; fünf Teile plate/adapter/pin/screw/tube. Kein Bodenunterstand. Keine Buchse/Fügezone, keine Varianten A–C. Repository und Veröffentlichung autorisiert; Händlerkontakt/Bestellung nicht. Deutsch, sichtbare kleine Ergebnisse und regelmäßige Statusmeldungen; nach Abschluss keine laufenden Tasks behaupten.

## Reparaturumfang

- D-V03 als einheitlicher Einstieg, Original D02 und V01 als historische Referenzen; README/Plan/Toolchain/Viewer-Dokumentation bereinigt.
- Gemeinsame Entscheidungskette mit aktueller CAD-Stückliste, ausdrücklich abweichenden Recherchekandidaten, Nachweisen, Tätigkeiten und Abschlusskriterien.
- Plattenzustand über URL und Seitenlinks; Zeichnungs-/STEP-Auswahl unabhängig von WebGL. Keine 8/9-mm-Gesamtkosten vorgetäuscht.
- Animation erklärt die laufende Aktion statt den vorherigen Schritt. Ganzzahlige Schrittwahl zeigt Zielbild. Posefunktion unverändert. Sockelschnitt ohne rotierende Rohr-Halbschnitte; freie Ansichts-/Teilewerkzeuge während Montage gesperrt. Reset und Fehlerzustände bereinigt; reduzierte Bewegung über manuelle Schritte.
- Kostensummen im Text gerundet; exakte Rechenwerte bleiben im JSON. Studie betrifft andere Teile und ist kein Preis des aktuellen CAD.
- Dateihash-Manifest und Prüfung gegen generierte Dokumentseiten/lokale Links. Keine automatische universelle CAD-Parametrisierung behaupten.
- Frontend-Modifikationen ohne neue Modelle nur als spätere Ausbaustufe dokumentiert.

## Unverändert / offen

CAD, STEP, A3 und nominale Bewegungspose bleiben unverändert. Die gespeicherten mechanischen Prüfberichte stammen aus der vorherigen Sitzung. Aktuelle Softwareprüfung erzeugt keinen zusätzlichen Festigkeitsnachweis. Reale Maße, Schraubenkopf, Stiftsicherung, Losdrehen, Werkzeugzugang, obere Fackelschnittstelle und Standfestigkeit müssen physisch bzw. konstruktiv geklärt werden. Keine Fertigungs-/Betriebsfreigabe.

## Fortsetzung

Zuerst Remote-HEAD und Pages prüfen. `docs/viewer-runbook.md` enthält Befehle und Veröffentlichungskriterien. Bilder in `sources/previews/` zuerst nutzen; alte Scratch-Pfade können fehlen. Details zur Originalbewegung, Spiel und Schraubenwirkung: `docs/mechanik-d.md`. Nächste drei Nachweispakete in `docs/entscheidungen-d.md`.

## Softwareprüfung dieser Reparatur

Release-Prüfung: drei Modellidentitäten, generierte Dokumentseiten und lokale Links. 2.103 Posen gegenüber dem Ausgangscommit exakt identisch; ein festgehaltener Hash der 213 nominalen Abtastposen erkennt spätere Bewegungsänderungen. DOM-Integration prüft Plattenwahl und Downloads mit/ohne WebGL, Seitenkontext, Aktionszuordnung, Pause/Reset und reduzierte Bewegung. Dafür wird der Renderer ersetzt; das ist keine visuelle 3D-Prüfung. Der lokale Chromium-Download schlug fehl. Live-Dokumentprüfung folgt nach Veröffentlichung.

## Layoutkorrektur nach Nutzerkritik

Die frühere Karten-/Linkleisten-Erweiterung wurde gestalterisch zurückgenommen. Aktuelle Seiten nutzen `web/design.css` und die gemeinsame Navigation aus `model/site-shell.cjs`. Hauptseite: kurzer Kopf, drei Sprunglinks, Modellarbeitsfläche, danach Zeichnungen und Maße/Dateien. Doppelte Budget-/Montage-/Statuszusammenfassungen entfernt; vollständiger Inhalt bleibt auf den Fachseiten. Darstellungsoptionen sind aufklappbar, Montagebedienung erscheint nur im Modus. Kein klebender Kopf oder klebender Viewer. Bei WebGL-Ausfall wird die vorhandene Zusammenbau-Prüfzeichnung eindeutig als Ersatzansicht gezeigt. CAD und Posen unverändert.

## Separate mobile UX-Vorschau (2026-09-28)

`web/ux.html` bietet Modell / Aufbau / Projekt; `web/ux-review.html` dient der schmalen Browserprüfung. Hauptviewer nicht ersetzt. Konzept, Erweiterungsvertrag und tatsächlicher Prüfumfang: `docs/ux-entwurf.md`. CAD unverändert. Bildfolge mit acht Zielbildern, keine neue kontinuierliche Montageanimation. Mobile Browserrahmen geprüft, reale iOS-/Android-Geräte und WebGL noch offen. Für vollständige Umstellung müssen auch verlinkte Bestandsdokumente ins neue Layout überführt werden.

## Gemeinsame Projektoberfläche · 29.09.2026

Nutzer lehnt auch die Drei-Bereiche-Vorschau ab: vollständige Orchestrierung aller vorhandenen Funktionen beauftragt. Neuer Einstieg `web/projekt.html` mit nächster Tätigkeit und vollständigem Funktionsverzeichnis. Fotos/Maße, Entscheidungen, Modell/Zeichnungen, Bauteile, Mechanik, Montage, Beschaffung und Kosten verwenden die gemeinsame Oberfläche. `docs/projekt-integration.md` dokumentiert Quelle und Verbindung jeder Funktion. Bauteile verbinden Fotos, Kandidaten, Prüfungen, STEP und konkrete Animationsschritte. `web/ux.html` bleibt alter Entwurf; nicht zur Hauptseite machen. CAD und Posen unverändert. Reale Smartphone-Geräte und WebGL in der Cloud weiterhin nicht nachweisbar.


## Szenenwerkzeuge · September 2026

- Bauteilwahl per Liste und 3D-Treffer, Hervorhebung und Verbindungen zu Bauteilangaben, Fotos/Messliste, Beschaffung und Einbauschritt. Die Textauswahl funktioniert auch ohne WebGL.
- Fünf Untersuchungsfragen führen zu Kamerapositionen; Übergänge sind unterbrechbar und bei reduzierter Bewegung unmittelbar.
- Verschiebbarer Y-Schnitt mit Stencil-Schnittflächen; nur Darstellung, keine Änderung an CAD oder Downloads. Während Montage gelten die vorhandenen erklärenden Sockelschnitte.
- Montage hebt das aktive Teil hervor; Richtungspfeile und optionale vorherige Position ergänzen die unveränderte Posefunktion. Keine Rastung ergänzt.
- Technische/Produktdarstellung mit prozeduraler Studioumgebung; automatische oder manuelle Renderqualität. Oberflächen sind Visualisierungen, keine Materialfestlegung.
- Ansichtslink speichert Kamera, Plattenwahl, Teil, Darstellungszustand und pausierten Montageschritt. PNG kann Revision, Plattenstärke und Konzeptstatus enthalten.

Prüfung: DOM-Integration mit realer Three.js-Geometrie/Mathematik und ersetztem Renderer prüft Auswahl, Schnittzustand, Montage, Positionshilfe, Teilen, Reset und Qualität. Nominale Posen bleiben durch bestehenden Regressionstest geschützt. Der Cloud-Browser kann keinen WebGL-Kontext erstellen: Licht, Schatten, Stencil-Kappen und Antialiasing sind dort **nicht visuell geprüft**. Vor visueller Abnahme auf einem WebGL-fähigen Smartphone und Desktop insbesondere Schnitt durch Gewindesackloch, Bauteilauswahl, Touch-Scroll/Drehen und Wiederöffnung eines Ansichtslinks prüfen.
