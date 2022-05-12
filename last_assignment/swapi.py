from socket import NI_NAMEREQD
import sw_utils as utl


def assign_crew_members(starship, crew_positions, personnel):
    """Maps crew members by position to the passed in < starship > 'crew_members'
    key. Both the < crew_positions > and < personnel > lists should contain the same number
    of elements. The individual < crew_positions > and < personnel > elements are then paired
    by index position and stored in a dictionary structured as follows:

    {< crew_position[0] >: < personnel[0] >, < crew_position[1] >: < personnel[1] >, ...}

    The crew members dictionary is mapped (i.e., assigned) to the passed in
    starship's 'crew_members' key and the crewed starship is returned to the caller.

    WARN: The number of crew members that can be assigned to the passed in < starship > is
    limited by the starship's "crew_size" value. No additional crew members are permitted
    to be assigned to the < starship >.

    WARN: A single line dictionary comprehension that assigns a new dictionary to the passed in
    < starship >'s "crew_members" key must be written in order to earn full credit. Utilize the
    parameter names in the dictionary comprehension (DO NOT assign the passed in dictionary
    and lists to local variables and then reference them in the comprehension).

        Parameters:
            starship (dict): Representation of a starship
            crew_positions (list): crew positions (e.g., 'pilot', 'copilot', etc.)
            personnel (list): persons to be assigned to the crew positions

        Returns:
            dict: starship with assigned crew members
    """

    starship['crew_members'] = {crew_positions[i]: personnel[i] for i in range(starship['crew_size'])}

    return starship


def board_passengers(starship, passengers):
    """Assigns < passengers > to the passed in < starship > but limits boarding to less than
    or equal to the starship's "max_passengers" value. The passengers list (in whole or in part)
    is then mapped (i.e., assigned) to the passed in starship's 'passengers_on_board' key. After
    boarding the passengers the starship is returned to the caller.

    WARN: The number of passengers permitted to board a starship is limited by the starship's
    "max_passengers" value. If the number of passengers attempting to board exceeds the starship's
    "max_passengers" value only the first n passengers (where `n` = "max_passengers") are
    permitted to board the vessel.

        Parameters:
            starship (dict): Representation of a starship
            passengers (list): passengers to transport aboard starship

        Returns:
            dict: starship with assigned passengers
    """

    n = int(starship['max_passengers'])
    if len(passengers) > n:
        starship['passengers_on_board'] = passengers[0:n]
    else:
        starship['passengers_on_board'] = passengers

    return starship


def calculate_articles_mean_word_count(articles):
    """Calculates the mean (e.g., average) word count of the passed in list of < articles >.
    Excludes from the calculation any article with a word count of zero (0). Word counts
    are summed and then divided by the number of non-zero word count articles. The resulting mean
    value is rounded to the second (2nd) decimal place and returned to the caller.

    WARN: Add a local variable to hold a count of the number of articles with a word count of
    zero (0). Then subtract the zero word count from the total number of passed in articles in
    order to ensure that the divisor reflects the actual number of articles upon which to
    compute the mean.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        float: mean word count rounded to the second (2nd) decimal place
    """

    zero_count = 0
    word_count = 0
    for article in articles:
        if article['word_count'] == 0:
            zero_count += 1
        else:
            word_count = word_count + article['word_count']
    mean_word_count = round(word_count / (len(articles) - zero_count), 2)

    return mean_word_count


def convert_episode_values(episodes):
    """Converts select string values to either int, float, list, or None in the passed in list of
    nested dictionaries. The function delegates to the < utl.convert_to_* > functions the task of
    converting the specified strings to either int, float, or list (or None if utl.convert_to_none
    is eventually called).

    Conversions:
        str to int: 'series_season_num', 'series_episode_num', 'season_episode_num'
        str to float: 'episode_prod_code', 'episode_us_viewers_mm'
        str to list: 'episode_writers'

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: nested episode dictionaries containing mutated key-value pairs
    """

    for episode in episodes:
        for key, val in episode.items():
            if key in ('series_season_num', 'series_episode_num', 'season_episode_num'):
                episode[key] = utl.convert_to_int(val)
            elif key in ('episode_prod_code', 'episode_us_viewers_mm'):
                episode[key] = utl.convert_to_float(val)
            elif key == 'episode_writers':
                episode[key] = utl.convert_to_list(val, ', ')
    return episodes


def count_episodes_by_director(episodes):
    """Constructs and returns a dictionary of key-value pairs that associate each director with a
    count of the episodes that they directed. The director's name comprises the key and the
    associated value a count of the number of episodes they directed. Duplicate keys are NOT
    permitted.

    Format:
        {
            < director_name_01 >: < episode_count >,
            < director_name_02 >: < episode_count >,
            ...
        }

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        dict: a dictionary that store counts of the number of episodes directed
              by each director
    """

    director_dict = {}
    for episode in episodes:
        if episode['episode_director'] not in director_dict.keys():
            director_dict[episode['episode_director']] = 1
        else:
            director_dict[episode['episode_director']] += 1

    return director_dict


def create_droid(data):
    """Returns a new dictionary representation of a droid from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        equipment -> equipment (str to list)

    Key order:
        url
        name
        model
        manufacturer
        create_year
        height_cm
        mass_kg
        equipment
        instructions

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    for val in data.values():
        val = utl.convert_to_none(val)

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'model': data.get('model'),
        'manufacturer': data.get('manufacturer'),
        'create_year': data.get('create_year'),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
        'equipment': utl.convert_to_list(data.get('equipment'), '|'),
        'instructions': data.get('instructions')
    }


def create_person(data, planets=None):
    """Returns a new dictionary representation of a person from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Both the person's "homeworld" and "species" values are used to retrieve SWAPI dictionary
    representations of the planet and specie values. Retrieving the SWAPI homeworld and
    species data is delegated to the function < utl.get_resource >.

    If an optional Wookieepedia-sourced < planets > list is provided, the task of retrieving
    the appropriate nested dictionary (filters on the passed in homeworld planet
    name) is delegated to the function < get_wookieepedia_data >.

    Before the homeworld and species data is mapped (e.g. assigned) to the person's "homeworld"
    and "species" keys, the functions < create_planet > and < create_species > are called
    in order to provide new dictionary representations of the person's homeworld and species.

    Type conversions:
        height -> height_cm (str to float)
        mass -> mass_kg (str to float)
        homeworld -> homeworld (str to dict)
        species -> species (str to dict)

    Key order:
        url
        name
        birth_year
        height_cm
        mass_kg
        homeworld
        species
        force_sensitive

    Parameters:
        data (dict): source data
        planets (list): optional supplemental planetary data

    Returns:
        dict: new dictionary
    """

    for val in data.values():
        val = utl.convert_to_none(val)
    person_dict = {
        'url': data.get('url'),
        'name': data.get('name'),
        'birth_year': data.get('birth_year'),
        'height_cm': utl.convert_to_float(data.get('height')),
        'mass_kg': utl.convert_to_float(data.get('mass')),
    }
    homeworld_dict = utl.get_resource(utl.SWAPI_PLANETS, {'search': data.get('homeworld')})['results'][0]
    species_dict = create_species(utl.get_resource(utl.SWAPI_SPECIES, {'search': data.get('species')})['results'][0])
    if planets:
        planets_update = get_wookieepedia_data(planets, data['homeworld'])
        homeworld_dict.update(planets_update)
        person_dict['homeworld'] = create_planet(homeworld_dict)
    else:
        person_dict['homeworld'] = homeworld_dict
    person_dict['species'] = species_dict
    person_dict['force_sensitive'] = data.get('force_sensitive')

    return person_dict


def create_planet(data):
    """Returns a new dictionary representation of a planet from the passed in < data >,
    converting string values to the appropriate type whenever possible.

    Type conversions:
        suns -> suns (str->int)
        moon -> moons (str->int)
        orbital_period -> orbital_period_days (str to float)
        diameter -> diameter_km (str to int)
        gravity -> gravity_std (str to float)
        climate -> climate (str to list)
        terrain -> terrain (str to list)
        population -> population (str->int)

    Key order:
        url
        name
        region
        sector
        suns
        moons
        orbital_period_days
        diameter_km
        gravity_std
        climate
        terrain
        population

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    for val in data.values():
        val = utl.convert_to_none(val)

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'region': utl.convert_to_none(data.get('region')),
        'sector': utl.convert_to_none(data.get('sector')),
        'suns': utl.convert_to_int(data.get('suns')),
        'moons': utl.convert_to_int(data.get('moons')),
        'orbital_period_days': utl.convert_to_float(data.get('orbital_period')),
        'diameter_km': utl.convert_to_int(data.get('diameter')),
        'gravity_std': utl.convert_gravity_value(data.get('gravity')),
        'climate': utl.convert_to_list(data.get('climate'), ', '),
        'terrain': utl.convert_to_list(data.get('terrain'), ', '),
        'population': utl.convert_to_int(data.get('population'))
    }


def create_species(data):
    """Returns a new dictionary representation of a species from the passed in
    < data >, converting string values to the appropriate type whenever possible.

    Type conversions:
        average_lifespan -> average_lifespan (str to int)
        average_height -> average_height_cm (str to float)

    Key order:
        url
        name
        classification
        designation
        average_lifespan
        average_height_cm
        language

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    for val in data.values():
        val = utl.convert_to_none(val)

    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'classification': data.get('classification'),
        'designation': data.get('designation'),
        'average_lifespan': utl.convert_to_int(data.get('average_lifespan')),
        'average_height_cm': utl.convert_to_float(data.get('average_height')),
        'language': data.get('language')
    }


def create_starship(data):
    """Returns a new starship dictionary from the passed in < data >, converting string
    values to the appropriate type whenever possible.

    Assigning crews and passengers consitute separate
    operations.

    Type conversions:
        length -> length_m (str to float)
        max_atmosphering_speed -> max_atmosphering_speed (str to int)
        hyperdrive_rating -> hyperdrive_rating (str to float)
        MGLT -> MGLT (str to int)
        crew -> crew_size (str to int)
        passengers -> max_passengers (str to int)
        armament -> armament (str to list)
        cargo_capacity -> cargo_capacity_kg (str to int)

    Key order:
        url
        name
        model
        starship_class
        manufacturer
        length_m
        max_atmosphering_speed
        hyperdrive_rating
        top_speed_mglt
        armament
        crew_size
        crew_members
        max_passengers
        passengers_on_board
        cargo_capacity_kg
        consumables

    Parameters:
        data (dict): source data

    Returns:
        dict: new dictionary
    """

    for val in data.values():
        val = utl.convert_to_none(val)
    return {
        'url': data.get('url'),
        'name': data.get('name'),
        'model': data.get('model'),
        'starship_class': data.get('starship_class'),
        'manufacturer': data.get('manufacturer'),
        'length_m': utl.convert_to_float(data.get('length')),
        'max_atmosphering_speed': utl.convert_to_int(data.get('max_atmosphering_speed')),
        'hyperdrive_rating': utl.convert_to_float(data.get('hyperdrive_rating')),
        'top_speed_mglt': utl.convert_to_int(data.get('MGLT')),
        'armament': utl.convert_to_list(data.get('armament'), ','),
        'crew_size': utl.convert_to_int(data.get('crew')),
        'crew_members': data.get('crew_members'),
        'max_passengers': utl.convert_to_int(data.get('passengers')),
        'passengers_on_board': data.get('passengers_on_board'),
        'cargo_capacity_kg': utl.convert_to_int(data.get('cargo_capacity')),
        'consumables': data.get('consumables')
    }


def get_wookieepedia_data(wookiee_data, filter):
    """Attempts to retrieve a Wookieepedia sourced dictionary representation of a
    Star Wars entity (e.g., droid, person, planet, species, starship, or vehicle)
    from the < wookiee_data > list using the passed in filter value. The function performs
    a case-insensitive comparison of each nested dictionary's "name" value against the
    passed in < filter > value. If a match is obtained the dictionary is returned to the
    caller; otherwise None is returned.

    Parameters:
        wookiee_data (list): Wookieepedia-sourced data stored in a list of nested dictionaries
        filter (str): name value used to match on a dictionary's "name" value

    Returns
        dict|None: Wookieepedia-sourced data dictionary if match on the filter is obtained;
                   otherwise returns None
    """

    for data in wookiee_data:
        if filter.lower() == data['name'].lower():
            return data
    else:
        return None


def get_most_viewed_episode(episodes):
    """Identifies and returns a list of one or more episodes with the highest recorded
    viewership. Ignores episodes with no viewship value. Includes in the list only those
    episodes that tie for the highest recorded viewership. If no ties exist only one
    episode will be returned in the list. Delegates to the function < has_viewer_data >
    the task of determining if the episode includes viewership "episode_us_viewers_mm"
    numeric data.

    Parameters:
        episodes (list): nested episode dictionaries

    Returns:
        list: episode(s) with the highest recorded viewership.
    """

    viewer_count = 0
    top_episode = 0
    for i in range(len(episodes)):
        if has_viewer_data(episodes[i]):
            if episodes[i]['episode_us_viewers_mm'] > top_episode:
                viewer_count = viewer_count + episodes[i]['episode_us_viewers_mm']
                top_episode = episodes[i]['episode_us_viewers_mm']
                i += 1
        else:
            i += 1

    highest_recorded_viewership = []
    for episode in episodes:
        if episode['episode_us_viewers_mm'] == top_episode:
            highest_recorded_viewership.append(episode)

    return highest_recorded_viewership


def get_nyt_news_desks(articles):
    """Returns a list of New York Times news desks sourced from the passed in < articles >
    list. Accesses the news desk name from each article's "news_desk" key-value pair. Filters
    out duplicates in order to guarantee uniqueness.

    Delegates to the function < utl.convert_to_none > the task of converting "news_desk"
    values that equal "None" (a string) to None. Only news_desk values that are "truthy"
    (i.e., not None) are returned in the list.

    Parameters:
        articles (list): nested dictionary representations of New York Times articles

    Returns:
        list: news desk strings (no duplicates)
    """

    news_desks = []
    for article in articles:
        news_desk = utl.convert_to_none(article['news_desk'])
        if news_desk not in news_desks and news_desk != None:
            news_desks.append(news_desk)
    return news_desks


def group_nyt_articles_by_news_desk(news_desks, articles):
    """Returns a dictionary of "news desk" key-value pairs that group the passed in
    < articles > by their parent news desk. The passed in < news_desks > list provides
    the keys while each news desk's < articles > are stored in a list and assigned to
    the appropriate "news desk" key. Each key-value pair is structured as follows:

    {
        < news_desk_name_01 >: [{< article_01 >}, {< article_05 >}, ...],
        < news_desk_name_02 >: [{< article_20 >}, {< article_31 >}, ...],
        ...
    }

    Each dictionary that represents an article is a "thinned" version of the New York Times
    original and consists of the following key-value pairs ordered as follows:

    Key order:
        web_url
        headline_main (new name)
        news_desk
        byline_original (new name)
        document_type
        material_type (new name)
        abstract
        word_count
        pub_date

    Parameters:
        news_desks (list): list of news_desk names
        articles (list): nested dictionary representations of New York Times articles

    Returns
        dict: key-value pairs that group articles by their parent news desk
    """

    group_dict = {}
    for news_desk in news_desks:
        group = []
        for article in articles:
            if article['news_desk'] == news_desk:
                group.append(
                    {
                    'web_url': article['web_url'],
                    'headline_main': article['headline']['main'],
                    'news_desk': article['news_desk'],
                    'byline_original': article['byline']['original'],
                    'document_type': article['document_type'],
                    'material_type': article['type_of_material'],
                    'abstract': article['abstract'],
                    'word_count': article['word_count'],
                    'pub_date': article['pub_date']
                    }
                )
        group_dict[news_desk] = group
    return group_dict


def has_viewer_data(episode):
    """Checks the truth value of an episode's "episode_us_viewers_mm" key-value pair. Returns
    True if the truth value is "truthy" (e.g., numeric values that are not 0, non-empty sequences
    or dictionaries, boolean True); otherwise returns False if a "falsy" value is detected (e.g.,
    empty sequences (including empty or blank strings), 0, 0.0, None, boolean False)).

    Parameters:
        episode (dict): represents an episode

    Returns:
        bool: True if "episode_us_viewers_mm" value is truthy; otherwise False
    """

    if bool(episode.get('episode_us_viewers_mm')):
        return True
    else:
        return False

def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    # 9.1 CHALLENGE 01

    # TODO Refactor utl.read_csv()

    clone_wars = utl.read_csv('./clone_wars.csv')
    # print(f"9.1.2\nclone_wars = {clone_wars}")
    clone_wars_22 = clone_wars[1:5]
    # print(f"9.1.3\nclone_wars_22 = {clone_wars_22}")
    clone_wars_2012 = clone_wars[4:6]
    # print(f"9.1.3\nclone_wars_2012 = {clone_wars_2012}")
    clone_wars_url = clone_wars[-2][-1]
    # print(f"9.1.3\nclone_wars_url = {clone_wars_url}")
    clone_wars_even_num_seasons = clone_wars[2::2]
    # print(f"9.1.3\nclone_wars_seasons = {clone_wars_even_num_seasons}")


    # 9.2 Challenge 02

    # TODO Implement convert_to_none(), convert_to_int(), convert_to_float(), convert_to_list()

    # print(f"\nconvert_to_none -> None = {utl.convert_to_none(' N/A ')}")
    # print(f"\nconvert_to_none -> None = {utl.convert_to_none('')}")
    # print(f"\nconvert_to_none -> no change = {utl.convert_to_none('Yoda ')}")
    # print(f"\nconvert_to_none -> no change = {utl.convert_to_none(5.5)}")
    # print(f"\nconvert_to_none -> no change = {utl.convert_to_none((1, 2, 3))}")

    # print(f"\nconvert_to_int -> int = {utl.convert_to_int('506 ')}")
    # print(f"\nconvert_to_int -> None = {utl.convert_to_int(' unknown')}")
    # print(f"\nconvert_to_int -> no change = {utl.convert_to_int([506, 507])}")

    # print(f"\nconvert_to_float -> float = {utl.convert_to_float('5.5')}")
    # print(f"\nconvert_to_float -> float = {utl.convert_to_float(5)}")
    # print(f"\nconvert_to_float -> None = {utl.convert_to_float(' None')}")
    # print(f"\nconvert_to_float -> no change = {utl.convert_to_float((1, 2, 3))}")
    # print(f"\nconvert_to_float -> no change = {utl.convert_to_float(' Yoda')}")

    # print(f"\nconvert_to_list -> None = {utl.convert_to_list(' N/A')}")
    # print(f"\nconvert_to_list -> list = {utl.convert_to_list('a, b, c, d', ', ')}")
    # print(f"\nconvert_to_list -> list = {utl.convert_to_list('a b c d')}")
    # print(f"\nconvert_to_list -> no change = {utl.convert_to_list((1, 2, 3,))}")


    # 9.3 CHALLENGE 03

    # TODO Refactor utl.read_csv_to_dicts()

    clone_wars_episodes = utl.read_csv_to_dicts('./clone_wars_episodes.csv')
    # print(f"9.3.2\nclone_wars_episodes = {clone_wars_episodes}")

    # TODO Implement has_viewer_data()

    # TODO Implement loop

    episode_count = 0
    for i in range(len(clone_wars_episodes)):
        if has_viewer_data(clone_wars_episodes[i]):
            episode_count += 1
            i += 1
        else:
            episode_count += 0
            i += 1
    # print(f"9.3.4\nepisode_count = {episode_count}")


    # 9.4 Challenge 04

    # TODO Implement convert_episode_values()

    clone_wars_episodes = convert_episode_values(clone_wars_episodes)
    utl.write_json('stu-clone_wars-episodes_converted.json', clone_wars_episodes)


    # 9.5 Challenge 05

    # TODO Implemennt get_most_viewed_episode()

    most_viewed_episode = get_most_viewed_episode(clone_wars_episodes)
    # print(f"9.5.2\nmost_viewed_episode = {most_viewed_episode}")


    # 9.6 Challenge 06

    # TODO Implement count_episodes_by_director()
    director_episode_counts = count_episodes_by_director(clone_wars_episodes)
    # print(f"9.6.2\ndirector_episode_counts = {director_episode_counts}")
    utl.write_json('stu-clone_wars-director_episode_counts.json', director_episode_counts)

    # 9.7 CHALLENGE 07

    articles = utl.read_json('./nyt_star_wars_articles.json')

    # TODO Implement get_nyt_news_desks()

    news_desks = get_nyt_news_desks(articles)
    # print(f"9.7.2\nnews_desks = {news_desks}")

    utl.write_json('stu-nyt_news_desks.json', news_desks)


    # 9.8 CHALLENGE 08

    # TODO Implement group_nyt_articles_by_news_desk()

    news_desk_articles = group_nyt_articles_by_news_desk(news_desks, articles)
    utl.write_json('stu-nyt_news_desk_articles.json', news_desk_articles)


    # 9.9 CHALLENGE 09

    # TODO Implement calculate_articles_mean_word_count()

    ignore = ('Business Day', 'Movies')

    # TODO Implement loop

    mean_word_counts = {}
    for key, val in news_desk_articles.items():
        if key not in ignore:
            mean_word_counts[key] = calculate_articles_mean_word_count(val)

    # print(f"9.9.2\nmean_word_counts = {mean_word_counts}")
    utl.write_json('stu-nyt_news_desk_mean_word_counts.json', mean_word_counts)

    # 9.10 CHALLENGE 10

    # TODO Implement convert_gravity_value()

    # print(f"\nconvert_gravity_value -> float = {utl.convert_gravity_value('1 standard')}")
    # print(f"\nconvert_gravity_value -> None = {utl.convert_gravity_value('N/A')}")
    # print(f"\nconvert_gravity_value -> float = {utl.convert_gravity_value('0.98')}")

    # 9.11 CHALLENGE 11

    # TODO Implement get_wookieepedia_data()

    wookiee_planets = utl.read_csv_to_dicts('./wookieepedia_planets.csv')

    wookiee_dagobah = get_wookieepedia_data(wookiee_planets, 'dagobah')
    wookiee_haruun_kal = get_wookieepedia_data(wookiee_planets, 'HARUUN KAL')

    # print(f"9.11.2\nwookiee_dagobah = {wookiee_dagobah}")
    # print(f"9.11.2\nwookiee_haruun_kal = {wookiee_haruun_kal}")

    utl.write_json('stu-wookiee_dagobah.json', wookiee_dagobah)
    utl.write_json('stu-wookiee_haruun_kal.json', wookiee_haruun_kal)


    # 9.12 CHALLENGE 12

    # TODO Implement create_planet()

    swapi_tatooine = utl.get_resource(utl.SWAPI_PLANETS, {'search': 'Tatooine'})['results'][0]
    wookiee_tatooine = get_wookieepedia_data(wookiee_planets, 'Tatooine')
    for key, val in wookiee_tatooine.items():
        if val:
            swapi_tatooine.update(wookiee_tatooine)
    tatooine = create_planet(swapi_tatooine)

    utl.write_json('stu-tatooine.json', tatooine)


    # 9.13 CHALLENGE 13

    # TODO Implement create_droid()

    wookiee_droids = utl.read_json('./wookieepedia_droids.json')

    swapi_r2_d2 = utl.get_resource(utl.SWAPI_PEOPLE, {'search': 'R2-D2'})['results'][0]
    wookiee_r2_d2 = get_wookieepedia_data(wookiee_droids, 'R2-D2')
    for key, val in wookiee_r2_d2.items():
        if val:
            swapi_r2_d2.update(wookiee_r2_d2)

    r2_d2 = create_droid(swapi_r2_d2)

    utl.write_json('stu-r2_d2.json', r2_d2)


    # 9.14 Challenge 14

    # TODO Implement create_species()

    swapi_human_species = utl.get_resource(utl.SWAPI_SPECIES, {'search': 'Human'})['results'][0]

    human_species = create_species(swapi_human_species)

    utl.write_json('stu-human_species.json', human_species)

    # 9.15 Challenge 15

    # TODO Implement create_person()

    # 9.15.2
    wookiee_people = utl.read_json('./wookieepedia_people.json')

    swapi_anakin = utl.get_resource(utl.SWAPI_PEOPLE, {'search': 'Anakin'})['results'][0]
    wookiee_anakin = get_wookieepedia_data(wookiee_people, 'Anakin Skywalker')
    for key, val in wookiee_anakin.items():
        if val:
            swapi_anakin.update(wookiee_anakin)

    anakin = create_person(swapi_anakin, wookiee_planets)

    utl.write_json('stu-anakin_skywalker.json', anakin)


    # 9.16 CHALLENGE 16

    # TODO Implement create_starship()

    wookiee_starships = utl.read_csv_to_dicts('./wookieepedia_starships.csv')

    wookiee_twilight = get_wookieepedia_data(wookiee_starships, 'Twilight')

    twilight = create_starship(wookiee_twilight)

    utl.write_json('stu-twilight.json', twilight)


    # 9.17 CHALLENGE 17

    # TODO Implement board_passengers()

    swapi_padme = utl.get_resource(utl.SWAPI_PEOPLE, {'search': 'Padmé Amidala'})['results'][0]
    # print(swapi_padme)
    wookiee_padme = get_wookieepedia_data(wookiee_people, 'Padmé Amidala')
    # print(wookiee_padme)
    for key, val in wookiee_padme.items():
        if val:
            swapi_padme.update(wookiee_padme)
    # print(swapi_padme)

    padme = create_person(swapi_padme, wookiee_planets)

    swapi_c_3po = utl.get_resource(utl.SWAPI_PEOPLE, {'search': 'C-3PO'})['results'][0]
    wookiee_c_3po = get_wookieepedia_data(wookiee_droids, 'C-3PO')
    for key, val in wookiee_c_3po.items():
        if val:
            swapi_c_3po.update(wookiee_c_3po)

    c_3po = create_droid(swapi_c_3po)

    # TODO Get passengers aboard the starship Twilight

    twilight = board_passengers(twilight, [padme, c_3po, r2_d2])
    # print(f"9.17.2\ntwilight = {twilight}")

    # 9.18 CHALLENGE 18

    # TODO Implement assign_crew_members()

    swapi_obi_wan = utl.get_resource(utl.SWAPI_PEOPLE, {'search': 'Obi-Wan Kenobi'})['results'][0]
    wookiee_obi_wan = get_wookieepedia_data(wookiee_people, 'Obi-Wan Kenobi')
    for key, val in wookiee_obi_wan.items():
        if val:
            swapi_obi_wan.update(wookiee_obi_wan)

    obi_wan = create_person(swapi_obi_wan, wookiee_planets)


    # TODO Assign crew members to the starship Twilight

    twilight = assign_crew_members(twilight, ['pilot', 'copilot'], [anakin, obi_wan])
    # print(f"9.18.2\ntwilight = {twilight}")

   # TODO Add r2_d2 instructions
    r2_d2['instructions'] = ['Power up the engines']


    # 10.0 ESCAPE

    # TODO Add r2_d2 instruction (2nd order)
    r2_d2['instructions'].append('Release the docking clamp')
    # print(r2_d2)

    # TODO Escape from the Malevolence (write to file)

    utl.write_json('stu-twilight_departs.json', twilight)
    # PERSIST CACHE (DO NOT COMMENT OUT)
    utl.write_json(utl.CACHE_FILEPATH, utl.cache)


if __name__ == '__main__':
    main()
