# import libraries
import discord

# get client object
client = discord.Client()


# Event Listener for when bot comes online
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


# prevent bot from reading its own messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return


# help printout
# TODO: make a help message.
@client.event
async def on_message(message):
    await message.channel.send(
        "Nothing here yet!"
    )


client.run('CLIENTCODEHERE')
