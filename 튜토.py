import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string

async def 튜토(ctx):
  await ctx.reply('```md\n1. 가입을 진행 합니다\n2. 광산으로 이동을 합니다(?도움말 목록 채널 참조)\n3. 채굴을 진행합니다\n4. 마을로 가서 광물들을 매도합니다\n5. 매도를 해서 얻은 돈으로 밑의 서비스를 이용합니다\n  5-1. 강화(인기!)\n  5-2. 상점\n‎\n6. 오류를 발견하시면 서포트서버에 기재바랍니다(?shelp)\n7. 건의 사항은 건의 채널에 기재바랍니다\n8. 모든 명령어는 ?도움말을 참조바랍니다\n```')