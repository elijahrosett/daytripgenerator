import random
destinations = ["Utah", "Texas", "Arizona", "California", "Cabo"]
transportation_options = ["an Uber", "a rental car",
                          "a personal helicopter", "a bike"]
restraunts = ["Cafe Rio", "Mcdonalds", "Cheesecake Factory"]
entertainment = ["going for a hike", "going to a concert",
                 "going to the pool", "mountain biking"]
perfect_trip = []


def reselect_option(true_or_false, selected_list):
    while true_or_false == True:
        print("okay you picked yes")
    else:
        new_pick = random_selection(selected_list)
        are_you_happy_with_selected(new_pick, "destination")


def user_input_function(user_input):
    if user_input == "No":
        print("Okay, lets change that!")
        not_okay = False
        return not_okay
    elif user_input == "Yes":
        print("Awesome! Lets move on. ")
        yes_okay = True
        return yes_okay


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


def confirmation(list_to_confirm):
    print("Lets go over what you've selected.")
    print(f"Destination: {perfect_trip[0]}")
    print(f"Transportation: {perfect_trip[1]}")
    print(f"Restaurant: {perfect_trip[2]}")
    print(f"Entertainment {perfect_trip[3]}")
    print("Would you like to finalize this trip?")


def finalize(list_to_confirm):
    finalize_trip = input("Yes/No ")
    if finalize_trip == "Yes":
        print(
            f"Here is the plan for your trip. First, you will be going to {perfect_trip[0]}, While there, your transpertation will be {perfect_trip[1]}. You will eat at {perfect_trip[2]}. Finally, your entertainment will be {perfect_trip[3]}.")
    else:

        print("No problem! Please start over and we can make a new trip!"))


print("Welcome to the day trip generator! I hope you're ready for the perfect vacation!")
greeting("Trip")
selected_item_from_list=(random_selection(destinations))
user_input=are_you_happy_with_selected(
    selected_item_from_list, "destination")
user_answer=user_input_function(user_input)
while user_answer == False:
    selected_item_from_list=(random_selection(destinations))
    user_input=are_you_happy_with_selected(
        selected_item_from_list, "destination")
    user_answer=user_input_function(user_input)
else:
    perfect_trip.append(selected_item_from_list)


greeting("transportation")
selected_item_from_list=(random_selection(transportation_options))
user_input=are_you_happy_with_selected(
    selected_item_from_list, "transportation")
user_answer=user_input_function(user_input)
while user_answer == False:
    selected_item_from_list=(random_selection(transportation_options))
    user_input=are_you_happy_with_selected(
        selected_item_from_list, "transportation")
    user_answer=user_input_function(user_input)
else:
    perfect_trip.append(selected_item_from_list)


greeting("restraunt")
selected_item_from_list=(random_selection(restraunts))
user_input=are_you_happy_with_selected(
    selected_item_from_list, "restraunt")
user_answer=user_input_function(user_input)
while user_answer == False:
    selected_item_from_list=(random_selection(restraunts))
    user_input=are_you_happy_with_selected(
        selected_item_from_list, "restraunt")
    user_answer=user_input_function(user_input)
else:
    perfect_trip.append(selected_item_from_list)


greeting("entertainment")
selected_item_from_list=(random_selection(entertainment))
user_input=are_you_happy_with_selected(
    selected_item_from_list, "entertainment")
user_answer=user_input_function(user_input)
while user_answer == False:
    selected_item_from_list=(random_selection(entertainment))
    user_input=are_you_happy_with_selected(
        selected_item_from_list, "entertainment")
    user_answer=user_input_function(user_input)
else:
    perfect_trip.append(selected_item_from_list)

confirmation(perfect_trip)
finalize(perfect_trip)


print(perfect_trip)
