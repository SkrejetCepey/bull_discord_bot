import discord
import asyncio
import youtube_dl
import os

from itertools import cycle
from discord.voice_client import VoiceClient

from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = '%token%'

targs = {}

bot = commands.Bot(command_prefix='!')
global global_bull

bot.remove_command('help')

@bot.event
async def on_ready():
    print('[BullBot is online now!]')


async def self_bull(ctx):
    global global_bull
    await bot.wait_until_ready()
    while not bot.is_closed() and global_bull == 0:
        await ctx.send('Пошел нахуй, ' + str(ctx.author.mention))
        await asyncio.sleep(3)


async def trg_bull(ctx, target):
    await bot.wait_until_ready()
    global global_bull
    counter: int = 0
    while not bot.is_closed() and global_bull == 0:
        print(ctx.guild.members)
        for x in ctx.guild.members:
            if x.name == target:
                print(x.name)
                if str(x.id) == '249113009853693952':
                    await ctx.send('В буллинге отказано, причина: Создатель бота')
                    global_bull = 1
                    return
                counter = counter + 1
                await ctx.send('Пошел ####, ' + "<@!" + str(x.id) + ">")
        if counter == 0:
            await ctx.send('Здесь нет такого, не обманывай!')
            global_bull = 1;
        await asyncio.sleep(3)


@bot.command(pass_context=True)
async def target_bull(ctx, target):
    global global_bull
    global_bull = 0
    await trg_bull(ctx, target)
    pass

@bot.command(pass_context=True)
async def unsettarg(ctx, trg):
    for x in ctx.guild.members:
        if x.name == trg:
            # if str(x.id) == '249113009853693952':
            #    await ctx.send('В буллинге отказано, причина: Создатель бота')
            #    global_bull = 1
            #    return
            targs[int(x.id)] = None
    await ctx.send('Цель успешно ушла от надзора')
    pass


@bot.command(pass_context=True)
async def settarg(ctx, trg):
    for x in ctx.guild.members:
        if x.name == trg:
            # if str(x.id) == '249113009853693952':
            #    await ctx.send('В буллинге отказано, причина: Создатель бота')
            #    global_bull = 1
            #    return
            targs[int(x.id)] = x.name
    await ctx.send('Цель успешно попала под надзор')
    pass


@bot.command(pass_context=True)
async def bull(ctx):
    global global_bull
    global_bull = 0
    await self_bull(ctx)
    pass


@bot.command(pass_context=True)
async def unbull(ctx):
    global global_bull
    global_bull = 1;
    await ctx.send('Да ладно, я просто прикалываюсь!')
    pass


def to_upper(argument):
    return argument.upper()


@bot.command()
async def up(ctx, *, content: to_upper):
    await ctx.send(content)


@bot.event
async def on_message(ctx):
    # print(ctx.author)
    for x in ctx.guild.members:
        try:
            if str(ctx.author)[:-5] == targs[int(x.id)]:
                await ctx.channel.send('Да пошел ты ####, черт')
        except:
            pass

    if ctx.content == 'Булл':
        await ctx.channel.send("Че, " + str(ctx.author) + " ?")
    await bot.process_commands(ctx)


@bot.command(pass_context=True)
async def help(ctx):
    tmp = 'Список команд? Изи!\n' \
          '!help - список команд, на которые я откликаюсь\n' \
          '!test - тестовая команда. Нужна, чтобы проверить слышу ли я вас.\n' \
          'Скоро я обучусь новым командам, я надеюсь...'
    embed = discord.Embed(
        color=discord.Color.red()
    )
    embed.set_author(name="Helper")
    embed.add_field(name="!help", value="Вы находитесь здесь!", inline=False)
    embed.add_field(name="!target_bull <target>", value="Спам определенному человеку в конференции.", inline=False)
    embed.add_field(name="!unsettarg <target>", value="Отключение реакции бота на сообщения цели.",
                    inline=False)
    embed.add_field(name="!settarg <target>", value="Включение реакции бота на сообщения цели.", inline=False)
    embed.add_field(name="!bull", value="Привлеките к себе внимание!", inline=False)
    embed.add_field(name="!un_bull", value="Отключение любого буллинга.", inline=False)
    await ctx.send(ctx.author, embed=embed)
    # await ctx.send_message(ctx.author, embed=embed)
    await ctx.send("Куда пишешь? Тебе еще не надоело?")
    # await ctx.send(tmp)


bot.run(TOKEN)
