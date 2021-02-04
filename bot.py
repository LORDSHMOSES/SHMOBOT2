# import libraries
import discord
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
async def stat(ctx, arg):
    # TODO:add handler for null arg
    auth = r6sapi.Auth(username, password)
    player = await auth.get_player(arg, r6sapi.Platforms.UPLAY)
    await r6sapi.Player.load_general(player)
    await r6sapi.Player.load_queues(player)
    region = r6sapi.RankedRegions.NA
    Rank = await player.get_rank(region)
    rankstats = player.ranked
    rankkd = (round((rankstats.kills / rankstats.deaths), 2))
    kd = (round((player.kills / player.deaths), 2))
    mmr = Rank.mmr
    rankurl = Rank.get_icon_url()
    embed = discord.Embed(colour=discord.Colour(0xe75e15), description="Here are the stats for %s" % arg)
    staturlbase = "https://tabstats.com/siege/search/uplay/replace"
    newurl = staturlbase.replace('replace', arg)
    embed.set_thumbnail(url=rankurl)
    embed.set_author(name=arg, url=newurl)

    embed.add_field(name="Overall K/D", value=kd)
    embed.add_field(name="Ranked K/D", value=rankkd)
    embed.add_field(name="Top Operators", value="op1, op2, op3")
    embed.add_field(name="Current MMR", value=mmr)

    await ctx.send(embed=embed)
    await auth.close()


# init role command
@bot.command(help="Init role command ADMIN ONLY!!!")
async def initroles(ctx):
    await ctx.send(
        "Nothing here yet!"
    )


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


bot.run('INSERTCODEHERE')
