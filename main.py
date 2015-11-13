#!/usr/bin/python3

import re

import urllib
from urllib import parse
import subprocess

url = "https://www.google.ie/search?q=play+arijit+singh+songs&oq=play+arijit+singh+songs&aqs=chrome..69i57.16305j0j4&sourceid=chrome&es_sm=119&ie=UTF-8"
p = parse.urlparse(url)

if (re.match("^www.google..*", p.hostname)):
	query = re.match("q=[^&]+", p.query).group(0)[2:]
	query = parse.unquote(query)

	query = query.lower()

	if query.startswith("play+"):
		query = query[5:]

		query = query.replace("+", " ")

		print("mpsyt /%s, 1, all -a" % (query))
		proc = subprocess.Popen("mpsyt /%s, 1, all -a" % (query), shell=True)
