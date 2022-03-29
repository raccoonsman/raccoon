import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string
#1. 싱그러운_물\n2. 코X콜라\n3. 저울\n4. 전파시계\n5. 드워프의_망치\n6. 곡괭이\n7. 금화\n8. 에너지드링크\n9. 프로틴\n10. 가공된_목걸이
async def gifta(ctx, select):
  if select == 1:
    selects = '싱그러운_물'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})

  if select == 2:
    selects = '코X콜라'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})

  if select == 3:
    selects = '저울'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 4:
    selects = '전파시계'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 5:
    selects = '드워프의_망치'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 6:
    selects = '곡괭이'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 7:
    selects = '금화'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 8:
    selects = '에너지드링크'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 8:
    selects = '저울'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 9:
    selects = '프로틴'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
  if select == 10:
    selects = '가공된_목걸이'
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물/{selects}')
    gift = dir.get()
    if gift <= 0:
      await ctx.reply('해당 선물을 보유하고 계시지 않습니다')
      a = 1
      return a

    gift = gift - 1
    dir = db.reference(f'{ctx.author.id}/곡산대륙/선물')
    dir.update({selects : gift})
    
    