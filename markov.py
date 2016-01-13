from random import choice

import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_obj = open(file_path)

    file_text = file_obj.read()

    file_obj.close()

    return file_text
    
# text_file = open_and_read_file("green-eggs.txt")


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()  

    # list_of_keys = []
    

    chains_dict = {}

    for i in range(len(words) -2):
        key_tuple = (words[i], words[i + 1])
        
        # list_of_keys.append(key_tuple)

        if key_tuple not in chains_dict:
            chains_dict[key_tuple] = [words[i+2]]
        else: 
            chains_dict[key_tuple].append(words[i+2])
    
    return chains_dict


# chains_file = make_chains(text_file)


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    upper_case_key_tuples = []
    all_key_tuples = chains.keys()

    for word_set in all_key_tuples:
        if word_set[0][0].isupper():
            upper_case_key_tuples.append(word_set)


    random_key = choice(upper_case_key_tuples)

    final_output = [random_key[0], random_key[1]]

    while random_key in chains: 
        # keep looping as long as the word set is a key in the dictionary "chains" followed by words to add
        # if no key in dictionary, loop stops, poem completed
        
        random_key_position_two = choice(chains[random_key]) 
        random_key = (random_key[1], random_key_position_two)

        # random_key tuple = (random_key_position_1, random_key_position_2)
        # random_key tuple gets updated
        # so random_key_position_2 moves to random_key_position_1
        # and random_key_position_2 then filled by a random value from the value set matched by the random_key tuple

        final_output.append(random_key_position_two)

    text = (" ").join(final_output)

    # your code goes here

    return text 


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
