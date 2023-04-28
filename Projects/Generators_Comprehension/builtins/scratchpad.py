from data import plants_list

# for item in plants_list:
    # print(item)

# tmp = plants_list[0]
# print(tmp)
# print(tmp._replace(name = 'Test Name'))
# print(tmp)

## Changing the tuple with lambda and map
# tmp = map(lambda named_tuple: named_tuple._replace(name = "Test"), plants_list)
# for l in tmp:
#     print(l)

## Now using comprehension instead
# tmp = (named_tuple._replace(name = "Test") for named_tuple in plants_list)
# for l in tmp:
#     print(l)

# Testing on pandas dataframes
import pandas as pd
df = pd.DataFrame({
    'name' : ['Jim', 'Jon', 'Bob'],
    'score' : [100, 50, 75]
})

# print(df)

# apply function and lambda
df['score2'] = df['score'].apply(lambda x: (x+100)/2)

# using comprehension / generator
# for row in ((x+100)/2 for x in df['score']):
#     print(row)
# df['score3'] = list(((x+100)/2 for x in df['score']))  # generators have to be converted to list in this case
df['score3'] = [(x+100)/2 for x in df['score']]

def gen(col):
    for x in col:
        yield (x+100)/2


# df['score4'] = df['score'].apply(gen())
# df['score4'] = list(gen(df['score']))

print(list(gen(df['score'])))