# Projektintegration · 29.09.2026

Der Nutzer hat die Reduktion auf einen Sockel-Viewer und die Drei-Bereiche-Vorschau verworfen. Ziel ist die gemeinsame Arbeitsumgebung für alle vorhandenen Funktionen. Der neue Einstieg ist `projekt.html`; `ux.html` ist kein aktueller Projekteinstieg.

| Funktion | Erreichbarkeit | Quelle / Zustand |
|---|---|---|
| Übersicht und nächste Tätigkeit | Projektstart | projekt-d.md; keine behauptete physische Erledigung |
| Originalfotos und Messliste | Fotos & Maße, Bauteillinks | measurements.md und sources/README.md; beim Rendern zusammengeführt |
| Festlegungen und offene Entscheidungen | Entscheidungen | entscheidungen-d.md |
| Modell, Schnitt, Transparenz, Explosion, Maße, Sichtbarkeit, PNG | Modell & Zeichnungen | unveränderte D-V03-Geometrien, sockel-d.js |
| Geführte Animation, Schritte, Pause, Tempo | Montage-Link öffnet Modell im Montagemodus | montage-d.js; Posen unverändert |
| Bauteilherkunft, Kandidat und Einbau | Bauteile, Modellseitenleiste | bauteile-d.md; Querverweise auf Originalbeleg und Artikelposition |
| Mechanik und Prüfberichte | Mechanik & Prüfung | bestehende geometrische Nachweise; keine neue Lastprüfung |
| Artikel und Händler | Beschaffung; Anker je Position mit Rückweg zum Bauteil | bestehende Recherche vom 28.09.; keine neue Preisabfrage |
| Mengen und Fertigungsannahmen | Kosten | bestehende 1/5/10-Studie mit abweichenden Teilen; keine 8/9-mm-Gesamtsumme |
| Zeichnungen, STEP und Druck | Modell & Zeichnungen, Bauteile, Dokumentdruck | Plattenwahl über URL und lokale Merkhilfe |

Auf allen neun aktuellen Seiten dieselbe Navigation. Plattenwahl 5/8/9 auf jeder Fachseite, URL gewinnt vor Merkhilfe. Bauteil- und Animationslinks erhalten zusätzliche Parameter. Mobile Tabellen zeigen Feldbeschriftungen ohne horizontalen Leseweg. Viewerwerkzeuge bleiben sichtbar. Modellgesten ausdrücklich aktivieren und beenden, Zoom auch mit Tasten.

Spätere Geometriebearbeitung bleibt zurückgestellt. Nachweise, Angebote und physische Prüfungen werden durch die Projektintegration nicht vervollständigt. Keine Händlerkommunikation.

## Verifikation

27 Kombinationen aus neun Seiten und drei Plattenstärken sowie Zustandswechsel per DOM geprüft. Alle neuen lokalen Sprungziele auf Existenz geprüft. Live: Plattenparameter im Montage-Link, Bauteil → Beschaffung und Rückverweis; mobile Rahmen 320/375/390 ohne horizontalen Inhaltsüberlauf. Desktop-Einstieg visuell geprüft. Cloud-WebGL nicht verfügbar; CAD-Bild und Downloads bleiben nutzbar. Keine reale iOS-/Android-Prüfung. Dokument- und Modellansichten enthalten weiterhin die vollständigen vorhandenen Fachinformationen.
