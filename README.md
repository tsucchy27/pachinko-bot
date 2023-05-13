# pachinko-bot

## 概要

Pythonを使ってパチンコBOTを作る(Discord Bot)

## git管理に入れないファイル

### dauth.py
DiscordBotのトークンを保存するためのファイル。

```python:dauth.py
# discordBot
TEST_TOKEN = 'token'

# ffmpeg
FFMPEG_LINUX = "/usr/bin/ffmpeg"
FFMPEG_WINDOWS = "C:/ffmpeg-4.4-essentials_build/bin/ffmpeg.exe"
```

dauthをインポートして使う。

```python:main.py
import dauth

client = discord.Client()

client.run(dauth.TEST_TOKEN)
```