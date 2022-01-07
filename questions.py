#import pokebase
import requests


def question_2():
    SPECIES_QUERY = 'raichu'
    species_set = set()
    for egg_group in pokebase.pokemon_species(SPECIES_QUERY).egg_groups:
        for species in egg_group.pokemon_species:
            print(species.name)
            species_set.add(species.id)
    
    return len(species_set)

def question_2_alt():
    SPECIES_QUERY = 'raichu'
    species_set = set()
    species_info = requests.get('https://pokeapi.co/api/v2/pokemon-species/{}'.format(SPECIES_QUERY)).json()
    for egg_group in species_info['egg_groups']:
        egg_group_info = requests.get(egg_group['url']).json()
        for egg_group_species in egg_group_info['pokemon_species']:
            species_set.add(egg_group_species['name'])
    
    return len(species_set)


if __name__ == '__main__':
    print(question_2_alt())