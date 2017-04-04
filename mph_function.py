def trip_calculator(time):
    print('Your trip will take {} hrs.'.format(miles/speed))

miles = int(input('What is the distance you are traveling?  '))
speed = int(input('How fast will you be traveling?  '))
time = miles / speed

trip_calculator(time)
