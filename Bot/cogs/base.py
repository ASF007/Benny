import discord
import discord.utils
import unicodedata
from discord.commands import Option, slash_command
from discord.ext import commands
from gears import cviews, style


"""@commands.dynamic_cooldown(custom_cooldown, commands.BucketType.user)
async def ping(ctx):
    await ctx.send("pong")"""


class Base(commands.Cog):
    """Cog Example Description"""

    def __init__(self, bot):
        self.bot = bot
        self.MemberConverter = commands.MemberConverter()

    @commands.command(
        name="about",
        description="""tells you some stuff about the bot""",
        help="""About the bot, why I built it, what it can and is going to do""",
        brief="About the bot",
        aliases=[],
        enabled=True,
        hidden=False,
    )
    @commands.cooldown(1.0, 5.0, commands.BucketType.channel)
    async def about_cmd(self, ctx):
        """About command"""
        embed = discord.Embed(
            title=f"About the Bot",
            description=f"""I first started making bots in 2020, these were mainly small community bots for me and my online/offline friends
            As I learned more and more I saw some popular bots and decided to learn more about them too.
            However as the time went on many of my favorite bots died for different reasons, Pokecord, Rythm, and other ones I will not be mentioning for reasons.
            
            This inspired me in a sense to create my first public bot, one that had features that were useful and up to date, things that users would actually want.
            You will always be able to suggest things to add, things to remove, and ways to optimise the bot for the smoothest interactions with users.
            
            I hope you've enjoyed using this bot thus far and I hope you'll enjoy the bot to come.
            - Ben""",
            timestamp=discord.utils.utcnow(),
            color=style.get_color("aqua"),
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="avatar",
        description="""Enlarge the avatar of an user""",
        help="""Show a users avatar in a nice clean embed.""",
        brief="""Short help text""",
        aliases=["av", "pfp"],
        enabled=True,
        hidden=False,
    )
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def avatar_cmd(self, ctx, *, user: discord.Member = None):
        """Show a users avatar"""
        view = cviews.DeleteView()
        if not user:
            user = ctx.author

        embed = discord.Embed(
            title=user.display_name, timestamp=discord.utils.utcnow(), color=user.color
        )
        embed.set_image(url=user.avatar.url)
        view.bctx = await ctx.send(embed=embed, view=view)

    @slash_command()
    async def avatar(
        self, ctx, user: Option(str, "Enter someone's Name", required=False)
    ):
        """Show a users avatar"""
        view = cviews.DeleteView(True)
        if not user:
            user = ctx.author
        else:
            user = await self.MemberConverter.convert(ctx, user)
        embed = discord.Embed(
            title=user.display_name, timestamp=discord.utils.utcnow(), color=user.color
        )
        embed.set_image(url=user.avatar.url)
        view.bctx = await ctx.respond(embed=embed, view=view)

    @commands.command(
        name="info",
        description="""Description of Command""",
        help="""Long Help text for this command""",
        brief="""Short help text""",
        aliases=["i"],
        enabled=True,
        hidden=False,
    )
    async def my_command(self, ctx, person: discord.Member = None):
        """View an users info"""
        if not person:
            person = ctx.author

        embed = discord.Embed(
            title=f"{person.name}#{person.discriminator} Info",
            description=f"""
            {person.bot}
            {person.created_at}
            {person.display_name}
            {person.id}
            {person.mention}
            {person.mutual_guilds}
            {person.public_flags}
            {person.system}""",
            timestamp=discord.utils.utcnow(),
            color=person.color,
        )
        embed.set_thumbnail(url=person.avatar)
        await ctx.send(embed=embed)

    @commands.command(
        name="charinfo",
        aliases=["ci"],
        description="""Get some charinfo yay""",
        help="""Evaluate some code, dev only.""",
        brief="Get one or multiple characters info",
        enabled=True,
        hidden=False,
    )
    async def charinfo(self, ctx, *, characters: str):
        """Gives you the character info"""

        def to_string(c):
            digit = f"{ord(c):x}"
            name = unicodedata.name(c, "Name not found.")
            return f"""```fix
\\U{digit:>08}
```
{c} - [{name}](http://www.fileformat.info/info/unicode/char/{digit})"""

        msg = "\n".join(map(to_string, characters))

        embed = discord.Embed(
            title="Charinfo",
            description=msg,
            timestamp=discord.utils.utcnow(),
            color=style.get_color(),
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="dog",
        description="""Dog command to give you a random image of a dog""",
        help="""What good bot doesn't have a dog command?""",
        brief="Get a random dog image",
        aliases=[],
        enabled=True,
        hidden=False,
    )
    @commands.cooldown(1.0, 3.0, commands.BucketType.user)
    async def dog_cmd(self, ctx):
        """dog command"""
        dog = await self.bot.aiosession.get("https://dog.ceo/api/breeds/image/random")

        dog_image = (await dog.json()).get("message")
        embed = discord.Embed(color=style.get_color())
        embed.set_image(url=dog_image)
        await ctx.send(embed=embed)

    @commands.command(
        name="pycord",
        description="""Stuff abt pycord""",
        help="""Why pycord bad, but why we still use it""",
        brief="Why pycord bad",
        aliases=[],
        enabled=True,
        hidden=True
    )
    @commands.cooldown(1.0, 5.0, commands.BucketType.channel)
    async def pyc_cmd(self, ctx):
        """. Just wanna write stuff here"""
        embed = discord.Embed(
            title=f"Why Pycord?",
            description=f"""Gonna be completely honest, it seems very shitty so far.
            After adding a few features and having delayed releases/betas and design choices I think are really shitty, pycord has almost* completely claimed all credit for this maintained fork.
            
            All the old maintainer of the library needs, is apparently a license mention and that's it. He's "famous enough", that being said, why don't I make a library then? or fork dpy for that matter?
            
            Not only do I not have the time, I would also say I'm not experienced enough to maintain such a massive library. So call me what you may but this library is only being used because it's the best among shitty forks.
            
            You can join pycords support server and take a snoop around if you want to learn more, it's up to you to judge, though if you're looking for a new library I would recommend not using python at all and moving onto another better language which with it could come with a much better library.
            
            - Ben""",
            timestamp=discord.utils.utcnow(),
            color=style.get_color()
        )
        embed.set_image(
            url="https://i.imgur.com/oca7K5s.png"
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
