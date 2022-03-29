import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio

async def 곡산광산채굴(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, att, MZ, ske, dmd):
    
    del ske[0]
    Hh3 = 5000
    msg = await ctx.reply('```css\n[곡산광산]에 오신것을 환영합니다.(로딩중..)\n> 채굴가능한 광물 : 석탄\n> 권장 스테미너 : 1000\n> 권장 채굴력 : 500\n```')
    await asyncio.sleep(3.0)
    
    #단전호흡 검사
    att = 50
    if N != 0:
      att = (50 - (50/N))
    msg2 = await ctx.reply(
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[곡산의 유물]\n내구력 : 5000    현재 내구력 : 5000\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh3}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    #한 = await ctx.send(f'> 현재 내구력 : {Hh}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
    skuse = 0
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : '곡산광산에서 채굴'})
    await msg.delete()
    e = 0
    while Hh3 >= 1:
      sp = sp - att
      Hh3 = Hh3 - power
      #await 한.edit(content = f'> 현재 내구력 : {Hh}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
      await msg2.edit(content = 
      f'```css\n[{ctx.author.name}의 채굴]\n‎\n[곡산의 유물]\n내구력 : 5000   현재 내구력 : {Hh3}\n소모스테미너 : {att}\n‎\n[{ctx.author.name}]\n레벨 : {mylv}LV\n스테미너 : {sp}\n채굴력 : {power}  (+{MZ}%)\n‎\nSKILL\n1.<{sk1}>\n2.<{sk2}>\n3.<{sk3}>\n\n채굴중....\n```\n‎\n> 현재 내구력 : {Hh3}\n> 현재 스테미너 : {sp}\n> 착용스킬 : {ske}')
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
    다이아 = random.randrange(1,6)
    에메랄드 = random.randrange(1,4)
    곡산광산보상경험치 = random.randrange(10,26) * (mylv * 5)
    embed = discord.Embed(title="", description="", color=0xE4E4E4)
    embed.add_field(name="채굴성공!‎", value=f"```css\n다이아 + {다이아}\n에메랄드 + {에메랄드}\n경험치 + {곡산광산보상경험치}\n```", inline=False)
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : 0})
    dir.update({'스테미너' : sp})
    dir = db.reference(f"{ctx.author.id}/광물/다이아")
    dia = dir.get()
    다이아 = dia + 다이아 
    dir = db.reference(f"{ctx.author.id}/광물/에메랄드")
    emd = dir.get()
    에메랄드 = emd + 에메랄드
    dir = db.reference(f"{ctx.author.id}/광물")
    dir.update({'다이아' : 다이아})
    dir.update({'에메랄드' : 에메랄드})
    dir = db.reference(f"{ctx.author.id}/경험치")
    exp = dir.get()
    곡산광산보상경험치 = 곡산광산보상경험치 + exp
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'경험치' : 곡산광산보상경험치})
    
    await ctx.reply(embed=embed)