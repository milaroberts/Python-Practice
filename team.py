# TODO Create an empty list to maintain the player names
players = []


# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
add_playersq = input("Would you like to add players to the list? Enter yes or no  ").lower()

while add_playersq == "yes":
    add_player = str(input("Add the name of the player to list?  "))
    players.append(add_player)
    add_playersq = input("Would you like to add players to the list? Enter yes or no  ").lower()


# TODO print the number of players on the team
print("\nThere are {} players on the team.".format(len(players)))
  

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in players:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

# TODO Select a goalkeeper from the above roster
goalkeeper = input("Please select a player to be the goalkeeper by selecting the player number. (1 - {})  ".format(len(players)))
goalkeeper = int(goalkeeper)

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Your goalkeeper is {}!".format(players[goalkeeper - 1]))
