###
# filename: number_to_word.py
#
# by: Abhay Gupta
# desc: This function takes in an argument a string representing a US phone number
# and outputs a string that transforms part or all of a phone number into a single
# "wordified" phone number that can be typed on a US telephone.
###

def number_to_word(number):
    """Converts a number to a word"""

    import enchant # English Dictionary
    from itertools import product # Cartesian Product

    # Create a dictionary for number to letter conversion
    alph_num_dict = {'2': ('a', 'b', 'c'),
                     '3': ('d', 'e', 'f'),
                     '4': ('g', 'h', 'i'),
                     '5': ('j', 'k', 'l'),
                     '6': ('m', 'n', 'o'),
                     '7': ('p', 'q', 'r', 's'),
                     '8': ('t', 'u', 'v'),
                     '9': ('w', 'x', 'y', 'z')}

    number = number[4:] # delete area code
    word = ""
    d = enchant.Dict("en_US")  # check if word is a real english word
    perm = list(product('012', repeat=7)) # Find all combinations of numbers

    #print(perm[0][1])
    i = 0

    while(1):

        for index in range(len(number)): # iterate through number and convert each number to a letter
            p = number[index]
            word += alph_num_dict[p][int(perm[i][index])] # add letter to word

        if d.check(word):
            return word
        else:
            i += 1
            word = ""


if __name__ == '__main__':
    number = '18007246837' # input number
    word = number_to_word(number)

    print(word)
