import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption




async def aoeh(ctx, bot, coal, steel, gold, ll, di, ai, no):
    dir = db.reference("단가/석탄")
    csa = dir.get()
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

    dir = db.reference(f"{ctx.author.id}/광물/석탄")
    석탄 = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/철")
    철 = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/금")
    금 = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/청금석")
    청금석 = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/다이아")
    다이아 = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/에메랄드")
    에메랄드 = dir.get()

    if ctx.author.dm_channel:
      await ctx.reply('DM을 확인해주세요!')
      msg = await ctx.author.dm_channel.send(
          "너구리시장!",
          components = [
              Select(
                  placeholder = "매도할 항목을 고르세요!",
                  options = [
                      SelectOption(emoji = coal, label = f"석탄 : {석탄}개", description =f"현재가격 : {csa}원", value = f"{ctx.author.id}A"),
                      SelectOption(emoji = steel, label = f"철 : {철}개", description =f"현재가격 : {i}원", value = f"{ctx.author.id}B"),
                      SelectOption(emoji = gold, label = f"금 : {금}개", description =f"현재가격 : {g}원", value = f"{ctx.author.id}C"),
                      SelectOption(emoji = ll, label = f"청금석 : {청금석}개", description =f"현재가격 : {l}원", value = f"{ctx.author.id}D"),
                      SelectOption(emoji = di, label = f"다이아 : {다이아}개", description =f"현재가격 : {d}원", value = f"{ctx.author.id}E"),
                      SelectOption(emoji = ai, label = f"에메랄드 : {에메랄드}개", description =f"현재가격 : {e}원", value = f"{ctx.author.id}F"),
                      SelectOption(emoji = no, label = f"매도을 취소합니다", value = f"{ctx.author.id}S")
                  ]
              )
          ]
      )

      interaction = await bot.wait_for("select_option")
      await msg.delete()

      c = interaction.values[0]
      print(c)
      if c == f'{ctx.author.id}S':
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if c == f'{ctx.author.id}A':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{석탄}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 석탄:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 석탄이 부족합니다...\n> 현재 석탄 개수 {석탄}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * csa


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/석탄")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"석탄" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"돈" : 돈})
          dir = db.reference(f"창고")
          석탄 = 석탄 + s
          dir.update({'석탄' : 석탄})
          

          embed = discord.Embed(title=f"석탄 {s}개 판매완료!", description=f"{돈}원", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None



      if c == f'{ctx.author.id}B':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{철}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 철:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 철이 부족합니다...\n> 현재 철 개수 {철}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * i


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/철")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"철" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"돈" : 돈})
          dir = db.reference(f"창고")
          철 = 철 + s
          dir.update({'철' : 철})
          

          embed = discord.Embed(title=f"철 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})
          return None
      
      if c == f'{ctx.author.id}C':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{금}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 금:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 금이 부족합니다...\n> 현재 금 개수 {금}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * g


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/금")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"금" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"금" : 돈})
          dir = db.reference(f"창고")
          금 = 금 + s
          dir.update({'금' : 금})
          

          embed = discord.Embed(title=f"금 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})          

          return None
      
      if c == f'{ctx.author.id}D':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{청금석}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 청금석:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 청금석이 부족합니다...\n> 현재 청금석 개수 {청금석}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * l


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/청금석")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"청금석" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"청금석" : 돈})
          dir = db.reference(f"창고")
          청금석 = 청금석 + s
          dir.update({'청금석' : 청금석})
          

          embed = discord.Embed(title=f"청금석 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None
      
      if c == f'{ctx.author.id}E':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{다이아}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 다이아:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 다이아가 부족합니다...\n> 현재 다이아 개수 : {다이아}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * d


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/다이아")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"다이아" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"다이아" : 돈})
          dir = db.reference(f"창고")
          다이아 = 다이아 + s
          dir.update({'다이아' : 다이아})
          

          embed = discord.Embed(title=f"다이아 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})
          return None
      
      if c == f'{ctx.author.id}F':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{에메랄드}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            return None
          if s > 에메랄드:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 에메랄드가 부족합니다...\n> 현재 에메랄드 개수 : {에메랄드}개")
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * e


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/에메랄드")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"에메랄드" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"에메랄드" : 돈})
          dir = db.reference(f"창고")
          에메랄드 = 에메랄드 + s
          dir.update({'에메랄드' : 에메랄드})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})
          

          embed = discord.Embed(title=f"에메랄드 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)

          return None
      return None
      await interaction.send(content = f"{interaction.values[0]} selected!")

    elif ctx.author.dm_channel is None:
      await ctx.reply('DM을 확인해주세요!')
      channel = await ctx.author.create_dm()
      msg = await channel.send(
          "너구리장터!",
          components = [
              Select(
                  placeholder = "매도할 항목을 고르세요!",
                  options = [
                      SelectOption(emoji = coal, label = f"석탄 : {석탄}개", description =f"현재가격 : {csa}원", value = f"{ctx.author.id}A"),
                      SelectOption(emoji = steel, label = f"철 : {철}개", description =f"현재가격 : {i}원", value = f"{ctx.author.id}B"),
                      SelectOption(emoji = gold, label = f"금 : {금}개", description =f"현재가격 : {g}원", value = f"{ctx.author.id}C"),
                      SelectOption(emoji = ll, label = f"청금석 : {청금석}개", description =f"현재가격 : {l}원", value = f"{ctx.author.id}D"),
                      SelectOption(emoji = di, label = f"다이아 : {다이아}개", description =f"현재가격 : {d}원", value = f"{ctx.author.id}E"),
                      SelectOption(emoji = ai, label = f"에메랄드 : {에메랄드}개", description =f"현재가격 : {e}원", value = f"{ctx.author.id}F"),
                      SelectOption(emoji = no, label = f"매도을 취소합니다", value = f"{ctx.author.id}S")
                  ]
              )
          ]
      )

      interaction = await bot.wait_for("select_option")
      await msg.delete()

      c = interaction.values[0]
      if c == f'{ctx.author.id}S':
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None
      if c == f'{ctx.author.id}A':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{석탄}개` 까지 판매 하실수 있습니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s < 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 석탄:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 석탄이 부족합니다...\n> 현재 석탄 개수 {석탄}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * csa


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/석탄")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"석탄" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"돈" : 돈})
          dir = db.reference(f"창고")
          석탄 = 석탄 + s
          dir.update({'석탄' : 석탄})
          

          embed = discord.Embed(title=f"석탄 {s}개 판매완료!", description=f" {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})
          return None
      
      if c == f'{ctx.author.id}B':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{철}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 철:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 철이 부족합니다...\n> 현재 철 개수 {철}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * csa


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/철")
          sw = dir.get()
          sw = sw - i
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"철" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"돈" : 돈})
          dir = db.reference(f"창고")
          철 = 철 + s
          dir.update({'철' : 철})
          

          embed = discord.Embed(title=f"철 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None
      
      if c == f'{ctx.author.id}C':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{금}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 금:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 금이 부족합니다...\n> 현재 금 개수 {금}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * g


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/금")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"금" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"금" : 돈})
          dir = db.reference(f"창고")
          금 = 금 + s
          dir.update({'금' : 금})
          

          embed = discord.Embed(title=f"금 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})
          await ctx.author.dm_channel.send(embed=embed)

          return None
      
      if c == f'{ctx.author.id}D':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{청금석}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 청금석:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 청금석이 부족합니다...\n> 현재 청금석 개수 {청금석}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * l


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/청금석")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"청금석" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"청금석" : 돈})
          dir = db.reference(f"창고")
          청금석 = 청금석 + s
          dir.update({'청금석' : 청금석})
          

          embed = discord.Embed(title=f"청금석 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None
      
      if c == f'{ctx.author.id}E':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{다이아}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          await ctx.author.dm_channel.send(embed=embed)
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 다이아:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 다이아가 부족합니다...\n> 현재 다이아 개수 : {다이아}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * d


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/다이아")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"다이아" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"다이아" : 돈})
          dir = db.reference(f"창고")
          다이아 = 다이아 + s
          dir.update({'다이아' : 다이아})
          

          embed = discord.Embed(title=f"다이아 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None
      
      if c == f'{ctx.author.id}F':
        msg = await ctx.author.dm_channel.send(f'판매하실 갯수를 정해주세요! (예) `1`\n(최대 `{에메랄드}개` 까지 판매 가능합니다.)')
        timeout = 10
        
        def check(m):
          return m.author == ctx.author

        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await msg.delete()
          embed = discord.Embed(title="제한시간이 지났습니다", description=f"다시 매도을 시작해주세요!", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        else:
          s = int(msg.content)
          if s <= 0:
            await ctx.reply('거부되었습니다.')
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None
          if s > 에메랄드:
            await ctx.author.dm_channel.send(f"현재 인벤토리에 에메랄드가 부족합니다...\n> 현재 에메랄드 개수 : {에메랄드}개")
            dir = db.reference(f"{ctx.author.id}")
            dir.update({'ing' : 0})
            return None

          dir = db.reference(f"{ctx.author.id}/돈")
          돈 = int(dir.get())
          purchase = s * e


          돈 = 돈 + purchase
          dir = db.reference(f"{ctx.author.id}/광물/에메랄드")
          sw = dir.get()
          sw = sw - s
          
          

          dir = db.reference(f"{ctx.author.id}/광물")
          dir.update({"에메랄드" : sw})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({"에메랄드" : 돈})
          dir = db.reference(f"창고")
          에메랄드 = 에메랄드 + s
          dir.update({'에메랄드' : 에메랄드})
          

          embed = discord.Embed(title=f"에메랄드 {s}개 판매완료!", description=f"현재 금액 : {돈}원", color=0xE4E4E4)
          await ctx.author.dm_channel.send(embed=embed)
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          dir.update({'돈' : 돈})

          return None
      return None
      await interaction.send(content = f"{interaction.values[0]} selected!")