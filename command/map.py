import discord
from firebase_admin import credentials
from firebase_admin import db
import uuid
import string

async def map(ctx):
    embed = discord.Embed(title="지도", description="", color=0xE4E4E4)
    embed.set_image(url="https://media.discordapp.net/attachments/934771156542713906/935024862718726194/32_20220124131443.png?width=625&height=469")
    embed.add_field(name="제1대륙(1,2,3,4)‎", value="1 : 태초마을\n2 : 초보자광산\n3 : 태초광산\n4. 태초항구", inline=False)
    embed.add_field(name="제2대륙(5,6,7,8)‎", value="5 : 곡산항구\n6 : 곡산광산\n7 : 태극광산\n8. 곡산마을", inline=False)
    embed.set_footer(text="<주의>대륙간의 이동은 항구에서만 가능합니다.\n이동은 `?ㅇㄷ (지역명)`")
    await ctx.reply(embed = embed)