import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def lvup(ctx):
    dir = db.reference(f"{ctx.author.id}/경험치")
    exp = dir.get()
    dir = db.reference(f"{ctx.author.id}/최대경험치")
    maxexp = dir.get()

    if exp >= maxexp:
        dir = db.reference(f"{ctx.author.id}/경험치")
        exp = dir.get()
        dir = db.reference(f"{ctx.author.id}/최대경험치")
        maxexp = dir.get()
        dir = db.reference(f"{ctx.author.id}/레벨")
        lv = dir.get()
        lv = lv + 1
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'레벨' : lv})
        ddd = exp - maxexp
        dir.update({'경험치' : ddd})
        maxexp = maxexp + (50 * lv)
        dir.update({'최대경험치' : maxexp})
        dir = db.reference(f"{ctx.author.id}/최대스테미너")
        st = dir.get()
        st = st + 20
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'최대스테미너' : st})
        dir.update({'스테미너' : st})
    
        await ctx.reply(f"```cs\n{lv}레벨 달성!\n\n최대 스테미너가 {st}로 증가했습니다.\n스테미너가 전부 회복되었습니다.\n```")

        if lv == 5:
          await ctx.send(
            '```css\n스킬획득!\n\n<SKILL : 단전호흡>을 획득하였습니다!\n기능 : 스테미너 소모속도 감소\n```')
          dir = db.reference(f"{ctx.author.id}/스킬보유")
          skm = dir.get()
          skn = ['단전호흡']
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스킬보유' : skm + skn})

        if lv == 10:
          await ctx.send(
            '```cs\n스킬획득!\n\n<SKILL : 축지법>을 획득하였습니다!\n기능 : 채굴시 광물 2배 경험치 1.5배 증가\n```')
          dir = db.reference(f"{ctx.author.id}/스킬보유")
          skm = dir.get()
          skn = ['축지법']
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스킬보유' : skm + skn})



        dir = db.reference(f"{ctx.author.id}/경험치")
        exp = dir.get()
        dir = db.reference(f"{ctx.author.id}/최대경험치")
        maxexp = dir.get()
        while exp >= maxexp:
          dir = db.reference(f"{ctx.author.id}/경험치")
          exp = dir.get()
          dir = db.reference(f"{ctx.author.id}/최대경험치")
          maxexp = dir.get()
          if exp <= 0:
            return None
          dir = db.reference(f"{ctx.author.id}/레벨")
          lv = dir.get()
          lv = lv + 1
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'레벨' : lv})
          if exp < maxexp:
            return None
          ddd = exp - maxexp
          if ddd < 0:
            return None
          dir.update({'경험치' : ddd})
          maxexp = maxexp + (50 * lv)
          dir.update({'최대경험치' : maxexp})
          dir = db.reference(f"{ctx.author.id}/최대스테미너")
          st = dir.get()
          st = st + 50
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'최대스테미너' : st})
          dir.update({'스테미너' : st})
    
          await ctx.reply(f"```cs\n{lv}레벨 달성!\n\n최대 스테미너가 {st}로 증가했습니다.\n스테미너가 전부 회복되었습니다.\n```")

          if lv == 5:
            await ctx.send(
              '```css\n스킬획득!\n\n<SKILL : 단전호흡>을 획득하였습니다!\n기능 : 스테미너 소모속도 감소\n```')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'스킬보유' : ['응급처치','단전호흡']})

          if lv == 10:
            await ctx.send(
              '```cs\n스킬획득!\n\n<SKILL : 축지법>을 획득하였습니다!\n기능 : 채굴시 광물 2배 경험치 1.5배 증가\n```')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'스킬보유' : ['응급처치','단전호  흡','축지법']})
          if exp < maxexp:
            return None
          await asyncio.sleep(1.0)