
def make_chains(text_string, n):
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

    for i in range(len(words) - n):

        key_tuple_list = []

        for j in range(n):
            key_tuple_list.append(words[i + j])
        
        # list_of_keys.append(key_tuple)

        key_tuple = tuple(key_tuple_list)

        if key_tuple not in chains_dict:
            chains_dict[key_tuple] = [words[i+n]]
        else: 
            chains_dict[key_tuple].append(words[i+n])
    
    return chains_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""


    upper_case_key_tuples = []
    all_key_tuples = chains.keys()

    number_of_items_in_tuples = len(all_key_tuples[0])

    for word_set in all_key_tuples:
        if word_set[0][0].isupper():
            upper_case_key_tuples.append(word_set)


    random_key = choice(upper_case_key_tuples)

    final_output = []

    for i in range(number_of_items_in_tuples):
        final_output.append(random_key[i])


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
