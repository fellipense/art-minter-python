import random
import json

part_types = []

# Loads the JSON file
with open('parts.json', 'r') as file:
    data = json.load(file)  # data is now a list of dictionaries

# Iterate through the list of objects
for obj in data:
    if obj['part'] not in part_types:
        part_types.append(obj['part'])

def draw():
    for t in part_types:

        temp_items = []

        for d in data:
            if d['part'] == t:
                temp_items.append(d)

        temp_items.sort(key=lambda item: item['chance'])

        dice = random.uniform(0, 1)

        for item in temp_items:
            if dice <= item['chance']: return item