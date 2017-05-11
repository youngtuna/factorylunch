#!/usr/local/bin/python

from bs4 import BeautifulSoup
import requests
import time

r = requests.get('http://www.ravintolafactory.com/aleksi/lounas/')

weekday = time.strftime("%a")
datediv = ""
getData = True

if weekday == "Mon":
    datediv = "lounasdate-1"
elif weekday == "Tue":
    datediv = "lounasdate-2"
elif weekday == "Wed":
    datediv = "lounasdate-3"
elif weekday == "Thu":
    datediv = "lounasdate-4"
elif weekday == "Fri":
    datediv = "lounasdate-5"
else:
    getData = False
    print("Failed to retrieve data.")

lounaat = BeautifulSoup(r.content, "lxml")

if getData is True:
    for lounas in lounaat.find_all(id=datediv):
        print(lounas.get_text())
