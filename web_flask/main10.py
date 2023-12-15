#!/usr/bin/python3
import sys
import requests
from lxml import html
import re

states = []

NO_PROXY = {
    'no': 'pass',
}


# Request
page = requests.get('http://0.0.0.0:5000/states', proxies=NO_PROXY)
if int(page.status_code) != 200:
    print("Status fail: {}".format(page.status_code))
    sys.exit(1)

# Parsing
tree = html.fromstring(page.content)
if tree is None:
    print("Can't parse page")
    sys.exit(1)

# H1
h1_tags = tree.xpath('//body/h1/text()')
if h1_tags is None or len(h1_tags) == 0:
    print("H1 tag not found")
    sys.exit(1)

if not re.search(r".*States.*", h1_tags[0]):
    print("Title `States` doesn't found")
    sys.exit(1)

# LI state ID
li_tags = list(filter(None, [x.replace(" ", "").strip(" ").strip(
    "\n").strip("\t") for x in tree.xpath('//body/ul/li/text()')]))
if li_tags is None or len(li_tags) != len(states):
    print("Doesn't find {} LI tags (found {})".format(len(states), len(li_tags)))
    sys.exit(1)

print("OK", end="")
