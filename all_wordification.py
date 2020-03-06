###
# filename: number_to_word.py
#
# by: Abhay Gupta
# desc: Converts telephone number to word, outputs all possible words
###

def number_to_word(number):
    """Converts a number to a word"""

    import enchant # English Dictionary
    from itertools import product # Cartesian Product
    from itertools import combinations # Combination

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
    all_words = []
    d = enchant.Dict("en_US")  # check if word is a real english word
    prod = list(product('012', repeat=7)) # Find all combinations of numbers
    comb = list(combinations([0, 1, 2, 3, 4, 5, 6], 2)) #F Find all inner combination of numbers

    #print(perm[0][1])
    i = 0

    for i in range(len(prod)):

        for index in range(len(number)): # iterate through number and convert each number to a letter
            p = number[index]
            word += alph_num_dict[p][int(prod[i][index])] # add letter to word

        #if d.check(word): # add new words to list
            #all_words.append(word)

        for j in comb:
            temp = word[j[0]:j[1]]
            if d.check(temp):
                temp = number[0:j[0]]+temp+number[j[1]:]
                all_words.append(temp)


        word = ""

    return(all_words)

if __name__ == '__main__':
    number = '18007246837' # input number
    word = number_to_word(number)

    print(word)