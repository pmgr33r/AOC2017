import operator
with open("AOC8input.txt") as f:
    realInput = f.read().splitlines()
finalSet = {}
maxTop = 0

for line in realInput:
	regBegin = line.find(" ")
	oper = line[regBegin +1 : regBegin+3]
	reg = line[0: regBegin]	
	finalSet[reg] = 0
print(finalSet)

for line in realInput:
	lineAsList = line.split()
	print(lineAsList)
	print("Line as List 0: " + str(lineAsList[0]))
	print("Line as List 1: " + str(lineAsList[1]))
	print("Line as List 2: " + str(lineAsList[2]))
	print("Line as List 3: " + str(lineAsList[3]))
	print("Line as List 4: " + str(lineAsList[4]))
	print("Line as List 5: " + str(lineAsList[5]))
	print("Line as List 6: " + str(lineAsList[6]))
	print(finalSet[lineAsList[0]])
	if (lineAsList[5] == '>'):
		if(finalSet[lineAsList[4]] > int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	if (lineAsList[5] == '<'):
		if(finalSet[lineAsList[4]] < int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	if (lineAsList[5] == '>='):
		if(finalSet[lineAsList[4]] >= int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	if (lineAsList[5] == '<='):
		if(finalSet[lineAsList[4]] <= int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	if (lineAsList[5] == '=='):
		if(finalSet[lineAsList[4]] == int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	if (lineAsList[5] == '!='):
		if(finalSet[lineAsList[4]] != int(lineAsList[6])):
			if (lineAsList[1] == 'inc'):
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] + int(lineAsList[2])
			else:
				finalSet[lineAsList[0]] = finalSet[lineAsList[0]] - int(lineAsList[2])
	top = finalSet[max(finalSet, key=finalSet.get)]
	print("Top : " + str(top) + " vs maxTop : " + str(maxTop))
	if (top > maxTop):
		maxTop = top
print(finalSet)


top = max(finalSet, key=finalSet.get)
print("-----> Final Answer: " + str(finalSet[top]))
print(maxTop)