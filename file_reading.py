#f = open('if_poem.txt')
#f.close()

word_dictionary = {'grape': 0, 'king': 1, 'olive': 2}
number_list = []

# open file
# break file into lines
# break lines into words
# count each word
# check against other items in the dictonary
# print highest

with open('if_poem.txt') as f: # opens a file, then closes it after its done
    for line in f.readlines():
        for word in line.split(' '):
            if word in word_dictionary:
                word_dictionary[word] += 1
            elif word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                print('else broken')

sorted_list = sorted(word_dictionary.items(), key=lambda item: item[1])
for key, value in sorted_list:
    word_dictionary[key] = value
    
print(word_dictionary)

first_word = ['king']
second_word = ['olive']
third_word = ['grape']

for word in word_dictionary.keys():
    if word_dictionary[word] > word_dictionary[first_word[0]] and word != '   ':
        first_word = [word]
    elif word_dictionary[word] >= word_dictionary[second_word[0]]and word != '   ':
        if word_dictionary[word] == word_dictionary[second_word[0]]:
            second_word.append(word)
        else:
            second_word = [word]
    elif word_dictionary[word] >= word_dictionary[third_word[0]]and word != '   ':
        if word_dictionary[word] == word_dictionary[third_word[0]]:
            third_word.append(word)
        else:
            third_word = [word]    
    elif word_dictionary[word] == word_dictionary[third_word[0]]:
        print(word, third_word)
    else:
        pass



print('{} occurs {} times.'.format(first_word, word_dictionary[first_word[0]]))
print('{} occurs {} times.'.format(second_word, word_dictionary[second_word[0]]))
print('{} occurs {} times.'.format(third_word, word_dictionary[third_word[0]]))
    
# reorganise dictionary into highest to lowest
# for k in desired_order_list:
    # new_dict = {k: old_dict[k]}
#
 #if word_dictionary[word] > word_dictionary[first_word] and word != '   ':
        #com_word = word


new_string = input('what would you like to add to the poem?: ')

with open('if_poem.txt', 'w') as f:
    f.write('\n New addition \n')
    f.write(new_string)