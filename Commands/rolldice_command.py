import numpy as np

# Method for rolling dice
def return_diceRoll(args, author):
  # Removing command string
  args = args.replace('roll ','')
  replyString = ''
  # Check for command format and throw error
  if not args[:1].isdigit():
    replyString = '```*Wrong command format! Use $info to find out more*```'
    return replyString

  dice_details = get_DiceDetails(args)

  # Roll the dice
  diceroll_list = diceRoll(dice_details[0], dice_details[1], dice_details[2])

  # Reply String concatenation
  replyString ="```Dice Rolls for " + author + "'s " + args + " is\n" + ", ".join(map(str,diceroll_list)) + "\n\nTotal: " + str(sum(diceroll_list))

  if((20 + int(dice_details[2])) in diceroll_list):
    replyString += "\n\nNAT 20, DA BIG BONK STICK"
  if((1 + int(dice_details[2])) in diceroll_list):
    replyString += "\n\nNINOMAE, The exit is that way"
  replyString += "```"

  return replyString

  
# method to retrieve dice details
def get_DiceDetails(args):
  modifier = 0

  # command example : !1d12+3; consist of 3 arguments
  # 1   - No of Dice to roll
  # 12  - Die Sides
  # 3   - Modifer
  if "-" in args:
    args_details = args.split('-')
    modifier = int(args_details[1]) * -1
  elif "+" in args:
    args_details = args.split('+')
    modifier = int(args_details[1])
  else:
    args_details = args.split(" ")

  dice_details = args_details[0].split('d')
  dice_details.append(modifier)

  return dice_details

# static method for dice rolling
def diceRoll(totalDice, dieSide, modifier):
  return np.random.randint(low = 1 + int(modifier), high = int(dieSide) + 1 + int(modifier), size=int(totalDice)) 

