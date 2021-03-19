import requests
import json
from configparser import ConfigParser
class TelegramBot():
	def __init__(self, config):
		self.bot_token = self.unpack_config(config=config)
		self.base = f'https://api.telegram.org/bot{self.bot_token}/'
	
	def getUpdates(self, offset=None, timeout=100):
		url = self.base + f'getUpdates?timeout={timeout}'
		if offset > 0:
			url = url + f'&offset={offset}'
		response = requests.get(url)
		return json.loads(response.text)
	
	def sendMessage(self, message, chat_id):
		if not message:
			return 'unpassed parameter message'
		if not chat_id:
			return 'unpassed parameter chat_id'
		url = self.base + f'sendMessage?text={message}&chat_id={chat_id}'
		message = requests.get(url)
		return json.loads(message.text)
	def unpack_config(self, config):
		parser = ConfigParser()
		parser.read(config)
		return parser.get('creds', 'token')
