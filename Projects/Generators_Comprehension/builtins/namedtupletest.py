from data import basic_plants_list, plants_list

print(plants_list[0])

for plant in basic_plants_list:
    print(plant[0])

for plant in plants_list:
    print(plant.name)  # named tupple (class) creates attributes for each field
    print(plant[0])  # can use index as well

print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle = 'Annual')  # replace lifecycle field value
print(example)