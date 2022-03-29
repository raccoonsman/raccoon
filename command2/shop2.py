import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption

async def shop2(ctx, bot):
    회복url = "https://media.discordapp.net/attachments/941151376568897538/950670652132720670/50_20220308172050.png?width=469&height=469"
    아url = 'https://media.discordapp.net/attachments/941151376568897538/950678284776140830/54_20220308174331.png?width=469&height=469'
    베url = "https://media.discordapp.net/attachments/941151376568897538/950678284532854814/56_20220308175521.png"
    dir = db.reference(f"{ctx.author.id}/현재위치")
    location = dir.get()
    print('s')
    if location != '태초마을':
      if location != '곡산마을':
        await ctx.reply('상점은 `태초마을/곡산마을`에서만 열립니다.')
        return None
    
    ticket = bot.get_emoji(952075776210137108)
    no = bot.get_emoji(943780055761440779)
    adrnr = bot.get_emoji(950679783182831637)
    회복술사 = bot.get_emoji(950675322477633536)
    베테랑 = bot.get_emoji(950678109806534676)
    tickets = bot.get_emoji(945209841230696488)
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
                  SelectOption(emoji = ticket, label = "100LV 강화권 : 150000원", description ="자신의 곡괭이를 100렙으로 변경", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = 회복술사, label = "T SKILL : 미성 : 90000원",description ="모든 친밀도 증가량 +1 증가", value = f"{ctx.author.id}B"),
                    SelectOption(emoji = adrnr, label = "D SKILL : 부스터엔진 : 50000원",description ="대륙간의 이동 -50%",  value = f"{ctx.author.id}C"),
                    SelectOption(emoji = 베테랑, label = "T SKILL : 네크로멘서 : 100000원",description ="스테미너를 회복 + 2초간 무적", value = f"{ctx.author.id}D"),
                    SelectOption(emoji = tickets, label = "HK TICKET : 100000원", description ="다른 대륙으로 이동할 수 있는 티켓입니다.", value = f"{ctx.author.id}E"),
                    SelectOption(emoji = no, label = "구매를 취소합니다", value = f"{ctx.author.id}N")
                  ]
              )
          ]
      )
      urll = "https://media.discordapp.net/attachments/941151376568897538/952075822393593936/70_20220312142903.jpg?width=469&height=469"
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
        dir = db.reference(f"{ctx.author.id}/곡산대륙/강화권")
        TICKET = dir.get()
        TICKET = TICKET + 1
        money = money - 150000
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'돈' : money})
        dir.update({'ing' : 0})
        dir = db.reference(f"{ctx.author.id}/곡산대륙")
        dir.update({'강화권' : TICKET})
        
        embed = discord.Embed(title="100LV 강화권 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url=urll)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'100LV 강화권 구매완료!\n> 잔액 : {money}원')
        await asyncio.sleep(2.0)
        await smg.delete()
        return None
      if cs == f'{ctx.author.id}E':
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
        if '미성' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 50000
        
        skils = ['미성']
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': asdf + skils})
        dir.update({'돈' : money})
        embed = discord.Embed(title="T스킬 : 미성 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 아url)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'T스킬 : 미성 구매완료!\n> 잔액 : {money}원')
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
        if '부스터엔진' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 60000
        
        skils = ['부스터엔진']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 부스터엔진 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="D스킬 : 부스터엔진 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
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
        dir = db.reference(f"{ctx.author.id}/스킬보유")
        asdf = dir.get()
        if '네크로멘서' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 100000
        
        skils = ['네크로멘서']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'T스킬 : 네크로멘서 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="T스킬 : 네크로멘서 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
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
                    SelectOption(emoji = ticket, label = "100LV 강화권 : 150000원", description ="자신의 곡괭이를 100렙으로 변경", value = f"{ctx.author.id}A"),
                    SelectOption(emoji = 회복술사, label = "T SKILL : 미성 : 90000원",description ="모든 친밀도 증가량 +1 증가", value = f"{ctx.author.id}B"),
                    SelectOption(emoji = adrnr, label = "D SKILL : 부스터엔진 : 50000원",description ="대륙간의 이동 -50%",  value = f"{ctx.author.id}C"),
                    SelectOption(emoji = 베테랑, label = "T SKILL : 네크로멘서 : 100000원",description ="스테미너를 회복 + 2초간 무적", value = f"{ctx.author.id}D"),
                    SelectOption(emoji = tickets, label = "HK TICKET : 100000원", description ="다른 대륙으로 이동할 수 있는 티켓입니다.", value = f"{ctx.author.id}E"),
                    SelectOption(emoji = no, label = "구매를 취소합니다", value = f"{ctx.author.id}N")
                  ]
              )
          ]
      )
      urll = "https://media.discordapp.net/attachments/941151376568897538/952075822393593936/70_20220312142903.jpg?width=469&height=469"
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
        dir = db.reference(f"{ctx.author.id}/곡산대륙/강화권")
        TICKET = dir.get()
        TICKET = TICKET + 1
        money = money - 150000
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'돈' : money})
        dir.update({'ing' : 0})
        dir = db.reference(f"{ctx.author.id}/곡산대륙")
        dir.update({'강화권' : TICKET})
        
        embed = discord.Embed(title="100LV 강화권 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url=urll)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'100LV 강화권 구매완료!\n> 잔액 : {money}원')
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
        if '미성' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 50000
        
        skils = ['미성']
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': asdf + skils})
        dir.update({'돈' : money})
        embed = discord.Embed(title="T스킬 : 미성 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
        embed.set_image(url= 아url)
        smg = await ctx.author.dm_channel.send(embed = embed)
        await ctx.reply(f'T스킬 : 미성 구매완료!\n> 잔액 : {money}원')
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
        if '부스터엔진' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 60000
        
        skils = ['부스터엔진']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'D스킬': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'D스킬 : 부스터엔진 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="D스킬 : 부스터엔진 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
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
        dir = db.reference(f"{ctx.author.id}/스킬보유")
        asdf = dir.get()
        if '네크로멘서' in asdf:
          await ctx.author.dm_channel.send('이미 구매한 스킬입니다')
          dir = db.reference(f"{ctx.author.id}")
          dir.update({'ing' : 0})
          return None

        money = money - 100000
        
        skils = ['네크로멘서']
        skill = asdf + skils
        if '없음' in skill:
          del skill[0]
        dir = db.reference(f"{ctx.author.id}")
        dir.update({'스킬보유': skill})
        dir.update({'돈' : money})
        dir = db.reference(f"{ctx.author.id}/D스킬")
        asdf = dir.get()
        
        await ctx.reply(f'T스킬 : 네크로멘서 구매완료!\n> 잔액 : {money}원')
        embed = discord.Embed(title="T스킬 : 네크로멘서 구매완료!", description=f"잔액 : {money}원", color=0x62c1cc)
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


      if cs == f'{ctx.author.id}E':
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
      await interaction.send(content = f"{interaction.values[0]}   selected!")



