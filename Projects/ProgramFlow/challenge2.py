# Make sure options are strings because that's default format of input()
# Note: logical testing if integer is inside a range obj can yield true
# options = [*range(1,5)]    # use arg-unpack operator rng -> list of int
# options = [str(n) for n in options] # convert each element -> string
# option_display = [
#     "Exit",
#     "Learn Python",
#     "Learn C++",
#     "Go swimming",
#     "Have dinner",
#     "Go to bed"
# ]
#
# option_prompts = [
#     "Exiting\n",
#     "Monte Python would be proud\n",
#     "I took you to be an A++ student\n",
#     "Try not to get wet\n",
#     "Yummy!\n",
#     "Good night\n"
# ]
#
# while True:
#     # option_selected = input("Select an option 1-9, or type 0 to exit ")
#     option_selected = input(
#         "Please choose your option from the list below:\n\
#         1. {1}\n\
#         2. {2}\n\
#         3. {3}\n\
#         4. {4}\n\
#         5. {5}\n\
#         0. {0}\n".format(option_display[0],
#                          option_display[1],
#                          option_display[2],
#                          option_display[3],
#                          option_display[4],
#                          option_display[5]
#                          )
#     )
#
#     if option_selected in options:
#         print("{}".format(option_prompts[int(option_selected)]))
#     else:
#         print("{} is not a valid option\n"
#               .format(option_selected))
#     if option_selected == "0":
#         break

# choice = "-999"
# while True:
#
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose: {}".format(choice))
#     else:
#         print("""\
# Please choose your option from the list below:\n\
# 1:\tLearn Python\n\
# 2:\tLearn Java\n\
# 3:\tGo swimming\n\
# 4:\tHave Dinner\n\
# 5:\tGo to bed\n\
# 0:\tExit\n""")
#
#     choice = input()

choice = "-999"
while choice != "0":
    if choice in "12345":
        print("You chose: {}".format(choice))
    else:
        print("""\
Please choose your option from the list below:\n\
1:\tLearn Python\n\
2:\tLearn Java\n\
3:\tGo swimming\n\
4:\tHave Dinner\n\
5:\tGo to bed\n\
0:\tExit\n""")

    choice = input()





