import os, json

root = "notes"
manifest = {}

for category in os.listdir(root):
    category_path = os.path.join(root, category)
    if not os.path.isdir(category_path):
        continue

    manifest[category] = []

    for file in os.listdir(category_path):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(category_path, file)
            size_kb = round(os.path.getsize(full_path) / 1024)

            manifest[category].append({
                "name": file.replace(".pdf", ""),
                "file": f"{category}/{file}",
                "size": f"{size_kb} KB"
            })

with open(os.path.join(root, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=4)

print("Updated manifest.json successfully!")
