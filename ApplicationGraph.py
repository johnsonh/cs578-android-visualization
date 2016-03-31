"""
{
	"componentName": "com.instagram.android.nux.ao"
	"parentApp": "Instagram"
	"edges": [
		{
			"consumerMethod": "startActivity",
			"component": "com.instagram.android.activity.MainTabActivity",
			"action": null
		},
		{
			"consumerMethod": "startActivity", 
			"component": null
			"action": "android.intent.action.VIEW"
		},
		{
			"consumerMethod": "startActivity",
			"component": "com.twitter.android.PostActivity",
			"action": "com.twitter.android.post.status",
		}
	]
}

{
  "dataType": "null",
  "consumerMethod": "startActivity",
  "component": "com.twitter.android.PostActivity",
  "action": "com.twitter.android.post.status",
  "sender": "com.twitter.android.BaseActivity"
}
"""

import json

from ComponentNode import ComponentNode

class ApplicationGraph(object):
	def __init__(self, applications):
		self.applications = applications


	def getAllComponents(self, componentNodeSet):
		for application in self.applications:
			appNodes = self.getComponentsForApp(application)
			componentNodeSet.update(appNodes)

		return componentNodeSet

	def getComponentsForApp(self, application):
		componentNodeSet = set()

		components = application.myComponents
		for componentDict in components:
			node = ComponentNode(componentDict, application.name)
			componentNodeSet.add(component)

		return componentNodeSet

	def determineConnectionsBetweenInternalComponents(self, componentNodeSet):
		intents = self.application.myIntents
		for intent in intents:
			if intent["component"] and intent["action"]:
				print(intent)























