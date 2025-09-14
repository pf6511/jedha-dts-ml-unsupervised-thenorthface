import json
import os

notebook_path = "TheNorthFace.ipynb"  # Path to your notebook

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Remove the widgets metadata entirely
if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print(f"Removed widgets metadata from {notebook_path}")