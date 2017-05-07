import os
pathToNodeDirectories = "/home/rylangrayston/Desktop/nodeChecker/nodeFiles/"

nodesInSpreadSheet = []
with open( "/home/rylangrayston/Desktop/nodeChecker/nodes.csv") as f:
	for line in f.readlines():
		print line.strip()
		nodesInSpreadSheet.append(line.strip())

nodeDirectories = os.listDir(pathToNodeDirectories)


