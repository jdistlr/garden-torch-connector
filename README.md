# Gartenfackel: Verbindungsrohr gemeinsam nachbauen

Hier sammeln wir alles, was wir brauchen, um ein vorhandenes Verbindungsrohr für eine Gartenfackel-Vorrichtung nachvollziehbar zu dokumentieren und daraus später einen Fertigungsauftrag zu machen.

**Stand: 28. September 2026 — Bilder und Planung sind vorhanden. Die Maße sind noch zu bestätigen; ein CAD-Modell und eine Fertigungszeichnung gibt es noch nicht.**

## Ab jetzt: ein sichtbares Ergebnis pro Runde

Wir beginnen mit einem **Formabgleich aus Fotos und einer einfachen Skizze**. Danach folgen wenige CAD-Ansichten, ein minimaler drehbarer Web-Viewer und gezielte Maßkorrekturen. Ein früher Entwurf darf klar markierte Foto-Schätzungen enthalten; er ist nicht fertigungsfreigegeben.

Der erste Viewer bekommt nur Drehen/Zoomen, Ansicht zurücksetzen und eine Infobox mit Maßen und Status. Schnitte und weitere Panels folgen schrittweise. Pro Runde klären wir höchstens drei konkrete Fragen. Siehe [kurzer Projektplan](docs/plan.md) und [wiederverwendbarer Ablauf](docs/workflow.md).

## Neu dabei? Hier anfangen

Du brauchst zum Mitlesen keine CAD-Software und musst nichts installieren. Dieses Repository ist unser gemeinsamer Projektordner mit nachvollziehbarer Änderungshistorie. Die README ist seine Startseite.

1. Schau dir unten das Bauteil und die [Bildübersicht](sources/README.md) an.
2. In der [Maßliste](docs/measurements.md) steht, was wir noch messen und klären müssen.
3. Der [Projektplan](docs/plan.md) beschreibt den Weg bis zum Auftragspaket.

## Um welches Teil geht es?

Im Mittelpunkt steht das **Metallrohr mit einem offenen Längsschlitz und einer seitlichen Aussparung**. Auf den Fotos liegt daneben ein Erdspieß mit einem dickeren Kopf und einem seitlich herausstehenden Stift.

![Vorhandenes Rohr und Erdspieß nebeneinander](sources/previews/06.jpg)

*Originalbauteile, noch kein CAD-Rendering.*

Der Stift scheint im Schlitz geführt und durch Verdrehen in die seitliche Aussparung bewegt zu werden. **Diese Steck-Dreh-Funktion ist bisher eine Interpretation der Fotos und muss am Bauteil bestätigt werden.**

Zunächst bearbeiten wir das Rohr. Der Erdspieß dient als Gegenstück, damit die Verbindung später passt. Seine Neufertigung ist bisher nicht Teil des Auftrags. Wie die Fackel am anderen Rohrende befestigt wird, ist noch zu klären.

## Was ist schon erledigt?

| Bestandteil | Stand |
|---|---|
| Bilder sichten und zuordnen | Erledigt: 16 Dateien, davon 14 unterschiedliche Fotos |
| Bildübersicht im Repository | Vorhanden |
| Projektplan und Werkzeugvorschlag | Vorhanden |
| Maßliste und offene Fragen | Vorhanden |
| Maße verbindlich bestätigen | Offen |
| Änderbares 3D-Modell erstellen | Geplant |
| Bemaßte Zeichnung und STEP-Datei | Geplant |
| Auftragspaket für einen Fertiger | Geplant |
| Engineering-Web-Viewer mit Informationspanels | Geplant; fester Bestandteil des Zielumfangs |

Die Fotos 07 und 12 sind exakte Duplikate von 02 beziehungsweise 03. Im Repository liegen 14 verkleinerte Vorschauen ohne übernommene Kamera-Metadaten. Die hochauflösenden Originale sind hier noch nicht enthalten. Dateinamen und Prüfsummen der Originale stehen im [Quelleninventar](sources/inventory.json).

## Was wollen wir am Ende haben?

- **Ein 3D-Modell**, dessen Maße sich gezielt ändern lassen.
- **Eine technische Zeichnung als PDF**, mit Ansichten, Schnitt und Detail des Schlitzes.
- **Eine STEP-Datei**, mit der ein Fertiger das räumliche CAD-Modell weiterverwenden kann.
- **Einen Engineering-Web-Viewer**, in dem ihr das Modell drehen, schneiden und mit Maß-, Kennwert- und Quellenpanels untersuchen könnt.
- **Anschauliche Modellbilder**, damit Form und Zusammenbau leicht verständlich sind.
- **Eine kurze Auftragsbeschreibung** mit Material, Stückzahl, Oberfläche und abgestimmten Anforderungen.

Ein schönes Modellbild zeigt die Form. Für die Fertigung brauchen wir zusätzlich eindeutige Maße, zulässige Abweichungen und Materialangaben.

## Wie gehen wir vor?

1. **Bestand verstehen:** Fotos zuordnen und die tatsächliche Montagebewegung erklären.
2. **Maße aufnehmen:** Vorhandene Linealfotos auswerten und relevante Werte direkt am Bauteil bestätigen.
3. **Modell aufbauen:** Rohr und Ausschnitte aus den bestätigten Maßen erzeugen.
4. **Gemeinsam prüfen:** Passen Aussparung, Stift, Drehrichtung und Gegenstück zusammen?
5. **Zeichnung und Auftrag fertigstellen:** Material, Oberfläche, Stückzahl und zulässige Maßabweichungen mit dem Fertiger abstimmen.

Dabei unterscheiden wir immer zwischen **auf dem Foto gesehen**, **aus dem Foto geschätzt**, **gemessen und bestätigt** und **neu entschieden**. So wird eine Schätzung nicht versehentlich zur Fertigungsvorgabe.

## Das Modell im Browser untersuchen

Geplant ist eine Three.js-Ansicht mit technischen Standardansichten, sichtbaren Kanten, Transparenz und einer Schnittebene. Daneben zeigen Panels Maße, Materialvolumen, Modellstand, Bildquellen und offene Punkte. Masse wird erst bei bekanntem Material und bekannter Dichte berechnet.

Das Browserbild wird aus dem CAD-Modell abgeleitet. Verbindliche Maße und Kennwerte stammen aus der CAD-Geometrie; ein angeklicktes Dreieck im Browser wäre nur eine Näherung. Der Viewer ist noch nicht gebaut. [Funktionen und Qualitätsanforderungen](docs/web-viewer.md) sind jetzt dokumentiert.

## Was könnt ihr jetzt beitragen?

Für die erste Runde bitte diese fünf Werte in **Millimetern** aufnehmen:

| Maß | Was genau messen? |
|---|---|
| Rohrlänge | Von einer Stirnfläche bis zur anderen |
| Außendurchmesser | Außen über das Rohr, möglichst an mehreren Stellen |
| Innendurchmesser | Die Öffnung am ungeschlitzten Ende |
| Schlitzbreite | Abstand zwischen den geraden Schlitzseiten |
| Gesamte Schlitztiefe | Vom geschlitzten Rohrende bis zum entferntesten Punkt der Rundung |

Durchmesser und Schlitzbreite möglichst mit einem Messschieber messen. Die seitliche Aussparung und das Gegenstück erfassen wir anschließend nach der [ausführlichen Maßliste](docs/measurements.md).

Zum Durchgeben reicht beispielsweise diese Vorlage:

> Rohrlänge: … mm  
> Außendurchmesser: … mm  
> Innendurchmesser: … mm  
> Schlitzbreite: … mm  
> Gesamte Schlitztiefe: … mm  
> Messmittel: …  
> Gemessen am: …

Zusätzlich helfen Antworten auf diese Fragen:

- Soll das Rohr exakt nachgebaut oder verändert werden?
- Wie wird die Verbindung zusammengesteckt, verdreht und wieder gelöst?
- Was sitzt am anderen Rohrende?
- Welches Material und wie viele Stück werden gewünscht?

Ihr könnt Maße und Erläuterungen im gemeinsamen Chat durchgeben. Wer einen GitHub-Account hat, kann auch unter [Issues](https://github.com/jdistlr/garden-torch-connector/issues) eine Frage oder Messung festhalten. Bitte das zugehörige Foto beziehungsweise Bauteil nennen. Zum bloßen Mitlesen braucht ihr beim aktuell öffentlichen Repository keinen Account.

## Welche Werkzeuge sind vorgesehen?

| Werkzeug | Einfach erklärt |
|---|---|
| **CadQuery** | Erstellt das 3D-Modell aus einem Programm und einer Maßtabelle. Eine Maßänderung kann dadurch in das Modell übernommen werden. |
| **FreeCAD mit TechDraw** | Öffnet CAD-Modelle und hilft, technische Zeichnungen daraus abzuleiten. |
| **GitHub** | Bewahrt Dateien, Entscheidungen und Änderungen gemeinsam auf. |

CadQuery ist als zentrale Modellquelle vorgesehen. Ein zusätzlicher MCP-Server ist für diesen dateibasierten Ablauf zunächst nicht nötig. Die CAD-Umgebung und Exportabläufe sind noch nicht eingerichtet oder getestet.

Die Begründung und offiziellen Dokumentationslinks stehen in der [Werkzeugentscheidung](docs/toolchain.md).

## Wo finde ich was?

| Datei oder Ordner | Inhalt |
|---|---|
| [sources/README.md](sources/README.md) | Bildübersicht mit festen Bildnummern |
| [sources/inventory.json](sources/inventory.json) | Original-Dateinamen, Prüfsummen und Duplikatzuordnung |
| [docs/plan.md](docs/plan.md) | Arbeitsschritte und Kriterien für den Abschluss |
| [docs/measurements.md](docs/measurements.md) | Ausführliche Maßliste und Funktionsfragen |
| [docs/toolchain.md](docs/toolchain.md) | Werkzeugwahl und geplante Dateiformate |
| [docs/web-viewer.md](docs/web-viewer.md) | Browseransicht, Informationspanels und Qualitätsanforderungen |
| [parameters/connector.json](parameters/connector.json) | Vorbereitete Maßtabelle für das spätere Modell |

In der Parameterdatei bedeutet `null`: **noch unbekannt**, nicht null Millimeter.

## Freigabe und Veröffentlichung

Das Repository ist derzeit **öffentlich**. GitHub Pages und eine interaktive 3D-Ansicht sind noch nicht eingerichtet.

Aktuell liegt eine **Projektgrundlage, keine Fertigungsfreigabe** vor. Erst wenn relevante Maße, Material, Funktion und Anforderungen geprüft sind, wird ein eindeutig gekennzeichnetes Auftragspaket zusammengestellt.
