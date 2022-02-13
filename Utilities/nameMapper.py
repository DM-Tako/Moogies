# TODO: To Upgrade this class when DB storage is in place



## Map name to ID for mapping
def mentionViaPersonalName(name):
  if(name.casefold() == 'Andy'.casefold()):
    return '<@407072361842606092>'
  elif(name.casefold() == 'Dom'.casefold()):
    return '<@180248652785254410>'
  else:
    return '@everyone'


## Map ID to nam
def mentionViaId(id, personal):
  if(personal == 'yes'):
    if(str(id) == '407072361842606092'):
      return 'Andy'
    elif(str(id) == '180248652785254410'):
      return 'Dom'
    else:
      return 'Everyone'
  elif(personal == 'no'):
    if(str(id) == '407072361842606092'):
      return '<@407072361842606092>'
    elif(str(id) == '180248652785254410'):
      return '<@180248652785254410>'
    else:
      return '@everyone'

  else:
    return ''