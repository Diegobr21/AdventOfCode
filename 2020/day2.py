readlist = []

with open('day2.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        readlist.append(line)

policies = [[] for i in range(len(readlist))]

c = 0
for x in readlist:
    policies[c].append(x.split())
    c += 1

amount = []
letter = []
password = []

for i in range(len(policies)):
    amount.append(policies[i][0][0])
    letter.append(policies[i][0][1])
    password.append(policies[i][0][2])

amountNum = []
for a in amount:
    x = a.split('-')
    amountNum.append(x)

letterLook = []
for a in letter:
    x = a.replace(':', '')
    letterLook.append(x)

def Part1():

    invalid_pssds = 0
    valid_pssds = 0
    for i in range(len(password)):
        l = letterLook[i]
        minamount = int(amountNum[i][0])
        maxamount = int(amountNum[i][1])
        p = password[i]
        c = 0
        for j in range(len(p)):
            if(p[j] == l):
                c += 1
        if((c < minamount) or (c > maxamount)):
            invalid_pssds += 1

    valid_pssds = len(password) - invalid_pssds
    print('Amount of valid passwords in part 1: ', valid_pssds)

    return valid_pssds

def Part2():

    invalid_pssds = 0
    valid_pssds = 0
    for i in range(len(password)):
        l = letterLook[i]
        firstPosition = (int(amountNum[i][0]) - 1)
        secondPosition = (int(amountNum[i][1]) - 1)
        p = password[i]
        c = 0
        if p[firstPosition] == l:
            c += 1
        if p[secondPosition] == l:
            c += 1
        if (c!= 1):
            invalid_pssds +=1

        

    valid_pssds = len(password) - invalid_pssds
    print('Amount of valid passwords in part 2: ',valid_pssds)

    return valid_pssds

Part1()
Part2()