import webbrowser
from urllib.parse import urlencode, quote


def get_text(info):
	return "Beste " + info['name'] + ",\n Je huidige deb stand is " + str(info['debt']) + "euro.\nDit kan je aflossen via: " + info['link'] + "\n Met vriendelijke groet, \n Wouter"


def open_link(text, number):
	url = "https://api.whatsapp.com/send?"
	link = url + urlencode({'phone': number, "text": text}, quote_via=quote)
	print(link)
	# webbrowser.open(link, new=2)
	

def send_all(data):
	for key, info in data.items():
		open_link(get_text(info), info['phone'])
