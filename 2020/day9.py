inputT = []

with open('day9.txt', 'r', encoding='utf-8') as var:
    for line in var:
        line = line.rstrip()
        inputT.append(line)
nums = inputT.copy()

def findMismatch():
    match = True
    num = 0
    while match:
        preamble = nums[:25]
        sums = []
        for i in range(len(preamble)):
            for j in range(len(preamble)):
                sums.append(int(preamble[i]) + int(preamble[j]))

        if(int(nums[25]) not in sums):
            num = int(nums[25])
            match = False
        else:
            nums.pop(0)
    return num

def findSum4Mismatch():
    mismatch = findMismatch()
    foundSum = False
    start = 0
    index = 0
    while (foundSum == False):
        currentSum = 0
        while currentSum < mismatch:
            num = int(inputT[index])
            currentSum += num
            
            if(currentSum == mismatch):
                contiguousList = [int(n) for n in inputT[start:index + 1]]
                print(sum(contiguousList))
                foundSum = True
            index += 1
        start += 1
        index = start
    minimum = min(contiguousList)
    maximum = max(contiguousList)
    weakness = minimum + maximum
    print(weakness)
findSum4Mismatch()

            

            

        

    





