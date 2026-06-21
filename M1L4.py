import discord
from discord.ext import commands
import random
import string
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='/',
    intents=intents,
    help_command=None
)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def bye(ctx):
    await ctx.send("🙂")

@bot.command()
async def gen_pass(ctx, length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    await ctx.send(f"Sua senha é: `{password}`")

@bot.command()
async def ball(ctx, *, pergunta):
    respostas = [
        "Sim!",
        "Não!",
        "Talvez.",
        "Com certeza!",
        "Pergunte novamente mais tarde."
    ]
    await ctx.send(
        f"🎱 Pergunta: {pergunta}\nResposta: {random.choice(respostas)}"
    )

@bot.command()
async def coin(ctx):
    resultado = random.choice(["Cara", "Coroa"])
    await ctx.send(f"🪙 Resultado: {resultado}")

@bot.command()
async def dado(ctx):
    numero = random.randint(1, 6)
    await ctx.send(f"🎲 Você tirou {numero}!")

@bot.command()
async def help(ctx):
    await ctx.send("""
📋 Comandos disponíveis:

/hello - Cumprimenta o usuário
/bye - Envia um emoji
/gen_pass [tamanho] - Gera uma senha
/ball [pergunta] - Bola mágica responde
/dado - Rola um dado de 6 lados
/help - Mostra esta lista de comandos
""")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if not message.content.startswith('/'):
        await message.channel.send(message.content)

    await bot.process_commands(message)

bot.run("TOKEN")
