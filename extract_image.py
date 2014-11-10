import binascii
import fnmatch
import os
import pickle
import random
import re
import sys

if(len(sys.argv) < 3):
  print "usage is: ./run.sh path/to/lr/catalog path/to/lr/previews/dir"
  exit()

preview_file_path  = sys.argv[1]
output_file_path   = sys.argv[2]

if not os.path.exists(output_file_path):
    os.makedirs(output_file_path)

# Markers in the binary that indicate you found a JPEG
# http://stackoverflow.com/a/1602428/67166
JPEG_START_BYTES = '\xff\xd8\xff\xee'
JPEG_END_BYTES   = '\xff\xd9'

# a serialized map from UID -> filename. Generated by uid_to_name.py
uid_to_name      = pickle.load(open('/tmp/uid_to_name.pickle','rb'))

# regex that matches a UID
uid_regex        = re.compile('([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})')
uid              = uid_regex.search(preview_file_path)

if uid:
    # Byte array of the entire preview file
    all_bytes    = open(preview_file_path.rstrip(), "rb").read()
    length       = len(all_bytes)

    # The preview file will have multiple jpegs of varrying resolutions
    # embedded in it. We will store them all and write out only the highest resolution
    # at the end
    images        = []

    # If this is true, it means our cursor is currently with 
    reading_image = False
    image_number  = 0
    i             = 0

    # Iterate through every byte in the preview binary 2 at a time.
    # scanning for JPEGS and storing them as byte arrays inside images[]
    while i + 3 < length:
        twoBytes  = all_bytes[i] + all_bytes[i+1]
        fourBytes = all_bytes[i] + all_bytes[i+1] + all_bytes[i+2] + all_bytes[i+3]
       
        # a start byte was found, initialize a new bytearray() in images[]
        if (fourBytes == JPEG_START_BYTES):
            images.insert(image_number, bytearray())
            reading_image = True

        # The current byte is part of a JPEG so write it to the current byte array
        if reading_image:
            images[image_number].extend(twoBytes)

        if twoBytes == JPEG_END_BYTES:
            reading_image = False
            image_number += 1

        i += 2

    images.sort(key = len)
    
    # We only want to write out the highest resolution preview found
    largest_preview = images.pop()

    # If no filename can be found write out a random number
    filename  = uid_to_name.get(uid.group(0), str(random.random()))
    out       = output_file_path + "/" + filename
    print "writing: " + out
    with open (out, "w+") as f:
        f.write(bytearray(largest_preview))
else:
    print "uid not found in filename: " + preview_file_path
