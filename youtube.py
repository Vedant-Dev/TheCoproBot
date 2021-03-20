from pytube import YouTube as YT

class Youtube():
	def __init__(self,link):
		self.link = link
		self.video = YT(link)
	def audio(self):
		return video.streams.filter(type='audio').first()
	def video(self):
		return video.stream.filter(type='video').first()
