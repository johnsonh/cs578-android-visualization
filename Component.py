from CommonEqualityMixin import CommonEqualityMixin

class Component(CommonEqualityMixin):
	def __init__(self, type, name, filters):
		self.type = type
		self.name = name
		self.filters = filters

	def reprJSON(self):	
		return dict(type=self.type, name=self.name, filters=self.filters) 

class Filter(CommonEqualityMixin):
	def __init__(self, actions, categories, data):
		self.actions = actions
		self.categories = categories
		self.data = data

	def reprJSON(self):	
		return dict(actions=self.actions, categories=self.categories, data=self.data) 

class IntentFilterData(CommonEqualityMixin):
	def __init__(self, scheme, mimeType, host):
		self.scheme = scheme
		self.mimeType = mimeType
		self.host = host

	def reprJSON(self):
		return dict(scheme=self.scheme, mimeType=self.mimeType, host=self.host) 