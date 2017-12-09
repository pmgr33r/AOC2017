import re

test6 = "{{{}}}"
test5 = "{{},{}}"
test16= "{{{},{},{{}}}}"
test1a = "{<{},{},{{}}>}"
test9 = "<{o\"i!a,<{i<a>"
test9a= "{{<a>},{<a>},{<a>},{<a>}}"
test3 = "{{<!>},{<!>},{<!>},{<a>}}"

with open("AOC9input.txt") as f:
    realInput = f.read()

def removeBang(data):
	newData = re.sub(r"!.", "", data)
	#print(newData)
	return(newData)

def countGarbage(data):
	garbageChars = re.findall("<(.*?)>", data)
	print(garbageChars)
	count = 0
	for g in garbageChars:
		count += len(g)
	return count

def removeGarbage(data):
	newData = re.sub(r"<.*?>", "", data)
	#print(newData)
	return(newData)

def countGroups(data):
	score = 0
	finalScore = 0
	for c in data:
		if c == '{':
			score += 1
		if c == '}':
			finalScore += score
			score -= 1
	print("Final Score = " + str(finalScore))


removeGarbage(test9a)

countGroups(removeGarbage(removeBang(test9a)))

print(countGarbage(removeBang(realInput)))
