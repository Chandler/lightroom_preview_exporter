import pickle
import re
import sys

uid_to_name = {}

for line in sys.stdin:
  # matches a line found in the lightroom catalog binary that looks like this:
  # 9DD10023-1313-41EB-8BCE-0C3E166CFA2Amy_photo_namejpgA
  # which is the UID followed by a filename with no period followed by an A
  m = re.match(
        '^([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})(.+)(jpg|jpeg|tif|nef|gif)A$',
        line,
        re.IGNORECASE)
  if m:
      # ('BF98706D-971C-41DA-AE1C-A86391C9AD1C', 'DSC_0831', 'NEF')
      uid_to_name[m.group(1)] = m.group(2) + '.' + m.group(3)

pickle.dump(uid_to_name, open('/tmp/uid_to_name.pickle','wb'))
