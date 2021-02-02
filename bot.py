# import libraries
import discord
import r6sapi
import getpass

# get client object
client = discord.Client()


# Event Listener for when bot comes online
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    # get uplay username and password for API
    username = input("Username: ")
    password = getpass.getpass('Password: ')

# prevent bot from reading its own messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return


newuserdm = "Welcome!"


# help printout
# TODO: make a help message.
@client.event
async def on_message(message):
    if message.content.startswith("!help"):
        await message.channel.send(
            "Nothing here yet!"
        )


# stat lookup command
@client.event
async def on_message(message):
    if message.content.startswith("!stat"):
        await message.channel.send(
            "Nothing here yet!"
        )


# send welcome dm to new users!
# TODO: testing
@client.event
async def on_member_join(member):
    await member.send(newuserdm)


client.run('NjM4MTIxNzA3NTUwNTM5Nzc4.XbYHJg.tflWbIeXRkgCjC9b90exZxwyBNs')
