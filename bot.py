import discord
from discord import user
from discord import channel
from discord.ext import commands,tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands.core import cooldown
from discord.flags import Intents
from discord.utils import parse_time
import datetime
import json
from discord.ext.commands.cooldowns import BucketType
import asyncio
import random
intents = discord.Intents.all()
intents.members = True
from discord.ext import commands
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')


async def colors():
    color = random.choice([0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0xa84300,0xe74c3c,0x992d22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5])
    return color

async def brightest_color():
    color = random.choice([
    0xFF0000,  # Red
    0xFFC000,  # Orange
    0xFFFF00,  # Yellow
    0x00FF00,  # Green
    0x00FFFF,  # Cyan
    0x0000FF,  # Blue
    0xFF00FF   # Magenta
    ])
    return color

def get_id(name):
    with open('config.json', 'r') as f:
        data = json.load(f)
    if name == "guild":
        return data['guild']
    elif name == "welcome":
        return data["welcome_channel"]
    elif name == "rules":
        return data["rules_channel"]


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')
    print("The bot is ready!")

async def update_ids(id):
    with open('join.txt', 'a') as f:
        f.write(f',{id}')

async def members_ids():
    with open('join.txt','r') as f:
        data = f.read()
        if data == '':
            with open('join.txt', 'a') as f:
                f.write('0')
            return [0,0]
        else:
            ids = [int(num) for num in data.split(',')]
            print(ids)
            return ids


async def welcoming(member):
    guild = bot.get_guild(get_id("guild")) # Server ID
    channel = guild.get_channel(get_id("welcome")) #Welcome channle ID.
    c2 = guild.get_channel(get_id("rules")) # Rules channel ID or any channel ID that you want user to visit. || 
    embed = discord.Embed(title="WELCOME ", colour=await colors(), url="https://discordapp.com", description="Welcome to this server.")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url = "https://media.discordapp.net/attachments/763779046999064609/853927975539965982/pexels-photo-1190298.jpeg")
    avatar_url = member.avatar if member.avatar else "https://i.imgur.com/MbDsCla.jpeg" #if the member doesn't have image this will add its own image
    embed.set_thumbnail(url = f"{avatar_url}")
    embed.set_author(name=f"{member.name}", url="https://discordapp.com", icon_url = f"{avatar_url}\n")
    embed.set_footer(text=f"{member.name}", icon_url = f"{avatar_url}\n")
    embed.add_field(name="Check it out!", value=f"{c2.mention} {member.mention}\n") 
    embed.add_field(name="Created at: ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%m %p UTC"))
    embed.add_field(name="Joined at: ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    await channel.send(embed=embed)
    asyncio.create_task(led(member)) ## this will call function creating a thread, which will give the led effects.
            
@bot.event
async def on_member_join(member):
    ids = await members_ids()
    if member.id not in ids: 
        asyncio.create_task(welcoming(member))
    else:
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)
        try:
            await member.send(f'Thank you for rejoining!!!')
        except:
            pass

async def led(member):
    guild = bot.get_guild(get_id("guild"))
    selectedrole = discord.utils.get(member.guild.roles, name="Welcome")
    print(f"{member} has joined")
    temp_role = selectedrole
    try:
    ##provides the role named welcome and starts changing the color
        await member.add_roles(temp_role)
    except: ##If the role named Welcome is missing.
        await guild.create_role(name="Welcome")
        temp_role = discord.utils.get(member.guild.roles, name="Welcome")
        await member.add_roles(temp_role)
    for i in range(20):   
        await selectedrole.edit(colour = await brightest_color())
    await member.remove_roles(temp_role)
    #Removes the color and give the role named Member     
    await update_ids(member.id) # This will save the member id who has already joined. 
    #>>It prevents the user to misue the feautre by joining multiple times
     
    try:
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)
    except:
        await guild.create_role(name="Member") 
        role = discord.utils.get(member.guild.roles, name="Member")
        await member.add_roles(role)

bot.run('Your token goes here')