import numpy as np
## Yabai 1 -https://64.media.tumblr.com/37f81a33307252f3935132d9bcd5988b/tumblr_nsvh87aE8o1st2hpko1_540.gifv

## Big brain 
## 


## Generate random cheer of memes url
def return_cheer():
  random = __numberGenerator(5) 
  
  if random == 1:
    return 'https://c.tenor.com/7LXNeJqHry0AAAAC/himouto-party.gif'
  elif random == 2:
    return 'https://c.tenor.com/iDwEk9lG3rIAAAAC/saber-dance.gif'
  elif random == 3:
    return 'https://media1.giphy.com/media/m8Z2UqDYU20SY/giphy.gif'
  elif random == 4:
    return 'https://c.tenor.com/660xvspq7swAAAAM/nanashi-mumei-nanashi.gif'
  else:
    return 'https://c.tenor.com/7LXNeJqHry0AAAAC/himouto-party.gif'

## Generate random hello meme
def return_hello():
  random = __numberGenerator(3)

  if random == 1:
    return 'https://c.tenor.com/lUFliafCu_MAAAAM/hello.gif'
  if random == 2:
    return 'https://c.tenor.com/pvFJwncehzIAAAAM/hello-there-private-from-penguins-of-madagascar.gif'
  else:
    return ''

## Generate random big brain meme
def return_brain():
  random = __numberGenerator(7)

  if random == 1:
    return 'https://c.tenor.com/TgPXdDAfIeIAAAAd/gawr-gura-gura.gif'
  if random == 2:
    return 'https://c.tenor.com/smmsu2CX0yYAAAAM/loading-mumei.gif'
  if random == 3:
    return 'https://c.tenor.com/mtJLmTOlJ_gAAAAC/nenomae-inanis-inanis.gif'
  if random == 4:
    return 'https://c.tenor.com/K3LslQdLo04AAAAd/inugami-korone-hololive.gif'
  else:
    return 'https://c.tenor.com/qjFOSfNKedIAAAAM/nanashi-mumei-hololive.gif'

##  Generate nope meme
def return_nope():
  random = __numberGenerator(3)

  if random == 1:
    return 'https://c.tenor.com/cL8_kHp3L7MAAAAd/roboco-panic-hologra.gif'
  else:
    return 'https://media0.giphy.com/media/yMaLDA976YtUs/200.gif'

## Generator number
def __numberGenerator(maxMeme):
  return np.random.randint(low = 0, high = maxMeme , size=1)