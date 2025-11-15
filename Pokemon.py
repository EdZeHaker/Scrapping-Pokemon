#J'importe toutes les librairies nécessaires pour l'exercice:
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import os
import pandas as pd
from PIL import Image
import pillow_avif
import requests
import shutil

# Je récupère le code HTML de la page d'accueil, et la transforme en objet intelligible avec BeautifulSoup :
url_pokedex = "https://pokemondb.net/pokedex/national"
response = requests.get(url_pokedex, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "lxml")

# J'affiche le code HTML de manière élégante pour mieux comprendre le balisage :
print(soup.prettify())

#Je cherche le nom de tous les pokemon grâce a leurs balise et classe et les ajoutes à une liste name_list :
pokemon_names = soup.find_all('a', class_="ent-name")

name_list = []

for name in pokemon_names :
    name_list.append(name.text)

print(f"Le nombres de pokemons est : {len(name_list)}.")

#Je créé une fonction qui me permet de récupérer les codes HTML des pages de chaque Pokémon :
def get_name(name) :
    base_url = "https://pokemondb.net/pokedex/"
    pokemon_url = base_url + name.lower()
    response = requests.get(pokemon_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "lxml")
    return soup

#Je créé une fonction qui me permet de récupérer les 4 premières vital tables de chaque Pokémon et je les ajoutes dans un dictionnaire:
def get_tables(page) :
    dico_tables = {}
    pokemon_tables = page.find_all("table", class_="vitals-table")[:4]
    
    for table in pokemon_tables :
        rows = table.find_all("tr")
        for row in rows :
            label = row.find("th").text.strip()
            value = row.find("td").text.strip()
            dico_tables[label] = value

    return dico_tables

# Je créé une fonction pour afficher les 10 premiers Pokémon (avec leurs datas et noms) dans un DataFrame Pandas :
def get_pokemons_data (names, n =10) :

    data_list = []

    for name in names[:n] :
        page = get_name(name)
        data = get_tables(page)
        data["name"] = name
        data_list.append(data) 
    
    df = pd.DataFrame(data_list)
    return(df)

df = get_pokemons_data(name_list, 10)
print(df)

#Je créé une fonction pour récuperer les images (qui sont en AVIF et non JPG) et les ajoutent a un dossier appelé "images" :
def get_image(names, n=5) :
        
    if not os.path.exists("images"):
        os.makedirs("images")

    for name in names[:n] :

        pokemon_image_url = f"https://img.pokemondb.net/artwork/avif/{name.lower()}.avif"
        response = requests.get(pokemon_image_url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code == 200 :
            with open(f"images/{name}.avif", "wb") as f:
                f.write(response.content)
            print(f"Image telechargee : {name}")
        else :
            print("erreur")

get_image(name_list, 5)

#Je boucle sur la liste des noms de Pokémon jusqu'au Pokémon 5 pour les afficher avec MatPlotLib. Comme skimage.io.imread ne supporte pas AVIF, nous utilisons Pillow  :
for name in name_list[:5] :
    path = f"images/{name}.avif"
    image = Image.open(path)
    plt.figure()
    plt.imshow(image)
    plt.axis("off")
    plt.show()