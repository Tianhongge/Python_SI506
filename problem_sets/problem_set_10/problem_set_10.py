from operator import itemgetter
import swapi_entities as ent
def main():
    # Problem 1.0
    planet_data = ent.read_json('./swapi_planets.json')

    people = []
    for planet in planet_data:
        for resident in planet['residents']:
            item = ent.create_person(ent.convert_data(ent.get_resource(ent.CACHE_NAME, resident), planet_data))
            people.append(item)

    ent.write_json('full_residents.json', people)

if __name__ == '__main__':
    main()
