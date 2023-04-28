# ---------------------------------------------
# 2023-04-28
# Fate of reduce() in Python 3000: https://www.artima.com/weblogs/viewpost.jsp?thread=98196
# This argues the removal of these function
# ---------------------------------------------
import timeit

# map(<fnc>, <iterator>)
# iterator can be str, list, dict (anything)
# map is pretty much a comprehension but harder to see what is happening

text = "what have the romans ever done for us"

# Capital letters with comprehension
def capletter(text):
    capitals = [char.upper() for char in text]
    # print(capitals)
    return capitals

# Capital letters with map()
def capletter_m(text):
    map_capitals = list(map(str.upper, text))
    # print(map_capitals)
    return map_capitals

# Capital Words with comprehension
def capword(text):
    words = [word.upper() for word in text.split(' ')]
    # print(words)
    return words

# Capital Wrods with map()
def capword_m(text):
    map_words = list(map(str.upper, text.split(' ')))
    # print(map_words)
    # print()
    return map_words

# # Iterate over the list produced by map()
# for x in map(str.upper, text.split(' ')):
#     print(x)

if __name__ == "__main__":
    # print(capletter())
    # print(capletter_m())
    # print(capword())
    # print(capword_m())

    # test1 = timeit.timeit(capletter, number=1000)
    # test1 = timeit.timeit(capletter_m, number=1000)
    # test1 = timeit.timeit(capword, number=1000)
    # test1 = timeit.timeit(capword_m, number=1000)

    test1 = timeit.timeit(stmt="x = capletter(text)", setup="from __main__ import capletter, text", number=10000)
    test2 = timeit.timeit(stmt="x = capletter_m(text)", setup="from __main__ import capletter_m, text", number=10000)
    test3 = timeit.timeit(stmt="x = capword(text)", setup="from __main__ import capword, text", number=10000)
    test4 = timeit.timeit(stmt="x = capword_m(text)", setup="from __main__ import capword_m, text", number=10000)

    print(test1)
    print(test2)
    print(test3)
    print(test4)

    # print("capital letters w/ comprehension: {}".format(test1))
    # print("capital letters w/ map: {}".format(test2))
    # print("capital words w/ comprehension: {}".format(test3))
    # print("capital words w/ map: {}".format(test4))