import logging

from discord import Forbidden, Message

"""
MIT License.

Copyright (c) 2021 Python Discord

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


async def handle_forbidden_from_block(error: Forbidden, message: Message | None = None) -> None:
    """
    Handles ``discord.Forbidden`` 90001 errors, or re-raises if ``error`` isn't a 90001 error.

    Args:
        error: The raised ``discord.Forbidden`` to check.
        message: The message to reply to and include in logs, if error is 90001 and message is provided.
    """
    if error.code != 90001:
        # The error ISN'T caused by the nianbot attempting to add a reaction
        # to a message whose author has blocked the nianbot, so re-raise it
        raise error

    if not message:
        logging.info("Failed to add reaction(s) to a message since the message author has blocked the nianbot")
        return

    if message:
        logging.info(
            "Failed to add reaction(s) to message %d-%d since the message author (%d) has blocked the nianbot",
            message.channel.id,
            message.id,
            message.author.id,
        )
        await message.channel.send(
            f":x: {message.author.mention} failed to add reaction(s) to your message as you've blocked me.",
            delete_after=30
        )
