import discord, os, requests, json, datetime

os.environ[
    'TOKEN'] = 'PlaceholderSoThatDiscordDoesntResetMyTokenMTAwOTU3MTY1NzUzNjUxNjA5Ng.G9HVU0.kHfcG34SZIImap-D2YDiCgwc6VknrlRuNLRXeUPlaceholderSoThatDiscordDoesntResetMyToken'.replace(
    "PlaceholderSoThatDiscordDoesntResetMyToken", "")

bot = discord.Client(intents=discord.Intents.default())


def get_status():
    data = json.loads(requests.get("https://api.whatexploitsare.online/status").text)

    def onlineCheck(num, exploit):
        if type(exploit) != str:
            return -1
        if type(num) != int:
            return -1
        isOnline = data[num][exploit]["updated"]
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
        version = data[num][exploit]['exploit_version']
        version = version.replace(" Cubed Alpha", "")
        version = version.replace("V", "")
        version = version.replace("v", "")
        return version

    def timeCheck(num, exploit):
        if type(exploit) != str:
            return -1
        if type(num) != int:
            return -1
        updateTime = data[num][exploit]['last_update_unix']
        timeConverted = datetime.datetime.utcfromtimestamp(updateTime).strftime('**%m-%d-%Y** at **%H:%M:%S**')
        return timeConverted.encode("unicode_escape").decode("utf-8")

    return f":green_circle: : **Working** | :red_circle: : **Not Working** | :orange_circle: : **In Testing** | :yellow_circle: : **API / Website Down**\n \n \
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
    **Comet**:              {onlineCheck(10, 'Comet')} (version: **{versionCheck(10, 'Comet')}** | last updated on {timeCheck(10, 'Comet')})"


@bot.event
async def on_ready():
    print("Connected!")


@bot.event
async def on_message(message):
    if message.author == bot.user: return

    if message.content.startswith('!help'):
        await message.author.send('```!status - Check if your ROBLOX exploit is online.\n!help - Show this message.```')
    elif message.content.startswith('!status'):
        await message.channel.send(embed=discord.Embed(title="Exploit Status", description=get_status(), url="https://youtube.com/@gameguyonyt/", color=0xffff00))


bot.run(os.getenv('TOKEN'))
