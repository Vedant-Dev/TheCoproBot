class User:
	def __init__(self,id,is_bot,first_name,last_name,username=None,language_code=None, *args, **kwargs):
		self.id = id
		self.is_bot = is_bot
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.language_code = language_code

class Chat:
	def __init__(self,id,type,title=None,username=None,first_name=None,
		last_name=None,bio=None,discription=None, *args, **kwargs):
		self.id = id
		self.type = type
		self.title = title
		self,username = username
		self.first_name = first_name
		self.last_name = last_name
		self.bio = bio
		self.discription = discription

class Message:
	def __init__(self,message_id,from_=None,sender_chat=None,date=None,chat=None,
		reply_to_message=None,text=None,animation=None,audio=None,document=None,
		photo=None,sticker=None,video=None, *args, **kwargs):
		self.message_id = message_id
		self.from_ = User(**from_)
		self.sender_chat = Chat(**sender_chat) if sender_chat else None
		self.date = date
		self.reply_to_message = reply_to_message
		self.text = text
		self.animation = Animation(**animation) if animation else None
		self.audio = Audio(**audio) if audio else None
		self.document = Document(**document) if document else None
		self.photo = [PhotoSize(**p) for p in photo if p] if photo else None 
		self.sticker = Sticker(**sticker) if sticker else None
		self.video = Video(**video) if video else None
class MessageId:
	def __init__(self,message_id, *args, **kwargs):
		self.message_id = message_id

class PhotoSize:
	def __init__(self,file_id,file_unique_id,width,height,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.width = width
		self.height = height
		self.file_size = file_size

class Animation:
	def __init__(self,file_id,file_unique_id,width,height,duration,
		thumb=None,file_name=None,mime_type=None,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.width = width
		self.height = height
		self.duration = duration
		self.thumb = PhotoSize(**thumb) if thumb else None
		self.file_name = file_name
		self.mime_type = mime_type
		self.file_size = file_size

class Audio:
	def __init__(self,file_id,file_unique_id,duration,performer,
		title,thumb=None,file_name=None,mime_type=None,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.duration = duration
		self.performer = performer
		self.title = title
		self.thumb = PhotoSize(**thumb) if thumb else None
		self.file_name = file_name
		self.mime_type = mime_type
		self.file_size = file_size

class Document:
	def __init__(self,file_id,file_unique_id,thumb=None,file_name=None,mime_type=None,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.thumb = PhotoSize(**thumb) if thumb else None
		self.file_name = file_name
		self.mime_type = mime_type
		self.file_size = file_size

class Video:
	def __init__(self,file_id,file_unique_id,width,height,duration,
		thumb=None,file_name=None,mime_type=None,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.width = width
		self.height = height
		self.duration = duration
		self.thumb = PhotoSize(**thumb) if thumb else None
		self.file_name = file_name
		self.mime_type = mime_type
		self.file_size = file_size

class Sticker:
	def __init__(self,file_id,file_unique_id,width,height,is_animated,
		thumb=None,emoji=None,set_name=None,file_size=None, *args, **kwargs):
		self.file_id = file_id
		self.file_unique_id = file_unique_id
		self.width = width
		self.height = height
		self.is_animated = is_animated
		self.thumb = PhotoSize(**thumb) if thumb else None
		self.emoji = emoji
		self.set_name = set_name
		self.file_size = file_size

class BotCommand:
	def __init__(self,command,discription):
		self.command = command
		self.discription = discription

class ChatPhoto:
	def __init__(self,small_file_id,small_file_unique_id,big_file_id,big_file_unique_id):
		self.small_file_id = small_file_id
		self.small_file_unique_id = small_file_unique_id
		self.big_file_id = big_file_id
		self.big_file_unique_id = big_file_unique_id