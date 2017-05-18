# """
# Write a function that returns the meal for any given hour of the day.
# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM
# Dinner: 7PM - 9PM
# Hammer: 10PM - 4AM
# >>> meal(7)
# 'Breakfast time.'
# >>> meal(13)
# 'Lunch time.'
# >>> meal(20)
# 'Dinner time.'
# >>> meal(21)
# 'No meal scheduled at this time.'
# >>> meal(0)
# 'No meal scheduled at this time.'
# >>> meal(3)
# 'Hammer time.'
# >>> meal(9999)
# 'Not a valid time.'
# """

def meals():
    meal_time = int(input('What time are you thinking you would like to eat?  '))
    if 7 <= meal_time <= 9:
        print('Breakfast Time!')
    elif 12 <= meal_time <= 13:
        print('Lunch Time!')
    elif 18 <= meal_time <= 20:
        print('Dinner Time!')
    elif meal_time > 24:
        print('That\'s not a time.  You have bigger problems than figuring out what your meal is.')
    else:
        option = input('There is no meal scheduled at this time.  Would you like to quit(q) or continue (c)?  ')
        if option is 'q':
            print('Goodbye.')
            quit()
        else:
            meals()

while True:
    meals()
