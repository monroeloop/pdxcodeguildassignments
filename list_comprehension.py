#This is a lab to try out list comprehensions.  Below each lab is worked out using for loops followed by
#list comprehension.

names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']
people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

#'names' is a list of strings.
#'people' is a list of tuples.


def long_names():
    new_list = []
    for newnames in names:
        if len(newnames) < 5:
            new_list.append(newnames)
    print(new_list)

    new_list2 = [newnames for newnames in names if len(newnames) < 5]
    print(new_list2)

long_names()

def names_w_x():
    new_list = []
    for frames in names:
        if 'k' in frames.lower():
            new_list.append(frames)
    print(new_list)

    new_list2 = [frames for frames in names if 'f' in frames.lower()]
    new_list3 = [frames for frames in names if frames[0] == 'S']
    print(new_list2)
    print(new_list3)

names_w_x()

def last_names():
    new_list = []
    for lames in people:
        new_list.append(lames[1])
    print(new_list)
    # new_people = people[1][1]
    # print(new_people)

    new_list2 = [lames[1] for lames in people]
    print(new_list2)

last_names()

def smoosh():
    new_list = []
    new_list2 = []
    for smoo in people:
        for smoos in smoo:
            new_list.append(smoos)
        # condensed = ''.join(smoo)
        # new_list.append(smoo)

    # condensed_more = ''.join(new_list)
    # new_list2.append(condensed_more)

    print(new_list)
    # print(new_list2)

    new_list3 = [x for i in people for x in i]
    new_list4 = [''.join(x for i in people for x in i)]
    print(new_list3)
    print(new_list4)

smoosh()