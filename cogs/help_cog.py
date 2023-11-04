import discord
from discord.ext import commands

class helper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
General commands:
-help - Displays all the available commands
-p <keywords> - Finds the current song on youtube and plays it in your current channel. Will resume playing if paused.
-q - Displays the current music queue
-skip - Skips the current song being played
-clear - Stops the music and clears the queue
-leave - Disconnects the bot from the voice channel
-pause - Pauses the current song being played or resumed if already paused
-resume - Resumes playing the current song
```
"""
        # self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog ready!')
        # for guild in self.bot.guilds:
        #     for channel in guild.text_channels:
        #         self.text_channel_text.append(channel)

        #     await self.send_to_all(self.help_message)
    
    # async def send_to_all(self, msg):
    #     for text_channel in self.text_channel_text:
    #         await text_channel.send(msg)

    @commands.command(name="help", aliases=["h"], help="Displays help options")
    async def help(self, ctx):
        await ctx.send(self.help_message)



async def setup(bot):
    await bot.add_cog(helper(bot))