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

# ラッシュチャンス時
async def rush(message):
    global num, score, bet
    rush_num = 0    # RUSH回数
    print("rush event")

    # 突入判定
    time.sleep(0.2)
    await message.channel.send("RUSHチャンス!!60以下でRUSH突入!!")
    r = random.randint(1, 100)

    # 値出力
    time.sleep(1)
    await message.channel.send(r)
    time.sleep(0.2)
    if r > 60:
        await message.channel.send("RUSH失敗...")
        return

    # RUSH突入
    await message.channel.send("RUST突入!!80以下でRUSH継続!!")
    print(f"{r} - RUSH突入")
    f = True
    while(f):
        # 値出力
        r = random.randint(1, 100)
        time.sleep(1)
        await message.channel.send(r)
        rush_num += 1
        
        # 継続判定
        time.sleep(0.2)
        if r <= 80:
            await message.channel.send(f"RUSH継続!! [{rush_num}]")
        else:
            f = False
            await message.channel.send(f"RUSH終了 [{rush_num}]")
            print(f"{r} - RUSH終了")

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
        b = random.randint(1, 5)
        print(f"player:{p} bot:{b}")
        await message.channel.send(f"{b} ({num})")

        # 判定 当たり->Rush突入、回数初期化
        if p == b:
            print(f"{num}回目で当たり")
            num = 0
            await message.channel.send("当たり")
            await asyncio.create_task(rush(message))

client.run(dauth.PACHINKO_TOKEN)