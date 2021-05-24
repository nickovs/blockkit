# BlockKit: A Pythonic library for constructing Slack Block Kit API structures.

# Copyright 2021 Nicko van Someren
#
# Licensed under the Apache License, Version 2.0 (the "License")
# See the LICENSE.txt file for details

# SPDX-License-Identifier: Apache-2.0

# pylint: disable=too-few-public-methods

"""Types of block available within Block Kit"""

from typing import List, Union
from .base import Block, Element

from .components import Text


# The block types themselves
class Actions(Block):
    """A block that is used to hold interactive elements.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#actions>`
    for details.
    """
    elements: List[Element]


class Context(Block):
    """Displays message context, which can include both images and text.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#context>`
    for details.
    """
    elements: List[Union[Element, Text]]


class Divider(Block):
    """A content divider to split up different blocks inside of a message.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#divider>`
    for details.
    """
    # Since the block_id is defined automatically, there is nothing to do here


class File(Block):
    """Displays a remote file.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#file>`
    for details.
    """
    external_id: str
    source: str = "remote"


class Header(Block):
    """A header is a plain-text block that displays in a larger, bold font.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#header>`
    for details.
    """
    text: Text


class ImageBlock(Block):
    """A simple image block.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#image>`
    for details.
    """
    _type = "image"
    image_url: str
    alt_text: str
    title: Text = None


class Input(Block):
    """A block that collects information from users.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#input>`
    for details.
    """
    label: Text
    element: Block
    dispatch_action: bool = None
    hint: Text = None
    optional: bool = None


class Section(Block):
    """A section that can hold text and optionally side-by-side with any other block elements.

    See the `Slack API <https://api.slack.com/reference/block-kit/blocks#section>`
    for details.
    """
    text: Text = None
    fields: List[Text] = None
    accessory: Block = None
