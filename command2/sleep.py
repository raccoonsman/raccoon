import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio



async def sleep(ctx):
  dir = db.reference(f'{ctx.author.id}/곡산대륙/현재시간')
  chtime = dir.get()
  if chtime != '밤':
    if chtime != '새벽':
      await ctx.reply('밤에서만 잘 수 있습니다')
      return None
  dir = db.reference(f'{ctx.author.id}/현재위치')
  local = dir.get()
  if local != '곡산마을':
    await ctx.reply('`곡산마을`에서만 취침이 가능합니다')
    return None

  msg = await ctx.reply('아침까지 5초...')
  await asyncio.sleep(5.0)
  await ctx.reply('아침이 되었습니다.')
  await msg.delete()
  dir = db.reference(f'{ctx.author.id}/곡산대륙')
  dir.update({'현재시간' : '오전'})
  dir.update({'시간' : 2})