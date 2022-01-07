import pokebase

def question_2():
    SPECIES_QUERY = 'raichu'
    species_set = set()
    for egg_group in pokebase.pokemon_species(SPECIES_QUERY).egg_groups:
        for species in egg_group.pokemon_species:
            print(species.name)
            species_set.add(species.id)
    
    return len(species_set)

if __name__ == '__main__':
    print(question_2())