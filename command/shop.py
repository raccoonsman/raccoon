import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption

async def shop(ctx, bot):
    회복url = "https://media.discordapp.net/attachments/941151376568897538/947302323938537512/122_20220227004251.png?width=469&height=469"
    아url = 'https://media.discordapp.net/attachments/941151376568897538/947303924510117979/157_20220226193012.png?width=469&height=469'
    베url = "https://media.discordapp.net/attachments/941151376568897538/947754902690598973/157_20220227122955.png?width=469&height=469"
    dir = db.reference(f"{ctx.author.id}/현재위치")
    location = dir.get()

    if location != '태초마을':
      if location != '곡산마을':
        await ctx.reply('상점은 `태초마을/곡산마을`에서만 열립니다.')
      return None
      await ctx.reply('상점은 `태초마을/곡산마을`에서만 열립니다.')
      return None

    ticket = bot.get_emoji(945209841230696488)
    no = bot.get_emoji(943780055761440779)
    adrnr = bot.get_emoji(947096750940901436)
    회복술사 = bot.get_emoji(947294870974898186)
    베테랑 = bot.get_emoji(947341606456029244)

    dir = db.reference(f"{ctx.author.id}/ing")
    ing = dir.get()
    if ing != 0:
      await ctx.reply(f'상점이 불가능합니다!(사유 : {ing}중)') 
      return None
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing':'상점구매'})


  
    if ctx.author.dm_channel:
      await ctx.reply('DM을 확인해주세요!')
      msg = await ctx.author.dm_channel.send(
        "```\nD SKILL : 장착하지 않아도 효과가 나타납니다\nT SKILL : 장을 한 상태에서만 효과가 나타납니다\n```",
        components = [
            Select(
                placeholder = "구입할 물품을 골라주세요",
                options = [
                  SelectOption(emoji = ticket, label = "HK TICKET : 100000원", description ="다른 대륙으로 이동할 수 있는 티켓입니다.", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = adrnr, label = "T SKILL : 아드레날린 : 50000원",description ="채굴력 + 20%",  value = f"{ctx.author.id}B"),
                    SelectOption(emoji = 회복술사, label = "D SKILL : 회복술사 : 60000원",description ="이동시 20% 확률로 스테미너가 회복된다.", value = f"{ctx.author.id}C"),
                    SelectOption(emoji = 베테랑, label = "D SKILL : 베테랑 : 100000원",description ="이동시 10% 확률로 청금석 이상 에메랄드 이하의 광물을 랜덤으로 한개 얻는다", value = f"{ctx.author.id}D"),
                    SelectOption(emoji = no, label = "구매를 취소합니다", value = f"{ctx.author.id}N")
                  ]
              )
          ]
      )
      urll = "https://media.discordapp.net/attachments/941151376568897538/947298328360661043/115_20220221011924.png?width=625&height=469"
      interaction = await bot.wait_for("select_option")
      cs = interaction.values[0]
      if cs == f'{ctx.author.id}A':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 100000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/탑승권")
        TICKET = dir.get()
        TICKET = TICKET + 1
        money = money - 100000
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'돈' : money})
        dir.update({'탑승권' : TICKET})
        dir.update({'ing' : 0})
        embed = discord.Embed(title="HK TICKET 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url=urll)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'HK TICKET 구매완료!\n> 잔액 : {money}원')
        await asyncio.sleep(2.0)
        await smg.delete()
        return None
        
      if cs == f'{ctx.author.id}B':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 50000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/스킬보유")
        asdf = dir.get()
        if '아드레날린' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 50000
        
        skils = ['아드레날린']
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': asdf + skils})
        dir.update({'돈' : money})
        embed = discord.Embed(title="T스킬 : 아드레날린 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 아url)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'T스킬 : 아드레날린 구매완료!\n> 잔액 : {money}원')
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}C':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 60000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        if '회복술사' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 60000
        
        skils = ['회복술사']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 회복술사 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="D스킬 : 회복술사 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 회복url)
        await ctx.author.dm_channel.send(embed=embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}D':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 100000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        if '베테랑' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 100000
        
        skils = ['베테랑']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 베테랑 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="D스킬 : 베테랑 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 베url)
        await ctx.author.dm_channel.send(embed=embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}N':
        await msg.delete()
        await ctx.author.dm_channel.send('구매를 취소하였습니다')
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None
      await interaction.send(content = f"{interaction.values[0]}   selected!")

      



      
    elif ctx.author.dm_channel is None:
      await ctx.reply('DM을 확인해주세요!')
      channel = await ctx.author.create_dm()
      msg =  await channel.send(
        "```\nD SKILL : 장착하지 않아도 효과가 나타납니다\nT SKILL : 장착을 한 상태에서만 효과가 나타납니다\n```",
        components = [
            Select(
                placeholder = "구입할 물품을 골라주세요",
                options = [
                    SelectOption(emoji = ticket, label = "HK TICKET : 100000원", description ="다른 대륙으로 이동할 수 있는 티켓입니다.", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = adrnr, label = "T SKILL : 아드레날린 : 50000원",description ="채굴력 + 20%",  value = f"{ctx.author.id}B"),
                    SelectOption(emoji = 회복술사, label = "D SKILL : 회복술사 : 60000원",description ="이동시 20% 확률로 스테미너가 회복된다.", value = f"{ctx.author.id}C"),
                    SelectOption(emoji = 베테랑, label = "D SKILL : 베테랑 : 100000원",description ="이동시 10% 확률로 청금석 이상 에메랄드 이하의 광물을 랜덤으로 한개 얻는다", value = "D"),
                    SelectOption(emoji = no, label = "구매를 취소합니다", value = f"{ctx.author.id}N")
                  ]
              )
          ]
      )
      urll = "https://media.discordapp.net/attachments/941151376568897538/947298328360661043/115_20220221011924.png?width=625&height=469"
      interaction = await bot.wait_for("select_option")
      cs = interaction.values[0]
      if cs == f'{ctx.author.id}A':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 100000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/탑승권")
        TICKET = dir.get()
        TICKET = TICKET + 1
        money = money - 100000
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'돈' : money})
        dir.update({'탑승권' : TICKET})
        dir.update({'ing' : 0})
        embed = discord.Embed(title="HK TICKET 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url=urll)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'HK TICKET 구매완료!\n> 잔액 : {money}원')
        await asyncio.sleep(2.0)
        await smg.delete()
        return None
        
      if cs == f'{ctx.author.id}B':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 50000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/스킬보유")
        asdf = dir.get()
        if '아드레날린' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 50000
        
        skils = ['아드레날린']
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': asdf + skils})
        dir.update({'돈' : money})
        await ctx.reply(f'T스킬 : 아드레날린 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="T스킬 : 아드레날린 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 아url)
        smg = await ctx.author.dm_channel.send(embed = embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}C':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 60000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        if '회복술사' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 60000
        
        skils = ['회복술사']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 회복술사 구매완료!\n> 잔액 : {money}원')
        
        embed = discord.Embed(title="D스킬 : 회복술사 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 회복url)
        await ctx.author.dm_channel.send(embed=embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}D':
        await msg.delete()
        dir = db.reference(f"{ctx.author.id}/돈")
        money = dir.get()
        if money < 100000:
          await ctx.author.dm_channel.send(f'돈이 부족합니다. 현재 금액 {money}원')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        if '베테랑' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 100000
        
        skils = ['베테랑']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 베테랑 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="D스킬 : 베테랑 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 베url)
        await ctx.author.dm_channel.send(embed=embed)
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None

      if cs == f'{ctx.author.id}N':
        await msg.delete()
        await ctx.author.dm_channel.send('구매를 취소하였습니다')
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'ing' : 0})
        return None
      await interaction.send(content = f"{interaction.values[0]}   selected!")



