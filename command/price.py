import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio



async def pricetag(ctx):
    dir = db.reference("단가/석탄")
    c = dir.get()
    dir = db.reference("단가/철")
    i = dir.get()
    dir = db.reference("단가/금")
    g = dir.get()
    dir = db.reference("단가/청금석")
    l = dir.get()
    dir = db.reference("단가/다이아")
    d = dir.get()
    dir = db.reference("단가/에메랄드")
    e = dir.get()
    dir = db.reference("단가/석탄전")
    cv = dir.get()
    dir = db.reference("단가/철전")
    iv = dir.get()
    dir = db.reference("단가/금전")
    gv = dir.get()
    dir = db.reference("단가/청금석전")
    lv = dir.get()
    dir = db.reference("단가/다이아전")
    dv = dir.get()
    dir = db.reference("단가/에메랄드전")
    ev = dir.get()

    



    embed = discord.Embed(title="너구리장터 실시간 가격표", description="", color=0xE4E4E4)
    
    embed.add_field(name="‎", value="**일반광물**", inline=False)
    embed.add_field(name="‎석탄", value=f"```\n{cv} → {c}원\n```", inline=False)
    embed.add_field(name="‎철", value=f"```\n{iv} → {i}원\n```", inline=False)
    embed.add_field(name="‎금", value=f"```\n{gv} → {g}원\n```", inline=False)
    embed.add_field(name="‎청금석", value=f"```\n{lv} → {l}원‎‎\n```", inline=False)
    embed.add_field(name="‎다이아", value=f"```\n{dv} → {d}원‎‎\n```", inline=False)
    embed.add_field(name="‎에메랄드", value=f"```\n{ev} → {e}원\n```", inline=False)
    embed.set_footer(text="가격은 실시간 변동입니다.")

    await ctx.reply(embed=embed)


async def price(ctx, name):
    dir = db.reference("단가")
    lists = dir.get()

    if name not in lists:
      return None
    dir = db.reference(f"단가/{name}")
    cs = dir.get()
    dir = db.reference(f"단가/{name}전")
    cv = dir.get()
      
    await ctx.reply(f'> 현재 `{name}`의 가격은 `{cv}원` → `{cs}원`입니다!')
