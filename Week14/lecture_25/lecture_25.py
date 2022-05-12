# SI 506 Lecture 25

import lecture_25_utils as utl


def create_film(data):
    """Returns a new film dictionary from the passed in < data >.

    Key order:
        url
        title
        director
        release_date
        opening_crawl

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    return {

    }


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible. Delegates to the function
    < create_film > the task of creating film dictionaries.

    Type conversions:
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> top_speed_mglt (str to int)
        crew -> crew_size (str to int)
        armament -> armament (str to list)

    Key order:
        url
        name
        model
        starship_class
        hyperdrive_rating
        top_speed_mglt
        crew_size
        armament
        film_credits

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    if data.get('films'):
        films = []
    else:
        films = None

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'model': data.get('model'),
        'starship_class': data.get('starship_class'),
        'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
        'top_speed_mglt': utl.convert_to_float(data.get('MGLT')),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'armament': utl.convert_to_list(data.get('armament'), ','),
        'film_credits': films
    }


def main():
    """Entry point for the script.

    Paramters:
        None

    Returns:
        None
    """

    # CHALLENGES 01-06

    swapi_starships = utl.read_json('./episode_iv_starships.json') # TODO Call function
    wookiee_starships = utl.read_csv_to_dicts('./wookieepedia_starships.csv') # TODO Call function

    # WARN: Run first then comment out
    # starships = [create_starship(starship) for starship in swapi_starships] # TODO Create new list
    starships = []
    for swapi_starship in swapi_starships:
        for wookiee_starship in wookiee_starships:
            if swapi_starship['model'].lower() == wookiee_starship['model'].lower():
                swapi_starship.update(wookiee_starship)
                break
        starships.append(create_starship(swapi_starship))

    # Write to file
    utl.write_json('stu-starships.json', starships)
    utl.write_json('stu-cache.json', utl.cache)


if __name__ == '__main__':
    main()
