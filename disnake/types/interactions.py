# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Literal, Optional, TypedDict, Union

from typing_extensions import NotRequired

from .channel import ChannelType
from .components import Component, Modal
from .embed import Embed
from .member import Member, MemberWithUser
from .role import Role
from .snowflake import Snowflake
from .user import User

if TYPE_CHECKING:
    from .message import AllowedMentions, Attachment, Message


ApplicationCommandLocalizations = Dict[str, str]


ApplicationCommandType = Literal[1, 2, 3]


class ApplicationCommand(TypedDict):
    id: Snowflake
    type: NotRequired[ApplicationCommandType]
    application_id: Snowflake
    guild_id: NotRequired[Snowflake]
    name: str
    name_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    description: str
    description_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    options: NotRequired[List[ApplicationCommandOption]]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[Optional[bool]]
    default_permission: NotRequired[bool]  # deprecated
    version: Snowflake


ApplicationCommandOptionType = Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class ApplicationCommandOption(TypedDict):
    type: ApplicationCommandOptionType
    name: str
    name_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    description: str
    description_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    required: NotRequired[bool]
    choices: NotRequired[List[ApplicationCommandOptionChoice]]
    options: NotRequired[List[ApplicationCommandOption]]
    channel_types: NotRequired[List[ChannelType]]
    min_value: NotRequired[float]
    max_value: NotRequired[float]
    min_length: NotRequired[int]
    max_length: NotRequired[int]
    autocomplete: NotRequired[bool]


ApplicationCommandOptionChoiceValue = Union[str, int, float]


class ApplicationCommandOptionChoice(TypedDict):
    name: str
    name_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    value: ApplicationCommandOptionChoiceValue


ApplicationCommandPermissionType = Literal[1, 2, 3]


class ApplicationCommandPermissions(TypedDict):
    id: Snowflake
    type: ApplicationCommandPermissionType
    permission: bool


class GuildApplicationCommandPermissions(TypedDict):
    id: Snowflake
    application_id: Snowflake
    guild_id: Snowflake
    permissions: List[ApplicationCommandPermissions]


InteractionType = Literal[1, 2, 3, 4, 5]


class _ApplicationCommandInteractionDataOption(TypedDict):
    name: str


class _ApplicationCommandInteractionDataOptionSubcommand(_ApplicationCommandInteractionDataOption):
    type: Literal[1, 2]
    options: List[ApplicationCommandInteractionDataOption]


class _ApplicationCommandInteractionDataOptionString(_ApplicationCommandInteractionDataOption):
    type: Literal[3]
    value: str


class _ApplicationCommandInteractionDataOptionInteger(_ApplicationCommandInteractionDataOption):
    type: Literal[4]
    value: int


class _ApplicationCommandInteractionDataOptionBoolean(_ApplicationCommandInteractionDataOption):
    type: Literal[5]
    value: bool


class _ApplicationCommandInteractionDataOptionSnowflake(_ApplicationCommandInteractionDataOption):
    type: Literal[6, 7, 8, 9, 11]
    value: Snowflake


class _ApplicationCommandInteractionDataOptionNumber(_ApplicationCommandInteractionDataOption):
    type: Literal[10]
    value: float


ApplicationCommandInteractionDataOption = Union[
    _ApplicationCommandInteractionDataOptionString,
    _ApplicationCommandInteractionDataOptionInteger,
    _ApplicationCommandInteractionDataOptionSubcommand,
    _ApplicationCommandInteractionDataOptionBoolean,
    _ApplicationCommandInteractionDataOptionSnowflake,
    _ApplicationCommandInteractionDataOptionNumber,
]


class ApplicationCommandResolvedPartialChannel(TypedDict):
    id: Snowflake
    type: ChannelType
    permissions: str
    name: str


class ApplicationCommandInteractionDataResolved(TypedDict, total=False):
    users: Dict[Snowflake, User]
    members: Dict[Snowflake, Member]
    roles: Dict[Snowflake, Role]
    channels: Dict[Snowflake, ApplicationCommandResolvedPartialChannel]
    messages: Dict[Snowflake, Message]
    attachments: Dict[Snowflake, Attachment]


class ApplicationCommandInteractionData(TypedDict):
    id: Snowflake
    name: str
    type: ApplicationCommandType
    resolved: NotRequired[ApplicationCommandInteractionDataResolved]
    options: NotRequired[List[ApplicationCommandInteractionDataOption]]
    # this is the guild the command is registered to, not the guild the command was invoked in (see interaction.guild_id)
    guild_id: NotRequired[Snowflake]
    target_id: NotRequired[Snowflake]


## Interaction components


class _BaseComponentInteractionData(TypedDict):
    custom_id: str


### Message interaction components


class MessageComponentInteractionButtonData(_BaseComponentInteractionData):
    component_type: Literal[2]


class MessageComponentInteractionSelectData(_BaseComponentInteractionData):
    component_type: Literal[3]
    values: List[str]


MessageComponentInteractionData = Union[
    MessageComponentInteractionButtonData,
    MessageComponentInteractionSelectData,
]


### Modal interaction components


class ModalInteractionSelectData(_BaseComponentInteractionData):
    type: Literal[3]
    values: List[str]


class ModalInteractionTextInputData(_BaseComponentInteractionData):
    type: Literal[4]
    value: str


ModalInteractionComponentData = Union[
    ModalInteractionSelectData,
    ModalInteractionTextInputData,
]


class ModalInteractionActionRow(TypedDict):
    type: Literal[1]
    components: List[ModalInteractionComponentData]


class ModalInteractionData(TypedDict):
    custom_id: str
    components: List[ModalInteractionActionRow]


## Interactions


# base type for *all* interactions
class _BaseInteraction(TypedDict):
    id: Snowflake
    application_id: Snowflake
    token: str
    version: Literal[1]


# common properties in non-ping interactions
class _BaseUserInteraction(_BaseInteraction):
    # the docs specify `channel_id` as optional,
    # but it is assumed to always exist on non-ping interactions
    channel_id: Snowflake
    locale: str
    app_permissions: NotRequired[str]
    guild_id: NotRequired[Snowflake]
    guild_locale: NotRequired[str]
    # one of these two will always exist, according to docs
    member: NotRequired[MemberWithUser]
    user: NotRequired[User]


class PingInteraction(_BaseInteraction):
    type: Literal[1]


class ApplicationCommandInteraction(_BaseUserInteraction):
    type: Literal[2, 4]
    data: ApplicationCommandInteractionData


class MessageInteraction(_BaseUserInteraction):
    type: Literal[3]
    data: MessageComponentInteractionData
    message: Message


class ModalInteraction(_BaseUserInteraction):
    type: Literal[5]
    data: ModalInteractionData
    message: NotRequired[Message]


Interaction = Union[
    ApplicationCommandInteraction,
    MessageInteraction,
    ModalInteraction,
]

BaseInteraction = Union[Interaction, PingInteraction]


class InteractionApplicationCommandCallbackData(TypedDict, total=False):
    tts: bool
    content: str
    embeds: List[Embed]
    allowed_mentions: AllowedMentions
    flags: int
    components: List[Component]
    # TODO: missing attachment field


class InteractionAutocompleteCallbackData(TypedDict):
    choices: List[ApplicationCommandOptionChoice]


InteractionResponseType = Literal[1, 4, 5, 6, 7]

InteractionCallbackData = Union[
    InteractionApplicationCommandCallbackData,
    InteractionAutocompleteCallbackData,
    Modal,
]


class InteractionResponse(TypedDict):
    type: InteractionResponseType
    data: NotRequired[InteractionCallbackData]


class InteractionMessageReference(TypedDict):
    id: Snowflake
    type: InteractionType
    name: str
    user: User


class EditApplicationCommand(TypedDict):
    name: str
    # TODO: properly seperate these payloads
    id: NotRequired[Snowflake] # when this is provided we are able to change the name, this is also slightly wrong in this payload
    name_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    description: NotRequired[str]
    description_localizations: NotRequired[Optional[ApplicationCommandLocalizations]]
    options: NotRequired[Optional[List[ApplicationCommandOption]]]
    default_member_permissions: NotRequired[Optional[str]]
    dm_permission: NotRequired[bool]
    default_permission: NotRequired[bool]  # deprecated
    # TODO: remove, this cannot be changed
    type: NotRequired[ApplicationCommandType]
