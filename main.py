from keep_alive import keep_alive
import asyncio
import firebase_admin
import discord
import random
from firebase_admin import credentials
from firebase_admin import db
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption
from discord import Intents
from discord.ext import commands
import string
from discord.ext import tasks
from itertools import cycle
from disrankmaster.disrank.generator import Generator

from command.signupu import signup
from command.information import myinformation

from command.mylocation import mylocation
from command.map import map
from command.gamehelp import gamehelp
from command.reinforce import reinforce
from economy.초보자광산채굴 import 초보자광산채굴
from economy.태초광산채굴 import 태초광산채굴
from command.lvup import lvup
from command.price import price, pricetag
from command.shop import shop
from economy.매도 import aoeh
from command.move import move
from command.invent import invent
from command2.shop2 import shop2
from 튜토 import 튜토
#import

#2대륙
from command2.embarkation import embarkation
from command2.cmove import cmove
from command2.곡산광산채굴 import 곡산광산채굴
from command2.card import card
from command2.태극광산 import 태극광산
from gotime import gotime
from command2.sleep import sleep
from command2.giftcord import giftcord
from gifta import gifta
from command2.사교 import sagu
intents = discord.Intents.default()
client = discord.Client(intents=intents)


bot = commands.Bot(
    command_prefix=['?', 'pip '],
    test_guilds=[929003453966065724], # Optional
    sync_commands_debug=True
)
bot = ComponentsBot(command_prefix = ['?', 'pip '])
status = cycle(["2챕 업데이트 완료!", "?도움말", f"도움말 갱신!", "이벤트!"])

#접두사

cred = credentials.Certificate('파일명')
firebase_admin.initialize_app(cred,{
    'databaseURL' : ''
})
#DB 연결

@bot.event
async def on_ready():
	change_status.start()



@bot.command(aliases=['ㄷㅇ', 'uhelp'])
async def 도움말(ctx):
  await gamehelp(ctx)
   # embed를 포함 한 채로 메시지를 전송합니다.https://discord.gg/SbHP932TFu
'''
@bot.command()
async def ghelp(ctx):
  await gamehelp(ctx) # embed를 포함 한 채로 메시지를 전송합니다.
'''
@bot.command(aliases=['서포트서버','오류신고'])
async def shelp(ctx):
  await ctx.reply('공식 서포트 섭입니다\n>>> https://discord.gg/5R5yhCyQQT')


@bot.command(aliases=['ㅌㅌ'])
async def 튜토리얼(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  await 튜토(ctx)



@bot.event
async def on_command_error(ctx, error):
  
  if isinstance(error, commands.CommandOnCooldown):
    msg = await ctx.send(f'`{round(error.retry_after, 2)}초` 후에 다시 명령어를 사용할 수 있어요!', reference=ctx.message, mention_author=False)
    await asyncio.sleep(1.0)
    await msg.delete()
    await ctx.message.delete()
    #쿨타임

#가입
@bot.command(aliases=['ㄱㅇ'])
async def 가입(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    
    msg = await ctx.reply('가입중.....')
    signup(ctx)
    await msg.delete()
    await ctx.channel.send(f'{ctx.message.author.mention}, 가입에 성공하였습니다!\n`?튜토리얼(=ㅌㅌ)`을 입력해보세요!', reference=ctx.message)
  else:
    await ctx.send('가입이 되어 있습니다.')
    #가입이 되있을 경우

#내위치/정보/스킬장착/인벤/이동/내위치/지도

#위치확인
@bot.command(aliases=['ㄴㅇㅊ','ㅇㅊ'])
async def 내위치(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
  else:
    await mylocation(ctx)
    

'''
#정보확인
@bot.command(aliases=['ㅈㅂ'])
async def 정보(ctx, users : discord.Member):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')#가입확인
  
  else:
    id = users.id
    name = users.name
    await myinformation(ctx)
'''    

#스킬장착123
@bot.command(aliases=['=1'])
async def 장착1(ctx, skillname):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!') #가입확인
  else:
    dir = db.reference(f"{ctx.author.id}/스킬보유")
    dir = str(dir.get())
    check = dir.find(skillname)
    if check == -1:
      await ctx.reply('보유하지 않거나 없는 스킬입니다.')

    else:
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬1")
      skil1 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬2")
      skil2 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬3")
      skil3 = dir.get()
      
      
      if skillname == skil1:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil2:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil3:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None
      
      
      await ctx.reply(
          f'```\nSKILL : <{skillname}>를 창착하였습니다\n```'
      )
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      dir.update({'스킬1' : skillname})
    
@bot.command(aliases=['=2'])
async def 장착2(ctx, skillname):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!') #가입확인
  else:
    dir = db.reference(f"{ctx.author.id}/스킬보유")
    dir = str(dir.get())
    check = dir.find(skillname)
    if check == -1:
      await ctx.reply('보유하지 않거나 없는 스킬입니다.')

    else:
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬1")
      skil1 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬2")
      skil2 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬3")
      skil3 = dir.get()
      
      
      if skillname == skil1:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil2:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil3:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None
      
      
      await ctx.reply(
          f'```\nSKILL : <{skillname}>를 창착하였습니다\n```'
      )
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      dir.update({'스킬2' : skillname})

@bot.command(aliases=['=3'])
async def 장착3(ctx, skillname):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!') #가입확인
  else:
    dir = db.reference(f"{ctx.author.id}/스킬보유")
    dir = str(dir.get())
    check = dir.find(skillname)
    if check == -1:
      await ctx.reply('보유하지 않거나 없는 스킬입니다.')

    else:
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬1")
      skil1 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬2")
      skil2 = dir.get()
      dir = db.reference(f"{ctx.author.id}/착용스킬/스킬3")
      skil3 = dir.get()
      
      
      if skillname == skil1:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil2:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None

      if skillname == skil3:
        await ctx.reply('이미 장착이 되어 있습니다.')
        return None
      
      
      await ctx.reply(
          f'```\nSKILL : <{skillname}>를 창착하였습니다\n```'
      )
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      dir.update({'스킬3' : skillname})

@bot.command(aliases=['인벤', 'ㅇㅂㅌㄹ', 'ㅇㅂ'])
async def 인벤토리(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
  else:   
    await invent(ctx, bot)

#위치이동


@bot.command(aliases=['ㅈㄷ'])
async def 지도(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
  else:
    await map(ctx)

#강화

@bot.command(aliases=['ㄱㅎ'])
async def 강화(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  dir = db.reference(f'{ctx.author.id}/대륙')
  dgs = dir.get()  
  if dgs == 2:
    dir = db.reference(f'{ctx.author.id}/곡산대륙/현재시간')
    nowtime = dir.get()
    if nowtime == '밤':
      await ctx.reply('밤에는 강화가 불가능합니다!')
      return None
    if nowtime == '새벽':
      await ctx.reply('새벽에는 강화가 불가능합니다!')
      return None
  await reinforce(ctx)

#메인컨텐츠
@bot.command(aliases=['ㅊㄱ'])
async def 채굴(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  
  #가입체크
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  

  #스테미너 체크=sp

  global sp, power, mylv, sk1, sk2, sk3, att
  dir = db.reference(f"{ctx.author.id}/스테미너")
  sp = dir.get()
  if sp <= 0:
    await ctx.reply('스테미너가 1이하입니다...\n> 치료방법\n> 근처마을에서 `?회복`명령어를 입력하세요')
    return None
  
  #채굴력=power
  dir = db.reference(f"{ctx.author.id}/채굴력")
  power = dir.get()

  dir = db.reference(f"{ctx.author.id}/레벨")
  mylv = dir.get()
  
  dan = bot.get_emoji(946784214978789376) #단전호흡
  dmd = bot.get_emoji(946784683587420203) #응급처치
  dkemfp = bot.get_emoji(947096750940901436) #아드레날린
  ske = ['없음']

  
  #skill=sk
  dir = db.reference(f"{ctx.author.id}/착용스킬/스킬1")
  sk1 = dir.get()
  dir = db.reference(f"{ctx.author.id}/착용스킬/스킬2")
  sk2 = dir.get()
  dir = db.reference(f"{ctx.author.id}/착용스킬/스킬3")
  sk3 = dir.get()
  
  #-------------
  #skillcheck
  N = 0
  Cj = 0
  if sk1 == '단전호흡':
    N = 5
    ㄷㄴㅎㅎ = [f'{dan}']
    ske = ske + ㄷㄴㅎㅎ

  if sk1 == '응급처치':
    Cj = 1
    ㅇㄱㅊㅊ = [f'{dmd}']
    ske = ske + ㅇㄱㅊㅊ

  if sk1 == '아드레날린':
    ㅇㄷㄹ = [f'{dkemfp}']
    ske = ske + ㅇㄷㄹ

    
  if sk2 == '단전호흡':
    N = 5
    ㄷㄴㅎㅎ = [f'{dan}']
    ske = ske + ㄷㄴㅎㅎ

  if sk2 == '응급처치':
    Cj = 1
    ㅇㄱㅊㅊ = [f'{dmd}']
    ske = ske + ㅇㄱㅊㅊ

  if sk2 == '아드레날린':
    ㅇㄷㄹ = [f'{dkemfp}']
    ske = ske + ㅇㄷㄹ

  
  if sk3 == '단전호흡':
    N = 5
    ㄷㄴㅎㅎ = [f'{dan}']
    ske = ske + ㄷㄴㅎㅎ
   
  if sk3 == '응급처치':
    Cj = 1
    ㅇㄱㅊㅊ = [f'{dmd}']
    ske = ske + ㅇㄱㅊㅊ
  
  if sk3 == '아드레날린':
    ㅇㄷㄹ = [f'{dkemfp}']
    ske = ske + ㅇㄷㄹ

    


  #중복/이동탐색체크
  dir = db.reference(f"{ctx.author.id}/ing")
  ing1 = dir.get()
  if ing1 != 0:
    if ing1 == '이동':
      await ctx.reply(f'현재 {ing1}중입니다.')
      return None
    await ctx.reply(f'현재 {ing1}중입니다.\n> 강제종료는 `?ㅈㄹ`를 입력해주세요')
    return None

  #---------------


  dir = db.reference(f"{ctx.author.id}")
  dir.update({'ing' : '탐색'})

  val = 0
  dir = db.reference(f"{ctx.author.id}/착용스킬")
  dir = str(dir.get())
  val = dir.find("아드레날린")
  MZ = 0
  if val != -1:
    power = int((power + (power / 100) * 20))
    MZ = 20

    
  dir = db.reference(f"{ctx.author.id}/현재위치")
  location = dir.get()
  #초보자광산
  if location == '초보자광산':
    await 초보자광산채굴(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, power, MZ, ske, dmd)
    await lvup(ctx)
    return None

  #태초광산  
  if location == '태초광산':
    await 태초광산채굴(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, power, MZ, ske, dmd)
    await lvup(ctx)
    return None

  if location == '곡산광산':
    await 곡산광산채굴(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, power, MZ, ske, dmd)
    await lvup(ctx)
    await gotime(ctx)
    return None

  if location == '태극광산':
    await 태극광산(ctx, N, Cj, sp, power, mylv, sk1, sk2, sk3, power, MZ, ske, dmd)
    await lvup(ctx)
    await gotime(ctx)
    return None


  await ctx.reply('채굴 명령어는 `~광산`지역에서만 가능합니다\n`?ㅇㅊ`명령어를 사용해 자신의 위치를 확인하세요')
  dir = db.reference(f"{ctx.author.id}")
  dir.update({'ing' : 0})
  return None





@bot.event
async def on_message(message):    
  if message.author.bot:
    return None
  


  if message.content == "?장착1":
    await message.channel.send('`?스킬장착1 (스킬명)`입니다.')

  if message.content == "?장착2":
    await message.channel.send('`?스킬장착1 (스킬명)`입니다.')

  if message.content == "?장착3":
    await message.channel.send('`?스킬장착1 (스킬명)`입니다.')

  #if message.content == "?장착":
    #await message.channel.send('`?스킬장착1/2/3 (스킬명)`입니다.')

  if message.content == "?정보":
    val = -1
    dir = db.reference('user')
    dir = str(dir.get())
    val = dir.find(f"{message.author.id}")
    if val == -1:
      await message.channel.send('`?가입`을 먼저 진행해주세요!')
      return None
    await myinformation(message)
    #await card(message)
  if message.content == "?ㅈㅂ":
    val = -1
    dir = db.reference('user')
    dir = str(dir.get())
    val = dir.find(f"{message.author.id}")
    if val == -1:
      await message.channel.send('`?가입`을 먼저 진행해주세요!')
      return None
    await myinformation(message)
    #await card(message)

  

  await bot.process_commands(message)



@bot.command(aliases=['ㄱㄱㅍ', 'ㄷㄱ'])
async def 가격표(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')#가입확인
  
  else:
    await pricetag(ctx)


@bot.command(aliases=['ㄱㄱ'])
async def 가격(ctx, name):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')#가입확인
  
  else:
    await price(ctx, name)

@bot.command(aliases=['ㄱㅈㅈㄹ','ㅈㄹ'])
async def 강제종료(ctx):
  dir = db.reference(f'{ctx.author.id}/ing')
  i1 = dir.get()
  if i1 == '이동':
    return None
  
  if i1 == 0:
    await ctx.reply('현재 어떠한 행동도 취하고 있지 않습니다.')
    return None


  dir = db.reference(f"{ctx.author.id}")
  dir.update({'ing' : 0})
  await ctx.reply('탐색이 강제종료가 되었습니다.')



@bot.command()
async def 해제(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
  
  else:
    dir = db.reference(f"{ctx.author.id}/착용스킬")
    dir.update({'스킬1' : '없음'})
    dir.update({'스킬2' : '없음'})
    dir.update({'스킬3' : '없음'})
    await ctx.reply('모든 스킬이 해제되었습니다.')




@bot.command(aliases=['ㅁㅇ'])
async def 매입(ctx):#thing = 광물명 cut = 갯수
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')#가입확인
  else:
    dir = db.reference(f"{ctx.author.id}/현재위치")#위치확인
    await ctx.reply('곧 업데이트 됩니다!')


#rank     
@bot.command(aliases=['ㅁㄷ'])
async def 매도(ctx):#thing = 광물명 cut = 갯수
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')#가입확인
  else:
    dir = db.reference(f"{ctx.author.id}/현재위치")#위치확인
    location = dir.get()
    if location != '태초마을':#마을인가?
      if location != '곡산마을':#마을인가?
        await ctx.reply('광석매도은 `~마을`에서만 가능합니다!')
        return None

        
    dir = db.reference(f"{ctx.author.id}/ing")
    schs = dir.get()
    if schs != 0:
      await ctx.reply(f'매도이 불가능합니다!(사유 : {schs}중)')
      return None

    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : '매도'})
    coal = bot.get_emoji(941149938115543081)
    steel = bot.get_emoji(941150022467223602)
    gold = bot.get_emoji(941151007386238976)
    ll = bot.get_emoji(941151091532369960)
    di = bot.get_emoji(941151238588866580)
    ai = bot.get_emoji(941151289633562624)
    no = bot.get_emoji(943780055761440779)
    
    await aoeh(ctx, bot, coal, steel, gold, ll, di, ai, no)

#개발자전용
@bot.command()
async def 지급(ctx, x : int, y, z, g : int):#아이디, 코드, 이름, 갯수
  a = ['712838792595112006','914528773121146940']
  b = str(ctx.author.id)

  if b not in a:
    await ctx.reply('개발자만 사용 가능합니다')
    return None

  if y == '광물':
    dir = db.reference(f"{x}/{y}/{z}")
    h = dir.get()
    h = h + g
    dir = db.reference(f"{x}/{y}")
    dir.update({z : h})
    await ctx.reply('증정성공')
    return None

  dir = db.reference(f"{x}/{y}")
  h = dir.get()
  h = h + g
  dir = db.reference(f"{x}")
  dir.update({y : h})
  await ctx.reply('증정성공')

@bot.command(aliases=['ㅇㄷ'])
async def 이동(ctx):
 
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None
  else:
    dir = db.reference(f"{ctx.author.id}/ing")
    ings = dir.get()
    if ings != 0:
      await ctx.reply(f'이동이 불가합니다.(사유 : {ings}중)')
      return None
    dir = db.reference(f"{ctx.author.id}")
    dir.update({'ing' : '이동'})
    dir = db.reference(f"{ctx.author.id}/현재위치")
    location = dir.get()
    dir = db.reference(f"{ctx.author.id}/대륙")
    continent = dir.get()
    if continent == 1:
      _LENGTH = 1
      string_pool = string.ascii_uppercase
      result = ""
      for i in range(_LENGTH):
        result += random.choice(string_pool)
      print(result)
      yes = result

      A = bot.get_emoji(943064541309308969)
      B = bot.get_emoji(943064559877513297)
      C = bot.get_emoji(943064574469484604)
      D = bot.get_emoji(943064587127906305)
      S = bot.get_emoji(943780055761440779)
      
      val = -1
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      dir = str(dir.get())
      val = dir.find("축지법")
      CH = 2
      if val == -1:
        CH = 1
        

      print(CH)
      MTX = int(10 / CH)
      print(MTX)
      await move(ctx, bot, A, B, C, D, S, result, yes, location, MTX)
      return None

      
    if continent == 2:#곡산
      _LENGTH = 1
      string_pool = string.ascii_uppercase
      result = ""
      for i in range(_LENGTH):
        result += random.choice(string_pool)
      print(result)
      yes = result

      A = bot.get_emoji(943064541309308969)
      B = bot.get_emoji(943064559877513297)
      C = bot.get_emoji(943064574469484604)
      D = bot.get_emoji(943064587127906305)
      S = bot.get_emoji(943780055761440779)
      
      val = -1
      dir = db.reference(f"{ctx.author.id}/착용스킬")
      dir = str(dir.get())
      val = dir.find("축지법")
      CH = 2
      if val == -1:
        CH = 1
        

      print(CH)
      MTX = int(10 / CH)
      print(MTX)
      await cmove(ctx, bot, A, B, C, D, S, result, yes, location, MTX)
      return None
      
@bot.command()
async def 관리자종료(ctx, users : discord.Member):#아이디, 코드, 이름, 갯수
  a = ['712838792595112006','914528773121146940']
  b = str(ctx.author.id)

  if b not in a:
    await ctx.reply('개발자만 사용 가능합니다')
    return None

  ids = users.id
  dir = db.reference(f"{ids}")
  dir.update({'ing' : 0})
  await ctx.reply('완료')


@bot.command()
async def 관리자정보(ctx):#아이디, 코드, 이름, 갯수
  a = ['712838792595112006','914528773121146940']
  b = str(ctx.author.id)

  if b not in a:
    await ctx.reply('개발자만 사용 가능합니다')
    return None

  

@bot.command(aliases=['ㅅㅈ'])
async def 상점(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  dir = db.reference(f'{ctx.author.id}/대륙')
  dst = dir.get()
  print(dst)
  if dst == 1:
    await shop(ctx, bot)

  elif dst == 2:
    await shop2(ctx, bot)

@tasks.loop(seconds=3)    # n초마다 다음 메시지 출력
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))
#################

@bot.command(aliases=['ㅅㅅ', 'ㄷㄹㅇㄷ'])
async def 승선(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  dir = db.reference(f'{ctx.author.id}/대륙')
  dgs = dir.get()
  if dgs == 2:
    dir = db.reference(f'{ctx.author.id}/곡산대륙/현재시간')
    nowtime = dir.get()
    if nowtime == '밤':
      await ctx.reply('밤에는 대륙의 이동이 불가능합니다!')
      return None
    if nowtime == '새벽':
      await ctx.reply('새벽에는 대륙의 이동이 불가능합니다!')
      return None
  await embarkation(ctx, bot)




@bot.command(aliases=['시간', 'ㅅㄱ', '체크','ㅊㅋ'])
async def lvl(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None
  dir = db.reference(f'{ctx.author.id}/대륙')
  asdf = dir.get()
  if asdf == 1:
    return None
  await card(ctx)

@bot.command(aliases=['ㅊㅊ'])
async def 취침(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  dir = db.reference(f'{ctx.author.id}/대륙')
  asdf = dir.get()
  if asdf == 1:
    return None
  await sleep(ctx)

gift = [
  '싱그러운_물', '코X콜라', '저울', '전파시계', '드워프의_망치', '곡괭이', '금화', '에너지드링크', '프로틴', '가공된_목걸이'
]

@bot.command(aliases=['ㅃㄱ','가챠','ㄴㄱㄴㄱㅁㅅ'])
async def 너굴너굴머신(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None
  dir = db.reference(f'{ctx.author.id}/대륙')
  asdf = dir.get()
  if asdf == 1:
    return None

    
  await giftcord(ctx, gift)
  

@bot.command()
async def 사교(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None
  dir = db.reference(f"{ctx.author.id}/ing")
  ings = dir.get()
  if ings != 0:
    await ctx.reply(f'사교가 불가합니다.(사유 : {ings}중)')
    return None
  await ctx.reply('로딩중...')
  await sagu(ctx, bot)

@bot.command()
async def 사용(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None

  print('s')
  dir = db.reference(f'{ctx.author.id}/곡산대륙/강화권')
  ser = dir.get()
  await ctx.reply(f'사용할 아이템을 선택해주세요!```\n1. 100LV 강화권 {ser}개\n```')
  timeout = 10
  def check(m):
    return m.author == ctx.author

  try:
    msg = await bot.wait_for('message',check=check, timeout=timeout)
  except asyncio.TimeoutError:
    await ctx.reply('10초 안에 선택해주세요!')
    return None
  else:
    s = int(msg.content)
    if s == 1:
      if ser <= 0:
        await ctx.reply('강화권을 보유하고 있지 않습니다')
        return None
      dir = db.reference(f'{ctx.author.id}')
      dir.update({'곡괭이 레벨' : 100})
      dir.update({'채굴력' : 505})
      dir.update({'강화최대돈' : 2980})
      ser = ser - 1
      dir = db.reference(f'{ctx.author.id}/곡산대륙')
      dir.update({'강화권' : ser})      
      await ctx.reply('[100LV 강화권]을 사용했습니다!')
      return None
  
    await ctx.reply('Type Error : 현재 `1`만 사용이 가능합니다')

   

@bot.command()
async def 스킬도감(ctx):
  embed = discord.Embed(
            title = f"스킬목록", description = f"", color = 0x2f3136
          )
  
  embed.add_field(name=f"001 : 응급처치", value = '스테미너가 30 이하일시 회복한다.(최초소지)', inline = False)
  embed.add_field(name=f"002 : 단전호흡", value = '스테미너 소모속도가 20% 절감한다(5LV)', inline = False)
  embed.add_field(name=f"003 : 축지법", value = '이동시간이 50% 단축된다(10LV)', inline = False)
  embed.add_field(name=f"004 : 아드레날린", value = '채굴력이 20% 증가한다(상점)', inline = False)
  embed.add_field(name=f"005 : 회복술사", value = '이동시 10%의 확률로 스테미너가 회복한다(상점)', inline = False)
  embed.add_field(name=f"006 : 베테랑", value = '이동시 10%의 확률로 청금석 이상\n다이아 이하의 광물을 한개 얻는다(상점)', inline = False)
  embed.add_field(name=f"007 : 부스터엔진", value = '대륙이동시간이 50% 단축된다(상점)', inline = False)
  embed.add_field(name=f"008 : 미성", value = '사교시 얻는 호감도가 2배가 된다(상점)', inline = False)
  embed.add_field(name=f"009 : 네크로멘서", value = '채굴시 가끔 스테미너가 줄지 않는다.(상점)', inline = False)
  embed.add_field(name=f"010 : 대장장이의_손길", value = '강화 파괴시 50%확률로 무효화된다\n(불카와의 친밀도 : MAX)', inline = False)
  await ctx.reply(embed=embed)
  

@bot.command(aliases=['ㅈㅊ'])
async def 장착(ctx):
  val = -1
  dir = db.reference('user')
  dir = str(dir.get())
  val = dir.find(f"{ctx.author.id}")
  if val == -1:
    await ctx.send('`?가입`을 먼저 진행해주세요!')
    return None
  dir = db.reference(f'{ctx.author.id}/착용스킬/스킬1')
  ski = dir.get()
  dir = db.reference(f'{ctx.author.id}/착용스킬/스킬2')
  skii = dir.get()
  dir = db.reference(f'{ctx.author.id}/착용스킬/스킬3')
  skiii = dir.get()
  msgs = await ctx.reply(f'스킬을 장착할 슬롯을 선택해주세요!(예 `1`, `2`\n```\n1. <{ski}>   2. <{skii}>   3. <{skiii}>```')
  timeout = 10

  try:
    msg = await bot.wait_for('message',check=lambda m: m.content in ['1','2','3'], timeout=timeout)
  except asyncio.TimeoutError:
    await msgs.delete()
    await ctx.reply('10초 안에 선택해주세요!')
    return None
  else:
    s = int(msg.content)
    mache = s
    await msgs.delete()
    dir = db.reference(f'{ctx.author.id}/스킬보유')
    skilllist = dir.get()   
    msgs = await ctx.reply(f'장착할 스킬을 선택해주세요!(예 `1`, `2`\n```md\n{skilllist}\n```')
    lens = int(len(skilllist))
    try:
      msg = await bot.wait_for('message',check=lambda m: int(m.content) <= lens, timeout=timeout)
    except asyncio.TimeoutError:
      await msgs.delete()
      await ctx.reply('10초 안에 선택해주세요!')
      return None
    else:
      s = int(msg.content)
      s = s - 1
      selectskil = skilllist[s]
      if selectskil == ski or selectskil == skii or selectskil == skiii:
        await ctx.reply('이미 장착이 되어 있습니다')
        return None
      await ctx.reply(f'```md\n SKILL : [{selectskil}] 장착성공\n```')
      if mache == 1:
        dir = db.reference(f'{ctx.author.id}/착용스킬')
        dir.update({'스킬1' : selectskil})
      if mache == 2:
        dir = db.reference(f'{ctx.author.id}/착용스킬')
        dir.update({'스킬2' : selectskil})
      if mache == 3:
        dir = db.reference(f'{ctx.author.id}/착용스킬')
        dir.update({'스킬3' : selectskil})
      

keep_alive()
bot.run('TOKEN')
