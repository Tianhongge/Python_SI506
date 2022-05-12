# SI 506: Lab Exercise 05

## Background

This week's lab exercise focuses on reading from and writing to a text file. The source file provided is Nelson Mandela's famous "I am prepared to die" speech. He delivered the speech from the dock on 20 April 1964 during the so-called Rivonia Trial in which Mandela and nine others were charged with sabotage and other crimes against the apartheid state. The trial ended in the conviction of all ten defendents; eight including Mandela were sentenced to life imprisonment. Mandela served 27 years in prison before being released in 1990. He was elected President of South Africa in 1994.

There are two versions of the Mandela speech, the one he prepared and the one he delivered. This lab focuses on the text of the prepared speech. The full text of the speech can be found in `mandela-prepared_speech.txt`. The original document's spacing between paragraphs has been removed for ease of parsing; punctuation has been retained.

## 1.0 Problem 01 (4 Points)

1. Implement the `read_file()` function.  The function accepts a filepath string and returns each line in the text file as a list element. Read the docstring for full details on parameters, return values, etc., but this function should:

   * utilize the built-in `open()` function and the `with` keyword to open the file.
   * the `readlines()` method is a great tool in reading a text file.
   * return a list of the lines you read in from the file.

## 2.0 Problem 02 (3 Points)

1. Implement the `has_phrase()` function. The function accepts two parameters: a list of lines from the speech and a phrase (it can be a single word or a full phrase) that you are trying to check for in the speech. To implement this function, you need to loop through the `speech` list use an `if` statement that utilizes the `in` keyword to see whether the phrase exists in that line of the speech. This function will be used in later problems.

   * In this problem, you will need to write a `for` loop and an `if` statement inside the loop.
   * The comparison should be case insensitive so you will need to employ the `string.lower()` function
   * If the phrase is in the speech, return `True`, otherwise return `False`.

## 3.0 Problem 03 (4 Points)

1. Implement the `find_phrases()` function. The function accepts two parameters: a list of lines from the speech and a list of phrases you are trying to check for in the speech. To implement this function, you need to loop through the list of phrases and call `has_phrase()` to identify in that phrase is in the speech. For each phrase, you will need to take the phrase and the result of `has_phrase()`, put it into a tuple, and append that tuple to a list that the function returns.

   * In this problem, you will need to write a `for` loop to iterate of the phrases.
   * In the `for` loop, you'll call `has_phrase()` to see if the speech has that phrase.
   * Put the result into a tuple with the phrase and the result of `has_phrase()` and put it in a list you return.

## 4.0 Problem 04 (4 Points)

1. Implement the `write_file` function. The function accepts two arguments: a filepath string and a
sequence (e.g., `list`). The function _must_ write each list element to its own line in the file created.

## 5.0 Problem 05 (3 points)
Now let's put it all together!

1. Using the `filepath` provided, call `read_file()` and assign it to speech.

2. Using the `phrases` list provided, call `find_phrases()` with `speech` and `phrases` and assign it to `present_phrases`

3. Call the function `write_file()` and pass to it the filepath string `'stu_find_phrases_results.txt'` and the list of tuples `present_phrases` returned from the previous step.

## 6.0 Problem 06 (2 points)

1. Let's practice some tuple unpacking. Take the first item from the `present_phrases` list and unpack it into the appropriate number of variables. You can test this using `print` statements.
