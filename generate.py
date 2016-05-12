import json
import random
import string

pokeapis = ['pokemon', 'move', 'location']

def setup(poems, pokemon):
	with open('lines.json', 'r') as f:
		poems = json.load(f)
	for api in pokeapis:
		with open( './' + api + '.json', 'r') as f:
			pokemon += json.load(f)
	return [poems, pokemon]


def generate():
	arrays = setup([], [])
	poems = arrays[0]
	pokemon = arrays[1]
	
	line = random.choice(poems)
	while not line.split():
		line = random.choice(poems)
	reversed = line.split()
	reversed.reverse()
	for word in reversed:
		start = word[:3].lower()
		similar = []
		
		# there's probably a data structure to do this faster
		for pokeword in pokemon:
			if pokeword.lower().startswith(start):
				similar.append(pokeword)
		
		if similar:
			return line.replace(word, random.choice(similar))

print generate()