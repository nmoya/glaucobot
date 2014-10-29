# -*- coding: utf-8-*-
import re
import random
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir) 
import utils
import re

WORDS = ["affirmatives"]
PRIORITY = 0


def handle(text):
	content = utils.open_file(os.path.join(os.getcwd(),"glaucobot/assets/interrogatives.txt"))
	return random.choice(content)

def isValid(text):
	"""
	A valid input should be in the form of: weather <city>
	"""
	return True


if __name__ == "__main__":
	print handle("What's the meaning of life?")