inputT = []

with open('day8.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)
#print(inputT)
instructions = []
for e in inputT:
    text = e.split(' ')
    instructions.append(text)

for i in range(len(instructions)):
    instructions[i].append(0)
print(len(instructions))


def GetAccumulator(list_instructions):
    acc = 0
    repetition = False
    i = 0
    while (repetition == False):
        jump_index = 0            
        if(list_instructions[i][2] == 0):
            #print(list_instructions[i], i)
            if(list_instructions[i][0] == 'acc'):
                acc += int(list_instructions[i][1])
                list_instructions[i][2] = 1
                i += 1
            elif(list_instructions[i][0] == 'nop'):
                list_instructions[i][2] = 1
                i += 1

            elif(list_instructions[i][0] == 'jmp'):
               jump_index =  i + int(list_instructions[i][1])
               list_instructions[i][2] = 1
               i = jump_index
                

        else:
            print(list_instructions[i], i)
            repetition = True
    print(acc)
    return i
    


def GetAccumulatorChange(list_instructions):
    not_last = True
    this_list = []
    new_list = [i for i in list_instructions]
    while not_last:
        for i in range(len(new_list)):            
            if(new_list[i][0] == 'jmp'):                
                new_list[i][0] = 'nop'
                last_i = GetAccumulator(new_list)
                if( last_i >= 628):
                    this_list = list(new_list)
                    not_last = False
                else:
                    new_list[i][0] = 'jmp'

            elif(new_list[i][0] == 'nop'):                
                new_list[i][0] = 'jmp'
                last_i = GetAccumulator(new_list)
                if(last_i >= 628):
                    this_list = list(new_list)
                    not_last = False
                else:
                    new_list[i][0] = 'nop'


        



GetAccumulatorChange(instructions)      
        

