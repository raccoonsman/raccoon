import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
import random
import asyncio
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from gifta import gifta
from gotime import gotime



async def sagu(ctx, bot):
  dir = db.reference(f'{ctx.author.id}/곡산대륙/현재시간')
  time = dir.get()
  if '밤' == time:
    await ctx.reply('야간에는 사교가 불가능합니다!')
    return None
  if '새벽' == time:
    await ctx.reply('야간에는 사교가 불가능합니다!')
    return None
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/싱그러운_물')
  ga = dir.get()
  dir = db.reference(f'{ctx.author.id}/착용스킬')
  slist = str(dir.get())
  if '미성' in slist:
    N = 2
    print('dd')

  else:
    N = 1
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/코X콜라')
  gb = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/저울')
  gc = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/전파시계')
  gd = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/드워프의_망치')
  ge = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/곡괭이')
  gf = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/금화')
  gg = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/에너지드링크')
  gh = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/프로틴')
  gi = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/가공된_목걸이')
  gj = dir.get()
    
  dir = db.reference(f'{ctx.author.id}/대륙')
  asdf = dir.get()
  if asdf == 1:
    return None
  dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC/대장장이')
  불칸 = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC/상인')
  리우스 = dir.get()
  dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC/NPC1')
  프러드 = dir.get()
  dir = db.reference(f'{ctx.author.id}')
  dir.update({'ing' : '사교'})  
  msg = await ctx.send(
        "반드시 사교 전에 `?사교튜토리얼`을 필독하여 주세요!",
        components = [
            Select(
                placeholder = "사교할 상대를 선택해주세요!",
                options = [
                    SelectOption(label = "대장장이 : 불카", description =f"친밀도 : {불칸}", value = f"{ctx.author.id}A"),
                    SelectOption(label = "상인 : 리우스", description =f"친밀도 : {리우스}", value = f"{ctx.author.id}B"),
                    SelectOption(label = "광부 : 프러드", description =f"친밀도 : {프러드}", value = f"{ctx.author.id}C"),
                  SelectOption(label = "사교 취소하기", value = f"{ctx.author.id}N")
                ]
            )
        ]
    )

  interaction = await bot.wait_for("select_option")
  check = interaction.values[0]
  if check == f"{ctx.author.id}A":
    if 불칸 == 'MAX':
      await ctx.reply('불카와의 친밀도가 이미 MAX상태입니다.')
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})
      await msg.delete()
      return None
    await interaction.send(content = f"불카와 잡다한 이야기를 하며 시간을 보냈습니다...")
    await gotime(ctx)
    await asyncio.sleep(3.0)
    s = await ctx.reply(content = f"불카와의 친밀도가 증가했습니다.\n```\n불카에게 선물을 주시겠습니까?\n1. 예 | 2.아니오\n```")
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC')
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await s.delete()
      await ctx.send('우물쭈물 하고 있는 당신을 보며 불카는 의문을 가집니다')
      await ctx.send(f'불카와의 친밀도가 {1*N} 상승하였습니다!')
      불칸 = 불칸 + (1*N)
      dir.update({'대장장이' : 불칸})
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})  
      return None
    else:
      s = int(msg.content)
      if s == 1:
        b = await ctx.reply(f'**불카에게 줄 선물을 고르세요!**\n```\n1. 싱그러운_물 : {ga}개\n2. 코X콜라 : {gb}개\n3. 저울 : {gc}개\n4. 전파시계 : {gd}개\n5. 드워프의_망치 : {ge}개\n6. 곡괭이 : {gf}개\n7. 금화 : {gg}개\n8. 에너지드링크 : {gh}개\n9. 프로틴 : {gi}개\n10. 가공된_목걸이 : {gj}개\n```\n> 숫자를 적어주세요!\n**보유하지 않은 선물을 줄 시 사교가 바로 종료됩니다**')
        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await b.delete()
          await ctx.send('우물쭈물 하고 있는 당신을 보며 불카는 의문을 가집니다')
          await ctx.send(f'불카와의 친밀도가 {1*N} 상승하였습니다!')
          불칸 = 불칸 + (1*N)
          dir.update({'대장장이' : 불칸})
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})  
          return None
        else:
          s = int(msg.content)
          checks = [1, 5, 7, 10]
          sb = await gifta(ctx, s)
          if sb == 1:
            return None
          if s not in checks:
            await ctx.reply('불카 : 음....미안하지만 이건 별로인데...다시 가져가게나')
            await asyncio.sleep(1.0)
            await ctx.reply('불카는 별로 기뻐보이지 않습니다.')
            await asyncio.sleep(1.0)
            await ctx.send('불카와의 친밀도가 1 하락하였습니다!')
            불칸 = 불칸 - 1
            dir.update({'대장장이' : 불칸})
            dir = db.reference(f'{ctx.author.id}')
            dir.update({'ing' : 0})  
            return None
            
          msg = await ctx.send('```\n불카 : 음..? 이건?\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n불카 : 음..? 이건?\n{ctx.author.name} : 선물이야\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n불카 : 음..? 이건?\n{ctx.author.name} : 선물이야\n불카 : 호오...이 물건은 매력있는 물건이구만...고맙네!\n```')
          await asyncio.sleep(1.0)
          await ctx.reply('불카는 기뻐합니다!')
          await asyncio.sleep(1.0)
          await ctx.send(f'불카와의 친밀도가 {5*N} 상승하였습니다!')
          불칸 = 불칸 + 5*N
          dir.update({'대장장이' : 불칸})
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})
          if 불칸 >= 100:
            await ctx.send(f'> {ctx.author.name} : 오늘도 잘부탁드립니다.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : 흐음..자네..혹시')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : [시간의 조각]이라는 걸 아나?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : [시간의 조각]이요? 그게 뭔가요?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : 자네도 알다시피 곡괭이강화로 채굴력을 높일수 있는 방법은 한계가 있어.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : 내가 알기로는 200강 이상부터는 [시간의 조각]이 반드시 필요하지')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : [시간의 조각]이 뭐길래...')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : [시간의 조각]은 시간을 과거로 돌린 반동으로 생겨난 반작용물질이야.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : [시간의 조각]을 사용하여 곡괭이를 강화하면 더욱더 강해지게 된다.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 오호...그렇군요...[시간의 조각]은 어디서 얻나요?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 불카 : 그건...나도 모르겠군...미안하다...')
            await asyncio.sleep(1.5)
            await ctx.reply(f'**[시간의 조각]의 정보를 얻었습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**불카와의 친밀도가 최대가 되었습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**불카와의 사교를 컴플리트했습니다!**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**[SKILL : 대장장이의 손길]을 얻었습니다.**')
            dir = db.reference(f'{ctx.author.id}/스킬보유')
            skillist = dir.get()
            ska = ['대장장이의_손길']
            dir = db.reference(f'{ctx.author.id}')
            dir.update({'스킬보유' : skillist + ska})
            dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC')
            dir.update({'대장장이' : 'MAX'})
          return None
      if s == 2:
        await ctx.send(f'불카와의 친밀도가 {1*N} 상승하였습니다!')
        불칸 = 불칸 + 1*N
        dir.update({'대장장이' : 불칸})
        dir = db.reference(f'{ctx.author.id}')
        dir.update({'ing' : 0})  
        return None

      await ctx.reply('unknown error')
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})  

  if check == f"{ctx.author.id}B":
    if 리우스 == 'MAX':
      await ctx.reply('리우스와의 친밀도가 이미 MAX상태입니다.')
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})
      await msg.delete()
      return None
    
    await interaction.send(content = f"리우스와 주식에 관한 이야기를 하며 시간을 보냈습니다...")
    await asyncio.sleep(3.0)
    await gotime(ctx)
    s = await ctx.reply(content = f"리우스와의 친밀도가 증가했습니다.\n```\n리우스에게 선물을 주시겠습니까?\n1. 예 | 2.아니오\n```")
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC')
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await s.delete()
      await ctx.send('우물쭈물 하고 있는 당신을 보며 리우스는 의문을 가집니다')
      await ctx.send(f'리우스와의 친밀도가 {1*N} 상승하였습니다!')
      리우스 = 리우스 + 1
      dir.update({'상인' : 리우스})
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})  
      return None
    else:
      s = int(msg.content)
      if s == 1:
        b = await ctx.reply(f'**리우스에게 줄 선물을 고르세요!**\n```\n1. 싱그러운_물 : {ga}개\n2. 코X콜라 : {gb}개\n3. 저울 : {gc}개\n4. 전파시계 : {gd}개\n5. 드워프의_망치 : {ge}개\n6. 곡괭이 : {gf}개\n7. 금화 : {gg}개\n8. 에너지드링크 : {gh}개\n9. 프로틴 : {gi}개\n10. 가공된_목걸이 : {gj}개\n```\n> 숫자를 적어주세요!\n**보유하지 않은 선물을 줄 시 사교가 바로 종료됩니다**')
        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await b.delete()
          await ctx.send('우물쭈물 하고 있는 당신을 보며 리우스는 의문을 가집니다')
          await ctx.send(f'리우스와의 친밀도가 {1*N} 상승하였습니다!')
          리우스 = 리우스 + 1*N
          dir.update({'상인' : 리우스})
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})  
          return None
        else:
          s = int(msg.content)
          checks = [1, 2, 3, 4, 7, 10]
          sb = await gifta(ctx, s)
          if sb == 1:
            return None
          if s not in checks:
            await ctx.reply('리우스 : 하? 이게 뭔가?')
            await asyncio.sleep(1.0)
            await ctx.reply('리우스는 별로 기뻐보이지 않습니다.')
            await asyncio.sleep(1.0)
            await ctx.send('리우스와의 친밀도가 1 하락하였습니다!')
            리우스 = 리우스 - 1
            dir.update({'상인' : 리우스})
            dir = db.reference(f'{ctx.author.id}')
            dir.update({'ing' : 0})  
            return None
            
          msg = await ctx.send('```\n리우스 : 허? 이게 뭔가?\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n리우스 : 허? 이게 뭔가?\n{ctx.author.name} : 선물이야\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n리우스 : 허? 이게 뭔가?\n{ctx.author.name} : 선물이야\n리우스 : 고맙군! 특별히 자네에게는 특별한 서비스를 해주도록 하지.\n```')
          await asyncio.sleep(1.0)
          await ctx.reply('리우스는 기뻐합니다!')
          await asyncio.sleep(1.0)
          await ctx.send(f'리우스와의 친밀도가 {5*N} 상승하였습니다!')
          리우스 = 리우스 + 5*N
          dir.update({'상인' : 리우스})
          if 리우스 >= 100:
            await ctx.send(f'> {ctx.author.name} : 오늘도 잘부탁드립니다.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 오 자네군! 잘왔어!')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 자네에게 서비스를 해준다고 한걸 이제 지키게 되었구만!')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 와! 드디어')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 내가 오늘 어떤 사람에게서 구해온 거라네')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 그 사람이 말하기론 [시간의 조각]이라고 하던데 혹시 자네는 이게 뭔지 아는가?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : ....[시간의 조각]이요..?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 나도 이거에 대해선 몰라')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 하지만 그냥 장식용으로 쓰면 되겠구나 해서 가져온거라네')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 오....일단 감사합니다!')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 리우스 : 다음에도 이용해주게나!')
            await asyncio.sleep(1.5)
            await ctx.reply(f'**[시간의 조각]을 10개 얻었습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**리우스와의 친밀도가 최대가 되었습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**리우스와의 사교를 컴플리트했습니다!**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**앞으로 리우스에게 광물을 살수 있습니다! `?매입`**')
            dir = db.reference(f'{ctx.author.id}/스킬보유')
            
            dir.update({'상인' : 'MAX'})
            dir = db.reference(f'{ctx.author.id}/곡산대륙')
            dir.update({'시간의조각' : 10})            
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})  
          return None
      if s == 2:
        await ctx.send(f'리우스와의 친밀도가 {1*N} 상승하였습니다!')
        리우스 = 리우스 + 1
        dir.update({'상인' : 리우스})
        dir = db.reference(f'{ctx.author.id}')
        dir.update({'ing' : 0})  
        return None


  if check == f"{ctx.author.id}C":
    if 프러드 == 'MAX':
      await ctx.reply('프러드와의 친밀도가 이미 MAX상태입니다.')
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})
      await msg.delete()
      return None
    
    await interaction.send(content = f"프러드와 광물에 관한 이야기를 하며 시간을 보냈습니다...")
    await gotime(ctx)
    await asyncio.sleep(3.0)
    s = await ctx.reply(content = f"프러드와의 친밀도가 증가했습니다.\n```\n프러드에게 선물을 주시겠습니까?\n1. 예 | 2.아니오\n```")
    timeout = 10
    def check(m):
      return m.author == ctx.author

    try:
      dir = db.reference(f'{ctx.author.id}/곡산대륙/NPC')
      msg = await bot.wait_for('message',check=check, timeout=timeout)
    except asyncio.TimeoutError:
      await s.delete()
      await ctx.send('우물쭈물 하고 있는 당신을 보며 프러드는 의문을 가집니다')
      await ctx.send(f'프러드와의 친밀도가 {1*N} 상승하였습니다!')
      프러드 = 프러드 + 1*N
      dir.update({'NPC1' : 프러드})
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})  
      return None
    else:
      s = int(msg.content)
      if s == 1:
        b = await ctx.reply(f'**프러드에게 줄 선물을 고르세요!**\n```\n1. 싱그러운_물 : {ga}개\n2. 코X콜라 : {gb}개\n3. 저울 : {gc}개\n4. 전파시계 : {gd}개\n5. 드워프의_망치 : {ge}개\n6. 곡괭이 : {gf}개\n7. 금화 : {gg}개\n8. 에너지드링크 : {gh}개\n9. 프로틴 : {gi}개\n10. 가공된_목걸이 : {gj}개\n```\n> 숫자를 적어주세요!\n**보유하지 않은 선물을 줄 시 사교가 바로 종료됩니다**')
        try:
          msg = await bot.wait_for('message',check=check, timeout=timeout)
        except asyncio.TimeoutError:
          await b.delete()
          await ctx.send('우물쭈물 하고 있는 당신을 보며 프러드는 의문을 가집니다')
          await ctx.send(f'프러드와의 친밀도가 {1*N} 상승하였습니다!')
          프러드 = 프러드 + 1*N
          dir.update({'NPC1' : 프러드})
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})  
          return None
        else:
          s = int(msg.content)
          checks = [1, 6, 8, 9, 10]
          sb = await gifta(ctx, s)
          if sb == 1:
            return None
          if s not in checks:
            await ctx.reply('프러드 : 음...')
            await asyncio.sleep(1.0)
            await ctx.reply('프러드는 별로 기뻐보이지 않습니다.')
            await asyncio.sleep(1.0)
            await ctx.send('프러드와의 친밀도가 1 하락하였습니다!')
            프러드 = 프러드 - 1
            dir.update({'NPC1' : 프러드})
            dir = db.reference(f'{ctx.author.id}')
            dir.update({'ing' : 0})  
            return None
            
          msg = await ctx.send('```\n프러드 : 오? 이게 뭔가?\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n프러드 : 오 이게 뭔가?\n{ctx.author.name} : 선물이야\n```')
          await asyncio.sleep(1.5)
          await msg.edit(f'```\n프러드 : 오? 이게 뭔가?\n{ctx.author.name} : 선물이야\n프러드 : 고마워! 이걸로 질 좋은 광물을 채굴할 수 있을꺼 같아!\n```')
          await asyncio.sleep(1.0)
          await ctx.reply('프러드는 기뻐합니다!')
          await asyncio.sleep(1.0)
          await ctx.send(f'프러드와의 친밀도가 {5*N} 상승하였습니다!')
          프러드 = 프러드 + 5*N
          dir.update({'NPC1' : 프러드})
          if 프러드 >= 100:
            await ctx.send(f'> {ctx.author.name} : 오늘도 잘부탁드립니다.')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 오 자네군! 좋은 타이밍이야!')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 자네...시간되나?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 무슨일이죠?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 오늘 같이 채굴하러 가지 않겠나?')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 혼자 채굴하면 심심하거든')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 좋아요!')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 그래! 날 따라 오게나!')
            await asyncio.sleep(1.5)
            await ctx.send(f'**프러드와 같이 채굴을 했습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'> {ctx.author.name} : 오....힘드네요....')
            await asyncio.sleep(1.5)
            await ctx.send(f'> 프러드 : 자네 왜이리 채굴을 잘하는가? 진짜 자네가 맘에 드는구만!')
            await asyncio.sleep(1.5)
            await ctx.send(f'다행이네요....')
            await asyncio.sleep(1.5)
            await ctx.send(f'**프러드와의 친밀도가 최대가 되었습니다**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**프러드와의 사교를 컴플리트했습니다!**')
            await asyncio.sleep(1.5)
            await ctx.send(f'**다른 사람과 같이 채굴이 가능해집니다!**')
            dir = db.reference(f'{ctx.author.id}/스킬보유')
            
            dir.update({'NPC1' : 'MAX'})
          dir = db.reference(f'{ctx.author.id}')
          dir.update({'ing' : 0})  
          return None
      if s == 2:
        await ctx.send(f'프러드와의 친밀도가 {1*N} 상승하였습니다!')
        프러드 = 프러드 + 1*N
        dir.update({'NPC1' : 프러드})
        dir = db.reference(f'{ctx.author.id}')
        dir.update({'ing' : 0})  
        return None

      await ctx.reply('unknown error')
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'ing' : 0})

  if check == f"{ctx.author.id}N":
    dir = db.reference(f'{ctx.author.id}')
    dir.update({'ing' : 0})
    await msg.delete()
    await ctx.reply('취소되었습니다')