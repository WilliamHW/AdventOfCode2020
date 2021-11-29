from get_aoc import get_input

rawInput = get_input(8)

splitInput = rawInput.split("\n") # Splitting the data into a list
print("splitInput = ")
print(splitInput)
print(len(splitInput)) # Number of list groups

def run_line(instruction):
    #print("running line")
    movement = 0
    added_value = 0
    if instruction[0] == "acc":
        added_value = instruction[1]
    elif instruction[0] == "jmp":
        movement = instruction[1]
        #print("im here")
    #elif instruction[0] == "nop": 
    if movement == 0: movement =1
    #print("movement is " +str(movement))
    #print("added value is " +str(added_value))
    return movement, added_value

instructions = []
list_instructions = []
for instruction in splitInput:
    operation = instruction[:3]
    argument = int(instruction[3:])
    #operation, argument = understand_instruction(instruction)
    instructions.append([operation, argument])
    list_instructions.append(operation)
print(instructions)
print(len(instructions))  
print(list_instructions)
print(len(list_instructions))

has_line_been_run = []
counter = 0
while counter < len(instructions):
    has_line_been_run.append(0)
    counter += 1
print(has_line_been_run)
print(len(has_line_been_run))
blank_hlbr = has_line_been_run
print("it should also be all zeros")
print(blank_hlbr)

position = 0
not_finished = True
accumulator = 0
while not_finished == True:
    has_line_been_run[position] = 1
    instruction = instructions[position]
    #print(instruction)
    #print("running line: " + str(position))
    movement, added_value = run_line(instruction)
    #print("line position is:" + str(position))
    position = position + movement
    #print("line position is:" + str(position))
    accumulator = accumulator + added_value
    #print(position, accumulator)
    #print(has_line_been_run)
    if has_line_been_run[position] == 1:
        not_finished = False
    
print("Part 1:")
print(accumulator)

def flip (corrupt_test):
    if corrupt_test == "nop": corrupt_test = "jmp"
    elif corrupt_test == "jmp": corrupt_test = "nop"
    return corrupt_test

position_test = list_instructions.index("nop" or "jmp")
corrupt_test = list_instructions[position_test]
print("position, then corruption, test is")
print(position_test)
print(corrupt_test)
corrupted_not_found = True
accumulator = 0
corrupted_counter = 0
while corrupted_not_found == True:
    new_instructions = instructions
    has_line_been_run = []
    counter = 0
    while counter < len(instructions):
        has_line_been_run.append(0)
        counter += 1
    print(has_line_been_run)
    print(len(has_line_been_run))   
    instruction = instructions[position_test]
    print(instruction)
    while instruction[0] != ("nop" or "jmp"):
        print("not a line we should change")
        print(instructions[position_test])
        print(position_test)
        position_test = position_test =+ 1
        print(position_test)
        print(instructions[position_test])
        #position_test =+ 1
        instruction = instructions[position_test]
        print(instruction)

    if instruction[0] == "nop" and instruction[1] == 0:
        print("well i'm fucked")
        change = "nop"        
    else:
        change = flip(instruction[0])
    instruction[0] = change
    print(instruction)
    instructions[position_test] = instruction
    position = 0
    not_finished = True
    accumulator = 0
    print("it should also be all zeros")
    #print(blank_hlbr)
    new_has_line_been_run = has_line_been_run
    print("the new hlbr is: ")
    print(new_has_line_been_run)
    while not_finished == True:
        new_has_line_been_run[position] = 1
        print(new_has_line_been_run)
        instruction = instructions[position]
        print(instruction)
        print("running line: " + str(position))
        movement, added_value = run_line(instruction)
        print("line position is:" + str(position))
        position = position + movement
        print("line position is:" + str(position))
        accumulator = accumulator + added_value
        print(position, accumulator)
        #print(has_line_been_run)
        if new_has_line_been_run[position] == 1:
            print("I'm here??")
            not_finished = False
    print(position, accumulator)
    if position == len(has_line_been_run):
        corrupted_not_found = False    
    print(instructions[position_test])
    position_test = position_test =+ 1
    print(instructions[position_test])
    print("position test is " + str(position_test))
    print("WE COMPLETED A LOOP")
    print("Part 1ish:")
    print(accumulator)
print("Part 2:")
print(accumulator)   
    