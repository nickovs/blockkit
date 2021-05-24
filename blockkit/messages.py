# BlockKit: A Pythonic library for constructing Slack Block Kit API structures.

# Copyright 2021 Nicko van Someren
#
# Licensed under the Apache License, Version 2.0 (the "License")
# See the LICENSE.txt file for details

# SPDX-License-Identifier: Apache-2.0

# pylint: disable=too-few-public-methods

"""Types of message structure used by the Block Kit API"""

from typing import List
from .base import Block, Component


class Attachment(Component):
    """An attachment to a message"""
    blocks: List[Block] = None
    color: str = None


class Message(Component):
    """A message that can be sent with the Slack API"""
    channel: str
    blocks: List[Block] = None
    text: str = None
    attachments: List[Attachment] = None
    thread_ts: str = None
    mrkdwn: bool = None
    draft_id: str = None
    icon_emoji: str = None
    icon_url: str = None
    link_names: bool = None
    parse: str = None
    reply_broadcast: bool = None
    thread_ts: str = None
    unfurl_links: bool = None
    unfurl_media: bool = None
    as_user: bool = None
    username: str = None
