import discord
from discord.ext import commands

TOKEN = 'token aq'
TARGET_USER_ID = 890768957374615573 # ID do usuário que você quer limpar 

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logado como {bot.user.name}')

    for guild in bot.guilds:
        print(f'Apagando mensagens em: {guild.name}')
        for channel in guild.text_channels:
            try:
                print(f'→ Canal: {channel.name}')
                async for message in channel.history(limit=None):
                    if message.author.id == TARGET_USER_ID:
                        try:
                            await message.delete()
                        except:
                            pass
            except Exception as e:
                print(f'Erro no canal {channel.name}: {e}')

    print('✅ Limpeza finalizada.')
    await bot.close()

bot.run(TOKEN)
