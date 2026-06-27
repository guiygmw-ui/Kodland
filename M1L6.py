import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix='/',
    intents=intents,
    help_command=None
)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Olá! Eu sou o EcoBot. Estou aqui para ajudar você a cuidar do meio ambiente!")

@bot.command()
async def eco(ctx):
    dicas = [
        "Use uma garrafa reutilizável em vez de comprar garrafas plásticas.",
        "Separe o lixo reciclável do lixo comum.",
        "Feche a torneira enquanto escova os dentes.",
        "Apague as luzes ao sair de um cômodo.",
        "Leve uma sacola reutilizável ao mercado.",
        "Sempre que possível, caminhe ou use bicicleta.",
        "Evite o desperdício de alimentos."
    ]
    await ctx.send(random.choice(dicas))

@bot.command()
async def curiosidade(ctx):
    curiosidades = [
        "Uma árvore pode absorver cerca de 20 kg de CO₂ por ano.",
        "O vidro pode ser reciclado várias vezes sem perder a qualidade.",
        "Reciclar uma lata de alumínio economiza muita energia.",
        "Menos plástico nos rios ajuda a proteger os animais marinhos.",
        "Pequenas atitudes diárias fazem diferença para o planeta."
    ]
    await ctx.send(random.choice(curiosidades))

@bot.command()
async def desafio(ctx):
    desafios = [
        "Desafio: Passe um dia sem usar plástico descartável.",
        "Desafio: Tome um banho de até 5 minutos.",
        "Desafio: Separe todo o lixo reciclável da sua casa hoje.",
        "Desafio: Desligue as luzes quando não estiver usando.",
        "Desafio: Plante uma flor ou cuide de uma planta."
    ]
    await ctx.send(random.choice(desafios))

@bot.command()
async def help(ctx):
    await ctx.send("""
**Comandos do EcoBot**

/hello - Apresenta o bot.
/eco - Receba uma dica ecológica.
/curiosidade - Veja uma curiosidade sobre o meio ambiente.
/desafio - Receba um desafio sustentável.
/help - Mostra esta lista de comandos.
""")

bot.run("TOKEN")
