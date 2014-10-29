# -*- coding: utf-8-*-
import re
import requests
import json
import time
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from bs4 import BeautifulSoup
import utils
import datelib
import urls


WORDS = ["currency"]
PRIORITY = 3


def handle(text):

	text = utils.escape_query(text)
	text = [t.strip() for t in text[text.find("currency"):].split(" ") if t != '']
	cur1, cur2 = text[1].upper(), text[3].upper()
	r = requests.get(urls.currency % (cur1, cur2))
	soup = BeautifulSoup(r.text)
	value = 0
	for table in soup.findAll("tr", attrs={'class': re.compile(urls.curr_class)}):
		value =  table.findAll("td")[-1].string.split(" ")[0].encode("utf-8")
	return "1 %s is worth %s %s on %s %s" % (cur2, value[11:15], cur1, datelib.seconds_to_formatted_date(str(time.time())), datelib.seconds_to_formatted_time(str(time.time())))



def isValid(text):
	"""
	A valid input should be in the form of: currency <CUR1> to <CUR2>
	"""
	return bool(re.search(r'\bcurrency \w{3} to \w{3}\b', text, re.IGNORECASE))


if __name__ == "__main__":
	print handle("currency BRL to USD")