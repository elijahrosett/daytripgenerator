import random
destinations = ["Utah", "Texas", "Arizona", "California", "Cabo"]
transportation_options = ["an Uber", "a rental car",
                          "a personal helicopter", "a bike"]
restraunts = ["Cafe Rio", "Mcdonalds", "Cheesecake Factory"]
entertainment = ["going for a hike", "going to a concert",
                 "going to the pool", "mountain biking"]
perfect_trip = []


def random_selection(select_list):
    random_output = random.choice(select_list)
    return random_output


def greeting(whats_being_selected):
    print(f"Lets select your {whats_being_selected}!")


def are_you_happy_with_selected(picked_item, what_is_the_list_of):
    print(f"Your {what_is_the_list_of} has been selected as {picked_item}")
    print("Are you happy with this decision?")
    user_input = input("Yes/No ")
    return user_input


# happy_with_location = True
# print("Welcome to the day trip generator! I hope you're ready for the perfect vacation!")
# while happy_with_location is True:
#     picked_item = random_selection(destinations)
#     print(
#         f"Your destination has been selected as {picked_item}")
#     print("Are you happy with this decision?")
#     user_input = input("Yes/No ")
#     if user_input == "No":
#         print("Okay, lets change that!")
#         happy_with_location = True
#     elif user_input == "Yes":
#         print("Awesome! Lets move on. ")
#         perfect_trip.append(picked_item)
#         happy_with_location = False


# greeting("Transportation")


# def happy_with_decision(which_list, what_is_the_list_of):
#     happy_with_transportation = False
#     while happy_with_transportation is False:
#         picked_item = random_selection(which_list)
#     print(f"Your {what_is_the_list_of} has been selected as {picked_item}")
#     print("Are you happy with this decision?")


#     user_input = are_you_happy_with_selected(picked_item, "transportation")
#     if user_input == "No":
#         print("Okay, lets change that!")
#         happy_with_transportation = True
#     elif user_input == "Yes":
#         print("Awesome! Lets move on. ")
#         perfect_trip.append(picked_item)
#         happy_with_transportation = True


# print_this = happy_with_decision(transportation_options, "transportation")
# print(print_this)


# happy_with_food = True
# print("Next lets pick where you will eat!")
# while happy_with_food is True:
#     picked_item = random_selection(restraunts)
#     print(
#         f"Your restaurant has been selected as {picked_item}")
#     print("Are you happy with this decision?")
#     user_input = input("Yes/No ")
#     if user_input == "No":
#         print("Okay, lets change that!")
#         happy_with_food = True
#     elif user_input == "Yes":
#         print("Awesome! Lets move on. ")
#         perfect_trip.append(picked_item)
#         happy_with_food = False
#         break


# happy_with_entertainment = True
# print("Next lets pick your entertainment!")
# while happy_with_entertainment is True:
#     picked_item = random_selection(entertainment)
#     print(
#         f"Your activity has been selected as {picked_item}")
#     print("Are you happy with this decision?")
#     user_input = input("Yes/No ")
#     if user_input == "No":
#         print("Okay, lets change that!")
#         happy_with_entertainment = True
#     elif user_input == "Yes":
#         print("Awesome! Lets move on. ")
#         perfect_trip.append(picked_item)
#         happy_with_entertainment = False
#         break

# print("Lets go over what you've selected.")
# print(f"Destination: {perfect_trip[0]}")
# print(f"transportation: {perfect_trip[1]}")
# print(f"Restaurant: {perfect_trip[2]}")
# print(f"Entertainment {perfect_trip[3]}")
# print("Would you like to finalize this trip?")
# finalize_trip = input("Yes/No ")
# if finalize_trip == "Yes":
#     print(
#         f"Here is the plan for your trip. First, you will be going to {perfect_trip[0]}, While there, your transpertation will be {perfect_trip[1]}. You will eat at {perfect_trip[2]}. Finally, your entertainment will be {perfect_trip[3]}.")
# else:
#     print("What would you like to change?")
#     change_trip = input(
# #         "No problem! Please start over and we can make a new trip!")
# happy_with_location = True


# def day_trip_function(which_list, what_are_we_picking):
#     while happy_with_location is True:
#         picked_item = random_selection(which_list)
#     print(
#         f"Your {what_are_we_picking} has been selected as {picked_item}, Are you happy with this decision?")
#     user_input = input("Yes/No ")
#     if user_input == "No":
#         print("Okay, lets change that!")
#         happy_with_location = True
#     elif user_input == "Yes":
#         print("Awesome! Lets move on. ")
#         perfect_trip.append(picked_item)
#         happy_with_location = False


def second_part_of_function(user_input):
    if user_input == "No":
        print("Okay, lets change that!")
        not_okay = " "
        return not_okay
    elif user_input == "Yes":
        print("Awesome! Lets move on. ")
        yes_okay = " "
        return yes_okay


greeting("Trip")
selected_destination = (random_selection(destinations))
user_input = are_you_happy_with_selected(selected_destination, "destination")
second_part_of_function(user_input)


# perfect_trip.append(picked_item)
