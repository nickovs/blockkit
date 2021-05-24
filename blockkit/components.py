# BlockKit: A Pythonic library for constructing Slack Block Kit API structures.

# Copyright 2021 Nicko van Someren
#
# Licensed under the Apache License, Version 2.0 (the "License")
# See the LICENSE.txt file for details

# SPDX-License-Identifier: Apache-2.0

# pylint: disable=too-few-public-methods

"""Components used within various Block Kit elements and blocks"""

from typing import List

from .base import Component


# Low-level components
class Text(Component):
    """An object containing some text, formatted either as plain text or using markdown

    See the `Slack API <https://api.slack.com/reference/block-kit/composition-objects#text>`
    for details.
    """
    text: str
    _type: str = "plain_text"
    emoji: bool = None
    verbatim: bool = None

    PLAIN = "plain_text"
    MARKDOWN = "mrkdwn"

    @classmethod
    def validate_value(cls, value):
        """Validate is a value can be used to where this class is expected"""
        if isinstance(value, str):
            return (True, cls(value))
        if isinstance(value, Text):
            return (True, value)
        return (False, None)


class Confirm(Component):
    """An object that defines a dialog to confirm selection in any interactive element.

    See the `Slack API <https://api.slack.com/reference/block-kit/composition-objects#confirm>`
    for details.
    """
    title: Text
    text: Text
    confirm: Text
    deny: Text
    style: str = None


class Option(Component):
    """An object that represents a single selectable item in a menu.

    See the `Slack API <https://api.slack.com/reference/block-kit/composition-objects#option>`
    for details.
    """
    text: Text
    value: str
    description: Text = None
    url: str = None


class OptionGroup(Component):
    """Provides a way to group options in a select menu or multi-select menu.

    See the `Slack API <https://api.slack.com/reference/block-kit/composition-objects#option_group>`
    for details.
    """
    label: Text
    options: List[Option]


class DispatchActionConf(Component):
    """Determines when a plain-text input element will trigger a block_actions payload.

    See the `Slack API
    <https://api.slack.com/reference/block-kit/composition-objects#dispatch_action_config>`
    for details.
    """
    trigger_actions_on: List[str]


class ConversationFilter(Component):
    """Provides a way to filter the list of options in a conversations menu.

    See the `Slack API
    <https://api.slack.com/reference/block-kit/composition-objects#filter_conversations>`
    for details.
    """
    include: List[str]
    exclude_external_shared_channels: bool = None
    exclude_bot_users: bool = None
