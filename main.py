import discord
import random
import re
import time
import asyncio
import dauth

client = discord.Client(intents=discord.Intents.all())
fastHunt = "!"
num = 0     # RUSHまでの回数
score = 0   # スコア
bet = 4     # 1玉何円か

# ラッシュ突入時
async def rush(message):
    global num, score, bet

    print("rush event")
    await message.channel.send("RUSH突入!!40以下でRUSH継続!!")
    f = True
    while(f):
        # ランダムな値を出力
        r = random.randint(1, 100)
        time.sleep(1)
        await message.channel.send(r)
        # 判定
        time.sleep(1)
        if r <= 40:
            await message.channel.send("RUSH継続!!")
        else:
            f = False
            await message.channel.send("RUSH終了")

@client.event
async def on_ready():
    print('bot online.')

@client.event
async def on_message(message):
    global num, score, bet

    if message.author.bot:
        return
    
    if re.compile(f"^{fastHunt}p.+").search(message.content):
        # playerの手を取得
        try:
            p = int(message.content[2:])
        except ValueError:
            print("lost")
            return

        # 回数+1
        num += 1

        # botの手
        b = random.randint(1, 319)
        print(f"player:{p} bot:{b}")
        await message.channel.send(f"{b} ({num})")

        # 判定 当たり->Rush突入、回数初期化
        if p == b:
            print(f"{num}回目で当たり")
            num = 0
            await message.channel.send("当たり")
            await asyncio.create_task(rush(message))

client.run(dauth.PACHINKO_TOKEN)