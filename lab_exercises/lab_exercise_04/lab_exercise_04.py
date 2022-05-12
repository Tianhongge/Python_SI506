# START LAB EXERCISE 04
from os import remove


print('Lab Exercise 04 \n')

#SETUP
top_songs = [
    ["One Dance", 2096000],
    ["God's Plan", 1892000],
    ["Sicko Mode", 1569000],
    ["Work", 1299000],
    ["In My Feelings", 1220000],
    ["Hotline Bling", 1138000],
    ["MIA", 1058000]
]

# END SETUP

# PROBLEM 1 (3 points)

def get_title(song):
    return song[0]

# TODO Implement function

title = get_title(top_songs[0]) # call function

print(f"\n1. First song title: {title}")



# PROBLEM 2 (3 points)

def get_streams(song):
    return song[1]

# TODO Implement function

streams = get_streams(top_songs[1]) # call function

print(f"\n2. Number of streams of the second song: {streams}")



# PROBLEM 3 (5 points)

def remove_song(song_list, song):
    if song in song_list:
        song_list.remove(song)

# TODO Implement function

mia = top_songs[-1]

# TODO call function

remove_song(top_songs, mia)

print(f"\n3. {top_songs}")



# Problem 4 (6 points)

def add_song(songs_list, song, idx=0):
    songs_list.insert(idx, song)

life_is_good = ["Life is Good", 1028000]
# TODO Create variable

add_song(top_songs, life_is_good, 1)
# TODO call function

print(f"\n4. {top_songs}")



# Problem 5 (3 points)

nice_for_what = ["Nice for What", 960000]
# TODO Implement function
# TODO call function

add_song(idx=2, song=nice_for_what, songs_list=top_songs)

print(f"\n5. {top_songs}")
# END LAB EXERCISE

