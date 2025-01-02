import requests, json, os


def gpt(text, promt="", history=None, memory=False):
	if memory:
		if os.path.isfile(f'memory/{history}.json'):
			with open(f'memory/{history}.json', 'r', encoding='utf-8') as file:
				context = json.load(file)
		else:
			with open(f'memory/{history}.json', 'w', encoding='utf-8') as file:
				json.dump([], file)
			with open(f'memory/{history}.json', 'r', encoding='utf-8') as file:
				context = json.load(file)
		
		if not context:
			table = {"role": "user", "content": promt + text}
			context.append(table)
			res = requests.post('http://api.onlysq.ru/ai/v1', json=context)
		else:
			table = {"role": "user", "content": text}
			context.append(table)
			res = requests.post('http://api.onlysq.ru/ai/v1', json=context)
		
		context.append({"role": "assistant", "content": res.json()['answer']})
		with open(f'memory/{history}.json', 'w', encoding='utf-8') as file:
			json.dump(context, file)
	else:
		table = [{"role": "user", "content": promt + text}]
		res = requests.post('http://api.onlysq.ru/ai/v1', json=table)
	
	response = res.json()
	return response['answer']
