import discord
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

nama_pertama = ["Alpha", "Beta"]
nama_kedua = ["Charlie", "Delta"]

info_pertama = {
    "Alpha" : "Satu",
    "Beta" : "Dua"
}

info_kedua = {
    "Charlie" : "Tiga",
    "Delta" : "empat"
}


@bot.tree.command(name="list_nama", description="List nama yang tersedia")
async def list_nama(interaction : discord.Interaction):
    list_pertama = "\n".join([f"{i}. {name}" for i, name in enumerate(info_pertama, start=1)])
    list_kedua = "\n".join([f"{i}. {name}" for i, name in enumerate(info_kedua, start=1)])

    semua_list = f"List Pertama:\n{list_pertama}\n\n:List kedua:\n{list_kedua}"
    await interaction.response.send_message(f"Ini adalah list yang tersedia!\n{semua_list}")


async def nameautocomplete(interaction : discord.Interaction, current : str):
    all_name = nama_pertama + nama_kedua
    return [
        app_commands.Choice(name= nama, value=nama)
        for nama in all_name if current.lower() in nama.lower()
    ]


@bot.tree.command(name="info_name", description="info about name")
@app_commands.autocomplete(name = nameautocomplete)
async def info_name(interaction : discord.Interaction, name : str):
    if name in nama_pertama:
        await interaction.response.send_message(nama_pertama[name])
    elif name in nama_kedua:
        await interaction.response.send_message(nama_kedua[name])
