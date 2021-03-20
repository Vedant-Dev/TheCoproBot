from bot import TelegramBot as Bot
import bs4
import requests
import re

bot = Bot(config='config.py')


def send_reply(message):
	if not message:
		return 'Message to aaya hi nahi'
	return gangsterize(message)

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
			try:
				message = item['message']['text']
			except:
				message = None
			user_id = item['message']['from']['id']
			bot.sendMessage(message=send_reply(message),chat_id=user_id)

