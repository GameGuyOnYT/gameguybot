import datetime, discord, json, requests
from discord.ext import commands, tasks

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")
token = 'placeholderMTAwOTU3MTY1NzUzNjUxNjA5Ng.G9HVU0.kHfcG34SZIImap-D2YDiCgwc6VknrlRuNLRXeUplaceholder'.replace("placeholder", "")

@bot.listen()
async def on_ready():
    task_loop.start()  # important to start the loop

@tasks.loop(seconds=10)
async def task_loop():
    print("loop point")
    content = json.loads(requests.get("https://api.whatexploitsare.online/status").text)

    def onlineCheck(num, exploit):
        if type(exploit) != str:
            return -1
        if type(num) != int:
            return -1
        isOnline = content[num][exploit]["updated"]
        if isOnline == True:
            isOnline = ":green_circle:"
        elif isOnline == False:
            isOnline = ":red_circle:"
        elif isOnline == 3:
            isOnline = ":yellow_circle:"
        elif isOnline == 4:
            isOnline = ":orange_circle:"
        return isOnline

    def versionCheck(num, exploit):
        if type(exploit) != str:
            return -1
        if type(num) != int:
            return -1
        version = content[num][exploit]['exploit_version']
        version = version.replace(" Belgium Tax Evasion", "")
        version = version.replace("V", "")
        version = version.replace("v", "")
        return version

    def timeCheck(num, exploit):
        if type(exploit) != str:
            return -1
        if type(num) != int:
            return -1
        updateTime = content[num][exploit]['last_update_unix']
        timeConverted = datetime.datetime.utcfromtimestamp(updateTime).strftime('**%m-%d-%Y** at **%H:%M:%S**')
        return timeConverted.encode("unicode_escape").decode("utf-8")

    embed_status = discord.Embed(colour=discord.Colour.yellow(), title="Exploit Status")
    guild = bot.get_guild(1039596383717568512)
    channel = guild.get_channel(1039596384195715127)
    msg = await channel.fetch_message(1039606848661245992)
    statuses = (
        f":green_circle: : **Working** | :red_circle: : **Not Working** | :orange_circle: : **In Testing** | :yellow_circle: : **API / Website Down**\n \n \
                **Synapse**:          {onlineCheck(0, 'Synapse')} (version: **{versionCheck(0, 'Synapse')}** | last updated on {timeCheck(0, 'Synapse')})\n \
                **Script-Ware**: {onlineCheck(1, 'Script-Ware')} (version: **{versionCheck(1, 'Script-Ware')}** | last updated on {timeCheck(1, 'Script-Ware')})\n \
                **KRNL**:                 {onlineCheck(2, 'KRNL')} (version: **{versionCheck(2, 'KRNL')}** | last updated on {timeCheck(2, 'KRNL')})\n \
                **DX9WARE**:      {onlineCheck(3, 'DX9WARE')} (version: **{versionCheck(3, 'DX9WARE')}** | last updated on {timeCheck(3, 'DX9WARE')})\n \
                **Electron**:          {onlineCheck(4, 'Electron')} (version: **{versionCheck(4, 'Electron')}** | last updated on {timeCheck(4, 'Electron')})\n \
                **JJSploit**:          {onlineCheck(5, 'WeAreDevs API')} (version: **{versionCheck(5, 'WeAreDevs API')}** | last updated on {timeCheck(5, 'WeAreDevs API')})\n \
                **Oxygen U**:       {onlineCheck(6, 'Oxygen')} (version: **{versionCheck(6, 'Oxygen')}** | last updated on {timeCheck(6, 'Oxygen')})\n \
                **Fluxus**:              {onlineCheck(7, 'Fluxus')} (version: **{versionCheck(7, 'Fluxus')}** | last updated on {timeCheck(7, 'Fluxus')})\n \
                **Ro-Ware**:         {onlineCheck(8, 'Ro-Ware')} (version: **{versionCheck(8, 'Ro-Ware')}** | last updated on {timeCheck(8, 'Ro-Ware')})\n \
                **Celestial**:         {onlineCheck(9, 'Celestial')} (version: **{versionCheck(9, 'Celestial')}** | last updated on {timeCheck(9, 'Celestial')})\n \
                **Comet**:              {onlineCheck(10, 'Comet')} (version: **{versionCheck(10, 'Comet')}** | last updated on {timeCheck(10, 'Comet')})")
    embed_status.description = statuses

    await msg.edit(embed=embed_status)

bot.run(token)
