import collections

def convertUnicodeDictToDict(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convertUnicodeDictToDict, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convertUnicodeDictToDict, data))
    else:
        return data
        
d = {
	u'key1':u'val1',
	u'key2':'val2',
  'key3':u'val3'
}        

print (convertUnicodeDictToDict(d))
#O/p: {'key3': 'val3', 'key2': 'val2', 'key1': 'val1'}
