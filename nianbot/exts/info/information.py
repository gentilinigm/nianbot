from collections import defaultdict

import arrow
import discord
from discord import Colour, Embed, Guild, Interaction, app_commands
from discord.ext.commands import GroupCog, command

from nianbot import constants
from nianbot.bot import Bot
from nianbot.errors import NonExistentRoleError


class Information(GroupCog, group_name="info", group_description="information about guild and members"):
    """A cog with commands for generating embeds with server info, such as server stats and user info."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @staticmethod
    def get_channel_type_counts(guild: Guild) -> defaultdict[str, int]:
        """Return the total amounts of the various types of channels in `guild`."""
        channel_counter = defaultdict(int)

        for channel in guild.channels:
            if channel.category_id in constants.Guild.arknights_categories:
                channel_counter["arknights"] += 1
            if channel.category_id in constants.Guild.genshin_categories:
                channel_counter["genshin"] += 1
            if isinstance(channel, discord.VoiceChannel):
                channel_counter["vc"] += 1
            else:
                channel_counter["other"] += 1

        return channel_counter

    @staticmethod
    def join_role_stats(role_ids: list[int], guild: Guild, name: str | None = None) -> dict[str, int]:
        """Return a dictionary with the number of `members` of each role given, and the `name` for this joined group."""
        member_count = 0
        for role_id in role_ids:
            if (role := guild.get_role(role_id)) is not None:
                member_count += len(role.members)
            else:
                raise NonExistentRoleError(role_id)
        return {name or role.name.title(): member_count}

    @staticmethod
    def get_member_counts(guild: Guild) -> dict[str, int]:
        """Return the total number of members for certain roles in `guild`."""
        role_ids = [
            constants.Roles.administrator,
            constants.Roles.moderator,
            constants.Roles.sub_moderator,
            constants.Roles.server_booster
        ]

        role_stats = {}
        for role_id in role_ids:
            role_stats.update(Information.join_role_stats([role_id], guild))

        return role_stats

    @command(name="guild")
    @app_commands.guild_only()
    async def info_guild(self, interaction: Interaction) -> None:
        """Sends an embed full of guild information."""
        embed = Embed(colour=Colour.green(), title="Guild Information")

        created = int(arrow.get(interaction.guild.created_at).timestamp())

        # Member status
        guild = await self.bot.fetch_guild(constants.Guild.id, with_counts=True)
        online_presences = guild.approximate_presence_count
        member_status = (
            f"{online_presences} - ({round((online_presences / guild.approximate_member_count) * 100)}%)"
        )

        embed.description = (
            f"Created: <t:{created}:R>"
            f"\nInvite: [link]({constants.Guild.invite})"
            f"\nOnline members: {member_status}"
        )
        embed.set_thumbnail(url=interaction.guild.icon.url)

        # Members
        total_members = f"{interaction.guild.member_count:,}"
        member_counts = self.get_member_counts(interaction.guild)
        member_info = "\n".join(f"{role}s: {count}" for role, count in member_counts.items())
        embed.add_field(name=f"Members: {total_members}", value=member_info)

        # Channels
        total_channels = len(interaction.guild.channels)
        channel_counts = self.get_channel_type_counts(interaction.guild)
        channel_info = "\n".join(
            f"{channel.title()}: {count}" for channel, count in sorted(channel_counts.items())
        )
        embed.add_field(name=f"Channels: {total_channels}", value=channel_info)

        await interaction.response.send_message(embed=embed)


async def setup(bot: Bot) -> None:
    """Load the Information cog."""
    await bot.add_cog(Information(bot))
