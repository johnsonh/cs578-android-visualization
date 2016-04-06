from CommonEqualityMixin import CommonEqualityMixin

class Link(CommonEqualityMixin):
	def __init__(self, intentDict, targetName, componentNameToIdxMap):
		self.source = componentNameToIdxMap[intentDict["sender"]]
		# self.target = componentNameToIdxMap[intentDict["component"]]
		self.target = componentNameToIdxMap[targetName]

		self.consumerMethod = intentDict["consumerMethod"]
		self.action = intentDict["action"] # TODO: turn this into numeric value for different weighted lines?

	def reprJSON(self):	
		return dict(source=self.source, target=self.target, consumerMethod=self.consumerMethod, action=self.action) 

