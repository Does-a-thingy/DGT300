#f = open('if_poem.txt')
#f.close()

word_dictionary = {'grape': 0, 'king': 0, 'olive'}


# open file
# break file into lines
# break lines into words
# count each word
# check against other items in the dictonary
# print highest

with open('if_poem.txt') as f:
    for line in f.readlines():
        for word in line.split(' '):
            if word in word_dictionary:
                word_dictionary[word] += 1
            elif word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                print('else broken')
                
first_word = 'king'
second_word = 'olive'
third_word = 'grape'

for word in word_dictionary.keys():
    if word_dictionary[word] > word_dictionary[first_word] and word != '   ':
        first_word = word
    elif word_dictionary[word] == word_dictionary[com_word]:
        print(word+' same '+com_word)
    else:
        pass

print('{} occurs {} times.'.format(com_word, word_dictionary[com_word]))
    
# reorganise dictionary into highest to lowest
# for k in desired_order_list:
    # new_dict = {k: old_dict[k]}
#
##if word_dictionary[word] > word_dictionary[first_word] and word != '   ':
        #com_word = word