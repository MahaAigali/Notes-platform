@echo off
python generate_manifest.py
git add .
git commit -m "Auto-update notes"
git pull --rebase
git push
pause
