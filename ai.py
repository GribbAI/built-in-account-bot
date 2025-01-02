import requests, json, os


def gpt(text, history, promt="", memory=False):
	if os.path.isfile(f'memory/{history}.json'):
		with open(f'memory/{history}.json', 'r') as file:
			context = json.load(file)
	else:
		with open(f'memory/{history}.json', 'w') as file:
			json.dump([], file)
		with open(f'memory/{history}.json', 'r') as file:
			context = json.load(file)
	
	if memory:
		if not context:
			table = {"role": "user", "content": promt + text}
			context.append(table)
			res = requests.post('http://api.onlysq.ru/ai/v1', json=context)
		else:
			table = {"role": "user", "content": text}
			context.append(table)
			res = requests.post('http://api.onlysq.ru/ai/v1', json=context)
		
		context.append({"role": "assistant", "content": res.json()['answer']})
		with open(f'memory/{history}.json', 'w') as file:
			json.dump(context, file)
	else:
		table = [{"role": "user", "content": promt + text}]
		res = requests.post('http://api.onlysq.ru/ai/v1', json=table)
	
	response = res.json()
	return response['answer']
