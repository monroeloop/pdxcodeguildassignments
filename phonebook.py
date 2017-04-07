pb = {'Monroe-Loop':
                {'name': 'Mike Monroe-Loop', 'phone': '503-440-1201'},
             'Loop':
                {'name': 'Jackie Loop', 'phone': '208-552-1587'},
             'Chevrolet':
                {'name': 'Frank Chevrolet', 'phone': '541-555-5555'}
            }



#
# def lookup(dictionary, name):
#     print(pb[name]['name'])
#     print(pb[name]['phone'])
#
# lookup(pb, 'Loop')

def delete():
    delete_entry = input('\n\tEnter the last name of who you would like to remove.  ')
    del(pb[delete_entry])
    print(pb)

def add_entry():
    question_fn = input('\n\tPlease enter the first name.  ')
    question_ln = input('\tPlease enter the last name.  ')
    question_n = input('\tPlease enter the phone number.  ')
    pb[question_ln] = {'name': [question_fn]+[question_ln], 'phone': [question_n]}

def view():
    view_ln = input('''\n\nPlease enter the last name of the person whose information you would like to view.  ''')
    print(pb[view_ln]['name'])
    print(pb[view_ln]['phone'])


def edit():
    edit_entry = input('\n\tEnter the last name of who you would like to edit or cancel (c).  ').lower()
    if edit_entry is 'c':
        start()
    del(pb[edit_entry])
    add_entry()
    # change_entry_fn= input('\n\tPlease enter the new first name.  ')
    # change_entry_ln = input('\tPlease enter the new last name.  ')
    # change_entry_n = input('\tPlease enter the new phone number.  ')
    # pb[change_entry_ln] = {'name': [change_entry_fn]+[change_entry_ln], 'phone': [change_entry_n]}
    # print(pb)

q = input('What number are you searching?  ')

# example Chris provided of a for loop in action
# for ke, va in phonelist.items():
#     for k, v in ke.items():
#         if q in v:
#             print('name: {}'.format(pb[ke]['name']))
#             print('name: {}'.format(pb[ke]['phone']))

print(pb.items())

def search():
    search_name = input('\n\tWhat name would you like to search?  ')
    try:
        print(pb[search_name])
    except KeyError:
        print('\n\tI\'m sorry. That name is not found')

def start():
    question = input('\nWould you like to search (s), add (a), edit (e), view (v) delete (d) an entry or exit (q)?  ')
    if question is 'a':
        add_entry()
    elif question is 's':
        search()
    elif question is 'e':
        edit()
    elif question is 'd':
        delete()
    elif question is 'v':
        view()
    elif question is 'q':
        question_2 = input('Would you like to quit? (y/n)  ')
        if question_2 is 'y':
            print('Goodbye')
            quit()
        elif question is 'n':
            start()

while True:
    start()
