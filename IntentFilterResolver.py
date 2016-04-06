
from multi_key_dict import multi_key_dict
from Component import IntentFilterData

class IntentFilterResolver(object):

	def __init__(self, nodelist):
		self.nodelist = nodelist

	# inefficient but i just need it to work, this should be backed by multi_key_dicts
	def getImplicitReceiversOfIntent(self, inputAction, inputData):
		receivers = []
		for node in self.nodelist:
			# print node.name
			for filt in node.filters:
				if inputAction in filt['actions']:
					if not filt['data'] or inputData in filt['data']:
						receivers.append(node.name)
						break
		return receivers


		"""
		can't get this to work right now...
		print"yayayay"
		self.actionDict = multi_key_dict()
		for node in nodelist:
			for filt in node.filters:
				actionList = filt['actions'] 
				print filt
				if filt['actions'] not in self.actionDict:
					dataMap = self.makeDataMap(filt['data'], node.name)
					self.actionDict[actionList] = dataMap
					# print node.filters
					pass
		# k[1000, 'kilo', 'k'] = 'kilo (x1000)'
		"""

	"""
	"data": [
        {
            "mimeType": null, 
            "host": "evernote.com", 
            "scheme": "https"
        }, 
        {
            "mimeType": null, 
            "host": "www.evernote.com", 
            "scheme": "https"
        }, 
        {
            "mimeType": null, 
            "host": "stage.evernote.com", 
            "scheme": "https"
        }, nL
        {
            "mimeType": null, 
            "host": "www.stage.evernote.com", 
            "scheme": "https"
        }
    ], 
    # Come back if i can
	def makeDataMap(self, dataList, componentName):
		dataDict = multi_key_dict()
		dataObjList = [None]
		for data in dataList:
			dataObjList.append(IntentFilterData(data['scheme'], data['mimeType'], data['host']))
		print dataObjList
		dataDict[dataObjList] = componentName
		return dataDict
	"""














