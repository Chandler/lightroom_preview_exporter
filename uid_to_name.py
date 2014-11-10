import re
import sys
import pickle
uid_to_name = {}

for line in sys.stdin:
  m = re.match(
        '^([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})(.+)(jpg|jpeg|tif|nef)A$',
        line,
        re.IGNORECASE
      )
  if m:
      # print('Match found: ', m.group(1), m.group(2), m.group(3))
      # ('Match found: ', 'BF98706D-971C-41DA-AE1C-A86391C9AD1C', 'DSC_0831', 'NEF')
      uid_to_name[m.group(1)] = m.group(2) + '.' + m.group(3)

f = open('/tmp/uid_to_name.pickle','wb')
pickle.dump(uid_to_name, f)
