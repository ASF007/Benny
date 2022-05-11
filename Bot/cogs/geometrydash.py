import asyncio
import discord
import discord.utils
from discord.ext import commands
from gears import style
import gd


class GeometryDash(commands.Cog):
    """Gonna be adding geodash stuff"""

    def __init__(self, bot):
        self.bot = bot
        self.gd = gd.Client()

    @commands.hybrid_group(
        name="gd",
        description="""Geometry dash related commands""",
        help="""Geometry dash related commands""",
        brief="Brief one liner about the command",
        aliases=["geometrydash"],
        enabled=True,
        hidden=False
    )
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def gd_cmd(self, ctx):
        """Does nothing on its own as of now"""
        if not ctx.invoked_subcommand:
            pass

    @gd_cmd.command(
        name="daily",
        description="""View the daily levels information""",
        help="""View the daily levels information""",
        brief="Daily level info",
        aliases=[],
        enabled=True,
        hidden=False
    )
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def get_daily(self, ctx) -> None:
        try:
            daily = await self.gd.get_daily()

        except gd.MissingAccess:
            embed = discord.Embed(
                title="Error Occured",
                description="Failed to get a daily level.",
                timestamp=discord.utils.utcnow(),
                color=style.Color.RED
            )
            return await ctx.send(embed=embed)

        embed = (
            discord.Embed(color=0x7289da).set_author(name="Current Daily")
            .add_field(name="Name", value=daily.name)
            .add_field(name="Difficulty", value=f"{daily.stars} ({daily.difficulty.title})")
            .add_field(name="ID", value=f"{daily.id}")
            .set_footer(text=f"Creator: {daily.creator.name}")
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GeometryDash(bot))