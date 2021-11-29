# I haven't written anything yet
# But it'll be Trumpian amazing when I do!!
print("hello world")

from get_aoc import get_input

rawInput = get_input(7)

splitInput = rawInput.split("\n") # Splitting the data into a list
#print("splitInput = ")
#print(splitInput)
#print(len(splitInput)) # Number of list groups

def each_bag_contains(bag_line):
    place_contain = bag_line.find("contain")
    bag = bag_line[:(place_contain-2)]
    #print("bag is question is " + bag)
    #print(bag)
    contains = bag_line[(place_contain+8):-1]
    #print(contains)
    contains_list = contains.split(", ")
    #print("contains list")
    #print(contains_list)
    contains_dict = {}
    #if contains_list(0) != "no other bags":
    bag_name = "I fucked up"
    for sub_bag in contains_list:
        if sub_bag != "no other bags":
            #print("yes")
            number = sub_bag[0]
            bag_name = sub_bag[2:]
            if bag_name[-1] == "s":
                #print("removed the 's'")
                bag_name = bag_name[:-1]
            contains_dict[bag_name] = number
        else:
            #print("no")
            pass
    #print("the contents of " + bag)
    #print(contains_dict)
    return(bag, contains_dict)

def can_contain(bag, bag_inside):
    contents = dictionary_of_bags[bag]
    if bag_inside in contents:
        return True
    else:
        return False

print("got to here")
dictionary_of_bags = {}
for line in splitInput:
    bag, contents = each_bag_contains(line)
    #print("DID I GET TO HERE??")
    dictionary_of_bags.update({bag: contents})
    #print(dictionary_of_bags)
    #each_bag_contains(splitInput[line])
print("so I've got the dictionay of dictionaries:")
print(dictionary_of_bags)

print("now check if SGB is it the list")
counter = 0
#if can_contain(dictionary_of_bags.keys(), "shiny gold bag") == True:
#    counter += 1
#    print("we got one")
bag_looking_for = "bright white bag" #"muted yellow bag" #"shiny gold bag"

possible_bags = []

def all_pos_tree (bag_looking_for,dictionary_of_bags):
    possible_bags = []
    for bag_line in dictionary_of_bags.keys(): 
        contents = dictionary_of_bags[bag_line]
        print("bag is question is " + bag_line)
        print(contents)

        if "shiny gold bag" in possible_bags:
            print("it's already in the list")
        elif "bag_looking_for" in contents.keys():
            print("it's a top level bag")
            possible_bags.append(bag_line)           
        else:
            print("in this place")
            #possible_bags = all_pos_tree(bag_line, dictionary_of_bags)
            #pass
        print("possible bags are: ")
        print(possible_bags)
    return possible_bags

x = all_pos_tree(bag_looking_for, dictionary_of_bags)
print("the possible bags are")
print(x)


#possible_bags = [bag for bag in dictionary_of_bags.keys() if can_contain(dictionary_of_bags(bag), "shiny gold bag") == True]

#for data_line 