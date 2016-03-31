from CommonEqualityMixin import CommonEqualityMixin

class Intent(CommonEqualityMixin):
	def __init__(self, sender, component, action, dataType, consumerMethod):
		self.sender = sender
		self.component = component
		self.action = action
		self.dataType = dataType
		self.consumerMethod = consumerMethod

	def reprJSON(self):
		return dict(sender=self.sender, component=self.component, action=self.action, dataType=self.dataType, consumerMethod=self.consumerMethod) 

	def __hash__(self):
		return hash((self.sender, self.component, self.action, self.dataType, self.consumerMethod))