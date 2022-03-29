#강화

import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def reinforce(ctx):
    dir = db.reference(f"{ctx.author.id}/현재위치")
    location = dir.get()
    dir = db.reference(f"{ctx.author.id}/돈")
    money = dir.get()
    dir = db.reference(f"{ctx.author.id}/강화최대돈")
    maxmoney = dir.get()
    dir = db.reference(f"{ctx.author.id}/채굴력")
    power = dir.get()
    dir = db.reference(f"{ctx.author.id}/곡괭이 레벨")
    picklv = dir.get()

    abcde = ['곡산마을','태초마을']
    if location not in abcde:
      await ctx.reply('강화는 `태초마을/곡산마을`에서만 가능합니다.')
      return None
    if money < maxmoney:
      m = maxmoney - money
      await ctx.reply(f'강화를 할려면 {maxmoney}원이 필요합니다.\n현재 {m}원이 부족합니다.')
      return None


    h = random.randrange(1,8)
    p = h * 5





    ##10레벨 이하는 100퍼
    if picklv <= 10:
      picklvd = picklv + h
      powerd = power + p
      
      await ctx.reply(f'강화에 `성공`하였습니다!\n> 곡괭이레벨  : {picklv}LV -> {picklvd}LV\n> 채굴력 : {power} - > {powerd}')
      dir = db.reference(f"{ctx.author.id}")
      dir.update({'곡괭이 레벨' : picklvd})
      dir.update({'채굴력' : powerd})
      money = money - maxmoney
      dir = db.reference(f"{ctx.author.id}")
      dir.update({'돈' : money})
      maxmoney = maxmoney + h * 20
      dir.update({'강화최대돈' : maxmoney})
      return None
    
    

    succus = random.randrange(1,7)
    fail = random.randrange(1,7)
    suc = random.randrange(1,101)
    print(f'{succus},{fail},{suc}')

    if suc <= 7:
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      s = str(dir.get())
      if '대장장이의_손길' in s:
        asb = random.randrange(1,11)
        if asb > 5:
          await ctx.reply(f'곡괭이가 7%의 확률로 `파괴`될뻔 했지만 `대장장이의 손길`로 살아났습니다!')
          return None
      await ctx.reply(f'곡괭이가 5%의 확률로 `파괴`되었습니다....\n> 곡괭이레벨 : {picklv}LV -> 1LV\n> 채굴력 : {power} - > 10')
      dir = db.reference(f"{ctx.author.id}")
      dir.update({'채굴력' : 10})
      dir.update({'강화최대돈' : 1000})
      dir.update({'곡괭이 레벨' : 1})
      return None
    

    if succus == fail:#강화실패
      picklvd = picklv - h
      powerd = power - p
      
      await ctx.reply(f'강화에 `실패`하였습니다....\n> 곡괭이레벨 : {picklv}LV -> {picklvd}LV\n> 채굴력 : {power} - > {powerd}')
      dir = db.reference(f"{ctx.author.id}")
      dir.update({'곡괭이 레벨' : picklvd})
      dir.update({'채굴력' : powerd})
      money = money - maxmoney
      dir = db.reference(f"{ctx.author.id}")
      dir.update({'돈' : money})
      maxmoney = maxmoney - (h*20)
      dir.update({'강화최대돈' : maxmoney})
      return None
    
    
    picklvd = picklv + h
    powerd = power + p
      
    await ctx.reply(f'강화에 `성공`하였습니다!\n> 곡괭이레벨 : {picklv}LV -> {picklvd}LV\n> 채굴력 : {power} - > {powerd}')
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'곡괭이 레벨' : picklvd})
    dir.update({'채굴력' : powerd})
    money = money - maxmoney
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'돈' : money})
    maxmoney = maxmoney + h* 20
    dir.update({'강화최대돈' : maxmoney})




