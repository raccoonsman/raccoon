import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string

async def gamehelp(ctx):
  embed = discord.Embed(title="너구리 도움말", description="", color=0xE4E4E4) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
  embed.add_field(name="`?가입(=ㄱㅇ)`", value="게임을 진행하기 위해 가입을 진행합니다.", inline=False)
  embed.add_field(name="`?이동(=ㅇㄷ)`", value="이동합니다", inline=False)
  embed.add_field(name="`?채굴(=ㅊㄱ)`", value="채굴합니다 이 명령어는 광산에서만 작동합니다", inline=True)
  embed.add_field(name="`?정보(=ㅈㅂ)`", value="자신의 레벨, 경험치, 채굴력, 스킬등을 봅니다", inline=False)
  embed.add_field(name="`?장착[1/2/3] [스킬명]`", value="스킬을 장착합니다.(스킬명은 정보탭에서 확인이 가능합니다)", inline=False)
  embed.add_field(name="`?해제`", value="스킬을 전부 해제합니다", inline=False)
  embed.add_field(name="`?인벤(=ㅇㅂ)`", value="자신의 돈, 채굴한 광물, 티켓을 봅니다", inline=False)
  embed.add_field(name="`?매도(=ㅁㄷ)`", value="마을에서 캔 광물을을 팔아 돈을 얻을 수 있습니다", inline=False)
  embed.add_field(name="`?강화(=ㄱㅎ)`", value="마을에서 강화를 하여 채굴력을 높입니다", inline=False)
  embed.add_field(name="`?상점(=ㅅㅈ)`", value="마을에서 스킬, 티켓등을 구매가 가능합니다", inline=False)
  embed.add_field(name="`?가격(=ㄱㄱ) [광물명]`", value="현재 광물의 가격을 봅니다", inline=False)
  embed.add_field(name="`?가격표(=ㄱㄱㅍ)`", value="광물들의 실시간 가격리스트를 보여줍니다.", inline=False)
  embed.add_field(name="`?내위치(=ㅇㅊ)`", value="현재 위치를 봅니다", inline=False)
  embed.add_field(name="`?지도(=ㅈㄷ)`", value="지도를 봅니다\n‎", inline=False)
  embed.add_field(name="**곡산대륙**", value="‎", inline=False)
  embed.add_field(name="`?시간(=ㅅㄱ)`", value="현재시각을 봅니다", inline=False)
  embed.add_field(name="`?사교`", value="NPC들과 사교를 진행합니다.", inline=False)
  embed.add_field(name="`?취침`", value="잠을 잘 수 있습니다.", inline=False)
  embed.add_field(name="`?사용(=ㅅㅇ)`", value="아이템을 사용합니다", inline=False)
  embed.set_footer(text="RCNS#4379") # 하단에 들어가는 조그마한 설명을 잡아줍니다.
  await ctx.send(embed=embed)


async def lhelp(ctx):
  embed = discord.Embed(title="설명서", description="", color=0xE4E4E4) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
  embed.add_field(name="`?도움말(=help)`", value="도움말입니다.", inline=False)
  embed.add_field(name="`?청소(=clear)`", value="메세지 삭제 가능입니다.", inline=True)
  embed.add_field(name="`?kick(=킥)`", value="멘션한 멤버를 추방합니다.", inline=False)
  embed.add_field(name="`?ban(=밴)`", value="멘션한 멤버를 차단합니다.", inline=True)
  embed.add_field(name="`?ghelp(채굴도움말)`", value="채굴기능 도움말입니다.", inline=False)
  embed.add_field(name="`?튜토리얼`", value="채굴 튜토리얼입니다!", inline=False)
  embed.set_footer(text="MISTOP#1039, RCNS#5227") # 하단에 들어가는 조그마한 설명을 잡아줍니다.
  await ctx.send(embed=embed)