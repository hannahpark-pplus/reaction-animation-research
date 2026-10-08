import json, glob, os
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
data = []
for f in sorted(glob.glob(os.path.join(root, "data", "v*.json"))):
    with open(f) as fh: data.append(json.load(fh))
html = open(os.path.join(here, "template.html")).read().replace("/*DATA*/[]", json.dumps(data, ensure_ascii=False))
open(os.path.join(root, "index.html"), "w").write(html)
print("built", len(data), "apps")
