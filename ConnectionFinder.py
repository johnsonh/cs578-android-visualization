import sys
import os
import json

from StringHelper import StringHelper
from Application import Application
from ApplicationGraph import ApplicationGraph

# python ConnectionFinder.py /Users/hsiehj/Documents/covert_dist/python/json-good

def checkCommandline():
	if os.path.isdir(sys.argv[1]):
		return True
	print("INVALID COMMAND LINE")
	return False

def getApplications(directory):
	applications = []
	for file in os.listdir(directory):
		if file.endswith(".json"):
			with open(directory + "/" + file, 'r') as myfile:
				jsonApplication = myfile.read()
				# print(jsonApplication)
				application = Application(jsonApplication, True)
				applications.append(application)
				# print(application)
	return applications

def writeToJson(objectList, fileName):
	jsonified = StringHelper.dumpJSON(objectList)
	print(jsonified)

	f = open(fileName, 'w')
	f.write(jsonified)
	f.close()


def main():
	checkCommandline()

	directory = sys.argv[1]
	applications = getApplications(directory)

	print("num applications = ")
	print(len(applications))

	graph = ApplicationGraph(applications)

	nodesList = graph.getAllComponents()
	print("num nodes = ")
	print(len(nodesList))

	links = graph.determineConnections(nodesList)
	print("num links = ")
	print(len(links))
	
	writeToJson(nodesList, "nodes.json")
	writeToJson(links, "links.json")


main()
















