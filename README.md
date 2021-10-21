# cooldowns
a custom discord.py cooldown module

# Usage:

### Example:
```python
import cooldowns
@bot.command(aliases=["e"])
async def hello(ctx):
  if cooldowns.checkcd(ctx): # checks for cooldown
    return
  
  await ctx.send("command ran")
  cooldowns.addcd(ctx,10) # starts cooldown must be in seconds!!!
```

### Functions:

```python
import time
import os
import json


class utils:
  def gettime(): # gets the current time in a list
    current = time.asctime( time.localtime(time.time()))
    current = current.split()
    current = current[3]
    current = current.replace(":"," ")
    current = current.split()
    hours = current[0]
    minutes = current[1]
    sec = current[2]
    return current

  def getsecs(): # converts current time to seconds
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

  def roundcd(seconds): # returns rounded cooldown in text with unit
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


getkeys - get key data

loadcd - load cooldowns in key data

resetcd - delete cooldown from key data
  
getcdleft - get amount of cooldown left in seconds

getcd - get the time in seconds the cooldown stops

cooldown - check/reset for cooldown

checkcd - function to check for cooldown and send how much time is left in channel

```
