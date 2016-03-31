from CommonEqualityMixin import CommonEqualityMixin
from Component import Component

class ComponentNode(CommonEqualityMixin):
	def __init__(self, componentDict, parentApp):
		self.type = componentDict["type"]
		self.name = componentDict["name"]
		self.filters = componentDict["filters"]
		self.parentApp = parentApp


	def reprJSON(self):	
		return dict(type=self.type, name=self.name, filter=self.filters, parentApp=self.parentApp) 