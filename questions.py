import requests


def question_1():
    all_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-species/?limit=2000').json() #all pokemon in one request
    return len([pokemon['name'] for pokemon in all_pokemon['results'] if ('at' in pokemon['name'] and pokemon['name'].count('a') == 2)])


def question_2():
    SPECIES_QUERY = 'raichu'
    species_set = set()
    species_info = requests.get('https://pokeapi.co/api/v2/pokemon-species/{}'.format(SPECIES_QUERY)).json()
    for egg_group in species_info['egg_groups']:
        egg_group_info = requests.get(egg_group['url']).json()
        for egg_group_species in egg_group_info['pokemon_species']:
            species_set.add(egg_group_species['name'])
    
    return len(species_set)


def question_3():
    pass



if __name__ == '__main__':
    print(question_1())