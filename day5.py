inputT = []

with open('day5.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)

def seatcheck():
    index = 0
    passenger_rows = ['' for i in range(len(inputT))]
    passenger_cols = ['' for i in range(len(inputT))]
    for seatcode in inputT:
        rows = [i for i in range(128)]
        columns = [i for i in range(8)]
        r = 128
        lower = 0
        c = 8
        lowerc = 0
        for i in range(len(seatcode[:7])):
            if(seatcode[i] == 'F'):
                rows = rows[:int((r/2))]
            else:
                lower = int((r/2))
                rows = rows[lower:]
            r = int(r/2)
        seatcode = seatcode[7:]
        for i in range(len(seatcode)):
            
            if(seatcode[i] == 'L'):
                columns = columns[:int((c/2))]
            else:
                lowerc = int((c/2))
                columns = columns[lowerc:]
            c = int(c/2)
        passenger_rows[index] += str(rows[0])
        passenger_cols[index] += str(columns[0])
        index += 1

    return passenger_rows, passenger_cols

def checkID():
    rowcols = seatcheck()
    prows = rowcols[0]
    pcols = rowcols[1]
    
    ids = [0 for i in range(len(prows))]
    for i in range(len(pcols)):
        ids[i] += ((int(prows[i]) * 8) + int(pcols[i]))
    return ids
#print(max(checkID()))

Ids = checkID()
Ids.sort()
def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst] 
print(find_missing(Ids))