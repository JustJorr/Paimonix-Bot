import discord
from discord.ext import commands
from discord import app_commands
from fives_characters import five_star_characters, five_star_characters_info, five_star_characters_build
from fours_characters import four_star_characters,four_star_characters_info,four_star_characters_build
from fives_weapons import five_star_sword_weapons, five_star_polearm_weapons, five_star_catalyst_weapons, five_star_claymore_weapons, five_star_bow_weapons, five_star_weapons_info
from regions import overworld_region, underworld_region, overworld_region_info, underworld_region_info


BOT_TOKEN = 'dummy'
CHANNEL_IDS = [
    123
]


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Hello! Paimonix Is ready!")
    await bot.change_presence(activity=discord.Game(name="Genshin Impact | /help"))
    for channel_id in CHANNEL_IDS:
        channel = bot.get_channel(channel_id)
        await channel.send("Hello! Paimonix ready!")
    
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}!")


@bot.tree.command(name="info", description="Get information about the bot")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Paimonix is specifically developed to help genshin players for information about the game. \nincluding the story and the character!"
    )


@bot.tree.command(name="credits", description="Credits For The Creation of the Bot")
async def bot_credits(interaction: discord.Interaction):
    await interaction.response.send_message(
        "The Creator of this bot is yorudan\n"
        "Build Source is from Lady Senki and Game8"
    )


@bot.tree.command(name="character_list", description="List available characters")
async def characterlist(interaction: discord.Interaction):
    five_star_list = "\n".join([f"{i}. {characters}" for i, characters in enumerate(five_star_characters, start=1)])
    four_star_list = "\n".join([f"{i}. {characters}" for i, characters in enumerate(four_star_characters, start=1)])

    character_list = f"\n5 Star Characters :\n{five_star_list} \n\n4 Star Characters :\n{four_star_list}"
    await interaction.response.send_message(f"Here are the available characters list!\n {character_list}")


@bot.tree.command(name="weapon_list", description="List available weapons")
async def weapon_list(interaction: discord.Interaction):
    five_star_sword = "\n".join([f"{i}. {weapons}" for i, weapons in enumerate(five_star_sword_weapons, start=1)])
    five_star_bow = "\n".join([f"{i}. {weapons}" for i, weapons in enumerate(five_star_bow_weapons, start=1)])
    five_star_claymore = "\n".join([f"{i}. {weapons}" for i, weapons in enumerate(five_star_claymore_weapons, start=1)])
    five_star_polearm = "\n".join([f"{i}. {weapons}" for i, weapons in enumerate(five_star_polearm_weapons, start=1)])
    five_star_catalyst = "\n".join([f"{i}. {weapons}" for i, weapons in enumerate(five_star_catalyst_weapons, start=1)])

    weapons_list = f"5 Star Weapons\n\n Sword:\n{five_star_sword}\n\n Bow:\n{five_star_bow}\n\n Claymore:\n{five_star_claymore}\n\n Catalyst:\n{five_star_catalyst}\n\n Polearm:\n{five_star_polearm}"
    await interaction.response.send_message(f"Here are the available weapons list!\n\n {weapons_list}")


async def weapon_info_autocomplete(interaction : discord.Interaction, current : str):
    all_weapon = five_star_weapons_info
    return [
        app_commands.Choice(name=weapon, value=weapon)
        for weapon in all_weapon if current.lower() in weapon.lower()
    ][:25]


@bot.tree.command(name="weapon_info", description="description of the weapon")
@app_commands.autocomplete(weapon_name = weapon_info_autocomplete)
async def weapon_info(interaction : discord.Interaction ,weapon_name : str):
    if weapon_name in five_star_sword_weapons :
        await interaction.response.send_message(five_star_weapons_info[weapon_name])
    elif weapon_name in five_star_bow_weapons:
        await interaction.response.send_message(five_star_weapons_info[weapon_name])
    elif weapon_name in five_star_claymore_weapons:
        await interaction.response.send_message(five_star_weapons_info[weapon_name])
    elif weapon_name in five_star_polearm_weapons:
        await interaction.response.send_message(five_star_weapons_info[weapon_name])
    elif weapon_name in five_star_catalyst_weapons:
        await interaction.response.send_message(five_star_weapons_info[weapon_name])
    else:
        await interaction.response.send_message("Weapon not found. Please make sure the weapon is in the list")


async def character_autocomplete(interaction : discord.Interaction, current: str):
    all_characters = five_star_characters + four_star_characters
    return [
        app_commands.Choice(name=char, value= char)
        for char in all_characters if current.lower() in char.lower()
    ][:25]


@bot.tree.command(name="character", description="Get character info")
@app_commands.autocomplete(character_name = character_autocomplete)
async def character(interaction: discord.Interaction, character_name: str):
    if character_name in five_star_characters:
        await interaction.response.send_message(five_star_characters_info[character_name] + "\nWould you like to also view this character's build?")
    elif character_name in four_star_characters:
        await interaction.response.send_message(four_star_characters_info[character_name] + "\nWould you like to also view this character's build?")
    else:
        await interaction.response.send_message("Character not Found. Please make sure the Character is in the list")


async def character_build_autocomplete(interation : discord.Interaction, current : str):
    all_character_build = five_star_characters_build | four_star_characters_info
    return [
        app_commands.Choice(name=build, value=build)
        for build in all_character_build if current.lower() in build.lower()
    ][:25]


@bot.tree.command(name="character_build", description="Get character build")
@app_commands.autocomplete(character_name = character_build_autocomplete)
async def character_build(interaction: discord.Interaction, character_name: str):
    if character_name in five_star_characters :
        await interaction.response.send_message(five_star_characters_build[character_name])
    elif character_name in four_star_characters:
        await interaction.response.send_message(four_star_characters_build[character_name])
    else:
        await interaction.response.send_message("Character not Found. Please make sure the Character is in the list")


@bot.tree.command(name="regions_list", description="Avalaible regions")
async def regions_list(interaction : discord.Interaction):
    over_region = "\n".join([f"{i}. {reg}" for i,reg in enumerate(overworld_region, start=1)])
    under_region = "\n".join([f"{i}. {reg}" for i,reg in enumerate(underworld_region, start=1)])

    all_region = f"Overworld Region:\n{over_region}\n\nUnderworld Region:\n{under_region}"
    await interaction.response.send_message(f"Here are avalaible Regions! :\n{all_region}")


async def regions_autocomplete(interaction : discord.Interaction, current : str):
    all_regions = overworld_region + underworld_region
    return [
        app_commands.Choice(name=reg, value=reg)
        for reg in all_regions if current.lower() in reg.lower()
    ][:25]


@bot.tree.command(name="regions_info", description="info about regions")
@app_commands.autocomplete(region_name = regions_autocomplete)
async def regions_info(interaction : discord.Interaction, region_name : str):
    if region_name in overworld_region:
        await interaction.response.send_message(overworld_region_info[region_name])
    elif region_name in underworld_region:
        await interaction.response.send_message(underworld_region_info[region_name])



@bot.tree.command(name="help", description="Get a list of commands")
async def bot_help(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Here are the list of commands!\n"
        "/hello\n"
        "/character_list\n"
        "/weapons_list\n"
        "/weapon_info\n"
        "/credits\n"
        "/info\n"
        "/character <\"character name\" (e.g \"Hu Tao\")>\n"
        "/character_build <\"character name\">"
    )


bot.run(BOT_TOKEN)

