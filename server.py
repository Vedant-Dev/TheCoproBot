from bot import TelegramBot as Bot
from components import Message, BotCommand

bot = Bot(config='config.py')

def send_reply(message):
	if not message:
		return 'Due to some problem I was not able to read your message! Please try again'
	if message.animation is not None:
		return 'U send a animation'
	if message.audio is not None:
		return 'U send a audio'
	if message.video is not None:
		return 'U send a video'
	if message.document is not None:
		return 'U send a document'
	if message.sticker is not None:
		return 'u send a sticker'
	if message.photo is not None:
		return 'u send a photo'
	return message.text
def execute_command(bot_command):
	if bot_command.command == '/meme':
		bot.sendTextMessage(message= f'Meme chaiye bsdke',chat_id=message.from_.id)
	elif bot_command.command == '/do':
		bot.sendTextMessage(message= f'kaam krtwa reh din bhar',chat_id=message.from_.id)

update_id = -1
while True:
	updates = bot.getUpdates(offset=(update_id + 1))
	result = updates['result']
	if result:
		for item in result:
			update_id = item['update_id']
			if 'message' in item:
				message = Message(**item['message'],from_=item['message']['from'])
				if 'entities' in item['message']:
					if item['message']['entities'][0]['type'] == 'bot_command':
						bot_command = BotCommand(command=message.text[item['message']['entities'][0]['offset']:item['message']['entities'][0]['length']], discription=message.text[item['message']['entities'][0]['length']:])
						execute_command(bot_command)
					else:
						bot.sendTextMessage(message=send_reply(message),chat_id=message.from_.id)
				else:
					bot.sendTextMessage(message=send_reply(message),chat_id=message.from_.id)
				
			else:
				message = Message(**item['edited_message'],from_=item['edited_message']['from'])
				bot.sendPhotoMessage(photo='https://core.telegram.org/file/811140015/1734/8VZFkwWXalM.97872/6127fa62d8a0bf2b3c',chat_id=message.from_.id,reply_to_message_id=message.message_id)

