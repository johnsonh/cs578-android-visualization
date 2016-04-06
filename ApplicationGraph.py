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

var nodes = [
    { x:   width/3, y: height/2 },
    { x: 2*width/3, y: height/2 }
];

// The `links` array contains objects with a `source` and a `target`
// property. The values of those properties are the indices in
// the `nodes` array of the two endpoints of the link.

var links = [
    { source: 0, target: 1 }
];

"""

import json

from ComponentNode import ComponentNode
from Link import Link
from IntentFilterResolver import IntentFilterResolver

class ApplicationGraph(object):
	actionToComponentsThatReceiveMap = {}

	def __init__(self, applications):
		self.applications = applications


	def getAllComponents(self):
		componentNodeSet = set()
		for application in self.applications:
			appNodes = self._getComponentsForApp(application)
			componentNodeSet.update(appNodes)

		return list(componentNodeSet)

	def _getComponentsForApp(self, application):
		componentNodeSet = set()

		for componentDict in application.myComponents:
			node = ComponentNode(componentDict, application.name)
			# print(node.name)
			componentNodeSet.add(node)

		return componentNodeSet

	def determineConnections(self, componentNodeList):
		componentNameToIdxMap = self._getComponentNameToIdxMap(componentNodeList)
		intentFilterResolver = IntentFilterResolver(componentNodeList)

		allLinks = []
		for application in self.applications:
			listOfLinks = self._findLinksFromApp(application, intentFilterResolver, componentNameToIdxMap)
			allLinks.extend(listOfLinks)
		return allLinks

	def _findLinksFromApp(self, application, intentFilterResolver, componentNameToIdxMap):
		print(application.name + "!!!!!!")
		links = []
		for intentDict in application.myIntents:
			if intentDict['sender'] not in componentNameToIdxMap:
				continue
			# print(intentDict)
			explicitLink = self._getExplicitComponentIntent(intentDict, componentNameToIdxMap)
			if explicitLink:
				links.append(explicitLink)

			# explicitActionLinks = self._getExplicitActionIntent(intentDict, intentFilterResolver, componentNameToIdxMap)
			# if explicitActionLinks:
			# 	links.extend(explicitActionLinks)

			implicitLinks = self._getImplicitIntent(intentDict, intentFilterResolver, 
				componentNameToIdxMap, ApplicationGraph.actionToComponentsThatReceiveMap)
			if implicitLinks:
				links.extend(implicitLinks)

		print(len(links))
		return list(set(links))

	def _getExplicitComponentIntent(self, intentDict, componentNameToIdxMap):
		if intentDict["sender"] in componentNameToIdxMap and intentDict["component"] in componentNameToIdxMap:
			return Link(intentDict, intentDict["component"], componentNameToIdxMap)

	# def _getExplicitActionIntent(self, intentDict, intentFilterResolver, componentNameToIdxMap):
	# 	# TODOOOOOOOO
	# 	if intentDict['action']:
	# 		# print intentDict['action']
	# 		pass
		

	def _getImplicitIntent(self, intentDict, intentFilterResolver, componentNameToIdxMap, actionToComponentsThatReceiveMap):
		# no category.... 
		receivers = intentFilterResolver.getImplicitReceiversOfIntent(intentDict['action'], intentDict['dataType'])
		results =[]
		for receiver in receivers:
			# if receiver in componentNameToIdxMap:
			results.append(Link(intentDict, receiver, componentNameToIdxMap))
		return results

	def _getComponentNameToIdxMap(self, componentNodeList):
		nameIdxMap = {}
		for idx, componentNode in enumerate(componentNodeList):
			if componentNode.name in nameIdxMap:
				print("A;SLDKJFLASKJDF;LKJDSF DUPLICATE COMPONENT NAMES!!!!")
				print(componentNode.name)
			else:
				nameIdxMap[componentNode.name] = idx
		return nameIdxMap

	"""
	{
        "data": [], 
        "categories": [], 
        "actions": [
            "com.evernote.action.SDCARD_CHANGED", 
            "com.evernote.action.SYNC_ERROR", 
            "com.evernote.action.DB_OPEN_CREATION_FAILED", 
            "com.evernote.action.SYNC_DONE", 
            "com.evernote.action.DB_CORRUPTED", 
            "com.evernote.action.SYNC_STARTED", 
            "com.evernote.action.DB_READ_ONLY", 
            "com.evernote.action.SAVE_NOTE_DONE"
        ]
    }
	"""
	def _getReceivedActionsToComponentNameMap(self, componentNodeList):
		# print("component name: " + componentNodeList[0].filters[0])
		pass

	"""
	{
		"consumerMethod": "startActivity",
		"component": "com.instagram.android.activity.MainTabActivity",
		"action": null
	}
	UNUSED
	"""
	def __writeIntentAsLink(self, intentDict, componentNameToIdxMap):
		link = {}
		link["source"] = componentNameToIdxMap[intentDict["sender"]]
		link["target"] = componentNameToIdxMap[intentDict["component"]]

		link["consumerMethod"] = intentDict["consumerMethod"]
		link["action"] = intentDict["action"]
		return link



















