# aware objects are aware of timezone offsets
# niave objects are not

import datetime

print()
print(datetime.datetime.today())
print(datetime.datetime.now()) # can provide tz
print(datetime.datetime.utcnow())
print()