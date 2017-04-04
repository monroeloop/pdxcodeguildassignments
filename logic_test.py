name = input('What is your name?  ')

valid_int = False
while not valid_int:
    try:
        age = int(input('Hello {}, how old are you?:  '.format(name)))
        valid_int = True
    except ValueError:
        print('That is not a valid entry. Please try again.')


if age >= 100:
    print('You should be dead by now!')
elif age > 20:
    print('You\'re getting old person.')
else:
    print('You\'re too young to be here.')
