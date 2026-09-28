# Viewer D-V03 · aktueller Funktionsvertrag

Fünf CAD-abgeleitete Teile, mm-Einheiten, drei vorhandene Plattenausführungen. Verfügbar: Drehen/Zoom, feste Ansichten, vorbereiteter Halbschnitt, Transparenz, Teileauswahl, Explosion, definierte Maßanzeigen, PNG-Export und geführte Konzeptmontage. Keine freie CAD-Messung, kein verschiebbarer exakter Schnitt, kein Geometrieeditor.

Plattenwahl, Zeichnungen, STEP und Dokumentnavigation funktionieren unabhängig von Three.js/WebGL. Die URL führt `plate=5`, `8` oder `9`; eine lokale Merkhilfe ist optional. Eine explizite URL-Auswahl hat Vorrang. Kosten zeigen die Auswahl, aber erklären ausdrücklich die abweichende 5-mm-Kandidatenstudie. Es wird kein Preis für 8/9 mm erfunden.

Montage: Zielbilder per Schrittwahl, passende Aktionsbeschreibung in Übergängen, Pause/Replay, kein Autoplay. Bei reduzierter Bewegung nur manuelle Schrittwahl. Freie Ansichts- und Ausblendwerkzeuge sind während geführter Montage gesperrt; Schnitt betrifft dort den Sockel, nicht das rotierende Rohr. Nach Verlassen ist freie Betrachtung wieder möglich. Auf kleinen Bildschirmen ist die Montageansicht verkleinert; sie bleibt im normalen Seitenfluss. Keine klebenden Elemente.

Keine Kraft-, Gewinde- oder Schwerkraftsimulation. Freier Rückweg; Kontakt unter Gewicht bleibt im Begleittext erklärt. Schnitte, Sichtbarkeit und Explosion verändern keine CAD-Datei. PNG enthält die 3D-Darstellung, keine vollständige Dokumentation oder Freigabe.

Fehlerfälle: 3D-Steuerung deaktivieren, verständlichen Status zeigen, keine veralteten Modelle als aktuelle Auswahl stehen lassen. Dokumente bleiben erreichbar. Revision und die fünf Teile-IDs werden beim Laden geprüft.

Spätere Vorschauänderungen ohne Modellgenerierung: [Backlog](next-features.md). Vor Umsetzung klare Trennung zwischen Anzeigeänderung und ungeprüfter Geometrieänderung festlegen.

## Gestaltung

Gemeinsame Navigation und `design.css` für alle sechs aktuellen Seiten. Keine dekorativen Karten, keine kastenförmigen Navigationslinks. Funktionale Bedienelemente sind von Dokumentlinks getrennt. Modell zuerst, weiterführende Texte auf den Fachseiten. WebGL-Ersatzansicht zeigt ausdrücklich die vorhandene Prüfzeichnung, kein vorgetäuschtes 3D.
