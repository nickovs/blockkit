# BlockKit: A Pythonic library for constructing Slack Block Kit API structures.

# Copyright 2021 Nicko van Someren
#
# Licensed under the Apache License, Version 2.0 (the "License")
# See the LICENSE.txt file for details

# SPDX-License-Identifier: Apache-2.0

# pylint: disable=too-few-public-methods

"""Elements used within Block Kit blocks"""

from typing import List

from .base import Element
from .components import Text, Option, OptionGroup, ConversationFilter, DispatchActionConf, Confirm

# Elements used inside block layouts
class Button(Element):
    """An interactive component that inserts a button."""
    text: Text
    action_id: str
    url: str = None
    value: str = None
    style: str = None
    confirm: Confirm = None


class Checkboxes(Element):
    """A checkbox group that allows multiple choices from a list of options."""
    action_id: str
    options: List[Option]
    initial_options: List[Option] = None
    confirm: Confirm = None


class DatePicker(Element):
    """An element which lets users easily select a date from a calendar style UI."""
    action_id: str
    placeholder: Text
    initial_date: str = None
    confirm: Confirm = None


class Image(Element):
    """An element to insert an image as part of a larger block of content."""
    image_url: str
    alt_text: str


class MultiStaticSelect(Element):
    """A menu that allows multiple selections from a static list."""
    _type = "multi_static_select"
    placeholder: Text
    action_id: str
    options: List[Option] = None
    option_groups: List[OptionGroup] = None
    initial_options: List[Option] = None
    confirm: Confirm = None
    max_selected_items: int = None


class MultiExternalSelect(Element):
    """A menu that allows multiple selections from a externally sourced list."""
    _type = "multi_external_select"
    placeholder: Text
    action_id: str
    min_query_length: int = None
    initial_options: List[Option] = None
    confirm: Confirm = None
    max_selected_items: int = None


class MultiUsersSelect(Element):
    """A menu that allows multiple selections from a list of users."""
    _type = "multi_users_select"
    placeholder: Text
    action_id: str
    initial_users: List[str] = None
    confirm: Confirm = None
    max_selected_items: int = None


class MultiConversationsSelect(Element):
    """A menu that allows multiple selections from a list of conversations."""
    _type = "multi_conversations_select"
    placeholder: Text
    action_id: str
    initial_conversations: List[str] = None
    default_to_current_conversation: bool = None
    confirm: Confirm = None
    max_selected_items: int = None
    filter: ConversationFilter = None


class MultiChannelsSelect(Element):
    """A menu that allows multiple selections from a list of channels."""
    _type = "multi_channels_select"
    placeholder: Text
    action_id: str
    initial_channels: List[str]
    confirm: Confirm = None
    max_selected_items: int = None


class Overflow(Element):
    """A popup menu presented off to the side."""
    action_id: str
    options: List[Option]
    confirm: Confirm = None


class PlainTextInput(Element):
    """A plain-text input, similar to the HTML <input> tag."""
    _type = "plain_text_input"
    action_id: str
    placeholder: Text
    initial_value: str = None
    multiline: bool = None
    min_length: int = None
    max_length: int = None
    dispatch_action_config: DispatchActionConf = None


class RadioButtons(Element):
    """A radio button group that allows choice of one item from a list of options."""
    _type = "radio_buttons"
    action_id: str
    options: List[Option]
    initial_option: Option = None
    confirm: Confirm = None


class StaticSelect(Element):
    """A single-selection menu from a static list."""
    _type = "static_select"
    placeholder: Text
    action_id: str
    options: List[Option] = None
    option_groups: List[OptionGroup] = None
    initial_option: Option = None
    confirm: Confirm = None


class ExternalSelect(Element):
    """A single-selection menu from an externally sourced list."""
    _type = "external_select"
    placeholder: Text
    action_id: str
    initial_option: Option = None
    min_query_length: int = None
    confirm: Confirm = None


class UsersSelect(Element):
    """A single-selection menu from a list of users."""
    _type = "users_select"
    placeholder: Text
    action_id: str
    initial_user: str = None
    confirm: Confirm = None


class ConversationsSelect(Element):
    """A single-selection menu from a list of conversations."""
    _type = "conversations_select"
    placeholder: Text
    action_id: str
    initial_conversations: str = None
    default_to_current_conversation: bool = None
    confirm: Confirm = None
    response_url_enabled: bool = None
    filter: ConversationFilter = None


class ChannelsSelect(Element):
    """A single-selection menu from a list of channels."""
    _type = "channels_select"
    placeholder: Text
    action_id: str
    initial_channel: str
    confirm: Confirm = None
    response_url_enabled: bool = None


class TimePicker(Element):
    """An element which allows selection of a time of day."""
    placeholder: Text
    action_id: str
    initial_time: str = None
    confirm: Confirm = None
