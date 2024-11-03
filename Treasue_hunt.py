print("Welcome to the Enchanted Forest.")
print("Your mission is to retrieve the Lost Crystal of Eternity.")

response = input("You are standing before two ancient paths, each leading into dense woods. \n Type 'mystic' to take the mystic path, or 'shadow' to take the shadowy path.\n")

if response.lower() == "mystic":
    choice = input("You encounter a shimmering river with magical fish jumping out. \n Type 'whistle' to play a tune and wait for help, or 'cross' to walk through the water.\n")
    if choice.lower() == "whistle":
        door_choice = input(
            "A friendly spirit appears and ferries you across safely. You find a mystical hut with 3 glowing doors: \n one silver, one emerald, and one amber.\n Which door do you choose?\n")
        if door_choice.lower() == "emerald":
            print("The door creaks open, revealing the Crystal of Eternity! You win!")
        else:
            print("A trap activates, and you fall into a chasm. Game Over.")
    elif choice.lower() == "cross":
        print("A whirlpool appears, and you're pulled under! Game Over.")

elif response.lower() == "shadow":
    choice = input("You find yourself lost in the thick fog. A whispering voice offers you two choices: \n Type 'follow' to follow the voice, or 'ignore' to navigate alone.\n")
    if choice.lower() == "follow":
        print("The voice leads you in circles, and you are forever trapped in the fog. Game Over.")
    elif choice.lower() == "ignore":
        door_choice = input(
            "You break free from the fog and reach an old stone archway with 3 doors: \n one black, one gold, and one sapphire.\n Which door do you choose?\n")
        if door_choice.lower() == "gold":
            print(
                "You enter a hidden sanctuary, where the Crystal of Eternity awaits. You win!")
        else:
            print("The door shuts behind you, trapping you in darkness. Game Over.")

else:
    print("You wander off the path and become hopelessly lost in the forest. Game Over.")
