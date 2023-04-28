# lambda() function (aka anonomous functions)
# used when you want to create a function that will only contain simple expressions
# or use a function just once

# General form:
# lambda <argument(s)> : <expression>
#
# arguement(s) = variable that will be used to hold the value you want
# to pass into the function expression. Can have multiple arguements.
#
# expression = code you want to execute in the lambda function.
#
# No 'return' keyword in the defined function, it automatically returns value.
#
# Basics: https://www.freecodecamp.org/news/python-lambda-function-explained/

# Example 1.
def f(x):
    return x * 2

print(f(3))
print((lambda x : x * 2)(3))  # calls lamba function


# Example 2
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, list1)
print(list(result))

# In pandas Pandas
import pandas as pd

df = pd.DataFrame(
    {'name': ['Jon', 'Tod', 'Trevor', 'Sheelah', 'Octavia'],
     'score': [50, 32, 45, 45, 23]
    }
)

print(df)
df['score_adj'] = df['score'].apply(lambda x: (x+100)/2)
print(df)