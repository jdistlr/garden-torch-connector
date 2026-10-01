# One More Thing · XR-DEMO / 01

Separater Nutzerauftrag vom 01.10.2026: eine fiktive Röntgenstrahler-Demonstration als Beleg für die Übertragbarkeit des Projekt-Workflows. **Kein realer Bauplan, keine Strahlenquelle, keine Fertigungs- oder Betriebsfreigabe.** D-V03 bleibt unverändert.

## Zusammenhängender Ablauf

Menüpunkt → Übersicht → Modell und Erklärmontage → Funktionsprinzip → fiktive Stückliste/Beschaffung → zwei A3-Schemablätter → zurück zur Gartenfackel.

Elf auswählbare Baugruppen einschließlich Kathode, Anodenteller mit Rotor und symbolischem Flüssigmetalllager. Die Erklärmontage verschiebt Baugruppen einzeln; sie ist weder Kollisionsprüfung noch reale Fertigungsfolge. Der separate Funktionsablauf visualisiert Elektronen, Entstehung von Röntgenstrahlung und Wärme sowie die Rolle der Rotation/Lagerung. Farben und Teilchenbahnen sind Symbolik, keine Simulation. Keine Betriebswerte oder reale Lagerauslegung.

Alle Maßzahlen, Anbieter und Preise sind erfunden. Summe 1.065 Demo-Euro pro Satz; keine echte Kostenkalkulation. Keine Händlerkontakte oder Bestellungen.

## Implementierung und Grenzen

- `web/xray-model.js`: gemeinsame illustrative Three.js-Netze, Posen, Metadaten und CPU-Vektorprojektion.
- `model/render_xray.mjs`: reproduzierbare HTML-, SVG-, JSON- und STL-Ausgaben. STL enthält Darstellungsnetze, keine fertigungstauglichen Volumenkörper; bewusst kein STEP.
- `web/xray.js`: Auswahl, Fokussieren, Sichtbarkeit, Transparenz, offener Halbschnitt, Schrittsteuerung/Pause, Ansichtslink und gekennzeichneter PNG-Export.
- `web/xray-principle.js`: separat steuerbarer schematischer Erklärablauf.
- Browser ohne WebGL erhalten dieselben Netze als interaktive CPU-SVG-Projektion. Überdeckungen und Transparenz sind vereinfacht. Reduzierte Bewegung verhindert automatisches Abspielen; Einzelsteps bleiben möglich.
- `npm run check` prüft Datenbezüge, endliche Posen, Sichtbarkeit und Veröffentlichungskonsistenz. Kein Test bestätigt Strahlenschutz, Festigkeit, Herstellbarkeit oder Physik.

## Hintergrundquellen

Nur für die allgemein erklärten Zusammenhänge, nicht als Modellvorlage:

- [Siemens Healthineers Academy: X-ray technology basics](https://academy.siemens-healthineers.com/_/en-us/x-ray-essentials-basics-of-x-ray-technology-job-aid/)
- [Siemens Healthineers OEM: X-ray tubes](https://www.oem-products.siemens-healthineers.com/x-ray-tube)

Quellenstand: 01.10.2026. Keine Nachbildung eines Herstellerprodukts.

## Prüfstand 01.10.2026

Automatische Prüfungen erfolgreich: elf IDs, 45 endliche Montageposen, Stücklisten-/Beschaffungsanker, isolierte Bauteilwahl, transparente Hülle, SVG-Projektion und unveränderte D-V03-Posen. Vier SVG-Dateien als XML geprüft.

Live-Browser: Desktop-Einstieg, Lagerauswahl/Fokussieren, Lager-Einbauschritt 4 → Kathode Schritt 5, Montage-Start/Pause, Funktionsschritte und Rücksprung zum Anodenteller sowie Ansichtslink-Erzeugung geprüft. Mobile 320-Pixel-Prüfansicht: Schrittwahl und Bedienelemente nutzbar; Kamera nach Prüfung an schmale Szenen angepasst. `web/xray-review.html` stellt echte 320/375/768/1280-Pixel-Browserrahmen bereit, keine Geräteemulation.

Der Cloud-Browser bietet keinen WebGL-Kontext. Visuell geprüft ist deshalb die CPU-Vektor-Ersatzansicht; reale GPU-Beleuchtung/Transparenz und Touch-Gesten auf einem physischen Telefon sind weiterhin nicht abgenommen. Schematische Bewegung ist kein Kollisionsnachweis.
