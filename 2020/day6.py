inputT = []

with open('day6.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)
#print(inputT)
missing_set = ['squmrdowjy', 'iusrcmzyodh', 'rnlsdmxuyefoz']
last = 0
index = 0
groups = [[]]
for i in range(len(inputT)):
    if(inputT[i] == ''):
        groups[index].append(inputT[last:i])
        groups.append([])
        last = i + 1
        index += 1
groups.pop(-1)
groups.append([missing_set])
#print(groups)

def anyone():
    sets = []
    for g in groups:
        gset = set()
        for word in g[0]:
            for i in range(len(word)):
                gset.add(word[i])
        u_list = list(gset)
        sets.append(u_list)
    #print(sets)

    sums = 0
    for i in range(len(sets)):
        #print(groups[i], sets[i], len(sets[i]))
        sums += len(sets[i])
    print(sums)

def everyone():
    shared = []
    people_per_group = []
    for j in range(len(groups)):
        letters = []
        people_per_group.append(len(groups[j][0]))
        for word in groups[j][0]:
            for i in range(len(word)):
                letters.append(word[i])
        letters2 = set()
        for i in range(len(letters)):
            if(letters.count(letters[i]) == people_per_group[j]):
                letters2.add(letters[i])
                #letters.pop(ind)
        shared.append(letters2)
    print(shared)

    sums = 0
    for i in range(len(shared)):
        #print(groups[i], sets[i], len(sets[i]))
        sums += len(shared[i])
    print(sums)
everyone()
