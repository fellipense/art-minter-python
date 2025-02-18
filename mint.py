from PIL import Image
import random
import json
import os

part_types = []
parts_json = "parts.json"
amount = 10
output_dir = "mints"

# Collects all data from json file
with open(parts_json, 'r') as file:
    data = json.load(file)  # data is now a list of dictionaries

# Maps all the existing mintable parts
for obj in data:
    if obj['part'] not in part_types:
        part_types.append(obj['part'])

# Draw a part for the mint
def draw(_type):

    # Store all parts of this type (ex: store all hats or shoes)
    temp_items = [d for d in data if d['part'] == _type]

    # Most rares are tested first
    temp_items.sort(key=lambda item: item['chance'])

    # "fire a gun"
    shoot = random.uniform(0, 1)

    # See what the shoot hit 
    for item in temp_items:
        if shoot <= item['chance']: return item
        else: shoot -= item['chance']

# Create the dir it doesn't exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create the amount of mints informed in 'amount'
for i in range(0, amount):

    # Minting
    mint = [draw(_type) for _type in part_types]

    # Generating the png art:

    # Sorting by z-layer
    mint.sort(key=lambda item: item['layer'])
    images = [Image.open(item['image']).convert("RGBA") for item in mint]

    # Output image will have the largest dimensions between all parts images
    max_height = max(img.height for img in images)
    max_width = max(img.width for img in images)
    final_image = Image.new("RGBA", (max_width, max_height), (0, 0, 0, 0))

    # Stack images one after the other
    for img in images:
        final_image.paste(img, (0, 0), img)

    # Generates a unique name for the file based on other existing files
    def generate_name(base_name, extension):
        counter = 1
        file_name = f"{base_name}{extension}"
        
        while os.path.exists(os.path.join(output_dir, file_name)):
            file_name = f"{base_name}-{counter}{extension}"
            counter += 1
        
        return file_name

    output_file_name = os.path.join(output_dir, generate_name("mint", ".png"))

    # Saves the final image generated
    final_image.save(output_file_name, "PNG")
    print(f"Image saved as: {output_file_name}")