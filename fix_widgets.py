import json

notebook_path = "TheNorthFace.ipynb"  # Path to your notebook

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Add empty 'state' key if missing
if "widgets" in nb.get("metadata", {}):
    if "state" not in nb["metadata"]["widgets"]:
        nb["metadata"]["widgets"]["state"] = {}

# Save the notebook back
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print(f"Fixed widgets metadata in {notebook_path}")