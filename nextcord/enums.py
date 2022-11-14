"""
The MIT License (MIT)

Copyright (c) 2015-2021 Rapptz
Copyright (c) 2021-present tag-epic

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import enum
from typing import Any, Dict, NamedTuple, Optional, Type, TypeVar

__all__ = (
    "Enum",
    "IntEnum",
    "StrEnum",
    "UnknownEnumValue",
    "ChannelType",
    "MessageType",
    "VoiceRegion",
    "SpeakingState",
    "VerificationLevel",
    "ContentFilter",
    "Status",
    "DefaultAvatar",
    "AuditLogAction",
    "AuditLogActionCategory",
    "UserFlags",
    "ActivityType",
    "NotificationLevel",
    "TeamMembershipState",
    "WebhookType",
    "ExpireBehaviour",
    "ExpireBehavior",
    "StickerType",
    "StickerFormatType",
    "InviteTarget",
    "Locale",
    "VideoQualityMode",
    "ComponentType",
    "ButtonStyle",
    "TextInputStyle",
    "StagePrivacyLevel",
    "InteractionType",
    "InteractionResponseType",
    "ApplicationCommandType",
    "ApplicationCommandOptionType",
    "NSFWLevel",
    "ScheduledEventEntityType",
    "ScheduledEventPrivacyLevel",
    "ScheduledEventStatus",
    "AutoModerationEventType",
    "AutoModerationTriggerType",
    "KeywordPresetType",
    "AutoModerationActionType",
    "SortOrderType",
)


class UnknownEnumValue(NamedTuple):
    """Proxy for the underlying name and value of an attribute not known to the Enum."""

    name: str
    value: Any

    def __str__(self):
        if isinstance(self.value, str):
            return self.value
        return self.name

    def __int__(self):
        if isinstance(self.value, int):
            return self.value
        raise TypeError(f"{self.name}.{self.value} cannot be converted to an int")

    def __repr__(self):
        return f"<{self.name}.{self.value!r}>"

    def __le__(self, other):
        try:
            return self.value <= other.value
        except AttributeError:
            return self.value <= other

    def __ge__(self, other):
        try:
            return self.value >= other.value
        except AttributeError:
            return self.value >= other

    def __lt__(self, other):
        try:
            return self.value < other.value
        except AttributeError:
            return self.value < other

    def __gt__(self, other):
        try:
            return self.value > other.value
        except AttributeError:
            return self.value > other

    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == other

    def __ne__(self, other):
        try:
            return self.value != other.value
        except AttributeError:
            return self.value != other

    def __hash__(self):
        return hash(self.value)


class Enum(enum.Enum):
    """An enum that supports trying for unknown values."""

    @classmethod
    def try_value(cls, value):
        try:
            return cls(value)
        except ValueError:
            return value


class IntEnum(int, Enum):
    """An enum that supports comparing and hashing as an int."""

    def __int__(self):
        return self.value


class StrEnum(str, Enum):
    """An enum that supports comparing and hashing as a string."""

    def __str__(self):
        return self.value


class ChannelType(IntEnum):
    """Specifies the type of channel.

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the channel type.

        .. describe:: int(x)

            Returns the value of the channel type.

        .. describe:: hash(x)

            Returns the hash of the channel type.

        .. describe:: x == y

            Checks if two channel types are equal.

        .. describe:: x != y

            Checks if two channel types are not equal.
    """

    text = 0
    """A text channel."""

    private = 1
    """A private text channel. Also called a direct message."""

    voice = 2
    """A voice channel."""

    group = 3
    """A private group text channel."""

    category = 4
    """A category channel."""

    news = 5
    """A guild news channel."""

    news_thread = 10
    """"A news thread.

    .. versionadded:: 2.0
    """

    public_thread = 11
    """A public thread.

    .. versionadded:: 2.0
    """

    private_thread = 12
    """A private thread.

    .. versionadded:: 2.0
    """

    stage_voice = 13
    """A guild stage voice channel.

    .. versionadded:: 1.7
    """

    guild_directory = 14
    """A channel containing the guilds in a `Student Hub`_

    .. _Student Hub: https://support.discord.com/hc/en-us/articles/4406046651927-Discord-Student-Hubs-FAQ

    .. versionadded:: 2.2
    """

    forum = 15
    """A forum channel.

    .. versionadded:: 2.1
    """

    def __str__(self):
        return self.name


class MessageType(IntEnum):
    """Specifies the type of :class:`Message`. This is used to denote if a message
    is to be interpreted as a system message or a regular message.

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the message type.

        .. describe:: int(x)

            Returns the value of the message type.

        .. describe:: hash(x)

            Returns the hash of the message type.

        .. describe:: x == y

            Checks if two message types are equal.

        .. describe:: x != y

            Checks if two message types are not equal.
    """

    default = 0
    """The default message type. This is the same as regular messages."""

    recipient_add = 1
    """The system message when a user is added to a group private
    message or a thread.
    """

    recipient_remove = 2
    """The system message when a user is removed from a group private
    message or a thread.
    """

    call = 3
    """The system message denoting call state, e.g. missed call, started call,
    etc.
    """

    channel_name_change = 4
    """The system message denoting that a channel's name has been changed."""

    channel_icon_change = 5
    """The system message denoting that a channel's icon has been changed."""

    pins_add = 6
    """"The system message denoting that a pinned message has been added to a channel."""

    new_member = 7
    """The system message denoting that a new member has joined a Guild."""

    premium_guild_subscription = 8
    """The system message denoting that a member has "nitro boosted" a guild."""

    premium_guild_tier_1 = 9
    """The system message denoting that a member has "nitro boosted" a guild
    and it achieved level 1.
    """

    premium_guild_tier_2 = 10
    """The system message denoting that a member has "nitro boosted" a guild
    and it achieved level 2.
    """

    premium_guild_tier_3 = 11
    """The system message denoting that a member has "nitro boosted" a guild
    and it achieved level 3.
    """

    channel_follow_add = 12
    """The system message denoting that an announcement channel has been followed.

    .. versionadded:: 1.3
    """

    guild_stream = 13
    """The system message denoting that a member is streaming in the guild.

    .. versionadded:: 1.7
    """

    guild_discovery_disqualified = 14
    """The system message denoting that the guild is no longer eligible for Server
    Discovery.

    .. versionadded:: 1.7
    """

    guild_discovery_requalified = 15
    """The system message denoting that the guild has become eligible again for Server
    Discovery.

    .. versionadded:: 1.7
    """

    guild_discovery_grace_period_initial_warning = 16
    """The system message denoting that the guild has failed to meet the Server
    Discovery requirements for one week.

    .. versionadded:: 1.7
    """

    guild_discovery_grace_period_final_warning = 17
    """The system message denoting that the guild has failed to meet the Server
    Discovery requirements for 3 weeks in a row.

    .. versionadded:: 1.7
    """

    thread_created = 18
    """The system message denoting that a thread has been created. This is only
    sent if the thread has been created from an older message. The period of time
    required for a message to be considered old cannot be relied upon and is up to
    Discord.

    .. versionadded:: 2.0
    """

    reply = 19
    """The system message denoting that the author is replying to a message.

    .. versionadded:: 2.0
    """

    chat_input_command = 20
    """The system message denoting that a slash command was executed.

    .. versionadded:: 2.0
    """

    thread_starter_message = 21
    """The system message denoting the message in the thread that is the one that started the
    thread's conversation topic.

    .. versionadded:: 2.0
    """

    guild_invite_reminder = 22
    """The system message sent as a reminder to invite people to the guild.

    .. versionadded:: 2.0
    """

    context_menu_command = 23
    """The system message denoting that a context menu command was executed.

    .. versionadded:: 2.0
    """

    auto_moderation_action = 24
    """The system message denoting that an auto moderation action was executed

    .. versionadded:: 2.1
    """


class VoiceRegion(StrEnum):
    us_west = "us-west"
    us_east = "us-east"
    us_south = "us-south"
    us_central = "us-central"
    eu_west = "eu-west"
    eu_central = "eu-central"
    singapore = "singapore"
    london = "london"
    sydney = "sydney"
    amsterdam = "amsterdam"
    frankfurt = "frankfurt"
    brazil = "brazil"
    hongkong = "hongkong"
    russia = "russia"
    japan = "japan"
    southafrica = "southafrica"
    south_korea = "south-korea"
    india = "india"
    europe = "europe"
    dubai = "dubai"
    vip_us_east = "vip-us-east"
    vip_us_west = "vip-us-west"
    vip_amsterdam = "vip-amsterdam"


class SpeakingState(IntEnum):
    none = 0
    voice = 1
    soundshare = 2
    priority = 4

    def __str__(self):
        return self.name


class VerificationLevel(IntEnum):
    none = 0
    low = 1
    medium = 2
    high = 3
    highest = 4

    def __str__(self):
        return self.name


class ContentFilter(IntEnum):
    disabled = 0
    no_role = 1
    all_members = 2

    def __str__(self):
        return self.name


class Status(StrEnum):
    online = "online"
    offline = "offline"
    idle = "idle"
    dnd = "dnd"
    do_not_disturb = "dnd"
    invisible = "invisible"


class DefaultAvatar(IntEnum):
    blurple = 0
    grey = 1
    gray = 1
    green = 2
    orange = 3
    red = 4

    def __str__(self):
        return self.name


class NotificationLevel(IntEnum):
    all_messages = 0
    only_mentions = 1


class AuditLogActionCategory(IntEnum):
    create = 1
    delete = 2
    update = 3


class AuditLogAction(IntEnum):
    # fmt: off
    guild_update                                = 1
    channel_create                              = 10
    channel_update                              = 11
    channel_delete                              = 12
    overwrite_create                            = 13
    overwrite_update                            = 14
    overwrite_delete                            = 15
    kick                                        = 20
    member_prune                                = 21
    ban                                         = 22
    unban                                       = 23
    member_update                               = 24
    member_role_update                          = 25
    member_move                                 = 26
    member_disconnect                           = 27
    bot_add                                     = 28
    role_create                                 = 30
    role_update                                 = 31
    role_delete                                 = 32
    invite_create                               = 40
    invite_update                               = 41
    invite_delete                               = 42
    webhook_create                              = 50
    webhook_update                              = 51
    webhook_delete                              = 52
    emoji_create                                = 60
    emoji_update                                = 61
    emoji_delete                                = 62
    message_delete                              = 72
    message_bulk_delete                         = 73
    message_pin                                 = 74
    message_unpin                               = 75
    integration_create                          = 80
    integration_update                          = 81
    integration_delete                          = 82
    stage_instance_create                       = 83
    stage_instance_update                       = 84
    stage_instance_delete                       = 85
    sticker_create                              = 90
    sticker_update                              = 91
    sticker_delete                              = 92
    scheduled_event_create                      = 100
    scheduled_event_update                      = 101
    scheduled_event_delete                      = 102
    thread_create                               = 110
    thread_update                               = 111
    thread_delete                               = 112
    auto_moderation_rule_create                 = 140
    auto_moderation_rule_update                 = 141
    auto_moderation_rule_delete                 = 142
    auto_moderation_block_message               = 143
    auto_moderation_flag_to_channel             = 144
    auto_moderation_user_communication_disabled = 145
    # fmt: on

    @property
    def category(self) -> Optional[AuditLogActionCategory]:
        # fmt: off
        lookup: Dict[AuditLogAction, Optional[AuditLogActionCategory]] = {
            AuditLogAction.guild_update:                                AuditLogActionCategory.update,
            AuditLogAction.channel_create:                              AuditLogActionCategory.create,
            AuditLogAction.channel_update:                              AuditLogActionCategory.update,
            AuditLogAction.channel_delete:                              AuditLogActionCategory.delete,
            AuditLogAction.overwrite_create:                            AuditLogActionCategory.create,
            AuditLogAction.overwrite_update:                            AuditLogActionCategory.update,
            AuditLogAction.overwrite_delete:                            AuditLogActionCategory.delete,
            AuditLogAction.kick:                                        None,
            AuditLogAction.member_prune:                                None,
            AuditLogAction.ban:                                         None,
            AuditLogAction.unban:                                       None,
            AuditLogAction.member_update:                               AuditLogActionCategory.update,
            AuditLogAction.member_role_update:                          AuditLogActionCategory.update,
            AuditLogAction.member_move:                                 None,
            AuditLogAction.member_disconnect:                           None,
            AuditLogAction.bot_add:                                     None,
            AuditLogAction.role_create:                                 AuditLogActionCategory.create,
            AuditLogAction.role_update:                                 AuditLogActionCategory.update,
            AuditLogAction.role_delete:                                 AuditLogActionCategory.delete,
            AuditLogAction.invite_create:                               AuditLogActionCategory.create,
            AuditLogAction.invite_update:                               AuditLogActionCategory.update,
            AuditLogAction.invite_delete:                               AuditLogActionCategory.delete,
            AuditLogAction.webhook_create:                              AuditLogActionCategory.create,
            AuditLogAction.webhook_update:                              AuditLogActionCategory.update,
            AuditLogAction.webhook_delete:                              AuditLogActionCategory.delete,
            AuditLogAction.emoji_create:                                AuditLogActionCategory.create,
            AuditLogAction.emoji_update:                                AuditLogActionCategory.update,
            AuditLogAction.emoji_delete:                                AuditLogActionCategory.delete,
            AuditLogAction.message_delete:                              AuditLogActionCategory.delete,
            AuditLogAction.message_bulk_delete:                         AuditLogActionCategory.delete,
            AuditLogAction.message_pin:                                 None,
            AuditLogAction.message_unpin:                               None,
            AuditLogAction.integration_create:                          AuditLogActionCategory.create,
            AuditLogAction.integration_update:                          AuditLogActionCategory.update,
            AuditLogAction.integration_delete:                          AuditLogActionCategory.delete,
            AuditLogAction.stage_instance_create:                       AuditLogActionCategory.create,
            AuditLogAction.stage_instance_update:                       AuditLogActionCategory.update,
            AuditLogAction.stage_instance_delete:                       AuditLogActionCategory.delete,
            AuditLogAction.sticker_create:                              AuditLogActionCategory.create,
            AuditLogAction.sticker_update:                              AuditLogActionCategory.update,
            AuditLogAction.sticker_delete:                              AuditLogActionCategory.delete,
            AuditLogAction.scheduled_event_create:                      AuditLogActionCategory.create,
            AuditLogAction.scheduled_event_update:                      AuditLogActionCategory.update,
            AuditLogAction.scheduled_event_delete:                      AuditLogActionCategory.delete,
            AuditLogAction.thread_create:                               AuditLogActionCategory.create,
            AuditLogAction.thread_update:                               AuditLogActionCategory.update,
            AuditLogAction.thread_delete:                               AuditLogActionCategory.delete,
            AuditLogAction.auto_moderation_rule_create:                 AuditLogActionCategory.create,
            AuditLogAction.auto_moderation_rule_update:                 AuditLogActionCategory.update,
            AuditLogAction.auto_moderation_rule_delete:                 AuditLogActionCategory.delete,
            AuditLogAction.auto_moderation_block_message:               None,
            AuditLogAction.auto_moderation_flag_to_channel:             None,
            AuditLogAction.auto_moderation_user_communication_disabled: None,
        }
        # fmt: on
        return lookup[self]

    @property
    def target_type(self) -> Optional[str]:
        v = self.value
        if v == -1:
            return "all"
        elif v < 10:
            return "guild"
        elif v < 20:
            return "channel"
        elif v < 30:
            return "user"
        elif v < 40:
            return "role"
        elif v < 50:
            return "invite"
        elif v < 60:
            return "webhook"
        elif v < 70:
            return "emoji"
        elif v == 73:
            return "channel"
        elif v < 80:
            return "message"
        elif v < 83:
            return "integration"
        elif v < 90:
            return "stage_instance"
        elif v < 93:
            return "sticker"
        elif v < 103:
            return "event"
        elif v < 113:
            return "thread"
        elif v < 122:
            return "application_command_or_integration"
        elif v < 140:
            return None
        elif v == 143:
            return "user"
        elif v < 143:
            return "auto_moderation_rule"
        else:
            return None


class UserFlags(IntEnum):
    """Represents Discord User flags.

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the user flag.

        .. describe:: int(x)

            Returns the value of the user flag.

        .. describe:: hash(x)

            Returns the hash of the user flag.

        .. describe:: x == y

            Checks if two user flags are equal.

        .. describe:: x != y

            Checks if two user flags are not equal.
    """

    staff = 1 << 0
    """The user is a Discord Employee."""

    partner = 1 << 1
    """The user is an owner of a Partnered Server."""

    hypesquad = 1 << 2
    """The user is a HypeSquad Events member."""

    bug_hunter = 1 << 3
    """The user is a Bug Hunter."""

    mfa_sms = 1 << 4
    """The user has SMS recovery for Multi Factor Authentication enabled."""

    premium_promo_dismissed = 1 << 5
    """The user has dismissed the Discord Nitro promotion."""

    hypesquad_bravery = 1 << 6
    """The user is a HypeSquad Bravery member."""

    hypesquad_brilliance = 1 << 7
    """The user is a HypeSquad Brilliance member."""

    hypesquad_balance = 1 << 8
    """The user is a HypeSquad Balance member."""

    early_supporter = 1 << 9
    """The user is an Early Nitro Supporter."""

    team_user = 1 << 10
    """The user is a Team User."""

    system = 1 << 12
    """The user is a system user (i.e. represents Discord officially)."""

    has_unread_urgent_messages = 1 << 13
    """The user has an unread system message."""

    bug_hunter_level_2 = 1 << 14
    """The user is a Bug Hunter Level 2."""

    verified_bot = 1 << 16
    """The user is a Verified Bot."""

    verified_bot_developer = 1 << 17
    """The user is an Early Verified Bot Developer."""

    discord_certified_moderator = 1 << 18
    """The user is a Discord Certified Moderator."""

    known_spammer = 1 << 20
    """The user is a Known Spammer."""

    active_developer = 1 << 22
    """The user is an Active Developer.

    .. versionadded:: 2.4
    """


class ActivityType(IntEnum):
    """Specifies the type of :class:`Activity`. This is used to check how to
    interpret the activity itself.

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the activity type.

        .. describe:: int(x)

            Returns the value of the activity type.

        .. describe:: hash(x)

            Returns the hash of the activity type.

        .. describe:: x == y

            Checks if two activity types are equal.

        .. describe:: x != y

            Checks if two activity types are not equal.
    """

    unknown = -1
    """An unknown activity type. This should generally not happen."""

    playing = 0
    """A "Playing" activity type."""

    streaming = 1
    """A "Streaming" activity type."""

    listening = 2
    """A "Listening" activity type."""

    watching = 3
    """A "Watching" activity type."""

    custom = 4
    """A custom activity type."""

    competing = 5
    """A competing activity type.

    .. versionadded:: 1.5
    """


class TeamMembershipState(IntEnum):
    invited = 1
    accepted = 2


class WebhookType(IntEnum):
    incoming = 1
    channel_follower = 2
    application = 3


class ExpireBehaviour(IntEnum):
    remove_role = 0
    kick = 1


ExpireBehavior = ExpireBehaviour


class StickerType(IntEnum):
    standard = 1
    guild = 2


class StickerFormatType(IntEnum):
    png = 1
    apng = 2
    lottie = 3

    @property
    def file_extension(self) -> str:
        # fmt: off
        lookup: Dict[StickerFormatType, str] = {
            StickerFormatType.png: 'png',
            StickerFormatType.apng: 'png',
            StickerFormatType.lottie: 'json',
        }
        # fmt: on
        return lookup[self]


class InviteTarget(IntEnum):
    unknown = 0
    stream = 1
    embedded_application = 2


class InteractionType(IntEnum):
    """Specifies the type of :class:`Interaction`.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the interaction type.

        .. describe:: int(x)

            Returns the value of the interaction type.

        .. describe:: hash(x)

            Returns the hash of the interaction type.

        .. describe:: x == y

            Checks if two interaction types are equal.

        .. describe:: x != y

            Checks if two interaction types are not equal.
    """

    ping = 1
    """Represents Discord pinging to see if the interaction response server is alive."""

    application_command = 2
    """Represents a slash command or context menu interaction."""

    component = 3
    """Represents a component based interaction, i.e. using the Discord Bot UI Kit."""

    application_command_autocomplete = 4
    """Represents a slash command autocomplete interaction."""

    modal_submit = 5
    """Represents a modal submit interaction."""


class InteractionResponseType(IntEnum):
    """Specifies the response type for the interaction.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the interaction response type.

        .. describe:: int(x)

            Returns the value of the interaction response type.

        .. describe:: hash(x)

            Returns the hash of the interaction response type.

        .. describe:: x == y

            Checks if two interaction response types are equal.

        .. describe:: x != y

            Checks if two interaction response types are not equal.
    """

    pong = 1
    """Pongs the interaction when given a ping.

    See also :meth:`InteractionResponse.pong`
    """

    # ack = 2 (deprecated)
    # channel_message = 3 (deprecated)
    channel_message = 4  # (with source)
    """Respond to the interaction with a message.

    See also :meth:`InteractionResponse.send_message`
    """

    deferred_channel_message = 5  # (with source)
    """Responds to the interaction with a message at a later time.

    See also :meth:`InteractionResponse.defer`
    """

    deferred_message_update = 6  # for components
    """Acknowledges the component interaction with a promise that
    the message will update later (though there is no need to actually update the message).

    See also :meth:`InteractionResponse.defer`
    """

    message_update = 7  # for components
    """Responds to the interaction by editing the message.

    See also :meth:`InteractionResponse.edit_message`
    """

    application_command_autocomplete_result = 8
    """Responds to the interaction with an autocomplete result containing suggested choices.

    See also :meth:`InteractionResponse.send_autocomplete`
    """

    modal = 9
    """Responds to the interaction with a modal.

    See also :meth:`InteractionResponse.send_modal`
    """


class ApplicationCommandType(IntEnum):
    chat_input = 1
    user = 2
    message = 3


class ApplicationCommandOptionType(IntEnum):
    sub_command = 1
    sub_command_group = 2
    string = 3
    integer = 4
    boolean = 5
    user = 6
    channel = 7
    role = 8
    mentionable = 9
    number = 10  # A double, AKA floating point.
    attachment = 11


class Locale(StrEnum):
    da = "da"
    """Danish | Dansk"""
    de = "de"
    """German | Deutsch"""
    en_GB = "en-GB"
    """English, UK | English, UK"""
    en_US = "en-US"
    """English, US | English, US"""
    es_ES = "es-ES"
    """Spanish | Español"""
    fr = "fr"
    """French | Français"""
    hr = "hr"
    """Croatian | Hrvatski"""
    it = "it"
    """Italian | Italiano"""
    lt = "lt"
    """Lithuanian | Lietuviškai"""
    hu = "hu"
    """Hungarian | Magyar"""
    nl = "nl"
    """Dutch | Nederlands"""
    no = "no"
    """Norwegian | Norsk"""
    pl = "pl"
    """Polish | Polski"""
    pt_BR = "pt-BR"
    """Portuguese, Brazilian | Português do Brasil"""
    ro = "ro"
    """Romanian, Romania | Română"""
    fi = "fi"
    """Finnish | Suomi"""
    sv_SE = "sv-SE"
    """Swedish | Svenska"""
    vi = "vi"
    """Vietnamese | Tiếng Việt"""
    tr = "tr"
    """Turkish | Türkçe"""
    cs = "cs"
    """Czech | Čeština"""
    el = "el"
    """Greek | Ελληνικά"""
    bg = "bg"
    """Bulgarian | български"""
    ru = "ru"
    """Russian | Pусский"""
    uk = "uk"
    """Ukrainian | Українська"""
    hi = "hi"
    """Hindi | हिन्दी"""
    th = "th"
    """Thai	| ไทย"""
    zh_CN = "zh-CN"
    """Chinese, China | 中文"""
    ja = "ja"
    """Japanese | 日本語"""
    zh_TW = "zh-TW"
    """Chinese, Taiwan | 繁體中文"""
    ko = "ko"
    """Korean | 한국어"""


class VideoQualityMode(IntEnum):
    auto = 1
    full = 2


class ComponentType(IntEnum):
    """Represents the type of a component.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: str(x)

            Returns the name of the component type.

        .. describe:: int(x)

            Returns the value of the component type.

        .. describe:: hash(x)

            Returns the hash of the component type.

        .. describe:: x == y

            Checks if two component types are equal.

        .. describe:: x != y

            Checks if two component types are not equal.
    """

    action_row = 1
    """Represents the group component which holds different components in a row."""

    button = 2
    """Represents a button component."""

    select = 3
    """Alias for :attr:`.string_select`."""

    string_select = 3
    """Represents a string select component."""

    text_input = 4
    """Represents a text input component."""

    user_select = 5
    """Represents a user select component.

    .. versionadded:: 2.3
    """

    role_select = 6
    """Represents a role select component.

    .. versionadded:: 2.3
    """

    mentionable_select = 7
    """Represents a mentionable select component.

    .. versionadded:: 2.3
    """

    channel_select = 8
    """Represents a channel select component.

    .. versionadded:: 2.3
    """


class ButtonStyle(IntEnum):
    primary = 1
    secondary = 2
    success = 3
    danger = 4
    link = 5

    # Aliases
    blurple = 1
    grey = 2
    gray = 2
    green = 3
    red = 4
    url = 5


class TextInputStyle(IntEnum):
    short = 1
    paragraph = 2


class StagePrivacyLevel(IntEnum):
    public = 1
    closed = 2
    guild_only = 2


class NSFWLevel(IntEnum):
    default = 0
    explicit = 1
    safe = 2
    age_restricted = 3


class ScheduledEventEntityType(IntEnum):
    stage_instance = 1
    voice = 2
    external = 3


class ScheduledEventPrivacyLevel(IntEnum):
    guild_only = 2


class ScheduledEventStatus(IntEnum):
    scheduled = 1
    active = 2
    completed = 3
    canceled = 4
    cancelled = 4


class AutoModerationEventType(IntEnum):
    message_send = 1


class AutoModerationTriggerType(IntEnum):
    keyword = 1
    spam = 3
    keyword_preset = 4
    mention_spam = 5


class KeywordPresetType(IntEnum):
    profanity = 1
    sexual_content = 2
    slurs = 3


class AutoModerationActionType(IntEnum):
    block_message = 1
    send_alert_message = 2
    timeout = 3


class SortOrderType(IntEnum):
    latest_activity = 0
    creation_date = 1


T = TypeVar("T")


def try_enum(cls: Type[T], val: Any) -> T:
    """A function that tries to turn the value into enum ``cls``.

    If it fails it returns a proxy invalid value instead.
    """

    try:
        return cls(val)
    except ValueError:
        return UnknownEnumValue(name=f"unknown_{val}", value=val)  # type: ignore
