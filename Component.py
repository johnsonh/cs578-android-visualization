from CommonEqualityMixin import CommonEqualityMixin

class Component(CommonEqualityMixin):
	def __init__(self, type, name, requiredPermissions, filters):
		self.type = type
		self.name = name
		self.requiredPermissions = requiredPermissions
		self.filters = filters

	def reprJSON(self):	
		return dict(type=self.type, name=self.name, requiredPermissions=self.requiredPermissions, filters=self.filters) 

class Filter(CommonEqualityMixin):
	def __init__(self, actions, categories, data):
		self.actions = actions
		self.categories = categories
		self.data = data

	def reprJSON(self):	
		return dict(actions=self.actions, categories=self.categories, data=self.data) 

"""
<Intent>
    <calledAt>com.instagram.android.activity.SimpleWebViewActivity: void a(android.content.Context,java.lang.String,boolean,java.lang.String)</calledAt>
    <sender>com.instagram.android.activity.SimpleWebViewActivity</sender>
    <component>com.instagram.android.activity.SimpleWebViewActivity</component>
    <action></action>
    <dataType></dataType>
    <scheme></scheme>
    <extra>true</extra>
    <sensitiveData>false</sensitiveData>
    <consumerMethod>startActivity</consumerMethod>
    <id>3k220l34otl7ngec3lime7bef3</id>
    <random/>
</Intent>

Not sure why there's nothing about category here... 
"""
class IntentFilterData(CommonEqualityMixin):
	def __init__(self, scheme, mimeType, host):
		self.scheme = scheme
		self.mimeType = mimeType
		self.host = host

	def reprJSON(self):
		return dict(scheme=self.scheme, mimeType=self.mimeType, host=self.host) 