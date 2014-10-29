#!/usr/local/bin/pythonw-32
import random
import datetime
import sys
import os
import codecs
import requests
import json


class Glauco():
    def __init__(self):
        self.responses = {}
        for _file in os.listdir(self.assets):
            self.responses[_file] = self.open_file(os.path.join(self.assets, _file))

    def search_query_list(self, _list, query):
        return str.lower(query) in [str.lower(el) for el in _list]

    def reply(self, query):
        response = self.parse_command(query)
        if response is not False:
            return response
        if query[-1] == "?":
            l = self.responses["affirmatives.txt"]
            return l[random.randint(0, len(l)-1)]
        else:
            l = self.responses["interrogatives.txt"]
            return l[random.randint(0, len(l)-1)]


if __name__ == "__main__":
    g = Glauco()
    print g.reply("Hello!")
    print g.reply("I am having a rough day")
    print g.reply("Goodbye")
    print g.reply("weather Curitiba")
    print g.reply("Whats the meaning of life?")
    print g.reply("whats the time?")
