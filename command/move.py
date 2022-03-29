import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption


async def move(ctx, bot, A, B, C, D, S, result, yes, location, MTX):
      ghlqhr = bot.get_emoji(947294870974898186)
      cornftls = bot.get_emoji(947341606456029244)
      dir = db.reference(f"{ctx.author.id}/D스킬")
      Dcheck = dir.get()
      if '회복술사' in Dcheck:
        sils = random.randrange(1,11)
      if '베테랑' in Dcheck:
        danganrop = random.randrange(1,11)
        danga = random.randrange(1,11)
        
      tip = ['태초광산은 레벨5부터 가는것을 추천해요!','캔 광물은 마을에서 팔아 돈을 얻으세요!','스킬을 착용함에 따라 난이도가 달라지는거 아시나요?','혹시 어려움이 있으시면 `?ㅌㅌ`(튜토리얼)을 입력해보세요!']
      tipran = random.randrange(0,4)
      msg = await ctx.send(
          "‎",
          components = [
              Select(
                  placeholder = "이동할 지역을 선택하세요!",
                  options = [
                      SelectOption(emoji = A, label = "태초마을", description ="기능 : 광물매도", value = f"{ctx.author.id}A"),
                      SelectOption(emoji = B, label = "초보자광산", description ="기능 : 광물채굴", value = f"{ctx.author.id}B"),
                      SelectOption(emoji = C, label = "태초광산", description ="기능 : 광물채굴", value = f"{ctx.author.id}C"),
                      SelectOption(emoji = D, label = "태초항구", description ="기능 : 광물매입, 대륙이동", value = f"{ctx.author.id}D"),
                      SelectOption(emoji = S, label = "이동취소", value = f"{ctx.author.id}S")
                  ]
              )
          ]
      )

      interaction = await bot.wait_for("select_option")
      a = interaction.values[0]
      if a == f'{ctx.author.id}A':
        if result != yes:
          await ctx.reply('오류가 발생했습니다!\n오류코드 : itsashifterror')
          return None
        
        if location == "태초마을":
          await msg.delete()
          await ctx.reply('현재 `태초마을`에 계십니다.')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        await msg.delete()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : '이동'})
        
        msg = await ctx.reply(f'`{location}`에서 `태초마을`로 이동합니다.(소요시간 {MTX}초..)\n> TIP : {tip[tipran]}')
        await asyncio.sleep(int(MTX))
        await msg.delete()
        embed = discord.Embed(title=f"`태초마을`에 도착하였습니다!", description=f"사용 가능한 명령어\n```\n회복/이동/지도/내위치/매도/강화/상점\n```", color=0xE4E4E4)
        await ctx.reply(embed = embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'현재위치' : '태초마을'})
        dir.update({'ing' : 0})
        
        if sils <= 2:
          await ctx.reply(f'> {ghlqhr} : 회복술사 발동!\n스테미너가 전부 회복되었습니다')
          dir = db.reference(f"{ctx.author.id}/최대스테미너")
          bnb = dir.get()
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스테미너' : bnb})
        if danganrop <= 1:
          CHSAB = '다이아'          
          if danga <=7 :
            CHSAB = '청금석'
          if danga >= 10:
            CHSAB = '에메랄드'
          await ctx.reply(f'> {cornftls} : 베테랑 발동!\n{CHSAB} 1개 발견했습니다!')
          dir = db.reference(f"{ctx.author.id}/광물/{CHSAB}")
          dirb = dir.get()
          dirb = dirb + 1
          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({CHSAB : dirb})
        return None
        
      
      if a == f'{ctx.author.id}B':
        if result != yes:
          await ctx.reply('오류가 발생했습니다!\n오류코드 : itsashifterror')
          return None
        
        if location == "초보자광산":
          await msg.delete()
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.reply('현재 `초보자광산`에 계십니다.')
          return None

        await msg.delete()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : '이동'})
        msg = await ctx.reply(f'`{location}`에서 `초보자광산`로 이동합니다.(소요시간 {MTX}초..)\n> TIP : {tip[tipran]}')
        await asyncio.sleep(int(MTX))
        await msg.delete()
        
        embed = discord.Embed(title=f"`초보자광산`에 도착하였습니다!", description=f"사용 가능한 명령어\n```\n채굴/이동/지도/내위치\n```", color=0xE4E4E4)
        await ctx.reply(embed = embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'현재위치' : '초보자광산'})
        dir.update({'ing' : 0})
        if sils <= 2:
          await ctx.reply(f'> {ghlqhr} : 회복술사 발동!\n스테미너가 전부 회복되었습니다')
          dir = db.reference(f"{ctx.author.id}/최대스테미너")
          bnb = dir.get()
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스테미너' : bnb})
        if danganrop <= 1:
          CHSAB = '다이아'          
          if danga <=7 :
            CHSAB = '청금석'
          if danga >= 10:
            CHSAB = '에메랄드'
          await ctx.reply(f'> {cornftls} : 베테랑 발동!\n{CHSAB} 1개 발견했습니다!')
          dir = db.reference(f"{ctx.author.id}/광물/{CHSAB}")
          dirb = dir.get()
          dirb = dirb + 1
          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({CHSAB : dirb})
        
        return None
      
      if a == f'{ctx.author.id}C':
        if result != yes:
          await ctx.reply('오류가 발생했습니다!\n오류코드 : itsashifterror')
          return None
        if location == "태초광산":
          await msg.delete()
          await ctx.reply('현재 `태초광산`에 계십니다.')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        await msg.delete()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : '이동'})
        msg = await ctx.reply(f'`{location}`에서 `태초광산`로 이동합니다.(소요시간 {MTX}초..)\n> TIP : {tip[tipran]}')
        await asyncio.sleep(int(MTX))
        await msg.delete()
        embed = discord.Embed(title=f"`태초광산`에 도착하였습니다!", description=f"사용 가능한 명령어\n```\n채굴/이동/지도/내위치\n```", color=0xE4E4E4)
        await ctx.reply(embed = embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'현재위치' : '태초광산'})
        dir.update({'ing' : 0})
        if sils <= 2:
          await ctx.reply(f'> {ghlqhr} : 회복술사 발동!\n스테미너가 전부 회복되었습니다')
          dir = db.reference(f"{ctx.author.id}/최대스테미너")
          bnb = dir.get()
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스테미너' : bnb})
        if danganrop <= 1:
          CHSAB = '다이아'          
          if danga <=7 :
            CHSAB = '청금석'
          if danga >= 10:
            CHSAB = '에메랄드'
          await ctx.reply(f'> {cornftls} : 베테랑 발동!\n{CHSAB} 1개 발견했습니다!')
          dir = db.reference(f"{ctx.author.id}/광물/{CHSAB}")
          dirb = dir.get()
          dirb = dirb + 1
          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({CHSAB : dirb})
        
        return None

      if a == f'{ctx.author.id}D':
        if result != yes:
          await ctx.reply('오류가 발생했습니다!\n오류코드 : itsashifterror')
          return None
        if location == "태초항구":
          await msg.delete()
          await ctx.reply('현재 `태초항구`에 계십니다.')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None


        await msg.delete()
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : '이동'})
        msg = await ctx.reply(f'`{location}`에서 `태초항구`로 이동합니다.(소요시간 {MTX}초..)\n> TIP : {tip[tipran]}')
        await asyncio.sleep(int(MTX))
        await msg.delete()
        embed = discord.Embed(title=f"`태초항구`에 도착하였습니다!", description=f"사용 가능한 명령어\n```\n이동/지도/내위치/승선\n```", color=0xE4E4E4)
        await ctx.reply(embed = embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'현재위치' : '태초항구'})
        dir.update({'ing' : 0})
        if sils <= 2:
          await ctx.reply(f'> {ghlqhr} : 회복술사 발동!\n스테미너가 전부 회복되었습니다')
          dir = db.reference(f"{ctx.author.id}/최대스테미너")
          bnb = dir.get()
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'스테미너' : bnb})
        if danganrop <= 1:
          CHSAB = '다이아'          
          if danga <=7 :
            CHSAB = '청금석'
          if danga >= 10:
            CHSAB = '에메랄드'
          await ctx.reply(f'> {cornftls} : 베테랑 발동!\n{CHSAB} 1개 발견했습니다!')
          dir = db.reference(f"{ctx.author.id}/광물/{CHSAB}")
          dirb = dir.get()
          dirb = dirb + 1
          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({CHSAB : dirb})
        
        return None

      if a == f'{ctx.author.id}S':
        await msg.delete()
        await ctx.reply('이동을 취소했습니다.')
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None
      await interaction.send(content = f"{interaction.values[0]} selected!")