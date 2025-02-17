import os
import json

parts_folder = "parts"
parts_json = "parts.json"
data = []

# Reset parts_json
with open(parts_json, "w") as f:
    json.dump([], f)

# Iterates for "parts" files (images)
for file_name in os.listdir(parts_folder):

    # Verify if it ends with ".png"
    if file_name.endswith(".png"):
        parts = file_name.split("-")
        
        part = parts[0]
        name = "-".join(parts[1:-1])
        chance = parts[-1].replace(".png", "")
        chance = float(chance[0] + '.' + chance[1:] if len(chance) > 1 else chance)
        
        data.append({"part": part, "name": name, "chance": chance})

# Write data on parts.json
with open(parts_json, "w") as f:
    json.dump(data, f, indent=4)

# Log
print(f"File {parts_json} updated with success!")