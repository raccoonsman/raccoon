import discord
from discord.ext import commands
from discord import Intents
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string

async def mylocation(ctx):
    dir = db.reference(f"{ctx.author.id}/현재위치")
    location = dir.get()

    if location == '태초마을':
      embed = discord.Embed(title="지도", description="현재위치 : 태초마을", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934994949143941180/32_20220124111448.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None
    
    if location == '초보자광산':
      embed = discord.Embed(title="지도", description="현재위치 : 초보자광산", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934994949693390908/32_20220124111456.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '태초광산':
      embed = discord.Embed(title="지도", description="현재위치 : 태초광산", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934994950406418462/32_20220124111513.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '태초항구':
      embed = discord.Embed(title="지도", description="현재위치 : 태초항구", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934994951241076736/32_20220124111526.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '곡산항구':
      embed = discord.Embed(title="지도", description="현재위치 : 곡산항구", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934999858115399770/32_20220124113530.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '곡산광산':
      embed = discord.Embed(title="지도", description="현재위치 : 곡산광산", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934995548279291975/32_20220124111757.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '태극광산':
      embed = discord.Embed(title="지도", description="현재위치 : 태극광산", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934995549873139744/32_20220124111815.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None

    if location == '곡산마을':
      embed = discord.Embed(title="지도", description="현재위치 : 곡산마을", color=0xE4E4E4)
      embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/934995549256548372/32_20220124111806.png?width=625&height=469")
      embed.set_footer(text="이동은 `?ㅇㄷ`")
      await ctx.reply(embed = embed)
      return None
