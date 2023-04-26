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

# Without comprehension

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         # print(meal)
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped.")
# print(meals)

# meals = [meal for meal in menu if "spam" not in meal]
# print(meals)

# list comprehension with filters
# else clauses are not permitted.
# [<expression> <iteration> <filter(s)>]
# [<meal> <for meal in menu> <if "spam" not in meal if "chicken" not in meal>]

# meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]  # and is not needed to chain if filters, but ...
# and is more common
# meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
# print(meals)

# any meals that ...
# 1. contains "spam" or "eggs".
# 2. does not contain "bacon" and "sausage" together.

# fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal if not ("bacon" in meal and "sausage" in meal)]
# fussy_meals = [meal for meal in menu if ("spam" in meal or "eggs" in meal) and not (
#     "bacon" in meal and "sausage" in meal)]  # with single filter "if" is less intuitive to read
# print(fussy_meals)

# Conditional expressions
# [<expression> <iteration>]
# [<meal if "spam" not in meal else "a meal was skipped"> <for meal in menu>]

# x = 15
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

# meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
# print(meals)

# several conditions
# if <value1> if <condition1> else <value2> if <condition2> else <value3> if <condtion3> ... else <value-x>
for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")
print()

# checking against set(s)

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print(f"{meal} contains {item}")
print()

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x %5 == 0 else str(x)
    print(fizzbuzz)