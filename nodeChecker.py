import os
import pyttsx
import time
engine = pyttsx.init()

while True:

	pathToNodeDirectories = "/home/rylangrayston/git/diasNodeChecker/testNodeData/"

	nodesInSpreadSheet = []
	with open("/home/rylangrayston/git/diasNodeChecker/test.csv") as f:
		for line in f.readlines():
			#print line.strip()
			nodesInSpreadSheet.append(line.strip())

	nodeDirectories = os.listdir(pathToNodeDirectories)
	#print nodeDirectories

	for node in nodesInSpreadSheet:
		if node not in nodeDirectories:
			print node
			engine.say(node[0])
			engine.runAndWait()
			engine.say(node[1])
			engine.runAndWait()
			time.sleep(2)

