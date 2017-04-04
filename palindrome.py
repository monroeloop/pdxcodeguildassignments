# def palindrome(word1):
#     if word1 == word1[::-1]:
#         print('You have a palindrome.')
#     else:
#         print('That ain\'t a palindrome.')
#
# word1 = input('You there! Type me a word.  ')
# palindrome(word1)

snake_to_camel = []

s_c = input('Type snake_case_phrase:  ')
c_c = s_c.split('_')
for word in c_c:
    snake_to_camel.append(word.capitalize())
j_c_w = ''.join(snake_to_camel)
print(j_c_w)

string = 'HelloHowAreYouToday'
string_list = []
last_index = 0
for letter in range(len(string)):
    if string[letter].isupper():
        if letter != 0:
            string_list.append(string[last_index:letter])
            last_index = letter
string_list.append(string[last_index:])

print('_'.join(string_list).lower())



# remove_space = snake_to_camel.replace('_',' ')
# print(remove_space)
# split_word = remove_space.split(' ')
# print(split_word)
# for word in split_word:
#     print(word.capitalize())
# print(first_word)
# capital_words = word.capitalize()
# join_capital_words = ''.join(capital_words)
# print(join_capital_words)



# make_space_up = remove_space.capitalize()
# print(make_space_up)



# word_list = words.split(' ')
# result = ', '.join(word_list)
# total = len(word_list)
