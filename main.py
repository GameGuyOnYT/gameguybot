import json, discord, requests
import os

os.environ['TOKEN'] = 'MTAwOTU3MTY1NzUzNjUxNjA5Ng.GwZvMU.qvTZj1nD12n23xKj3hN5RZ8VaflHMzecoYVA1I'
token = os.environ.get("TOKEN")

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("Connected!")


@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content == '!help':
        await message.author.send(
            '```!status - Check if a ROBLOX exploit is online. eg: !status comet, !status wrd...\n!help - Show this message.```')
    content = json.loads(requests.get("https://api.whatexploitsare.online/status").text)
    embed_status = discord.Embed(colour=discord.Colour.red(), title="Exploit Status")
    if message.content == '!status wrd' or message.content == '!status WeAreDevs_API' or message.content == '!status wearedevs_api' or message.content == '!status wearedevs_api' or message.content == '!status wearedevs' or message.content == '!status WeAreDevs': embed_status.description = f'WeAreDevs API / JJSploit: {content[6]["WeAreDevs API"]["updated"]} (version: {content[6]["WeAreDevs API"]["exploit_version"]})'
    if message.content == '!status temple': embed_status.description = f'Temple: {content[3]["Temple"]["updated"]} (version: {content[3]["Temple"]["exploit_version"]})'
    if message.content == '!status electron': embed_status.description = f'Electron: {content[5]["Electron"]["updated"]} (version: {content[5]["Electron"]["exploit_version"]})'
    if message.content == '!status dx9ware': embed_status.description = f'DX9WARE: {content[4]["DX9WARE"]["updated"]} (version: {content[4]["DX9WARE"]["exploit_version"]})'
    if message.content == '!status celestial': embed_status.description = f'Celestial: {content[10]["Celestial"]["updated"]} (version: {content[10]["Celestial"]["exploit_version"]})'
    if message.content == '!status comet': embed_status.description = f'Comet: {content[11]["Comet"]["updated"]} (version: {content[11]["Comet"]["exploit_version"]})'
    if message.content == '!status synapse' or message.content == '!status synapse_x' or message.content == '!status syn' or message.content == '!status syn_x': embed_status.description = f'Synapse:                  {content[0]["Synapse"]["updated"]} (version: {content[0]["Synapse"]["exploit_version"]})'
    if message.content == '!status scriptware' or message.content == '!status script_ware' or message.content == '!status sw': embed_status.description = f'Script-Ware: {content[1]["Script-Ware"]["updated"]} (version: {content[1]["Script-Ware"]["exploit_version"]})'
    if message.content == '!status roware' or message.content == '!status ro-ware': embed_status.description = f'Ro-Ware: {content[9]["Ro-Ware"]["updated"]} (version: {content[9]["Ro-Ware"]["exploit_version"]})'
    if message.content == '!status krnl' or message.content == '!status kernel': embed_status.description = f'KRNL: {content[2]["KRNL"]["updated"]} (version: {content[2]["KRNL"]["exploit_version"]})'
    if message.content == '!status oxygen' or message.content == '!status oxygen_u' or message.content == '!status oxy_u' or message.content == '!status oxygenu' or message.content == '!status oxyu': embed_status.description = f'Oxygen U: {content[7]["Oxygen"]["updated"]} (version: {content[7]["Oxygen"]["exploit_version"]})'
    if message.content == '!status fluxus' or message.content == '!status fluxware': embed_status.description = f'Fluxus: {content[8]["Fluxus"]["updated"]} (version: {content[8]["Fluxus"]["exploit_version"]})'
    if message.content == '!status aliegexecutor' or message.content == '!status Aliegexecutor' or message.content == '!status AliEgexecutor' or message.content == '!status AliEgExecutor': embed_status.description = 'AliEgExecutor: False (version: 1.0)'
    if message.content == '!status': embed_status.description = (
        f'Synapse: {content[0]["Synapse"]["updated"]} (version: {content[0]["Synapse"]["exploit_version"]})\n \
            Script-Ware: {content[1]["Script-Ware"]["updated"]} (version: {content[1]["Script-Ware"]["exploit_version"]})\n \
            KRNL: {content[2]["KRNL"]["updated"]} (version: {content[2]["KRNL"]["exploit_version"]})\n \
            Temple: {content[3]["Temple"]["updated"]} (version: {content[3]["Temple"]["exploit_version"]})\n \
            DX9WARE: {content[4]["DX9WARE"]["updated"]} (version: {content[4]["DX9WARE"]["exploit_version"]})\n \
            Electron: {content[5]["Electron"]["updated"]} (version: {content[5]["Electron"]["exploit_version"]})\n \
            WeAreDevs API / JJSploit: {content[6]["WeAreDevs API"]["updated"]} (version: {content[6]["WeAreDevs API"]["exploit_version"]})\n \
            Oxygen U: {content[7]["Oxygen"]["updated"]} (version: {content[7]["Oxygen"]["exploit_version"]})\n \
            Fluxus: {content[8]["Fluxus"]["updated"]} (version: {content[8]["Fluxus"]["exploit_version"]})\n \
            Ro-Ware: {content[9]["Ro-Ware"]["updated"]} (version: {content[9]["Ro-Ware"]["exploit_version"]})\n \
            Celestial: {content[10]["Celestial"]["updated"]} (version: {content[10]["Celestial"]["exploit_version"]})\n \
            Comet: {content[11]["Comet"]["updated"]} (version: {content[11]["Comet"]["exploit_version"]})\n \
            AliEgExecutor: False (version: 1.0)')
    if message.content.startswith('!status'):
        await message.author.send(embed=embed_status)


client.run(token)