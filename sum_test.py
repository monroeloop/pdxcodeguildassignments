# Return the sum of any number of integers using *args.
args = (980, 667, 4432, 788, 122, 9, 545, 222)
# 7765
def arguments(*args):
    sum_numbers = sum(args)
    print(sum_numbers)
    print(*args)

arguments(980, 667, 4432, 788, 122, 9, 545, 222)
