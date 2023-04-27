# In an early video, we used a for loop to print the times tables, for values from 1 to 10.
# That was a nested loop, which appears below.
#
# The challenge is to use a nested comprehension, to produce the same values.
# You can iterate over the list, to produce the same output as the for loop, or just print out the list.

## Original for-loop 
for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)
print()

## 2 iterator comprehension
## for tt in [(i, i*j) for i in range(1,11) for j in range(1,11)]:
for x, y in [(i, i*j) for i in range(1,11) for j in range(1,11)]:
    print(x, y)
print()

## nested comprehension
for tt in [[(i, i*j) for j in range(1,11)] for i in range(1,11)]:
    # print(tt)
    for x,y in tt:
        print(x, y)
print()

## using a generator expression (replace square brackets with parenthesis)
## does not create entire list in to store in memory -> instead it generates values each iteration
for x, y in ((i, i*j) for i in range(1,11) for j in range(1,11)):
    print(x, y)
print()