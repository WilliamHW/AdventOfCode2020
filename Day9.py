#Code to find the error number which is the first that doesn't have 2 numbers in the last 25 before it that add to it's value
from get_aoc import get_input_integers
from itertools import combinations

numbers = get_input_integers(9)

length_preamble = 25 #5 for test data, 25 for real data

for counter in range(length_preamble, len(numbers)):
    data_set = numbers[(counter-length_preamble):(counter)]
    testing_number = numbers[counter]
    preamble_pairs = list(combinations(data_set, 2))
    this = next((pair for pair in preamble_pairs if sum(pair) == testing_number), None)
    if this is None:
        break

"""while correct == True:
    goodnums = {testing_number-x for x in data_set if x <= half_that} & {x for x in data_set if x > half_that}
    print(goodnums)
    pair = {(testing_number - x, x) for x in goodnums}
    print(pair)
    print("here")
    if len(pair) == 0:
        break
    counter += 1
    data_set = numbers[(counter-length_preamble):(counter)]
    testing_number = numbers[counter]
    print(testing_number)
    print(data_set)"""

print("Part One")
print(testing_number)