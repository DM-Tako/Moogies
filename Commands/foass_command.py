import requests
import random

## FOASS API
## http://foaas.com/off/Tom/Everyone?shoutcloud.
foassUrl = 'http://foaas.com'

ENDPOINTS = [
  "/absolutely/:company/:from",
    "/anyway/:company/:from",
    "/asshole/:from",
    "/awesome/:from",
    "/back/:name/:from",
    "/bag/:from",
    "/ballmer/:name/:company/:from",
    "/bday/:name/:from",
    "/because/:from",
    "/blackadder/:name/:from",
    "/bm/:name/:from",
    "/bucket/:from",
    "/bus/:name/:from",
    "/bye/:from",
    "/chainsaw/:name/:from",
    "/cocksplat/:name/:from",
    "/cool/:from",
    "/cup/:from",
    "/dalton/:name/:from",
    "/dense/:from",
    "/deraadt/:name/:from",
    "/diabetes/:from",
    "/donut/:name/:from",
    "/dumbledore/:from",
    "/equity/:name/:from",
    "/even/:from",
    "/everyone/:from",
    "/everything/:from",
    "/family/:from",
    "/fascinating/:from",
    "/fewer/:name/:from",
    "/flying/:from",
    "/ftfy/:from",
    "/fts/:name/:from",
    "/fyyff/:from",
    "/gfy/:name/:from",
    "/give/:from",
    "/holygrail/:from",
    "/horse/:from",
    "/idea/:from",
    "/immensity/:from",
    "/ing/:name/:from",
    "/jinglebells/:from",
    "/keep/:name/:from",
    "/keepcalm/:reaction/:from",
    "/king/:name/:from",
    "/legend/:name/:from",
    "/life/:from",
    "/linus/:name/:from",
    "/logs/:from",
    "/look/:name/:from",
    "/looking/:from",
    "/lowpoly/:from",
    "/madison/:name/:from",
    "/maybe/:from",
    "/me/:from",
    "/mornin/:from",
    "/no/:from",
    "/nugget/:name/:from",
    "/off/:name/:from",
    "/outside/:name/:from",
    "/particular/:thing/:from",
    "/pink/:from",
    "/problem/:name/:from",
    "/programmer/:from",
    "/question/:from",
    "/ratsarse/:from",
    "/retard/:from",
    "/ridiculous/:from",
    "/rockstar/:name/:from",
    "/rtfm/:from",
    "/sake/:from",
    "/shakespeare/:name/:from",
    "/shit/:from",
    "/shutup/:name/:from",
    "/single/:from",
    "/thanks/:from",
    "/that/:from",
    "/think/:name/:from",
    "/thinking/:name/:from",
    "/this/:from",
    "/thumbs/:name/:from",
    "/too/:from",
    "/tucker/:from",
    "/understand/:name/:from",
    "/version",
    "/waste/:name/:from",
    "/what/:from",
    "/xmas/:name/:from",
    "/yeah/:from",
    "/yoda/:name/:from",
    "/you/:name/:from",
    "/zayn/:from",
    "/zero/:from"
]

header = {
    "Accept": "application/json"
}

## return api for FOASS call
def foass_praise(name):
  url = foassUrl + random.choice(ENDPOINTS)
  
  if ":name" in url:
    url = url.replace(":name", str(name))
  if ":category" in url:
    url = url.replace(":category", str(name))
  if ":from" in url:
    url = url.replace(":from", "Moogie")
  if ":reaction" in url:
    url = url.replace(":reaction", "watch ina")
  if ":reference" in url:
    url = url.replace(":reference", "Moogie")
  if ":something" in url:
    url = url.replace(":something", "marshmallow dance")
  if ":tool" in url:
    url = url.replace(":tool", "Moogie")
  if ":company" in url:
    url = url.replace(":company", "everyone")
  if ":noun" in url:
    url = url.replace(":noun", "waifu")
  if ":behavior" in url:
    url = url.replace(":behavior", "not eating ramen")
  if ":thing" in url:
    url = url.replace(":thing", "2.4")
  if ":language" in url:
    url = url.replace(":language", "memes")
  
  response = requests.get(url, headers=header).json()

  return str("```" + response['message'] + response['subtitle'] + "```")
