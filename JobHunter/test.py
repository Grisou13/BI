import feedparser
from bs4 import BeautifulSoup
import html
import requests
import os, sys
import re
import json
import csv

def determine_technos(self,*args,**kwargs):
    wantedWords = ['language',
    'experience',
    'knowledge',
    'expert',
    'skill',
    'proficient',
    'programming',
    'technologies',
    'technology']

    b = self.bs
    m = b.find(text=re.compile(r"require.*:"))
    technos = []
    #print(m)
    if m is None:
        return technos
    item = m.findNext('ul')

    if item is None:
        return technos
    for li in item.findAll('li'):
        line = li.get_text()
        if(not line.endswith('?') and any(word in line.lower() for word in wantedWords)):
            #print(line)
            techno1 = re.findall(r'\(([^)]+)\)', line)
            if techno1:
                techno1 = list(filter(None, re.split(r', |\/', techno1[0].replace('eg: ', '').replace('e.g. ', '').replace('etc.', ''))))
                technos = technos + techno1
            techno2 = line.replace('eg: ', '').replace('e.g. ', '').split(':')
            if len(techno2)==2:
                techno2 = techno2[1]
                techno2 = list(filter(None, re.split(r', |\/', techno2.replace('etc.', ''))))
                technos = technos + techno2

    return technos

url = "https://stackoverflow.com/jobs/158671/django-developer-zurich-divio?a=Rde33inhBLy"
print(url)

res = requests.get(url)
bs = BeautifulSoup(res.text, "html.parser")
technos = bs.find("section", { "class" : "-skills-requirements" })
print(technos)
print(determine_technos(technos))
