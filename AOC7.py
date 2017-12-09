with open("AOC7inputTest.txt") as f:
    realInput = f.read().splitlines()
print(realInput)

def getPrograms(data):
	rVal = {}
	for e in data:
		print(e.index("("))
		print(e.index(")"))
		print(e[e.index("(") + 1: e.index(")")])
		k = (e[0: e.index(" (")])
		v = (e[e.index("(") + 1: e.index(")")])
		rVal[k] = v
		#rVal.append(e[0: e.index(" (")])
	print(rVal)
	return rVal	

inStack = []

def getJustWords(data):
	rVal = []
	for e in data:
		#print(e.index(" ("))
		rVal.append(e[0: e.index(" (")])
	#print(rVal)
	return rVal	

def getInStack(data):
	rVal = {}
	tempList = []
	for e in data:
		if(e.find(">") != -1): 
			#print(e.index(">"))
			#print(e[e.rindex(">") + 2:].split(', '))
			tempList.append(e[e.rindex(">") + 2:].split(', '))
	rVal = [item for sublist in tempList for item in sublist]		
	#print(tempList)		
	#print(rVal)
	return rVal

def getGroupWeights(data, programs):
	rVal = {}
	tempList = []
	for e in data:
		if(e.find(">") != -1):
			name1 = e[0: e.index(" (")]
			tempList.append(e[e.rindex(">") + 2:].split(', '))
			
			for j in tempList:
				weight = 0
				for k in j:
					print(k)
					weight += int(programs.get(k))
				weight += int(programs.get(name1))
			print("Weight of " + name1 + ": " + str(weight))
			rVal[name1] = weight
	print("Group weights: " + str(rVal))
	return rVal

def findUnbalanced(realInput, groupWeigts, programs):
	rVal = []
	tempList = []
	for e in realInput:
		if(e.find(">") != -1): 
			#print(e.index(">"))
			#print(e[e.rindex(">") + 2:].split(', '))
			tempList.append(e[e.rindex(">") + 2:].split(', '))
			print("Temp List: " + str(tempList))
			tempWeights = []
			for i in tempList:
				tempWeights = []
				for j in i:
					print(j)
					tempWeights.append(int(programs.get(j)))
				if (len(set(tempWeights)) > 1):
					print("Mismatch set: " + str(j) + " - " + str(tempWeights))
	rVal = [item for sublist in tempList for item in sublist]





justWords = []
justWords = getJustWords(realInput)
programs = {}
programs = getPrograms(realInput)
inStack = {}
inStack = getInStack(realInput)
groupWeigts = {}
groupWeights = getGroupWeights(realInput, programs)
findUnbalanced(realInput, groupWeigts, programs)



print(justWords)
print(inStack)
print(list(set(justWords) - set(inStack)))