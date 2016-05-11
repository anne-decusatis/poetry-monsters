import urllib3
import json
import string

def process_name(name):
	name_with_spaces = string.replace(name, '-', ' ')
	return string.capwords(name_with_spaces)

apis = ['pokemon', 'move', 'location']

http = urllib3.PoolManager()
for api in apis:
	filename = './' + api + '.json'
	url = 'http://pokeapi.co/api/v2/' + api + '/'
	r = http.request('GET', url)
	result = []
	data = json.loads(r.data)
	while data.get('next') and data.get('next') is not 'null':
		result += [process_name(x.get('name')) for x in data.get('results')]
		r = http.request('GET', data.get('next'))
		data = json.loads(r.data)
	
	with open(filename, 'w') as file:
		json.dump(result, file)
	
	
