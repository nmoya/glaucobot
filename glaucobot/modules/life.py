# -*- coding: utf-8-*-
import re
import random

WORDS = ["meaning", "of", "life"]
PRIORITY = 1


def handle(text):
	messages = ["Computing. I will email you when I have the answer.",
				"42! Of course!",
				"I will have to think about it for some time.",
				"Ask @nikolasmoya"]

	return random.choice(messages)

def isValid(text):
	"""
	A valid input should be in the form of: weather <city>
	"""
	return bool(re.search(r'\bmeaning of life\b', text, re.IGNORECASE))


if __name__ == "__main__":
	print handle("What's the meaning of life?")