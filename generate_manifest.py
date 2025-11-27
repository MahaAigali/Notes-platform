# generate_manifest.py
import json
from pathlib import Path

NOTES_DIR = Path("notes")
OUT = NOTES_DIR / "manifest.json"

def human_readable(size):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024.0 or unit == 'TB':
            return f"{size:.2f} {unit}"
        size /= 1024.0

def main():
    if not NOTES_DIR.exists():
        print("notes/ folder not found. Create a folder named 'notes' and place PDFs inside.")
        return

    manifest = {}
    # check if notes/ has subfolders
    subdirs = [p for p in sorted(NOTES_DIR.iterdir()) if p.is_dir()]
    if subdirs:
        # treat each subfolder as a category
        for d in subdirs:
            cat = d.name
            manifest[cat] = []
            for f in sorted(d.iterdir()):
                if f.suffix.lower() == ".pdf":
                    size = f.stat().st_size
                    manifest[cat].append({
                        "name": f.name,
                        "file": f"{d.name}/{f.name}",
                        "size": human_readable(size)
                    })
    else:
        # no subfolders, use General category for PDFs in notes/
        manifest["General"] = []
        for f in sorted(NOTES_DIR.iterdir()):
            if f.suffix.lower() == ".pdf":
                size = f.stat().st_size
                manifest["General"].append({
                    "name": f.name,
                    "file": f.name,
                    "size": human_readable(size)
                })

    # ensure output folder exists (notes/)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(manifest, indent=2))
    print("Wrote", OUT)
    print("Categories:", ", ".join(manifest.keys()) if manifest else "None")

if __name__ == "__main__":
    main()
