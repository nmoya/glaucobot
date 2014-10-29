from __future__ import division
import codecs


def k2c(t):
	return t-273.15

def open_file(_file):
	txt = codecs.open(_file, "r", "utf-8")
	content = txt.read().split("\n")
	txt.close()
	content = [el.encode("utf-8") for el in content]
	return content

def escape_query(query):
	query = query.lower()
	query = query.strip()
	return query.replace("!", "")