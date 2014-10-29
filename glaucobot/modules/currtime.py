# -*- coding: utf-8-*-
import os,sys,inspect
import time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 
import datelib
import re

WORDS = ["time"]
PRIORITY = 1


def handle(text):
	message = "It's %s at Curitiba/Brasil" % (datelib.seconds_to_formatted_time(str(time.time())))

	return message

def isValid(text):
	"""
	A valid input should be in the form of: weather <city>
	"""
	return bool(re.search(r'\btime\b', text, re.IGNORECASE))


if __name__ == "__main__":
	print handle("time")