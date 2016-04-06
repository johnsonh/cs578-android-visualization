# stuff
from bs4 import BeautifulSoup
import sys
import os

from StringHelper import StringHelper
from Application import Application

# python parser.py /Users/hsiehj/Documents/covert_dist/app_repo/johnsonapps/analysis/merged/

# BASE_DIR = "/Users/hsiehj/Documents/covert_dist/app_repo/johnsonapps/analysis/merged/"
WRITE_RELATIVE_DIR = "json/"

def checkCommandline():
	if os.path.isdir(sys.argv[1]):
		return True
	print("INVALID COMMAND LINE")
	return False

def readAndWriteApplication(directory, appXmlName):
	soup = BeautifulSoup(open(directory + appXmlName), "xml")
	application = Application(soup.find("application"))
	# print(application.name)

	print("-----")

	jsonified = StringHelper.dumpJSON(application)
	# print(jsonified)

	appName = os.path.splitext(appXmlName)[0]
	f = open(WRITE_RELATIVE_DIR + appName + ".json", 'w')
	f.write(jsonified)
	f.close()

def main():
	checkCommandline()

	directory = sys.argv[1]
	for file in os.listdir(directory):
		if file.endswith(".xml"):
			readAndWriteApplication(directory, file)
			# print(readAndWriteApplication(directory, file))

	# readAndWriteApplication(appXmlName)
	

main()











