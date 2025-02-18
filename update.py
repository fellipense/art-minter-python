import os
import json

parts_folder = "parts"
parts_json = "parts.json"
data = []
partsFinal = []
weights = {}

# Reset parts_json
with open(parts_json, "w") as f:
    json.dump([], f)

# Iterates for "parts" files (images)
for file_name in os.listdir(parts_folder):

    # Verify if it ends with ".png"
    if file_name.endswith(".png"): continue

    # Dismembering part properties
    parts = file_name.split(";")
    layer = int(parts[0])
    part = parts[1]
    name = parts[2]
    image = f"{parts_folder}/{file_name}"
    weight = parts[3].replace(".png", "")
    weight = int(weight)
    weights[part] = weights.get(part, 0) + weight

    # Save raw
    data.append({"part": part, "name": name, "image": image, "layer": layer, "weight": weight})

# Save with calculated chances
for part in data:
    temp = part
    temp['chance'] = part['weight'] / weights[part['part']]
    partsFinal.append(temp)

# Write all data on json file
with open(parts_json, "w") as f:
    json.dump(partsFinal, f, indent=4)
print(f"File {parts_json} updated with success!")