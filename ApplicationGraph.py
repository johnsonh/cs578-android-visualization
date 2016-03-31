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

class ApplicationGraph(object):
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
			print(node.name)
			componentNodeSet.add(node)

		return componentNodeSet

	def determineConnections(self, componentNodeList):
		componentNameToIdxMap = self._getMap(componentNodeList)

		allLinks = []
		for application in self.applications:
			listOfLinks = self._findLinksFromApp(application, componentNameToIdxMap)
			allLinks.extend(listOfLinks)
		return allLinks

	def _findLinksFromApp(self, application, componentNameToIdxMap):
		print(application.name)
		links = []
		for intentDict in application.myIntents:
			explicitLink = self._getExplicitLink(intentDict, componentNameToIdxMap)
			if explicitLink:
				links.append(explicitLink)

			actionToComponentsThatReceiveMap = {}
			implicitLinks = self._getImplicitLinks(intentDict, componentNameToIdxMap, actionToComponentsThatReceiveMap)
			if implicitLinks:
				links.extend(implicitLinks)

		print(len(links))
		return list(set(links))

	def _getExplicitLink(self, intentDict, componentNameToIdxMap):
		if intentDict["sender"] in componentNameToIdxMap and intentDict["component"] in componentNameToIdxMap:
			return Link(intentDict, componentNameToIdxMap)

	def _getImplicitLinks(self, intentDict, componentNameToIdxMap, actionToComponentsThatReceiveMap):
		# TODOOOOOOOO
		pass

	"""
	{
		"consumerMethod": "startActivity",
		"component": "com.instagram.android.activity.MainTabActivity",
		"action": null
	}
	"""
	def __writeIntentAsLink(self, intentDict, componentNameToIdxMap):
		link = {}
		link["source"] = componentNameToIdxMap[intentDict["sender"]]
		link["target"] = componentNameToIdxMap[intentDict["component"]]

		link["consumerMethod"] = intentDict["consumerMethod"]
		link["action"] = intentDict["action"]
		return link

	def _getMap(self, componentNodeList):
		nameIdxMap = {}
		for idx, componentNode in enumerate(componentNodeList):
			if componentNode.name in nameIdxMap:
				print("A;SLDKJFLASKJDF;LKJDSF DUPLICATE COMPONENT NAMES!!!!")
				print(componentNode.name)
			else:
				nameIdxMap[componentNode.name] = idx
		return nameIdxMap



class Link(object):
	def __init__(self, intentDict, componentNameToIdxMap):
		self.source = componentNameToIdxMap[intentDict["sender"]]
		self.target = componentNameToIdxMap[intentDict["component"]]

		self.consumerMethod = intentDict["consumerMethod"]
		self.action = intentDict["action"]




















