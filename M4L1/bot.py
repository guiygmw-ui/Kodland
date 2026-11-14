import asyncio
import logging
import os
import tempfile

import discord
from discord.ext import commands
from PIL import UnidentifiedImageError

from model import get_class

CONFIDENCE_THRESHOLD = 0.6

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if not ctx.message.attachments:
        await ctx.send("Você esqueceu de enviar a imagem :(")
        return

    for attachment in ctx.message.attachments:
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                image_path = os.path.join(temp_dir, "upload")
                await attachment.save(image_path)
                label, confidence = await asyncio.to_thread(
                    get_class,
                    model_path="keras_model.h5",
                    labels_path="labels.txt",
                    image_path=image_path,
                )
        except (UnidentifiedImageError, OSError, ValueError) as error:
            logger.warning("Não foi possível processar o anexo %s: %s", attachment.filename, error)
            await ctx.send(
                f"Não consegui processar **{attachment.filename}**. "
                "Envie uma imagem válida e tente novamente."
            )
            continue

        if confidence < CONFIDENCE_THRESHOLD:
            await ctx.send("Desculpe, não tenho certeza do que está sendo mostrado na imagem.")
        else:
            await ctx.send(
                f"A imagem parece mostrar **{label}** "
                f"(confiança: {confidence:.0%})."
            )


@check.error
async def check_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        original_error = error.original
        logger.error(
            "Falha inesperada durante a inferência.",
            exc_info=(
                type(original_error),
                original_error,
                original_error.__traceback__,
            ),
        )
        await ctx.send("Ocorreu um erro ao analisar a imagem. Tente novamente mais tarde.")
        return

    raise error


token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("Defina a variável de ambiente DISCORD_TOKEN antes de iniciar o bot.")

bot.run(token)