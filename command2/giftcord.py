import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def giftcord(ctx, gift):
  dir = db.reference(f"{ctx.author.id}/돈")
  money = dir.get()
  if money < 1000:
    await ctx.reply('선물가챠는 1000원의 비용이 들어갑니다')
    return None
  git = random.choice(gift)
  dir = db.reference(f"{ctx.author.id}/곡산대륙/선물/{git}")
  gits = dir.get()
  gits = gits + 1
  dir = db.reference(f"{ctx.author.id}/곡산대륙/선물")
  dir.update({f"{git}" : gits})
  await ctx.reply(f'{git} 획득!\n> 보유 선물 갯수 {gits}개')
  money = money - 1000
  dir = db.reference(f"{ctx.author.id}")
  dir.update({'돈' : money})