import sys
import os
import json

from Application import Application

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


def main():
	checkCommandline()

	directory = sys.argv[1]
	applications = getApplications(directory)

	# readAndWriteApplication(appXmlName)
	

main()
