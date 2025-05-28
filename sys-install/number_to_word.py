###
# filename: number_to_word.py
#
# date: 03-05-20
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

    # remove unwanted digits
    number = number[6:] # delete area code
    number = number[:3] + number[4:] # remove hyphen

    word = ""
    d = enchant.Dict("en_US")  # check if word is a real english word

    # prod = list(product('012', repeat=7)) # Find all combinations of numbers (old cartesian product)
    temp = []
    prod = []
    # Find all combination of numbers
    for index in range(len(number)):
        if number[index] in ['9', '7']:
            temp.append([0,1,2,3])
        else:
            temp.append([0,1,2])

    for i in product(*temp):
        prod.append((i))

    # print(perm[0][1])
    i = 0

    while(1):

        for index in range(len(number)): # iterate through number and convert each number to a letter
            p = number[index]
            word += alph_num_dict[p][int(prod[i][index])] # add letter to word

        if d.check(word):
            return '1-800-' + word
        else:
            i += 1
            word = ""


if __name__ == '__main__':
    number = '1-800-724-6837' # input number
    # number = input("Enter your phone number: ")

    word = number_to_word(number)

    print(word)
