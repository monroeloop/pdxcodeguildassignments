import random
empty_list = []

name_one = input('Tell me your name please.  ')
name_two = input('Tell me another name please.  ')
name_three = input('And lastly, one more name please.  ')

empty_list.append(name_one)
empty_list.append(name_two)
empty_list.append(name_three)

for names in empty_list:
    print('Hello there {}.'.format(names))

random_name = random.choice(empty_list)
name_one_question = int(input('Ok, {}, how old are you?  '.format(random_name)))
age = name_one_question + 1

print('Dang, {}! You are going to be {} yrs old next year.'.format(random_name, age))
