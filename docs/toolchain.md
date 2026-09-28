# Aktuelle Werkzeugkette D-V03

CadQuery 2.7.0 erzeugt Volumenkörper, STEP und Mesh-JSON in Millimetern. `model/drawings_d.py` erzeugt die A3-PDFs mit ReportLab. Three.js stellt die CAD-abgeleiteten Netze und vorbereiteten Schnitte dar. FreeCAD/TechDraw war eine frühere Option und ist keine Voraussetzung des vorhandenen Exports. GLB ist derzeit nicht im Einsatz.

`model/render_docs.cjs` erzeugt Dokumentseiten aus Markdown. `model/check_release.py` prüft die gemeinsame Veröffentlichung gegen ein Dateihash-Manifest. Dieses Manifest dokumentiert Zusammengehörigkeit; es ist kein zusätzlicher mechanischer Nachweis.

Generatoren enthalten noch Konzeptkonstanten außerhalb der JSON-Parameterdatei. Bis zu einer vollständigen Parametrisierung müssen Geometrieänderungen gemeinsam durch CAD-, Zeichnungs-, Bewegungs- und Dokumentprüfung laufen. Keine beliebigen Werte als automatisch unterstützt darstellen.

[Konkrete Befehle und Grenzen](viewer-runbook.md).
