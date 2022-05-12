# Lab Exercise 02
print('Lab Exercise 02 \n')

# Setup
shows = [
    "Action Pack, Kids, 1, exciting",
    "The Queen of Flow, Telenovela, 2, Emotional",
    "Hype House, Reality, 1, scandalous",
    "Queer Eye, Lifestyle, 6, Feel-good",
    "Cocomelon, Kids, 4, educational",
    "Emily in Paris, Romantic Comedy, 2, Quirky",
    "The Witcher, Fantasy, 2, Exciting",
    "Stay Close, Crime, 8, emotional",
    "Cobra Kai, Dramedy, 4, exciting",
    "Cheer, Reality, 2, exciting"
]

# Problem 01 (3 points)

genres = []

for show in shows:
    genres.append(show.split(', ')[1])

print(f"\n1. genres = {genres}")

# Problem 02 (4 points)

emotional_shows = []

for show in shows:
    if show.split(', ')[-1].lower() == "emotional":
        emotional_shows.append(show.split(', ')[0])

print(f"\n2. emotional_shows = {emotional_shows}")

# Problem 03 (4 points)

count = 0

for show in shows:
    name = show.split(', ')[0].split()
    if len(name) > 1:
        # count = count + 1
        count += 1
print(f"\n3. There are a total of {count} shows with more than one word in their title.")

# PROBLEM 4 (4 Points)

new_shows = []

for show in shows:
    if int(show.split(', ')[2]) < 3:
        new_shows.append(show.split(', ')[0])

print(f'\n4. new_shows = {new_shows}')

# PROBLEM 5 (5 Points)

longest_show = None
curr_longest_seasons = 0

for show in shows:
    if int(show.split(', ')[2]) > curr_longest_seasons:
        curr_longest_seasons = int(show.split(', ')[2])
        longest_show = show.split(', ')[0]

print(f'\n5. longest_show = {longest_show}')

# END LAB EXERCISE
