inputT = []

with open('day7.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)
#print(inputT)

shinybag = []

bags_with_shiny = []

for r in inputT:
    text = r.split(' ')
    rule = [x for x in text[2:]]
    bag = text[:2]
    #print(bag, rule)
    for i in range(len(rule)):
        #print(word)
        if(rule[i] == 'shiny' and rule[i + 1] == 'gold'):
            bags_with_shiny.append([bag[0] , bag[1]])

    if (bag[0] == 'shiny' and bag[1]== 'gold'):
        shinybag = rule
#print(bags_with_shiny)
#print(shinybag)


amounts = []
colors = []
for i in range(len(shinybag)):
    
    try:
        amounts.append(int(shinybag[i]))
        colors.append([shinybag[i + 1], shinybag[i + 2]])
    except ValueError:
        pass
print(amounts)
print(colors)
print(list(zip(amounts, colors)))
colors2 = [[] for c in colors]
amounts2 = [[] for a in amounts]

for r in inputT:
    text = r.split(' ')
    rule = [x for x in text[2:]]
    bag = text[:2]
    if(bag in colors):
        index = colors.index(bag)
        shinybag = list(rule)
        for i in range(len(shinybag)):    
            try:
                amount = int(shinybag[i])                           
                new_color = [shinybag[i + 1], shinybag[i + 2]]
                if(new_color not in colors):
                    amounts2[index].append(int(shinybag[i]))
                    colors2[index].append([shinybag[i + 1], shinybag[i + 2]])                                
            except ValueError:
                pass

 
print(colors2)
print(amounts)

"""
for i in range(2):
    for r in inputT:
        text = r.split(' ')
        rule = [x for x in text[2:]]
        bag = text[:2]
        #new_colors = []
        for color in colors:
            if (bag[0] == color[0] and bag[1]== color[1]):
                shinybag = list(rule)
                for i in range(len(shinybag)):    
                    try:
                        amount = int(shinybag[i])                           
                        new_color = [shinybag[i + 1], shinybag[i + 2]]
                        if(new_color not in colors):
                            amounts.append(int(shinybag[i]))
                            colors.append([shinybag[i + 1], shinybag[i + 2]])                                
                    except ValueError:
                        pass
        #colors += new_colors
        print(colors)
    print(amounts)
    print(sum(amounts))
    #print(colors)
"""
#def findAmount(shinybag):
    
    
    
        
#findAmount(shinybag)

def findAll(n):
    #containing_shiny = list(rules_with_shiny)
    x = True
    i = 0
    while x:
        for r in inputT:
            text = r.split(' ')
            rule = [x for x in text[2:]]
            bag = text[:2]
            #print(bag, rule)
            for i in range(len(rule)):
                for shinybag in bags_with_shiny:
                #print(word)
                    if(rule[i] == shinybag[0] and rule[i + 1] == shinybag[1]):
                        color = [bag[0] , bag[1]]
                        if(color not in bags_with_shiny):
                            bags_with_shiny.append([bag[0] , bag[1]])

        print(len(bags_with_shiny))
        i += 1
        if(i == n):
            x = False
#findAll(1)
        