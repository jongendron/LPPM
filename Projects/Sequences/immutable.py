# result = True
# another_result = result
# print(id(result))           # returns identity of object
# print(id(another_result))   # does not necessarily return memory address
#
# # if python has to recreate this object, then id changes
# result = False
# print(id(result))           # different id than first result

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))               # This result has different ID now
print(id(another_result))       # still same

# This means that python created new object using "Correct" and adding "ish"
