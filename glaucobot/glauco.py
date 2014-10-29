#!/usr/local/bin/pythonw-32
import random
import datetime
import sys
import os
import codecs
import requests
import json
from datetime import date
from datetime import datetime
from datetime import timedelta
import time

def k2c(t):
    return t-273.15

def hms():
    ttime = time.localtime(time.time())
    str_time = "%s:%s:%s" % (ttime[3], ttime[4], ttime[5])
    return str_time

class Glauco():
    def __init__(self):
        self.responses = {}
        self.assets = os.path.join(os.getcwd(),"glaucobot/assets/")
        for _file in os.listdir(self.assets):
            self.responses[_file] = self.open_file(os.path.join(self.assets, _file))

    def open_file(self, _file):
        txt = codecs.open(_file, "r", "utf-8")
        content = txt.read().split("\n")
        txt.close()
        content = [el.encode("utf-8") for el in content]
        return content

    def search_query_list(self, _list, query):
        return str.lower(query) in [str.lower(el) for el in _list]

    def escape_query(self, query):
        return query.replace("!", "")

    def parse_command(self, query):
        # XXX: Todo, implement command pattern
        # XXX THIS IS DISGUISTING
        # http://api.openweathermap.org/data/2.5/weather?q=Curitiba
        if "weather" in str.lower(query):
            lst = query.split(" ")
            for i, el in enumerate(lst):
                if str.lower(el) == "weather":
                    break
            if (i+1) >= len(lst):
                return "Invalid command, please try again"
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s' % lst[i+1])
            str_json = r.text
            weather_info = json.loads(str_json)
            tmp = []
            for condition in weather_info['weather']:
                tmp.append(condition['main'])
            tmp = "/".join(tmp)
            return "%s in %s/%s. Min %.1f C, Max %.1f C." % (tmp, weather_info["name"], weather_info["sys"]["country"], 
                k2c(float(weather_info["main"]["temp_min"])), k2c(float(weather_info["main"]["temp_max"])))
        elif "meaning of life" in str.lower(query):
            return "Computing. I will email you when I have the answer."
        elif "time" in str.lower(query):
            return "It's %s at Curitiba/Brasil" % (hms())

        return False

    def reply(self, query):
        response = self.parse_command(query)
        if response is not False:
            return response

        query = self.escape_query(query)
        for key in ["salutations.txt", "goodbyes.txt"]:
            l = self.responses[key]
            if self.search_query_list(l, query):
                return l[random.randint(0, len(l)-1)]

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
