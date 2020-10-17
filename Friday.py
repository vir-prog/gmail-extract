import requests
import random
url = 'https://sidharthfridayassistant.pythonanywhere.com/api/all/?format=json'

r = requests.get(url)

data = r.json()

def do_task(task, line):
	q = line
	for work in task:
		if work == 'calculate':
			abc = 'abcdefghijklmnopqrstuvwxyz'
			for word in abc:
				q = q.replace(word, '')
			ans = eval(q)
			print(ans)
		if work == 'coronavirus':
			# use corona api
			print('coronavirus cases are on Ram\'s website')

def response(line):
	result = []
	tasks = []
	for values in data:
		valuesList = values['hotwords'].split('|')
		for hotword in valuesList:
			if hotword.lower() in line.lower():
				result.append(random.choice(values['responses'].split('|')))
				if values['tasks'] != None or '':
					tasks.append(values['tasks'])
	return result

while 1:
	line = input('You: ')
	print('friday: ', end='')
	for result in response(line):
		print(result)
