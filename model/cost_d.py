"""Transparent planning scenarios, not quotations; see docs/beschaffung-d.md."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
rows=[]
for n in (1,5,10):
 # Purchased entire 1m solid bar, exact-count plate, ten screws; candidate 20mm pins.
 known=5.99*n+10.78+8.90+5.32+(.17*n if n<10 else 1.54)+5.90
 # Rohr 185mm blanks: 5 €/m plus 0.50 each; 3 euro handling conservatively per blank.
 tube= (5*.185+.5+3)*n
 scenarios=[]
 for tag,shipping,tools,finish,consum,setup,hours,rate in [('niedrig',6,25,15,5,1,.65,60),('mittel',10,50,30,10,1.5,1,85),('hoch',20,90,60,20,2.5,1.5,120)]:
  diy=known+tube+shipping+tools+finish+consum
  # Workshop surface allowance replaces DIY coating purchase; tooling covered by rate.
  surface=max(60,12*n) if tag=='niedrig' else max(100,20*n) if tag=='mittel' else max(180,35*n)
  work=known+tube+shipping+(setup+hours*n)*rate*1.19+surface+consum
  scenarios.append(dict(scenario=tag,unknown_shipping_allowance=shipping,tooling_purchase_allowance=tools,diy_surface_purchase_allowance=finish,consumables_allowance=consum,setup_hours=setup,machining_hours_each=hours,shop_hourly_rate_net=rate,shop_surface_allowance_gross=surface,diy_cash_gross=round(diy,2),diy_hours=round(2+1.5*n,1),workshop_total_gross=round(work,2),workshop_each_gross=round(work/n,2)))
 rows.append(dict(quantity=n,known_candidate_purchase_gross=round(known,2),tube_and_handling_provisional=round(tube,2),solid_bar_purchased_mm=1000,solid_bar_consumed_mm=55*n,solid_bar_remainder_mm=1000-55*n,screws_purchased=10,screws_remaining=10-n,scenarios=scenarios))
d={'date':'2026-09-28','status':'planning scenarios, not final D-V03 quotation','scope':'5 mm plate; 25mm steel stock machined to24; candidate28x1.5 tube and4x20 pin require new geometry validation','rows':rows}
(R/'web/assets/sockel-d/cost-scenarios.json').write_text(json.dumps(d,indent=2)+'\n')
for r in rows:print(r['quantity'],r['known_candidate_purchase_gross'],[(s['scenario'],s['diy_cash_gross'],s['workshop_total_gross']) for s in r['scenarios']])
