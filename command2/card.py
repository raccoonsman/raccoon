import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from disrankmaster.disrank.generator import Generator



async def card(ctx):
  dir = db.reference(f"{ctx.author.id}/레벨")
  level = dir.get()
  dir = db.reference(f"{ctx.author.id}/경험치")
  exp = int(dir.get())
  dir = db.reference(f"{ctx.author.id}/최대경험치")
  max = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/현재시간')
  time = dir.get()
  if time == '오전':
    times = 'morning'    
    image = 'https://media.discordapp.net/attachments/942050880910397520/950572304725835796/nature-3125912_960_720.png?width=834&height=469'
  if time == '낮':
    times = 'afternoon'
    image = 'https://media.discordapp.net/attachments/942050880910397520/950577557835755540/nature-2689795_960_720.jpg'
  if time == '저녁':
    times = 'evening'
    image = 'https://media.discordapp.net/attachments/942050880910397520/950580337963053056/sunset-5222626_960_720.jpg'
  if time == '밤':
    times = 'night'
    image = 'https://media.discordapp.net/attachments/935202344965144626/950566801442488360/milky-way-2750627_960_720.png'
  if time == '새벽':
    times = 'dawn'
    image = 'https://cdn.pixabay.com/photo/2018/11/12/20/07/sky-3811643_960_720.jpg'
  args = {
	'bg_image' : image, # Background image link 
	'profile_image' : ctx.author.avatar_url, # User profile picture link
	'level' : level, # User current level 
	'current_xp' : 0, # Current level minimum xp 
	'user_xp' : exp, # User current xp
	'next_xp' : max, # xp required for next level
	'user_position' : times, # User position in leaderboard
	'user_name' : "TIME CHECK", # user name with descriminator 
	'user_status' : 'idle', # User status eg. online, offline, idle, streaming, dnd
  }
  image = Generator().generate_profile(**args)
  file = discord.File(fp=image, filename='image.png')
  await ctx.reply(file=file)