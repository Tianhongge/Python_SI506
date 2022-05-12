# SI 506: Lab Exercise 04

## This week's Lab Exercise

This week's lab exercise includes five (5) problems focused on creating and calling functions.

## Data description

Drake is a famous rapper/singer from Canada. The data from this week draws from his most streamed tracks (https://chartmasters.org/2021/07/streaming-masters-drake/). The tracks are assigned to the variable name `top_songs`, which is a list of nested lists with each song's title and its corresponding number of streams.

## 1.0 Problem 01 (3 Points)

Create a function named `get_title()` that defines a single parameter named "song" (a `list`) and returns the song title.

After implementing the function, call `get_title()` and pass to it as an argument the first "song" in `top_songs`. Assign the return value to a variable named `title`.

## 2.0 Problem 02 (3 Points)

Create a function named `get_streams()` that defines a single parameter named "song" (a `list`) and returns the number of streams for the song.

After implementing the function, call `get_streams()` and pass to it as an argument the second "song" in `top_songs`. Assign the return value to a variable named `streams`.


## 3.0 Problem 03 (5 Points)

Create a function named `remove_song()` that defines two parameters:

* songs_list (list of lists): a `list` of _nested_ song lists
* song (list): a song to be removed

Before removing the song, this function *must* confirm that the song to be removed is an element in `songs_list`. The function does not return a specified value (it returns `None` implicitly).

Create a variable named `mia` and assign the last song in the `top_songs` list to it.

Call the `remove_song()` function in order to remove `mia` from the list `top_songs`.


## 4.0 Problem 04 (6 points)

Create a function named `add_song()` that defines three parameters:

* songs_list (list of lists): a `list` of _nested_ song lists
* song (list): a song to add
* idx (int): the index position in the list of songs where the song will be inserted. _Assign a default value of `0` to the parameter._

The function does not return a specified value.

Create a list with two elements ["Life is Good", 1028000] and assign this list to a new variable named `life_is_good`.

Call the `add_song()` function and add the song `life_is_good` to `top_songs` in the *second* position.


## 5.0 Problem 05 (3 points)

Create a list with two elements ["Nice for What", 960000] and assign this list to a new variable named `nice_for_what`.

Call the `add_song()` function and add the song `nice_for_what` to `top_songs` in the *third* position using keyword arguments in _reverse order_.

:exclamation: You _must_ employ keyword arguments passed to the function in _reverse order_ in order to pass the auto grader. You must also style the keyword argument assignment correctly (e.g., `keyword_arg=value`, not `keyword_arg = value`).
