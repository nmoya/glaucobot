# -*- coding: utf-8-*-
import re
import requests
import json
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import utils


WORDS = ["weather"]
PRIORITY = 3


def handle(text):
	tmp = []

	text = utils.escape_query(text)
	text = [t.strip() for t in text[text.find("weather"):].split(" ") if t != '']
	command, city = text[0], text[1]
	r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s' % city)
	try:
		weather_info = json.loads(r.text)
	except ValueError:
		return "There was a problem with your request, please try again."

	for condition in weather_info['weather']:
		tmp.append(condition['main'])

	condition = "/".join(tmp)
	city      = weather_info["name"]
	country   = weather_info["sys"]["country"]
	min_temp  = utils.k2c(float(weather_info["main"]["temp_min"]))
	max_temp  = utils.k2c(float(weather_info["main"]["temp_max"]))
	response  = "%s in %s/%s. Min %.1f C, Max %.1f C." % (condition, city,
				country, min_temp, max_temp)
	return response

def isValid(text):
	"""
	A valid input should be in the form of: weather <city>
	"""
	return bool(re.search(r'\bweather +([a-zA-Z])+\b', text, re.IGNORECASE))


if __name__ == "__main__":
	print requests
	print handle("WeAThEr  curitiba")