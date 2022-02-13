import requests

## THERE IS A LIMIT TO API CALL WITHIN A TIME FRAME 
##  BEFORE YOU GET BLOCKED
##  https://discord.com/developers/docs/topics/rate-limits

# Dnd category list
def get_Category_List():
  return '```***Available categories for api***\n\nability-scores\nskills\nproficiencies\nlanguages\nalignment\nbackgrounds\nclasses\nsubclasses\nfeatures\nraces\nsubraces\ntraits\nequipment-categories\nequipment\nmagic-items\nweapon-properties\nspells\nfeats\nmonsters\nconditions\ndamage-types\nmagic-schools\nrules\n```'

# Dnd API to get search
def search_dnd_api(category, name, user):
  apiUrl = 'https://www.dnd5eapi.co/api/'
  
  if not name == None or not user == None:
    apiUrl = 'https://www.dnd5eapi.co/api/' + category + '/' + name + '/'

  response = requests.get(apiUrl).json()

  if category == 'ability-scores':
    return __getAbilityScores(response)
  elif category == 'skills':
    return __getSkills(response)
  elif category == 'proficiencies':
    return __getProficiencies(response)
  elif category == 'languages':
    return __getLanguages(response)
  elif category == 'alignments':
    return __getAlignments(response)
  elif category == 'backgrounds':
    return __getBackgrounds(response)
  elif category == 'classes':    
    return __getClasses(response)
  elif category == 'subclasses':
    return __getSubClasses(response)
  elif category == 'features':
    return __getFeatures(response)
  elif category == 'races':
    return __getRaces(response)
  elif category == 'subraces':
    return __getSubRaces(response)
  elif category == 'traits':
    return __getTraits(response)
  elif category == 'equipment':
    return __getEquipments(response)
  elif category == 'magic-items':
    return __getMagicItems(response)
  elif category == 'weapon-properties':
    return __getWeaponProperties(response)
  elif category == 'spells':
    return __getSpells(response)
  elif category == 'feats':
    return __getFeats(response)
  elif category == 'monsters':
    return __getMonsters(response)
  else:
    return "```Dont pop my single brain cell, cant find such command! use $info to summon the sacred tome```"

# Dnd Json Parsers for ability scores
def __getAbilityScores(response):
  return '```Description:\t' + "\n".join(map(str,response['desc'])) + '\n\nSkills affected:\t' + ", ".join(map(str, __getNestJsonValue(response, 'skills', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for skills
def __getSkills(response):
  return '```Description:\t' + "\n".join(map(str, response['desc'])) + '\n\nAbility Score:\t' + response['ability_score']['name'] + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for skills
def __getProficiencies(response):
  return '```Item name:\t' + response['name'] + '\n\nClasses:\t' +  ", ".join(map(str, __getNestJsonValue(response, 'classes', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Languages
def __getLanguages(response):
   return '```Language:\t' + response['name'] + '\n\nTypical Speakers:\t' +  ", ".join(map(str,response['typical_speakers'])) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Alignments
def __getAlignments(response):
   return '```Name:\t' + response['name'] + '\n\nDesc:\t' +  response['desc'] + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Backgrounds
def __getBackgrounds(response):
   return '```Name:\t' + response['name'] + "\nStarting Proficiencies:\t"+", ".join(map(str, __getNestJsonValue(response, 'starting_proficiencies', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Classes
def __getClasses (response):
   return '```Name:\t' + response['name'] + "\nHit_die:\t" +  str(response['hit_die']) + "\nProficiencies:\t" + ", ".join(map(str, __getNestJsonValue(response, 'proficiencies', 'name'))) + "\nSaving throws:\t" +  ", ".join(map(str, __getNestJsonValue(response, 'saving_throws', 'name'))) + '\nStarting Equipment:\t' + ", ".join(map(str, __getDualNestJsonValue(response, 'starting_equipment', 'equipment', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for SubClasses
def __getSubClasses(response):
   return '```Name:\t' + response['name'] + "\nSubclass flavor:\t" + response['subclass_flavor'] + "\nDesc:\t" + "\n".join(map(str, response['desc'])) +  '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Features
def __getFeatures(response):
  return '```Name:\t' + response['name'] + "\nSubclass flavor:\t" + response['level'] + "\nDesc:\t" + "\n".join(map(str, response['desc'])) +  '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Races
def __getRaces(response):
  return '```Name:\t' + response['name'] + "\nSpeed:\t" + str(response['speed']) + "\nAlignment:\t" + response['alignment'] + '\nLanguages:\t' + ", ".join(map(str, __getNestJsonValue(response, 'languages', 'name'))) + '\nTraits:\t' + ", ".join(map(str, __getNestJsonValue(response, 'traits', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Sub-Races
def __getSubRaces(response):
  return '```Name:\t' + response['name'] + "\nRace:\t" + str(response['race']['name']) + "\nDesc:\t" + response['desc'] + '\nAbility Bonus:\t' + ", ".join(map(str, __getDualNestJsonValue(response, 'ability_bonuses', 'ability_score', 'name'))) + '\nLanguages:\t' + ", ".join(map(str, response['languages'])) + ", ".join(map(str, __getNestJsonValue(response, 'racial_traits', 'name'))) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Traits
def __getTraits(response):
  return '```Name:\t' + response['name'] + "\nDesc:\t" + ", ".join(map(str, __getNestJsonValue(response, 'races', 'name'))) + "\nDesc:\t" + "\n".join(map(str,response['desc'])) + '\n\nUrl: ' + response['url'] + '```' 

# Dnd Json Parsers for Weapon
def __getEquipments(response):
  return '```Name:\t' + response['name'] + "\nWeapon Category:\t" + response['weapon_category'] + "\nWeapon Range:\t" + response['weapon_range'] + "\nDamage:\t" + response['damage']['damage_dice'] + "\nDamage Type:\t" + response['damage']['damage_type']['name'] + '\n\nUrl: ' + response['url'] + '```' 

# Dnd Json Parsers for Magic Items
def __getMagicItems(response):
  return '```Name:\t' + response['name'] + "\nDesc:\t" +  "\n".join(map(str,response['desc'])) + '\n\nUrl: ' + response['url'] + '```' 

# Dnd Json Parsers for Weapon Properties
def __getWeaponProperties(response):
  return '```Name:\t' + response['name'] + "\nDesc:\t" +  "\n".join(map(str,response['desc'])) + '\n\nUrl: ' + response['url'] + '```' 

# Dnd Json Parsers for Spells
def __getSpells(response):
  return '```Name:\t' + response['name'] + "\nDesc:\t" +  "\n".join(map(str,response['desc'])) +  "\nHigher Level:\t" +  "\n".join(map(str,response['higher_level'])) + "\nRange:\t" + response['range'] + "\nDuration:\t" + response['duration'] + "\nConcentration:\t" + str(response['concentration']) + "\nCasting Time::\t" + response['casting_time'] + "\nDamage Type:\t" + response['damage']['damage_type']['name'] + "\nDamage at slot level:\n " + str(response['damage']['damage_at_slot_level']).replace(',','\n').replace('{','').replace('}', '') + '\n\nUrl: ' + response['url'] + '```' 

# Dnd Json Parsers for Feats
def __getFeats(response):
  return "```Name:\t" + response['name'] + '\nDesc:\t' +  "\n".join(map(str,response['desc'])) + '\n\nUrl: ' + response['url'] + '```'

# Dnd Json Parsers for Monsters
def __getMonsters(response):
  return '```Name:\t' + response['name'] + '\nAlignment:\t' + response['alignment'] + "\nArmor Class:\t" + str(response['armor_class']) + "\HP:\t" + str(response['hit_points']) + "\nHit Dice:\t" + response['hit_dice'] + "\nStr:\t" + str(response['strength']) + "\nDex:\t" + str(response['dexterity']) + "\nCon:\t" + str(response['constitution']) + "\nInt:\t" + str(response['intelligence']) + "\nWis:\t" + str(response['wisdom']) + "\nCha:\t" + str(response['charisma']) + '\nLanguages:\t' +  response['languages'] + '\n\nUrl: ' + response['url'] + '```'

# Getting specific fields from nested json
def __getNestJsonValue(response, field, nestedfield):
  namelist = []

  for each in response[field]:
    namelist.append(each[nestedfield])

  return namelist

# Getting specific fields from nested json double tag
def __getDualNestJsonValue(response, field, nestedfield1, nestedfield2):
  namelist = []

  for each in response[field]:
    namelist.append(each[nestedfield1][nestedfield2])

  return namelist