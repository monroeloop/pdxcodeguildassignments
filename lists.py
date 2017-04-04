
numbers = [14, 24, 34, 44, 54, 64]

# rng = list(range(10))
# print(rng)

# print(len(animals))
# for a single number in total numbers in the range of 'numbers'
                                                # len() sets the total number
                                                # range() then sets 1 - total numbers
for single_number in range(len(numbers)):
    numbers[single_number] += 5
    print('index: {}, value: {}'.format(single_number, numbers[single_number]))

lst = [22, 33]
num = int(input('What is your favorite number?  '))

lst.append(num)

print(lst)
