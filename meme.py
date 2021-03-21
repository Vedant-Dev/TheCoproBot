from bs4 import BeautifulSoup
import requests
import webbrowser

def give_me_meme(query):
	url = f"https://www.google.com/search?q={query}&tbm=isch"
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "html.parser")
	images = soup.find_all('img')[1:3]
	src_of_images = [image['src'] for image in images]
	return src_of_images
