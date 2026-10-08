import json, glob, os
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
recipes = json.load(open(os.path.join(root, "data", "recipes.json")))
apps = []
for f in sorted(glob.glob(os.path.join(root, "data", "v*.json"))):
    d = json.load(open(f))
    if d["id"] in recipes["apps"]: apps.append({"id": d["id"], "app": d["app"]})
html = open(os.path.join(here, "template.html")).read()
html = html.replace("/*RECIPES*/{}", json.dumps(recipes, ensure_ascii=False)).replace("/*APPS*/[]", json.dumps(apps, ensure_ascii=False))
open(os.path.join(root, "index.html"), "w").write(html)
print("built", len(apps), "apps")
