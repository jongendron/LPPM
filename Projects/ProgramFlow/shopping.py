shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:
#     if item == "spam":
#         continue    # causes remaining code chunk to be skipped
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break    # terminates loop
    print("Buy " + item)
