import disnake
from disnake.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import uuid
from datetime import datetime, timedelta


async def gotime(ctx):
  dir = db.reference(f'{ctx.author.id}/곡산대륙/시간')
  timecheck = dir.get()
  if timecheck == 1:
    timeto = '오전'
    times = 2
    await ctx.send('오전이 되었습니다.')
  elif timecheck == 2:
    timeto = '낮'
    times = 3
  elif timecheck == 3:
    timeto = '저녁'
    times = 4
  elif timecheck == 4:
    timeto = '밤'
    times = 5
    await ctx.send('밤이 되었습니다. 소모되는 스테미너가 증가되니다')
  elif timecheck == 5:
    timeto = '새벽'
    times = 1

  dir = db.reference(f'{ctx.author.id}/곡산대륙')
  dir.update({'현재시간' : timeto})
  dir.update({'시간' : times})
    