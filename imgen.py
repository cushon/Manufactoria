#!/usr/bin/python

import sys
import urllib2
import re

selection = [int(x) for x in sys.argv[2:]]

solutions = open(sys.argv[1], 'r')
s = filter(None, [line.strip() for line in solutions])

while s:
  name = s.pop(0)
  code = s.pop(0)
  url = 'http://man.ozwebwiz.com'+code
  lvl = re.search('lvl=([0-9]+)', url).group(0)[4:]
  if not int(lvl) in selection:
    continue
  print "Generating {0}".format(lvl)
  image = urllib2.urlopen(url)
  with open("{0}_{1}.png".format(lvl, name.replace(' ', '_')), 'w+') as f:
    f.write(image.read())
