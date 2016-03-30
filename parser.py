# stuff
from bs4 import BeautifulSoup
import sys
import os

from CommonEqualityMixin import CommonEqualityMixin
from Component import Component
from Component import Filter
from Component import IntentFilterData
from Intent import Intent
from StringHelper import StringHelper

# BASE_DIR = "/Users/hsiehj/Documents/covert_dist/app_repo/johnsonapps/analysis/merged/"
WRITE_RELATIVE_DIR = "json/"

def checkCommandline():
	if os.path.isdir(sys.argv[1]):
		return True
	print("INVALID COMMAND LINE")
	return False

class Application(CommonEqualityMixin):
	def __init__(self, application):
		self.name = application.find("name", recursive=False).string
		self.packageName = application.find("packageName").string

		self.myComponents = []
		bsComponents = application.find_all("Component")
		for bsComponent in bsComponents:
			myComponent = self.transformComponent(bsComponent)
			self.myComponents.append(myComponent)
			# print(StringHelper.dumpJSON(myComponent))

		bsIntents = application.find_all("Intent")
		self.myIntents = self.transformIntents(bsIntents)

	def reprJSON(self):	
		return dict(name=self.name, packageName=self.packageName, myComponents=self.myComponents, myIntents=self.myIntents) 


	def transformComponent(self, bsComponent):
		type = bsComponent.find("type").string
		name = bsComponent.find("name").string

		bsFilters = bsComponent.find_all("filter")
		myFilters = []
		for bsfilter in bsFilters:
			bsActions = bsfilter.find_all("actions")
			actionList = self.getActions(bsActions)

			bsCategories = bsfilter.find_all("categories")
			categoryList = self.getCategories(bsCategories)

			bsData = bsfilter.find_all("data")
			dataList = self.getData(bsData)

			filter = Filter(actionList, categoryList, dataList)
			myFilters.append(filter)

		return Component(type, name, myFilters)
		

	def getActions(self, bsActions):
		actionList = []
		for action in bsActions:
			actionList.append(action.string)
		return actionList

	def getCategories(self, bsCategories):
		categoryList = []
		for category in bsCategories:
			categoryList.append(category.string)
		return categoryList

	def getData(self, bsData):
		dataList = []
		for data in bsData:
			myData = IntentFilterData(data.scheme.string, data.mimeType.string, data.host.string)
			dataList.append(myData)
		return dataList

	def transformIntents(self, bsIntents):
		myIntents = set()
		for intent in bsIntents:
			newIntent = Intent(intent.sender.string, StringHelper.stripQuotes(intent.action.string), 
				intent.dataType.string, intent.consumerMethod.string)
			myIntents.add(newIntent)
			# jsonified = json.dumps(newIntent.__dict__)
			# print(jsonified)
		return list(myIntents)


def readAndWriteApplication(directory, appXmlName):
	soup = BeautifulSoup(open(directory + appXmlName), "xml")
	application = Application(soup.find("application"))
	# print(application.name)

	print("-----")

	jsonified = StringHelper.dumpJSON(application)
	print(jsonified)

	appName = os.path.splitext(appXmlName)[0]
	f = open(WRITE_RELATIVE_DIR + appName + ".json", 'w')
	f.write(jsonified)
	f.close()

def main():
	checkCommandline()

	directory = sys.argv[1]
	for file in os.listdir(directory):
		if file.endswith(".xml"):
			print(readAndWriteApplication(directory, file))

	# readAndWriteApplication(appXmlName)
	

main()












