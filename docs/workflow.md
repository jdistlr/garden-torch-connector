# Wiederverwendbarer Ablauf: Foto → CAD → Ansicht → Auftrag

Für überschaubare mechanische Bauteile. Kein automatischer 3D-Scan: Aus Fotos wird die Geometrie interpretiert und durch gezielte Messungen abgesichert.

1. Quellen sammeln, Bilder nummerieren, Duplikate erkennen.
2. Zuerst alle getrennten Bauteile inventarisieren und den Modellumfang abgleichen. Dann sichtbare Merkmale markieren und die Funktion in einem Satz festhalten.
3. Nur die für den nächsten Entwurf erforderlichen Maße erfassen.
4. Ein parametrisches Modell und wenige Ansichten erzeugen.
5. Mit dem Original vergleichen, höchstens drei konkrete Fragen stellen, korrigieren.
6. Dasselbe Modell im einfachen Browser-Viewer zeigen.
7. Erst nach Maß- und Funktionsklärung Fertigungsunterlagen ableiten.

## Minimale Projektdaten

| Feld | Bedeutung |
|---|---|
| Bauteil | Name und Zweck |
| Merkmal | Eindeutige Bezeichnung, etwa Rohrlänge oder Schlitzbreite |
| Wert und Einheit | Unbekannt bleibt leer/null |
| Status | Foto-Schätzung, bestätigte Messung oder konstruktive Entscheidung |
| Quelle | Bildnummer, Messangabe oder Entscheidung |
| Unsicherheit | Ablesebereich oder Messunsicherheit, soweit bekannt |
| Revision | Stand, zu dem Angabe und Modell gehören |

Beispielstruktur ohne erfundene Maßzahlen:

```json
{
  "feature": "tube_length",
  "value": null,
  "unit": "mm",
  "status": "unknown",
  "source": null,
  "uncertainty": null
}
```

## Wiederverwenden ohne Umbau

Beim nächsten Bauteil diese Anleitung und die Ordnertrennung übernehmen: sources, parameters, model, exports und gegebenenfalls viewer. Ordner erst anlegen, sobald Inhalt entsteht. Bauteilgeometrie bleibt projektspezifisch. Ein gemeinsamer Viewer oder Exporthelfer wird erst nach praktischer Bewährung extrahiert.

## Qualität von Anfang an

Status und Einheiten sichtbar machen. Modell, Ansichten und Downloads aus derselben Revision ableiten. CAD-Kennwerte im CAD-Kern berechnen. Foto-Schätzungen nie als Fertigungsmaße ausgeben. Neue Infrastruktur nur hinzufügen, wenn sie ein beobachtetes Problem löst.
