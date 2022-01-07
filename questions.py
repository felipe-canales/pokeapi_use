import requests


def question_1():
    """Indicates how many pokemons have 'at' and exactly two 'a's in their names.

    Returns:
        int: amount of pokemon satifying the condition
    """    
    all_pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-species/?limit=2000').json() #get all pokemon in one request
    return len([pokemon['name'] for pokemon in all_pokemon['results'] if ('at' in pokemon['name'] and pokemon['name'].count('a') == 2)])


def question_2(): 
    """Indicates how many pokemon can breed with Raichu.

    Returns:
        int: amount of pokemon satifying the condition
    """    
    SPECIES_QUERY = 'raichu'
    species_set = set()
    species_info = requests.get('https://pokeapi.co/api/v2/pokemon-species/{}'.format(SPECIES_QUERY)).json()
    for egg_group in species_info['egg_groups']:
        egg_group_info = requests.get(egg_group['url']).json()
        for egg_group_species in egg_group_info['pokemon_species']:
            species_set.add(egg_group_species['name'])
    
    return len(species_set)


def question_3():
    """Indicates the maximum and minimum weights for gen 1 pokemon.

    Returns:
        list(int): max and min values
    """    
    GEN = 1
    TYPE = 'fighting'
    # Candidate pokemons are filtered by generation.
    # Assumption: an extra request is less efficient than an 'in' operation
    gen_pkmns = requests.get('https://pokeapi.co/api/v2/generation/{}'.format(GEN)).json()['pokemon_species']
    type_pkmns = requests.get('https://pokeapi.co/api/v2/type/{}'.format(TYPE)).json()['pokemon']
    gen_pkmn_names = [pokemon['name'] for pokemon in gen_pkmns]
    max_weigth = -1
    min_weight = 999999
    for pokemon in type_pkmns:
        if pokemon['pokemon']['name'] not in gen_pkmn_names:
            continue
        pokemon_weight = requests.get(pokemon['pokemon']['url']).json()['weight']
        if pokemon_weight > max_weigth:
            max_weigth = pokemon_weight
        if pokemon_weight < min_weight:
            min_weight = pokemon_weight

    return [max_weigth, min_weight]


if __name__ == '__main__':
    print(question_1())
    print(question_2())
    print(question_3())