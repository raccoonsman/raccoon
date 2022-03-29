import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string

async def invent(ctx, bot):
    dir = db.reference(f"{ctx.author.id}/광물/석탄")
    coal = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/철")
    steel = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/금")
    gold = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/청금석")
    ll = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/다이아")
    dia = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/에메랄드")
    em = dir.get()

    dir = db.reference(f"{ctx.author.id}/광물/철광석")
    coalr = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/석영")
    steelr = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/방해석")
    goldr = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/휘석")
    llr = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/루비")
    diar = dir.get()
    dir = db.reference(f"{ctx.author.id}/광물/오리할콘")
    emr = dir.get()
    dir = db.reference(f"{ctx.author.id}/돈")
    money = dir.get()
    dir = db.reference(f"{ctx.author.id}/탑승권")
    T = dir.get()

    if coal < 0:
      coal = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'석탄' : coal})
    if steel < 0:
      steel = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'철' : steel})
    if gold < 0:
      gold = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'금' : gold})

    if ll < 0:
      ll = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'청금석' : ll})

    if dia < 0:
      dia = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'다이아' : dia})

    if em < 0:
      em = 0
      dir = db.reference(f"{ctx.author.id}/광물")
      dir.update({'에메랄드' : em})
      
    c = bot.get_emoji(941149938115543081)
    s = bot.get_emoji(941150022467223602)
    g = bot.get_emoji(941151007386238976)
    l = bot.get_emoji(941151091532369960)
    d = bot.get_emoji(941151238588866580)
    e = bot.get_emoji(941151289633562624)
    #고급광물
    r = bot.get_emoji(952062123285037056)#루비
    b = bot.get_emoji(951665052035973160)#방해석
    suc = bot.get_emoji(951665011154096128)
    ori = bot.get_emoji(952076020998111262)
    chur = bot.get_emoji(951665105425301504)
    hus = bot.get_emoji(951664963653607434)
    cion = bot.get_emoji(941234234809528380)
    HKT = bot.get_emoji(945209841230696488)
    lvupcou = bot.get_emoji(952075776210137108)
    embed = discord.Embed(title= ctx.author.name + "의 가방", description="", color=0xE4E4E4) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
    embed.add_field(name="‎‎", value=f"**{cion} 코인\n{money}원**‎‎‎", inline=False)
    embed.add_field(name="‎‎", value="**일반광물**‎‎‎", inline=False)
  #루비, 방해석, 석영, 오리할콘, 철광석, 휘석
    embed.add_field(name=f"{c}석탄", value=f"{coal}개‎‎", inline=True)
    embed.add_field(name=f"{s}철", value=f"‎‎{steel}개", inline=True)
    embed.add_field(name=f"{g}금", value=f"‎‎{gold}개", inline=True)
    embed.add_field(name=f"{l}청금석", value=f"{ll}개‎", inline=True)
    embed.add_field(name=f"{d}다이아", value=f"{dia}개‎‎", inline=True)
    embed.add_field(name=f"{e}에메랄드", value=f"{em}개‎‎", inline=True)
    embed.add_field(name="‎‎", value="**고급광물**‎‎‎", inline=False)
    embed.add_field(name=f"{r}루비", value=f"{coalr}개‎‎", inline=True)
    embed.add_field(name=f"{b}방해석", value=f"‎‎{steelr}개", inline=True)
    embed.add_field(name=f"{suc}석영", value=f"‎‎{goldr}개", inline=True)
    embed.add_field(name=f"{ori}오리할콘", value=f"{llr}개‎", inline=True)
    embed.add_field(name=f"{chur}철광석", value=f"{diar}개‎‎", inline=True)
    embed.add_field(name=f"{hus}휘석", value=f"{emr}개‎‎", inline=True)
    embed.add_field(name="‎‎", value="**아이템**‎‎‎", inline=False)
    embed.add_field(name=f"{HKT}HK TICKET", value=f"{T}개‎‎", inline=True)
    embed.add_field(name=f"{lvupcou}100LV 강화권", value=f"{T}개‎‎", inline=True)
    embed.set_footer(text=f"{ctx.author.name}") # 하단에 들어가는 조그마한 설명을 잡아줍니다.
    await ctx.reply(embed=embed)