#advent of code day 4
#Camp cleanup by elves pairups
#? In how many assignment pairs does one range fully contain the other?

import pandas as pd

#? Outcome values dictionaries
def expand_range(list_ranges:list):
    elf1 = [c.split('-') for c in list_ranges]
    elf1_ranges = [[i for i in range(int(r[1]) - int(r[0]))] for r in elf1]
    elf1_ranges = [e + [e[-1] +1] if e != [] else [0] for e in elf1_ranges]

    elf1 = [[int(elf1[i][0]) + rg  for rg in elf1_ranges[i]] for i in range(len(elf1))]

    return elf1


#? strategy guide input
path = 'C:/Users/Diegob/Documents/pythonSnippets/AOC/AdventOfCode2020/2022/aoc_input_day4.txt' #AOC input txt
camp_cleanup_df = pd.read_csv(path, header=None, sep=',' )
camp_cleanup_df = camp_cleanup_df.set_axis(['Elf1', 'Elf2'], axis=1)
#print(camp_cleanup_df)

elf1 = camp_cleanup_df['Elf1'].values.tolist()
elf2 = camp_cleanup_df['Elf2'].values.tolist()

elf1_expanded = expand_range(elf1)
elf2_expanded = expand_range(elf2)

one_contains = [False for pair in elf1]
overlapped = [False for pair in elf1]
for i in range(len(elf1_expanded)):
    #if pair 1 fully contains pair 2 or if pair 2 fully contains pair 1
    if(all(ele in elf1_expanded[i] for ele in elf2_expanded[i]) or all(ele in elf2_expanded[i] for ele in elf1_expanded[i])):
        one_contains[i] = True

    #if pair 1 overlaps with pair 2 or if pair 2 overlaps with pair 1
    if(any(ele in elf1_expanded[i] for ele in elf2_expanded[i]) or any(ele in elf2_expanded[i] for ele in elf1_expanded[i])):
        overlapped[i] = True

camp_cleanup_df['FullyContained'] = one_contains
camp_cleanup_df['Overlapped'] = overlapped
#print(camp_cleanup_df)

print('Fully contained')
print(camp_cleanup_df[camp_cleanup_df['FullyContained'] == True].shape)
print('Overlapped')
print(camp_cleanup_df[camp_cleanup_df['Overlapped'] == True].shape)
    