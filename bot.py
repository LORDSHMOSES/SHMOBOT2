# import libraries
from discord.ext import commands
import r6sapi
import getpass

# get uplay username and password for API
username = input("Username: ")
password = getpass.getpass('Password: ')

# get client object
bot = commands.Bot(command_prefix='!')

# TODO: insert new user dm as a string below
newuserdm = "Welcome!"


# stat lookup command
@bot.command(help="Looks up the stats for a player")
async def stat(ctx):
    await ctx.send(
        "Nothing here yet!"
    )
    auth = r6sapi.Auth(username, password)
    # This is a test to prove the API works in this context.
    player = await auth.get_player("LORD_SHMOSES", r6sapi.Platforms.UPLAY)
    operator = await player.get_operator("mute")
    print(operator.kills)
    # TODO: gather stats here.
    await auth.close()


# Events

# send welcome dm to new users!
# TODO: testing
@bot.event
async def on_member_join(member):
    await member.send(newuserdm)


# Event Listener for when bot comes online
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


bot.run('TOKENGOESHERE')
