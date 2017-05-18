from random import choice as c

student_names = ['Malcolm', 'Ian', 'Chase', 'Tab', 'Mike', 'Joe']

def generate_team(lst):
    lst2 = lst[:]
    team_a = []
    team_b = []
    counter = 0
    for name in lst:
        if counter % 2 == 0:
            person = c(lst)
            team_a.append(person)
            lst2.remove(person)
            counter += 1
        else:
            person = c(lst)
            team_b.append(person)
            lst2.remove(person)
            counter += 1

    return team_a, team_b

generate_team(student_names)

print('A: {} \nB: {}'.format(', '.join(team_a),', '.join(team_b)))
