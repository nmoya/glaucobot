from TwitterAPI import TwitterAPI
import keys
import time
import json
from glaucobot import brain
from glaucobot import datelib


last_id_replied = 527224623864500225

api = TwitterAPI(
	keys.CONSUMER_KEY,
	keys.CONSUMER_SECRET,
	keys.ACCESS_TOKEN_KEY,
	keys.ACCESS_TOKEN_SECRET)


def save_last_id_replied(id):
	arq = open("last_id.txt", "w")
	arq.write(str(id))
	arq.close()

def load_last_id_replied():
	arq = open("last_id.txt", "r")
	content = arq.read()
	arq.close()	
	return int(content)

def save_item(item):
	arq = open("model.json", "w")
	arq.write(json.dumps(item))
	arq.close()
# r = api.request('statuses/update', {'status': "Performing self checks... 10% @glaucobot"})
# r = api.request('statuses/filter', {'track': TRACK_TERM})
# r = api.request('search/tweets', {'q': 'glaucobot'})


b = brain.Brain()
last_id_replied = load_last_id_replied()
# print b.query("WeAThEr  curitiba")
# print b.query("What's the meaning of Life?")
# print b.query("time")
# print b.query("Thanks!")
# print b.query("HI!!")
# print b.query("How are you?")
# print b.query("I'm fine")
# print b.query("currency BRL to USD")


while True:
	t_request = time.time()
	print "Request at:", datelib.hms()
	r = api.request('statuses/mentions_timeline', {'count': 350, 'since_id': last_id_replied})
	for item in r:
		if item.get("code") is not None:
			if item["code"] == 88:
				print "Rate limit exceeded"
		if item.get("text") is not None:
			text = item["text"]	
			text = text.encode("utf-8")
			last_id_replied = max(item["id"], last_id_replied)
			mentions_lst = ["@"+el["screen_name"] for el in item["entities"]["user_mentions"] if el["screen_name"] != "glaucobot"]
			sender = item["user"]["screen_name"]
			mentions_lst.append("@"+sender)
			glauco_reply = b.query(text)
			glauco_reply = " ".join(mentions_lst) + " " + glauco_reply
			if sender != "glaucobot":
				print "-", text
				print "-", glauco_reply
				print ""
				response = api.request('statuses/update', {'status': glauco_reply})
				save_last_id_replied(last_id_replied)

	if time.time() - t_request < 65:
		time.sleep(65)
