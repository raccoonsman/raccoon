import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def 태극광산(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, att, MZ, ske, dmd):
    
    del ske[0]
    Hh3 = 10000
    msg = await ctx.reply('```css\n[태극광산]에 오신것을 환영합니다.(로딩중..)\n> 채굴가능한 광물 : 루비, 방해석, 석영, 오리할콘, 철광석, 휘석\n> 권장 스테미너 : 2000\n> 권장 채굴력 : 1000\n```')
    await asyncio.sleep(3.0)
    
    #단전호흡 검사
    att = 100
    if N != 0:
      att = (100 - (100/N))
    msg2 = await ctx.reply(
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[태극의 결정]\n내구력 : 10000    현재 내구력 : 10000\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh3}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    #한 = await ctx.send(f'> 현재 내구력 : {Hh}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    skuse = 0
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : '태극광산에서 채굴'})
    await msg.delete()
    e = 0
    while Hh3 >= 1:
      sp = sp - att
      Hh3 = Hh3 - power
      #await 한.edit(content = f'> 현재 내구력 : {Hh}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
      await msg2.edit(content = 
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[태극의 결정]\n내구력 : 10000    현재 내구력 : {Hh3}\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh3}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
      if Cj == 1:
        if sp <= 30:
          if e == 0:
            await ctx.reply(f'> {dmd} 응급처치 발동!\n스테미너가 50회복되었습니다')
            sp = sp + 50
            e = 1
            

      if sp <= 0:
        await ctx.reply('스테미너가 다 소진되었습니다....마을로 이동합니다.(쿨타임 10초)')
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : '기절'})
        #await 한.delete()
        await msg2.delete()
        await asyncio.sleep(10.0)
        await ctx.reply('스테미너가 전부 회복되었습니다.')
        dir.update({'ing' : 0})
        dir.update({'현재위치' : '곡산마을'})
        dir = db.reference(f"{ctx.author.id}/최대스테미너")
        d = dir.get()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스테미너' : d})
        return None

      await asyncio.sleep(1.0)

    await msg2.delete()
    #await 한.delete()
    randoms = random.randrange(1, 101)
    방해석 = random.randrange(10, 31)
    if randoms <= 60:
      휘석 = random.randrange(10, 31)
    if randoms <= 50:
      철광석 = random.randrange(5, 26)
    if randoms >= 40:
      석영 = random.randrange(1, 21)
    if randoms >= 30:
      루비 = random.randrange(1, 31)
    if randoms >= 20:
      오리할콘= random.randrange(1, 31)
    태극광산보상경험치 = random.randrange(10,31) * (mylv * 5)
    embed = discord.Embed(title="", description="", color=0xE4E4E4)
    embed.add_field(name="채굴성공!‎", value=f"```css\n방해석 + {방해석}\n휘석 + {휘석}\n철광석 + {철광석}\n석영 + {석영}\n루비 + {루비}\n오리할콘 + {오리할콘}\n경험치 + {태극광산보상경험치}\n```", inline=False)
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : 0})
    dir.update({'스테미너' : sp})
    dir = db.reference(f"{ctx.author.id}/광물/방해석")
    dia = dir.get()
    방해석 = dia + 방해석
    dir = db.reference(f"{ctx.author.id}/광물/휘석")
    emd = dir.get()
    휘석 = emd + 휘석
    dir = db.reference(f"{ctx.author.id}/광물/철광석")
    dia = dir.get()
    철광석 = dia + 철광석
    dir = db.reference(f"{ctx.author.id}/광물/석영")
    emd = dir.get()
    석영 = emd + 석영
    dir = db.reference(f"{ctx.author.id}/광물/루비")
    dia = dir.get()
    루비 = dia + 루비
    dir = db.reference(f"{ctx.author.id}/광물/오리할콘")
    emd = dir.get()
    오리할콘 = emd + 오리할콘
    dir = db.reference(f"{ctx.author.id}/광물")
    dir.update({'방해석' : 방해석})
    dir.update({'휘석' : 휘석})
    dir.update({'철광석' : 철광석})
    dir.update({'석영' : 석영})
    dir.update({'루비' : 루비})
    dir.update({'오리할콘' : 오리할콘})
    dir = db.reference(f"{ctx.author.id}/경험치")
    exp = dir.get()
    태극광산보상경험치 = 태극광산보상경험치 + exp
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'경험치' : 태극광산보상경험치})
    
    await ctx.reply(embed=embed)