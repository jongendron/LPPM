# Warning: if you don't intend to store a list comprehension, use a generator instead!

burgers = ['beef', 'chicken', 'spicy bean']
toppings = ['cheese', 'egg', 'beans', 'spam']

## Comprehension with two iterators
## [<expression> <iteration1> <iteration2>]
## [(<value1a>,<value1b>) <iteration1> <iteration2>]
## iteration1 -> iteration2 -> expression
for meal in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meal)
print()

## equivalent for-loop
# for burger in burgers:
#     for topping in toppings:
#         print((burger, topping))
# print()

## Nested comprehension
## [[<list comprehension>] <iteration>]
## [[<expression> <iteration2>] <iteration1>]
## expression <- iteration2 <- iteration1
## outter iteration values are used first!
## produces a list of nested lists of nested tupples
for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:  # lists by  outter iteration (toppings)
    print(nested_meals)
print()
for nested_meals in [[(burger, topping) for topping in toppings] for burger in burgers]:  # lists by outter iteration (burgers)
    print(nested_meals)
print()