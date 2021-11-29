#### Lines about lettercount in def howManyAnswers could be combined?
#### While loops for the length of something with a counter variable seems bloated. What's the shorter way?
#### Stuck on how to sum up the values in my dictionary
#Checking the number of letter replies
from get_aoc import get_input

rawInput = get_input(6)

splitInput = rawInput.split("\n\n") # Splitting the data into a list
groups = [[set(answers) for answers in group.split()] for group in splitInput]

def howManyAnswers(group): # This finds how many difference answers a group gave
    return len(group[0].union(*group[1:]))

print("Part 1:")
print(sum(howManyAnswers(group) for group in groups))

def howManyNewAnswers(groups): # This finds how many identical answers a group gave
    return len(groups[0].intersection(*groups[1:]))

print("Part 2:")

print(sum(howManyNewAnswers(group) for group in groups))

def the_splat_operator(a, b):
    print("a is %d" % a)
    print("b is %d" % b)

the_splat_operator(1, 2)
array = [3, 4]
the_splat_operator(*array)
