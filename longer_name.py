# Return the longest.
# >>> choose_longer("Greg", "Rooney")
# 'Rooney'

def enter_names():
    first_name = input('Enter a name.  ')
    second_name = input('Enter another name.  ')
    if len(first_name) > len(second_name):
        print('The name \'{}\' is longer than the name \'{}\'.'.format(first_name, second_name))
    elif len(second_name) > len(first_name):
        print('The name \'{}\' is longer than the name \'{}\'.'.format(second_name, first_name))

enter_names()
# print(len(first_name))
