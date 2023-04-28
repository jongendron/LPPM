# writtig email client
# allowed user to choose people to receive email from contact DB
# user wants to send email
# we want to check that all people have email address
# if not, we have user edit list of recipients
# -> check second field of each people
# -> do this with list comprehension

from data import people, basic_plants_list, plants_list, plants_dict

# people = []  # careful, this returns false when tested -> check with bool()

if bool(people) and all([person[1] for person in people]):  # True is all emails are not empty -> causes short circuit (stops as soon as false is found)
    print("Sending email.")
else:
    print("User must edit the list of recipients.")

# Checking for grasses
# more readable with named tuple vs index
if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

# Using any() and a comprehension (or generator expression) to check the plants
# in platns_dict to see if there are any grasses in there.
# then search for catus instead.
print("*" * 80)
plant_type = "Grass"
if any((plant.plant_type == plant_type for plant in plants_dict.values())):  # over .values()
# if any((plants_dict[key].plant_type == plant_type for key in plants_dict)):  # with keys
    print(f"This pack contains {plant_type}")
else:
    print(f"No {plant_type} in this pack")



