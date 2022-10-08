# "," between print arguments adds a space, and without it there is none
# print("1:\tOption 1\n""2:\tOption 2\n""3:\tOption 3\n")
# print(
# "the dog"
# "swam"
# "in"
# "the"
# "lake"
# )

# l1 = ["v1","v2","v3"]
#
# print(enumerate(l1))

# data = [
#     "Andromeda - Shrub",
#     "Bellflower - Flower",
#     "China Pink - Flower",
#     "Daffodil - Flower",
#     "Evening Primrose - Flower",
#     "French Marigold - Flower",
#     "Hydrangea - Shrub",
#     "Iris - Flower",
#     "Japanese Camellia - Shrub",
#     "Lavender - Shrub",
#     "Lilac - Shrub",
#     "Magnolia - Shrub",
#     "Peony - Shrub",
#     "Queen Anne's Lace - Flower",
#     "Red Hot Poker - Flower",
#     "Snapdragon - Flower",
#     "Sunflower - Flower",
#     "Tiger Lily - Flower",
#     "Witch Hazel - Shrub",
# ]
#
# flowers = []
# shrubs = []
#
# # write your code here
# for index, flower in enumerate(data):
#     if "Flower" in flower:
#         flowers.append(flower)
#     elif "Shrub" in flower:
#         shrubs.append(flower)
#     else:
#         print("Neither shrub nor flower")
#
# print(flowers)
# print(shrubs)
#
# a = "1,2,3"
# b = a.split(",")
# print(b)
# c = []
# for value in b:
#     c.append(int(value))
# print(c)

user_input = input("Please enter three numbers separated by a <,>")
str_list = user_input.split(",")
int_list = []
for value in str_list:
    int_list.append(int(value))
#result = int_list[0] + int_list[1] - int_list[2]
a,b,c = int_list # set three variables = each list item respectively
print(a,b,c)
result = a + b - c
print(result)
