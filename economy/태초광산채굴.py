import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def 태초광산채굴(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, att, MZ, ske, dmd):
    del ske[0]
    Hh1 = 500
    msg3 = await ctx.reply('```css\n[태초광산]에 오신것을 환영합니다.(로딩중..)\n> 채굴가능한 광물 : <석탄>, <철>, <금>, <청금석>\n> 권장 스테미너 : 300\n> 권장 채굴력 : 50\n```')
    await asyncio.sleep(3.0)
    #단전호흡 검사
    att = 10
    if N != 0:
      att = (10 - (10/N))
    skuse = 0
    
    msg4 = await ctx.reply(
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[태초의 광물]\n내구력 : 500    현재 내구력 : 500\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh1}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    #태 = await ctx.send(f'> 현재 내구력 : {Hh1}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : '태초광산에서 채굴'})
    await msg3.delete()
    e = 0
    while Hh1 >= 1:
      sp = sp - att
      Hh1 = Hh1 - power
      await msg4.edit(content = 
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[태초의 광물]\n내구력 : 500    현재 내구력 : {Hh1}\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh1}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
      #await 태.edit(content = f'> 현재 내구력 : {Hh1}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
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
        #await 태.delete()
        await msg4.delete()
        await asyncio.sleep(10.0)
        dir.update({'ing' : 0})
        dir.update({'현재위치' : '태초마을'})
        dir = db.reference(f"{ctx.author.id}/최대스테미너")
        d = dir.get()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스테미너' : d})
        return None

      await asyncio.sleep(1.0)

    await msg4.delete()
    #await 태.delete()
    석탄 = random.randrange(1,21)
    dir = db.reference(f"{ctx.author.id}/광물/석탄")
    coals = dir.get()
    철 = random.randrange(1,11)
    dir = db.reference(f"{ctx.author.id}/광물/철")
    ins = dir.get()
    금 = random.randrange(1,10)
    dir = db.reference(f"{ctx.author.id}/광물/금")
    gold = dir.get()
    아니 = random.randrange(1,3)
    청금석 = 0
    dir = db.reference(f"{ctx.author.id}/광물/청금석")
    ll = dir.get()
    if 아니 <= 1:
      청금석 = random.randrange(1,3) 
    태초광산보상경험치 = random.randrange(10,26) * (mylv * 10)
    embed = discord.Embed(title="", description="", color=0xE4E4E4)
    embed.add_field(name="채굴성공!‎", value=f"```css\n석탄 + {석탄}\n철 + {철}\n금 + {금}\n청금석 + {청금석}\n경험치 + {태초광산보상경험치}\n```", inline=False)
    석탄 = 석탄 + coals
    철 = 철 + ins
    금 = 금 + gold
    청금석 = 청금석 + ll
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : 0})
    dir.update({'스테미너' : sp})
    dir = db.reference(f"{ctx.author.id}/광물")
    dir.update({'석탄' : 석탄})
    dir.update({'철' : 철})
    dir.update({'금' : 금})
    dir.update({'청금석' : 청금석})
    dir = db.reference(f"{ctx.author.id}/경험치")
    exp = dir.get()
    태초광산보상경험치 = 태초광산보상경험치 + exp
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'경험치' : 태초광산보상경험치})
    
    await ctx.reply(embed=embed)