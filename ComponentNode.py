class ComponentNode(object):
	def __init__(self, componentDict, parentApp):
		self.type = componentDict["type"]
		self.name = componentDict["name"]
		self.requiredPermissions = componentDict['requiredPermissions']
		self.filters = componentDict["filters"]
		self.parentApp = parentApp

	def reprJSON(self):	
		return dict(type=self.type, name=self.name, requiredPermissions=self.requiredPermissions, filter=self.filters, parentApp=self.parentApp) 

	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.name == other.name)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash((self.name))
