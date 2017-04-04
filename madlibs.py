name = input('Hey there, what is your name?: ')
animal = input('Tell me the name of an animal. ')
vegetable = input('What is your favorite vegetable? ')
star_wars_character = input('Tell me a character from Star Wars. ')

print("""
    Hello {}.  You are an amazing {} who loves to watch Star
    Wars. Your favorite Star Wars character is {}. Aren't you always saying
    that {} resembles a giant {}?
    """.format(name,
        animal.lower(),
        star_wars_character,
        star_wars_character,
        vegetable.lower()))
