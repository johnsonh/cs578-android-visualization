import json

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

class StringHelper(object):
	@staticmethod
	def dumpJSON(obj):
		return json.dumps(obj, indent=4, cls=ComplexEncoder)

	@staticmethod
	def stripQuotes(string):
		if string and string.startswith('"') and string.endswith('"'):
			return string[1:-1]
		return string

	def writeUNQUOTEDJsonField(key, value):
		return '"' + key + '": "' + value + '"'
