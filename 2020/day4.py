import re
inputT = []

with open('day4.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)

passports = []
passports.append([])
index = 0
last = 0
for i in range(len(inputT)):
    if(inputT[i] == ''):
        passports[index].append(inputT[last:i])
        passports.append([])
        last = i + 1
        index += 1
passports.pop(-1)

passports2 = [[] for p in passports]
for i in range(len(passports)):
    txt = []
    for j in passports[i][0]:
        txt += j.split(' ')
    for e in txt:
        passports2[i].append(e)

Birth_Year = 'byr:'
Issue_Year = 'iyr:'
Expiration_Year = 'eyr:'
Height = 'hgt:'
Hair_Color = 'hcl:'
Eye_Color = 'ecl:'
Passport_ID = 'pid:'

byr = [1920, 2002]
iyr = [2010, 2020]
eyr = [2020, 2030]
hcolor = re.compile('^#[a-z0-9A-Z]+')
eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
heights = ['cm', 'in']
heightcm = [150, 193]
heightin = [59, 76]

semivalid = []
valid_passports = 0
for passport in passports2:
    validators = 0
    if(len(passport) >= 0):
        for field in passport:
            if(Birth_Year in field):
                s = int(field[4:])
                if(s >= byr[0] and s <= byr[1]):
                    validators += 1
                    passport.pop((passport.index(field)))
        for field in passport:
            if(Issue_Year in field):
                s = int(field[4:])
                if(s >= iyr[0] and s <= iyr[1]):
                    validators += 1
                    passport.pop((passport.index(field)))
        for field in passport:
            if(Expiration_Year in field):
                s = int(field[4:])
                if(s >= eyr[0] and s <= eyr[1]):
                    validators += 1
                    passport.pop((passport.index(field)))
        for field in passport:
            if(Height in field):
                s = (field[4:])
                if('cm' in s):
                    n = int(s[:-2])
                    if(n >= heightcm[0] and n <= heightcm[1]):
                        validators += 1
                        passport.pop((passport.index(field)))
                elif('in' in s):
                    n = int(s[:-2])
                    if(n >= heightin[0] and n <= heightin[1]):
                        validators += 1
                        passport.pop((passport.index(field)))
        for field in passport:
            if(Hair_Color in field):
                s = (field[4:])
                if(hcolor.match(s) != None):
                    validators += 1
                    passport.pop((passport.index(field)))
        for field in passport:
            if(Eye_Color in field):
                s = (field[4:])
                if(s in eyecolors):
                    validators += 1
                    passport.pop((passport.index(field)))
        for field in passport:
            if(Passport_ID in field):
                s = (field[4:])
                if(len(s) == 9):
                    validators += 1
                    passport.pop((passport.index(field)))
        print(passport)
    
    if(validators == 7):
        valid_passports += 1
print(valid_passports)
