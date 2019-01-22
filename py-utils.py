import collections

# 1. Convert unicode dictionary key/value to string dictionary
def convertUnicodeDictToDict(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convertUnicodeDictToDict, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convertUnicodeDictToDict, data))
    else:
        return data
        
d = { u'key1':u'val1',u'key2':'val2','key3':u'val3'}        
print (convertUnicodeDictToDict(d)) #O/p: {'key3': 'val3', 'key2': 'val2', 'key1': 'val1'}


# 2. Replace string with another string throughout a file
def file_replace_string(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print ('"{old_string}" not found in {filename}.'.format(**locals()))
            return
    with open(filename, 'w') as f:
        print ('Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)
	
file_replace_string("test.txt","hello","world")	  #hello will be replaced with world where ever hello is present in the test.txt file
	
# 3. Find file in a path

def findFiles(path,search):
  for r,d,f in os.walk(path):
    for files in f:
      if search in files :
	print (os.path.join(r,files))
	
findFiles("D:\pyscripts","test.py") #prints the path within the directory D:\pyscripts if test.py exists


#4. Remove HTML tags from string
def removeHTMLtags(html_text):
    import re
    return re.sub(u'<[^<]+?>', u'\n', html_text) 

print (removeHTMLtags("<div>SirJayesh</div>")) #prints SirJayesh

#5 Check if url is Valid or Invalid
def is_valid_url(url):
    from urlparse import urlparse
	if not bool(urlparse(url).netloc):
        return False
    else:
        return True

print(is_valid_url("abc")) #returns False
print(is_valid_url("https://www.google.com")) #returns True

#6 Resize Excel Columns:
def resizeExcelColumns(fileName):
	import openpyxl
	from string import ascii_uppercase
	wb = openpyxl.load_workbook(filename = fileName)        
	worksheet = wb.active
	for col in worksheet.columns:
		 max_length = 0
		 column = col[0].column 
		 for cell in col:
			 try: 
				 if len(str(cell.value)) > max_length:
					 max_length = len(cell.value)
			 except:
				 pass
		 adjusted_width = (max_length + 2) * 1.2
		 worksheet.column_dimensions[column].width = adjusted_width
	wb.save(fileName)
	
#resizeExcelColumns("abc.xlsx")
