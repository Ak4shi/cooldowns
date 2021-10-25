import time
import os
import json


class utils:
  def gettime():
    current = time.asctime( time.localtime(time.time()))
    current = current.split()
    current = current[3]
    current = current.replace(":"," ")
    current = current.split()
    hours = current[0]
    minutes = current[1]
    sec = current[2]
    return current

  def getsecs():
    current = utils.gettime()
    hours = current[0]
    minutes = current[1]
    sec = current[2]
    sec = int(sec)
    e = int(hours)*360
    sec += int(e)
    f = int(minutes)*60

    sec += int(f)
    return sec

  def roundcd(seconds):
    sec = utils.getsecs()
    if int(sec) > int(seconds):
      return
    sec = int(seconds) - int(sec)
    if sec < 60:
      return f"{round(sec)} second(s)"
    if sec < 360:
      return f"{round(sec/60)} minute(s)"
    if sec < 21600:
      return f"{round(sec/360)} hour(s)"
    if sec < 86400:
      return f"{round(sec/21600)} day(s)"


def getkeys():
  files = []
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "cdkeys.json" not in files:
    print("-------\n Cooldown: Creating Core...\n")
    os.system("touch cdkeys.json")
    with open("cdkeys.json","w") as x:
      x.write("{}")
    print("-------\n Cooldown: Created Core!\n")
  with open("cdkeys.json","r") as z:
    y = json.load(z)
  return y
def writekeys(data):
  files = []
  for file in os.listdir(os.getcwd()):
    files.append(file)
  if "cdkeys.json" not in files:
    print("-------\n Cooldown: Creating Core...\n")
    os.system("touch cdkeys.json")
    with open("cdkeys.json","w") as x:
      x.write("{}")
  with open("cdkeys.json","w") as z:
    json.dump(data,z)
  return True
def loadcd(id,command,seconds):
  id = str(id)
  seconds = int(seconds)
  rn = utils.getsecs()
  tobe = rn + seconds
  cdkeys = getkeys()
  if id not in cdkeys:
    cdkeys[id] = {}
  if command not in cdkeys[id]:
    cdkeys[id][command] = tobe
    writekeys(cdkeys)
  if command in cdkeys[id]:
    raise ValueError(f"Cooldown for {command} already exists in keys")

def resetcd(id,command):
  id = str(id)
  cdkeys = getkeys()
  if id not in cdkeys:
    cdkeys[id] = {}
  if command in cdkeys[id]:
    del cdkeys[id][command]
    if cdkeys[id] == {}:
      del cdkeys[id]
    writekeys(cdkeys)
  if command not in cdkeys[id]:
    raise ValueError(f"Cooldown for {command} doesn't exist in keys")
def addcd(ctx,seconds):
  loadcd(str(ctx.author.id),ctx.command.name,seconds)
  
def getcdleft(ctx):
  cdkeys = getkeys()
  rn = utils.getsecs()
  if str(ctx.author.id) in cdkeys:
    if ctx.command.name in cdkeys[str(ctx.author.id)]:
      sec = cdkeys[str(ctx.author.id)][ctx.command.name]
      if int(rn) > int(sec):
        return
      e = sec - rn
      return int(e)

def getcd(ctx):
  cdkeys = getkeys()
  rn = utils.getsecs()
  if str(ctx.author.id) in cdkeys:
    if ctx.command.name in cdkeys[str(ctx.author.id)]:
      sec = cdkeys[str(ctx.author.id)][ctx.command.name]
      print(sec)
      return int(sec)



def cooldown(ctx):
  cdkeys = getkeys()
  try:
    rn = utils.getsecs()
    if int(rn) != int(cdkeys[str(ctx.author.id)][ctx.command.name]) and int(rn) < int(cdkeys[str(ctx.author.id)][ctx.command.name]):
      return True
    if int(rn) == int(cdkeys[str(ctx.author.id)][ctx.command.name]) or int(rn) > int(cdkeys[str(ctx.author.id)][ctx.command.name]):
      resetcd(str(ctx.author.id),ctx.command.name)
      return False
  except KeyError:
    return False

async def checkcd(ctx):
  if cooldown(ctx):
      left = cooldowns.getcd(ctx)
      left = cooldowns.utils.roundcd(left)
      await ctx.send(f"Cannot use command `{left}` left")
      return True

