from PIL import Image
import random
import json
import os

part_types = []
amount = 3
output_dir = "mints"

# Loads the JSON file
with open('parts.json', 'r') as file:
    data = json.load(file)  # data is now a list of dictionaries

# Iterate through the list of objects
for obj in data:
    if obj['part'] not in part_types:
        part_types.append(obj['part'])

def draw(_type):

    temp_items = []

    for d in data:
        if d['part'] == _type:
            temp_items.append(d)

    temp_items.sort(key=lambda item: item['chance'])

    dice = random.uniform(0, 1)

    for item in temp_items:
        if dice <= item['chance']: return item
        else: dice -= item['chance']

# Verifica se o diretório existe, se não, cria
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(0, amount):

    mint = []

    for _type in part_types:
        mint.append(draw(_type))


    # IA generated:

    # Abre todas as imagens e armazena em uma lista
    mint.sort(key=lambda item: item['layer'])
    imagens = [Image.open(item['image']).convert("RGBA") for item in mint]

    # Encontra a altura máxima e a largura máxima entre todas as imagens
    max_altura = max(img.height for img in imagens)
    max_largura = max(img.width for img in imagens)

    # Cria uma imagem vazia (fundo transparente) com as dimensões máximas
    imagem_final = Image.new("RGBA", (max_largura, max_altura), (0, 0, 0, 0))

    # Cola cada imagem na frente da imagem vazia
    for img in imagens:
        imagem_final.paste(img, (0, 0), img)  # O terceiro argumento (img) é a máscara de transparência

    def generate_name(base_nome, extensao):
        contador = 1
        nome_arquivo = f"{base_nome}{extensao}"
        
        # Verifica se o arquivo já existe
        while os.path.exists(os.path.join(output_dir, nome_arquivo)):
            nome_arquivo = f"{base_nome}-{contador}{extensao}"
            contador += 1
        
        return nome_arquivo

    # Gera um nome único para o arquivo de saída
    nome_arquivo_saida = os.path.join(output_dir, generate_name("mint", ".png"))

    # Salva a imagem final com o nome único
    imagem_final.save(nome_arquivo_saida, "PNG")


    print(f"Imagem salva como: {nome_arquivo_saida}")