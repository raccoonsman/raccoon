import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def embarkation(ctx, bot):
  dir = db.reference(f"{ctx.author.id}/곡산대륙/업뎃")
  updat = dir.get()
  if updat != 3:
    dir = db.reference(f"{ctx.author.id}/곡산대륙")
    dir.update({'현재시간' : '오전'})
    dir.update({'시간' : 1})
    dir.update({'강화권' : 0})
    dir.update({'업뎃' : 3})
    dir.update({'시간의조각' : 0})
    dir = db.reference(f"{ctx.author.id}/곡산대륙/NPC")
    dir.update({'대장장이' : 0})
    dir.update({'상인' : 0})
    dir.update({'NPC1' : 0})
    dir.update({'NPC2' : 0})
    dir.update({'NPC3' : 0})
    dir = db.reference(f"{ctx.author.id}/곡산대륙/선물")
    dir.update({'싱그러운_물' : 0})
    dir.update({'코X콜라' : 0})
    dir.update({'저울' : 0})
    dir.update({'전파시계' : 0})
    dir.update({'드워프의_망치' : 0})
    dir.update({'곡괭이' : 0})
    dir.update({'금화' : 0})
    dir.update({'에너지드링크' : 0})
    dir.update({'프로틴' : 0})
    dir.update({'가공된_목걸이' : 0})
  roding = bot.get_emoji(950182195891404830)
  dir = db.reference(f"{ctx.author.id}/현재위치")#위치확인
  location = dir.get()
  if location != '태초항구':#마을인가?
    if location != '곡산항구':#마을인가?
      await ctx.reply('대륙간의 이동은 `~항구`에서만 가능합니다!')
      return None

  #싱그러운 물', '코X콜라', '저울', '전파시계', '드워프의 망치', '곡괭이', '금화', '에너지드링크', '프로틴' '가공된 목걸이'
  dir = db.reference(f"{ctx.author.id}/ing")
  schs = dir.get()
  if schs != 0:
    await ctx.reply(f'대륙이동이 불가능합니다!(사유 : {schs}중)')
    return None


    #시작
  dir = db.reference(f"{ctx.author.id}/탑승권")
  ticket = dir.get()
  if ticket < 1:
    await ctx.reply('탑승권이 부족합니다! 마을상점에서 구매해주세요!')
    return None
  
  dir = db.reference(f"{ctx.author.id}/D스킬")
  skill = str(dir.get())
  N = 1
  item = 'ㅤ'
  if '부스터엔진' in skill:
    N = 2
    item = '(-50%)'
  dir = db.reference(f"{ctx.author.id}")
  dir.update({'ing' : '이동'})
  ticket = ticket - 1
  dir = db.reference(f"{ctx.author.id}/대륙")
  대륙 = dir.get()
  time = int(30/N)
  if 대륙 == 1:
    embed = discord.Embed(
            title = f"대륙을 이동합니다", description = f"", color = 0x2f3136
          )
  
    embed.add_field(name=f"현재대륙ㅤㅤㅤ다음대륙", value = f'태초대륙ㅤ{roding}ㅤ곡산대륙', inline = False)
    embed.set_footer(text=f"이동시간 : {time}초 {item}")
    msg = await ctx.reply(embed=embed)
    await asyncio.sleep(time)
    embed = discord.Embed(
            title = f"`곡산대륙`에 도착하였습니다!", description = f"현재위치 : **곡산항구**", color = 0x2f3136
          )
    await ctx.reply(embed=embed)
    await msg.delete()
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'대륙' : 2})
    dir.update({'현재위치' : '곡산항구'})
    dir.update({'탑승권' : ticket})
    dir.update({'ing' : 0})
  elif 대륙 == 2:
    embed = discord.Embed(
            title = f"대륙을 이동합니다", description = f"", color = 0x2f3136
          )
  
    embed.add_field(name=f"현재대륙ㅤㅤㅤ 다음대륙", value = f'곡산대륙ㅤ{roding}ㅤ태초대륙', inline = False)
    embed.set_footer(text=f"이동시간 : {time}초 {item}")
    msg = await ctx.reply(embed=embed)
    await asyncio.sleep(time)
    embed = discord.Embed(
            title = f"`태초대륙`에 도착하였습니다!", description = f"현재위치 : **태초항구**", color = 0x2f3136
          )
    await ctx.reply(embed=embed)
    await msg.delete()
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'대륙' : 1})
    dir.update({'현재위치' : '태초항구'})
    dir.update({'탑승권' : ticket})
    dir.update({'ing' : 0})