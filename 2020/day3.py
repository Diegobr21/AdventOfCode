
mapT = []

with open('day3.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        mapT.append([line])

h_length = len(mapT[0][0])

def Trees(hIncrease, vIncrease):
    h_position = 0
    trees = 0
    v_position = 0

    while v_position <= (len(mapT) - 1):
        
        if(h_position >= h_length):
            h_position = h_position - h_length
     
        if(mapT[v_position][0][h_position] == '#') :
            trees += 1
        h_position += hIncrease
        v_position += vIncrease

    return trees
print(Trees(1,1) * Trees(3,1) *  Trees(5,1) * Trees(7,1) * Trees(1,2))
