import copy

with open("AOC5input.txt") as f:
    realInput = f.read().splitlines()
numbers = [int(e.strip()) for e in realInput]
#print(realInput)
#print(numbers)
#inputList = [0, 3, 0, 1, -3]
inputList = numbers

currentIndex = 0
endOfList = len(inputList)
i = 0
count = 0
#print "End: " #+ str(end)

modList = copy.copy(inputList)
print ('End of List: ' + str(endOfList))
print ('Running.......')
while ((currentIndex < endOfList)):
    prevIndex = currentIndex
    currentIndex = currentIndex + modList[currentIndex]
    if (modList[prevIndex] >= 3):
        modList[prevIndex] -= 1
    else:
        modList[prevIndex] += 1
    #print ("modList: " + str(modList))
    i += 1
    count += 1

print(count)
