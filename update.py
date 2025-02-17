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
    if file_name.endswith(".png"):
        parts = file_name.split(";")
        
        part = parts[0]
        name = parts[1]
        weight = parts[2].replace(".png", "")
        weight = int(weight)
    
        weights[part] = weights.get(part, 0) + weight

        data.append({"part": part, "name": name, "weight": weight})

for part in data:
    temp = {}
    temp['part'] = part['part']
    temp['name'] = part['name']
    temp['chance'] = part['weight'] / weights[part['part']]
    partsFinal.append(temp)

print(partsFinal)

# Write data on parts.json
with open(parts_json, "w") as f:
    json.dump(partsFinal, f, indent=4)

# Log
print(f"File {parts_json} updated with success!")