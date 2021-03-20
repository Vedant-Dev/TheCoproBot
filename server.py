from bot import TelegramBot as Bot
import bs4
import requests
import re
import json
from components import Message

bot = Bot(config='config.py')

def send_reply(message):
	if not message:
		return 'Message to aaya hi nahi'
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
	return gangsterize(message.text)
def gangsterize(input_text):
	params = {"translatetext": input_text}
	target_url = "http://www.gizoogle.net/textilizer.php"
	resp = requests.post(target_url, data=params)
	# the html returned is in poor form normally.
	soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
	soup = bs4.BeautifulSoup(soup_input, "lxml")
	giz = soup.find_all(text=True)
	giz_text = giz[37].strip("\r\n")  # Hacky, but consistent.
	return giz_text

update_id = -1
while True:
	updates = bot.getUpdates(offset=(update_id + 1))
	result = updates['result']
	if result:
		for item in result:
			update_id = item['update_id']
			if 'message' in item:
				message = Message(**item['message'],from_=item['message']['from'])
				bot.sendTextMessage(message=send_reply(message),chat_id=message.from_.id)
			else:
				message = Message(**item['edited_message'],from_=item['edited_message']['from'])
				bot.sendTextMessage(message=send_reply(message),chat_id=message.from_.id,reply_to_message_id=message.message_id)

