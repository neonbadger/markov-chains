
from random import choice

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_obj = open(file_path)

    file_text = file_obj.read()

    file_obj.close()

    return file_text


def make_chains(text_string, n):
    """Takes input text as string and number for n-gram;
    returns a dictionary of markov chains.

    A chain will be a key that consists of a tuple of n-gram
    (word_1, word_2 ... word_n) and the value would be a list
    of the word(s) that follow those words in the input text.

    For example:

        >>> make_chains("Hi hi my friend how are you", 5)
        {("Hi", "hi", "my", "friend", "how"): ['are'],
         ("hi", "my", "friend", "how", "are"): ['you']}
    """

    words = text_string.split()

    chains_dict = {}

    for i in range(len(words) - n):

        key_tuple_list = []

        for j in range(n):
            key_tuple_list.append(words[i + j])

        key_tuple = tuple(key_tuple_list)

        if key_tuple not in chains_dict:
            chains_dict[key_tuple] = [words[i+n]]
        else: 
            chains_dict[key_tuple].append(words[i+n])
    
    return chains_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    all_key_tuples = chains.keys()
    upper_case_key_tuples = []

    n = len(all_key_tuples[0])
    # n counts the number of items in the key tuple
    # for making n-gram

    for word_set in all_key_tuples:
        if word_set[0][0].isupper():
            upper_case_key_tuples.append(word_set)


    random_key = choice(upper_case_key_tuples)

    final_output = []

    for i in range(n):
        final_output.append(random_key[i])
        # populate the final_output list with the items of 
        # the initial random_key

    while random_key in chains: 

        random_key_position_last = choice(chains[random_key]) 
        # get the last item for the *NEW* random_key

        random_key_list = []

        for i in range(n-1):
            random_key_list.append(random_key[i+1])
            # populate the *NEW* random_key list with items
            # from the current random_key[1] -- [n-1]
            # essentially drop random_key[0]

        random_key_list.append(random_key_position_last)
        # add the newly pulled value hashed to the key
        # to the last position to form a *NEW* random_key

        random_key = tuple(random_key_list)

        final_output.append(random_key_position_last)
        # the newly pulled value also forms part of the 
        # random text
    
    text = (" ").join(final_output)

    return text 



input_path = "gettysburg.txt"

input_text = open_and_read_file(input_path)

chains = make_chains(input_text, 4)

random_text = make_text(chains)

print random_text



