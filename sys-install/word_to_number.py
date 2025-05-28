###
# filename: word_to_number.py
#
# date: 03-05-20
# by: Abhay Gupta
# desc: Converts word to phone number
###


def word_to_number(word):
    """Converts a word to a number"""

    # create dictionary for letter to telephone number
    alph_num_dict = {'a': '2', 'b': '2', 'c': '2',
                     'd': '3', 'e': '3', 'f': '3',
                     'g': '4', 'h': '4', 'i': '4',
                     'j': '5', 'k': '5', 'l': '5',
                     'm': '6', 'n': '6', 'o': '6',
                     'p': '7', 'q': '7', 'r': '7', 's': '7',
                     't': '8', 'u': '9', 'v': '8',
                     'w': '9', 'x': '9', 'y': '9', 'z': '9'}

    word = word[6:].lower() # delete area code and lowercase letters
    number = ""

    for index in range(len(word)): # iterate through word and convert each letter to a number
        p = word[index]
        if p in alph_num_dict: # check if character or number
            number += alph_num_dict[p]
        else:
            number += p

    return('1-800-' + number[:3] + '-' + number[3:])

if __name__ == '__main__':
    word = '1-800-painter' # input word
    number = word_to_number(word)

    print(number)
