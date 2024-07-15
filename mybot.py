import discord
from discord.ext import commands
from kodland_utils import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send(pass_gen(10))

@bot.command()
async def flip(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def rps(ctx):
    choices = ['✊', '✋', '✌️']  # batu, kertas, gunting
    bot_choice = random.choice(choices)

    message = await ctx.send("Let's play Rock-Paper-Scissors! React with your choice:")
    for choice in choices:
        await message.add_reaction(choice)

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in choices

    reaction, user = await bot.wait_for('reaction_add', check=check)
    user_choice = str(reaction.emoji)
    result = determine_winner(user_choice, bot_choice)
    await ctx.send(f'You chose {user_choice}, I chose {bot_choice}. {result}')

def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "It's a tie!"
    elif (user_choice == '✊' and bot_choice == '✌️') or \
         (user_choice == '✋' and bot_choice == '✊') or \
         (user_choice == '✌️' and bot_choice == '✋'):
        return "You win! 🎉"
    else:
        return "I win! 😎"

bot.run()
