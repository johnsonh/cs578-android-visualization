import json

from CommonEqualityMixin import CommonEqualityMixin
from Component import Component
from Component import Filter
from Component import IntentFilterData
from Intent import Intent

from StringHelper import StringHelper

class Application(CommonEqualityMixin):

	def __init__(self, application, fromJson=False):
		if fromJson:
			self.__dict__ = json.loads(application)
			return

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
		actionList = set()
		for action in bsActions:
			actionList.add(action.string)
		return list(actionList)

	def getCategories(self, bsCategories):
		categoryList = set()
		for category in bsCategories:
			categoryList.add(category.string)
		return list(categoryList)

	def getData(self, bsData):
		dataList = []
		for data in bsData:
			myData = IntentFilterData(data.scheme.string, data.mimeType.string, data.host.string)
			dataList.append(myData)
		return dataList

	def transformIntents(self, bsIntents):
		myIntents = set()
		for intent in bsIntents:
			newIntent = Intent(intent.sender.string, intent.component.string, 
				StringHelper.stripQuotes(intent.action.string), 
				intent.dataType.string, intent.consumerMethod.string)
			myIntents.add(newIntent)
			# jsonified = json.dumps(newIntent.__dict__)
			# print(jsonified)
		return list(myIntents)
