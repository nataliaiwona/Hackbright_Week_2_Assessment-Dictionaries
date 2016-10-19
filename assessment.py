"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
    # splitting input string by spaces, creating list
    words = phrase.split()

    # initializing dictionary
    words_dict = {}

    # looping over each word in list of words
    for word in words:
        # check to see if each word in list is in dictionary
        # if it is, add 1 to current value
        # if it isn't, add the word to the dictionary as a key, the default 
        # value will be zero, and then add 1 
        words_dict[word] = words_dict.get(word, 0) + 1 

    # return the dictionary
    return words_dict

    # Not using .get():

    # check to see if each word in list is in dictionary
        # if yes, add 1 to the current value
        # otherwise, add the word to dictionary as a key and initialize value to 1

    # for word in words:
        # if word in words_dict:
        #     words_dict[word] += 1
        # else:
        #     words_dict[word] = 1


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Initialize dictionary with melon names as keys, prices as values.
    melon_dict = {
        "Watermelon": 2.95,
        "Cantaloupe": 2.50,
        "Musk": 3.25,
        "Christmas": 14.25
        }

    # Use .get() method to return the melon name (key) when the function is called. 
    # If the melon name is not in the dictionary, return our default value, 'No price found.'
    return melon_dict.get(melon_name, 'No price found')

    # Not using .get()
    # check to see if the melon name is in the dictionary.
    # if it is, return the name of the melon
    # otherwise, return message 'No price found'
    # 
    # if melon_name in melon_dict:
    #     return melon_dict[melon_name]
    # else:
    #     return 'No price found'


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # Initialize dictionary
    word_lengths = {}

    # for each word in passed-in list
    for word in words:
        # initializing variable to know the length of each word
        w_length = len(word)

        # checking to see if the word length is in the dictionary as a key
        # if yes, add another word to the value as a list
            # ex. 2 already exists, with the value "ok". Now, we add "an" to 
            # the value as a second element in that list.
        if w_length in word_lengths:
            word_lengths[w_length].append(word) 
        # otherwise, add the word length and the word as its value
        else:
            word_lengths[w_length] = [word]

        # sorting the dictionary by the value associated with each key
        word_lengths[w_length].sort()
    
    # Initializing variable to equal to dictionary turned into a list of tuples
    result = word_lengths.items()

    # Returning result
    return result


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Splitting the input string by each space, creating a list
    sentence = phrase.split()

    # Initializing empty list to store translated phrase in list-form
    pirate_sentence = []

    english_to_pirate = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        "man": "matey",
        "professor": "foul blaggart",
        "restaurant": "galley",
        "your": "yer",
        "excuse": "arr",
        "students": "swabbies",
        "are": "be",
        "restroom": "head",
        "my": "me",
        "is": "be",
    }

    for word in sentence:
        if word in english_to_pirate:
            pirate_sentence.append(english_to_pirate[word])
        else:
            pirate_sentence.append(word)
            
    return " ".join(pirate_sentence)




    # return " ".join([english_to_pirate.get(word, word) for word in sentence])

    # enumerate gives a list of tuples



    # EDIT: Not Pythonic, JS infiltrating code!!!
    # # Initialized variable i to zero
    # i = 0

    # # While loop to iterate over each word in the sentence list, while i is 
    # # less than the length of the list
    # while i < len(sentence): #(for word in sentence:)
    #     # initializing variable word to represent the sentence at a particular index
    #     word = sentence[i]

    #     # checking to see if a word is in the dictionary, if so, rebind word to 
    #     # equal the value, aka the translated word
    #     # could also use .get(): word = english_to_pirate.get(word, word)
    #     if word in english_to_pirate:
    #         word = english_to_pirate[word]

    #     # Take the translated word and add it to the empty list
    #     pirate_sentence.append(word)

    #     # Incrementing by one to access next word in list 
    #     i += 1

    # # returning the translation, which is joined back into a string by spaces.
    # return " ".join(pirate_sentence)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    PSEUDO CODE
    1. start_list = [x, y, z]
    2. new_list = [start_list[0]] AKA new_list.append(start_list[0])
    3. new_list[0]



    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """


    output = [names.pop(0)]

    print output

    letter_word_dict = {}
    # {first letter: [words beginning with that letter]}

    for word in names:
        first_letter = word[0]

        if first_letter not in letter_word_dict:
            letter_word_dict[first_letter] = [word]
        else:
            letter_word_dict[first_letter].append(word)

    while True:
        start_letter = output[-1][-1]

        if not letter_word_dict.get(start_letter):
            break

        match = letter_word_dict[start_letter].pop(0)
        output.append(match)

    return output

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
