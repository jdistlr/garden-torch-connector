"""Markup regression checks; not a substitute for browser/rendering QA."""
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter

root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=[]; self.hrefs=[]; self.summaries=0; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='a' and 'href' in a:self.hrefs.append(a['href'])
        if tag=='summary':self.summaries+=1

names=['projekt','quellen','entscheidungen','variants','bauteile','mechanik','montage','beschaffung','kosten']
for name in names:
    text=(root/f'web/{name}.html').read_text(); page=Page(text)
    assert all(n==1 for n in Counter(page.ids).values()),(name,'duplicate id')
    assert 'main-content' in page.ids
    assert 'workbench.css?rev=1' in text
    assert 'class="desktop-nav"' in text
    for slug in names:assert f'{slug}.html' in page.hrefs,(name,slug)
    for href in page.hrefs:
        if href.startswith('#'):assert href[1:] in page.ids,(name,href)
model=Page((root/'web/variants.html').read_text())
for id in ['viewport','thickness','select-part','selected-part','montage-mode','timeline','play-montage','section','transparent','moving-cut','cut-position','snapshot','share-view','scene-style','scene-quality','parts','checks','sheet','step-d']:
    assert id in model.ids,id
assert model.summaries>=5
print('Workbench: nine pages, unique IDs, navigation, chapter anchors and model control IDs verified.')
