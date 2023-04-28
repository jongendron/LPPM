import timeit

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
 
# for meal in menu:
#     if "spam" not in meal:
#         print(meal)
 
# print("-" * 40)
 
def spamless_comp():
    # meals = [meal for meal in menu if "spam" not in meal]
    meals = [meal for meal in menu if not_spam(meal)]  # using the function within a comprehension
    # print(meals)
    return meals
 

# print("-" * 40)


def not_spam(meal_list: list):
    return "spam" not in meal_list


# Using filter()
# comprehension is still easier to read
def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    # print(spamless_meals)
    return spamless_meals


# print("-" * 40)

if __name__ == '__main__':
    # print(spamless_comp())
    # print(spamless_filter)
    # using timeit: this method relies that menu loaded as global variable
    
    # Timeit using functions and globals
    # print(timeit.timeit(spamless_comp, number=10000))
    # print(timeit.timeit(spamless_filter, number=10000))

    # Timeit using stmt and globals()
    # print(timeit.timeit("spamless_comp()", globals=globals(), number=1000))
    # print(timeit.timeit("spamless_filter()", globals=globals(), number=1000))

    # Timeit using stmt and setup
    # but why is menu variable from __main__ available ?
    print(timeit.repeat("spamless_comp()", setup="from __main__ import spamless_comp", number=1000, repeat=3))
    print(timeit.repeat("spamless_filter()", setup="from __main__ import spamless_filter", number=1000, repeat=3))  # overhead from calling functions slows performance

