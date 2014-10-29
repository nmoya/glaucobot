# -*- coding: utf-8-*-
import re
import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 
import utils
import re

WORDS = ["goodbyes"]
PRIORITY = 1


def handle(text):
	content = utils.open_file(os.path.join(os.getcwd(),"glaucobot/assets/goodbyes.txt"))
	return random.choice(content)

def isValid(text):
	"""
	A valid input should be in the form of: weather <city>
	"""
	text = utils.escape_query(text)
	content = utils.open_file(os.path.join(os.getcwd(),"glaucobot/assets/goodbyes.txt"))
	for line in content:
		if bool(re.search(r'\w%s' %(line.lower()), text, re.IGNORECASE)):
			return True
	return False


if __name__ == "__main__":
	print handle("Hi!")