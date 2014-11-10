import binascii
import re
import fnmatch
import os
import random
import pickle
import sys

f = open('/tmp/uid_to_name.pickle','rb')
uid_to_name = pickle.load(f)

matcher = re.compile('([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})')
line    = sys.argv[1]
uid     = matcher.search(line)
if uid:
  with open (line.rstrip(), "r") as p:
    bytes         = None
    image_counter = 0
    images        = []
    reading_image = False

    while bytes != b"":
        bytes = p.read(4)
        if (bytes == '\xff\xd8\xff\xe0'):
          reading_image = True
          images.insert(image_counter, bytearray())  

        if reading_image:
          images[image_counter].extend(bytes)

        if bytes == '\xff\xd9':
          reading_image = False
          image_counter += 1

    images.sort(key = len)
    largest_preview = images.pop()
    filename        = uid_to_name.get(uid.group(0), str(random.random()))
    print "writing file " + filename
    with open ("photos/" + filename, "w") as f:
      f.write(bytearray(largest_preview))
else:
  print "uid not found for file: " + line



