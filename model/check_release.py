"""Bind reviewed files to a release snapshot; not a mechanical certification.
Run --write only after reviewing changes and re-running affected checks.
"""
from pathlib import Path
import hashlib,json,sys,re,subprocess
R=Path(__file__).resolve().parents[1]
M=R/'web/assets/sockel-d/release-manifest.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
paths=[]
for folder in ['parameters','model','docs']:
 paths.extend(p for p in (R/folder).glob('*') if p.is_file() and p.suffix in ['.json','.py','.mjs','.cjs','.md','.txt'])
paths.extend(p for p in (R/'web').glob('*') if p.is_file() and p.suffix in ['.html','.js','.css'])
paths.extend(p for p in (R/'web/assets/sockel-d').glob('*') if p.is_file() and p!=M)
paths.extend(R/p for p in ['README.md','AGENTS.md','package.json','package-lock.json'])
files={str(p.relative_to(R)):sha(p) for p in sorted(paths)}
for t in [5,8,9]:
 d=json.loads((R/f'web/assets/sockel-d/model-{t}.json').read_text())
 assert d['revision']=='D-V03'
 assert sorted(p['id'] for p in d['parts'])==['adapter','pin','plate','screw','tube']
# Markdown and published document pages must be in sync.
before={p:p.read_bytes() for p in (R/'web').glob('*.html')}
subprocess.run(['node','model/render_docs.cjs'],cwd=R,check=True)
assert all(p.read_bytes()==b for p,b in before.items()),'Generated documents stale; render and review before release'
# Local file references in current pages must resolve. Ignore remote URLs and fragment-only links.
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k not in ['href','src'] or not v:continue
   u=urlsplit(v)
   if u.scheme or u.netloc or not u.path:continue
   target=(self.page.parent/unquote(u.path)).resolve()
   assert target.exists(),f'{self.page}: missing {v}'
for name in ['variants','entscheidungen','mechanik','montage','beschaffung','kosten']:
 p=R/f'web/{name}.html';parser=Links();parser.page=p;parser.feed(p.read_text())
if '--write' in sys.argv:
 M.write_text(json.dumps({'revision':'D-V03','status':'concept; no manufacturing or operational release','scope':'File identity snapshot. Existing mechanical reports retain their own scope; hashes do not certify new checks.','files_sha256':files},indent=2)+'\n')
else:
 assert json.loads(M.read_text())['files_sha256']==files,'Release files changed; review changes and refresh manifest'
print(f'Release: {len(files)} files, 3 model identities, generated pages and local links verified.')
