from Commands import rolldice_command

## Retrieval of players initiative information 
def retrieve_players_info(combatantList, args):
  name,diceinfo = args

  print("Retrieve_players_info: args: " + str(args) + " Name of player: " + name + " Dice roll: " + diceinfo)

  dice_details = rolldice_command.get_DiceDetails(str(diceinfo))
  initiative = sum(rolldice_command.diceRoll(dice_details[0], dice_details[1], dice_details[2]))

  print('Name: ' + name + ' Initiative: ' + str(initiative))
  combatantList[name] = initiative
  combatantList = __order_combatant_by_initiative(combatantList)

  print("Retrieve_players_info [Sorted Combatent List])" + print_combatantList(combatantList))
  
  return combatantList

## Print the Dictionary
def print_combatantList(combatantList):
  replyString = ''
  playerCount = 0
  
  for item in combatantList:
    print(playerCount)
    if playerCount == 0:
      replyString += "\n-Player name: " + item + "\tInitiative: " + str(combatantList[item])
    else:
      replyString += "\nPlayer name: " + item + "\tInitiative: " + str(combatantList[item])
    playerCount += 1

  return replyString

## Order the list
def __order_combatant_by_initiative(combatantList):
  return dict(sorted(combatantList.items(), key=lambda x: x[1], reverse=True))