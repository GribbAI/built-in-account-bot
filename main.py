from pyrogram import Client, filters
import ai, analytic

# вставьте свои данные (api-id и api-hash можно получить на https://my.telegram.org)
API_ID = 'api_id'
API_HASH = 'api_hash'
PHONE_NUMBER = 'phone_number'
app = Client("session/name_app", api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)

@app.on_message()
def start(client, message):
	try:
		if '++ии ' in message.text:
			chat_id = message.chat.id
			messages = app.get_chat_history(chat_id, limit=100)
			history = "\n".join([f"{msg.from_user.first_name if msg.from_user else 'Неизвестный'}: {msg.text}" for msg in messages if msg.text])
			
			input = f"история чата: {history}, вопрос: {message.from_user.first_name}: {message.text.split('++ии')[1]}"
			message.reply(ai.gpt(input, chat_id, "тебе зовут GribAI. тебя создал Артём великий!!!", memory=True))
		
		if '++анализ ' in message.text:
			chat_id = message.chat.id
			messages = app.get_chat_history(chat_id, limit=int(message.text.split('++анализ')[1]))
			msg_text = "\n".join([f"{msg.from_user.first_name if msg.from_user else 'Неизвестный'}: {msg.text}" for msg in messages if msg.text])
			message.reply(ai.gpt(msg_text, "расскажи о участниках часах основаясь на этом: "))
		
		if '++активность ' in message.text:
			users_active = {}
			chat_id = message.chat.id
			messages = app.get_chat_history(chat_id, limit=int(message.text.split('++активность')[1]))
			for msg in messages:
				if not (msg.from_user.first_name if msg.from_user else 'Неизвестный') in users_active:
					users_active[msg.from_user.first_name if msg.from_user else 'Неизвестный'] = 1
				else:
					users_active[msg.from_user.first_name if msg.from_user else 'Неизвестный'] = users_active[msg.from_user.first_name if msg.from_user else 'Неизвестный'] + 1
			message.reply_photo(photo=analytic.create.diagram(users_active))
	except Exception as error:
		print(f'Произошла ошибкаи: {error}')


if __name__ == "__main__":
    print("STARTING BOT")
    app.run()