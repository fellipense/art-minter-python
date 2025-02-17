import random
import json

parts = []
types = []
used = []

# Loads the JSON file
with open('parts.json', 'r') as file:
    data = json.load(file)  # data is now a list of dictionaries

# Iterate through the list of objects
for obj in data:
    parts.append(obj)
    part_name = obj['part']
    if types.count(part_name) == 0:
        types.append(part_name)