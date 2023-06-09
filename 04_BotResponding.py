import discord

# specifying our server
GUILD = "{Server-von-Jana}"

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# discord token
	DISCORD_TOKEN = lines[1]
# close the file
f.close()

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	# print out nice statment saying our bot is online (only in command prompt)
	print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	# this prevents inifinte loops of bot talking to bot
	# if author of the message is the bot, don't do anything
	if message.author == client.user:
		return
	# ignore @everyone mentions
	if message.mention_everyone:
		return
	# if the message mentions the bot, then do something
	elif client.user.mentioned_in(message): 
		await message.channel.send("Hello!")


client.run(DISCORD_TOKEN)