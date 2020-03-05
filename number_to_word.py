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
    word = []

    for index in range(len(number)): # iterate through number and convert each number to a letter
        p = number[index]
        word.append(alph_num_dict[p][0])


    full_word = ""
    for element in word: # convert list of letters to single string
        full_word += element

    d = enchant.Dict("en_US") # check if word is a real english word
    if d.check(full_word):
        return full_word
    else:
        print(full_word)
        return 'False'


if __name__ == '__main__':
    number = '18007246837' # input number
    word = number_to_word(number)

    return(word)
