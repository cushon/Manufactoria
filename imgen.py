#!/usr/bin/python

import sys
import urllib2
import re

solutions = open(sys.argv[1], 'r')
s = filter(None, [line.strip() for line in solutions])

while s:
  url = 'http://man.ozwebwiz.com'+s.pop(1)
  lvl = re.search('lvl=([0-9]+)', url).group(0)[4:]
  print "Generating {0}".format(lvl)
  image = urllib2.urlopen(url)
  with open("{0}_{1}.png".format(lvl, s.pop(0).replace(' ', '_')), 'w+') as f:
    f.write(image.read())
