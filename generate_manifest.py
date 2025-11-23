import os, json

root = "notes"
manifest = {}

for category in os.listdir(root):
    cat_path = os.path.join(root, category)

    if os.path.isdir(cat_path):
        files = []

        for file in os.listdir(cat_path):
            if file.lower().endswith(".pdf"):
                size_mb = round(os.path.getsize(os.path.join(cat_path, file)) / (1024*1024), 2)
                files.append({
                    "name": file,
                    "file": f"{category}/{file}",
                    "size": f"{size_mb} MB"
                })

        manifest[category] = files

with open(os.path.join(root, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=4)

print(f"Generated notes/manifest.json successfully with {len(manifest)} category(ies).")
