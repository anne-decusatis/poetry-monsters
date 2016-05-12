import urllib3
import json
import urllib

POEMS = './poems.txt'
OUTPUT = './lines.json'

http = urllib3.PoolManager()

success = 0
fail = 0

result = []
with open(POEMS, 'r') as poemf:
	for poem in poemf.readlines():
		url = 'http://poetrydb.org/title/' + urllib.quote(poem.strip()) + '/lines.json'
		print url
		r = http.request('GET', url)
		try:
			data = json.loads(r.data)
			result += [x for x in data[0].get('lines')]
			success = success + 1
		except:
			print "error on " + poem
			fail = fail + 1
	
with open(OUTPUT, 'w') as file:
	json.dump(result, file)

print "Success: " + str(success)
print "Fail: " + str(fail)
	
