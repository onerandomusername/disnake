.. currentmodule:: disnake

API Reference
===============

The following section outlines the API of disnake.

.. note::

    This module uses the Python logging module to log diagnostic and errors
    in an output independent way.  If the logging module is not configured,
    these logs will not be output anywhere.  See :ref:`logging_setup` for
    more information on how to set up and use the logging module with
    disnake.

.. toctree::
    :titlesonly:
    :glob:

    *


Version Related Info
---------------------

There are two main ways to query version information about the library. For guarantees, check :ref:`version_guarantees`.

.. data:: version_info

    A named tuple that is similar to :obj:`py:sys.version_info`.

    Just like :obj:`py:sys.version_info` the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

.. data:: __version__

    A string representation of the version. e.g. ``'1.0.0rc1'``. This is based
    off of :pep:`440`.

Clients
--------

Client
~~~~~~~

.. attributetable:: Client

.. autoclass:: Client
    :members:
    :exclude-members: fetch_guilds, event

    .. automethod:: Client.event()
        :decorator:

    .. automethod:: Client.fetch_guilds
        :async-for:

AutoShardedClient
~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoShardedClient

.. autoclass:: AutoShardedClient
    :members:

Application Info
------------------

AppInfo
~~~~~~~~

.. attributetable:: AppInfo

.. autoclass:: AppInfo()
    :members:

PartialAppInfo
~~~~~~~~~~~~~~~

.. attributetable:: PartialAppInfo

.. autoclass:: PartialAppInfo()
    :members:

Team
~~~~~

.. attributetable:: Team

.. autoclass:: Team()
    :members:

TeamMember
~~~~~~~~~~~

.. attributetable:: TeamMember

.. autoclass:: TeamMember()
    :members:

InstallParams
~~~~~~~~~~~~~

.. attributetable:: InstallParams

.. autoclass:: InstallParams()
    :members:

Voice Related
---------------

VoiceClient
~~~~~~~~~~~~

.. attributetable:: VoiceClient

.. autoclass:: VoiceClient()
    :members:
    :exclude-members: connect, on_voice_state_update, on_voice_server_update

VoiceProtocol
~~~~~~~~~~~~~~~

.. attributetable:: VoiceProtocol

.. autoclass:: VoiceProtocol
    :members:

AudioSource
~~~~~~~~~~~~

.. attributetable:: AudioSource

.. autoclass:: AudioSource
    :members:

PCMAudio
~~~~~~~~~

.. attributetable:: PCMAudio

.. autoclass:: PCMAudio
    :members:

FFmpegAudio
~~~~~~~~~~~~

.. attributetable:: FFmpegAudio

.. autoclass:: FFmpegAudio
    :members:

FFmpegPCMAudio
~~~~~~~~~~~~~~~

.. attributetable:: FFmpegPCMAudio

.. autoclass:: FFmpegPCMAudio
    :members:

FFmpegOpusAudio
~~~~~~~~~~~~~~~~

.. attributetable:: FFmpegOpusAudio

.. autoclass:: FFmpegOpusAudio
    :members:

PCMVolumeTransformer
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: PCMVolumeTransformer

.. autoclass:: PCMVolumeTransformer
    :members:

Opus Library
~~~~~~~~~~~~~

.. autofunction:: disnake.opus.load_opus

.. autofunction:: disnake.opus.is_loaded



Async Iterator
----------------

Some API functions return an "async iterator". An async iterator is something that is
capable of being used in an :ref:`async for statement <py:async for>`.

These async iterators can be used as follows: ::

    async for elem in channel.history():
        # do stuff with elem here

Certain utilities make working with async iterators easier, detailed below.

.. class:: AsyncIterator

    Represents the "AsyncIterator" concept. Note that no such class exists,
    it is purely abstract.

    .. container:: operations

        .. describe:: async for x in y

            Iterates over the contents of the async iterator.


    .. method:: next()
        :async:

        |coro|

        Advances the iterator by one, if possible. If no more items are found
        then this raises :exc:`NoMoreItems`.

    .. method:: get(**attrs)
        :async:

        |coro|

        Similar to :func:`utils.get` except run over the async iterator.

        Getting the last message by a user named 'Dave' or ``None``: ::

            msg = await channel.history().get(author__name='Dave')

    .. method:: find(predicate)
        :async:

        |coro|

        Similar to :func:`utils.find` except run over the async iterator.

        Unlike :func:`utils.find`\, the predicate provided can be a
        |coroutine_link|_.

        Getting the last audit log with a reason or ``None``: ::

            def predicate(event):
                return event.reason is not None

            event = await guild.audit_logs().find(predicate)

        :param predicate: The predicate to use. Could be a |coroutine_link|_.
        :return: The first element that returns ``True`` for the predicate or ``None``.

    .. method:: flatten()
        :async:

        |coro|

        Flattens the async iterator into a :class:`list` with all the elements.

        :return: A list of every element in the async iterator.
        :rtype: list

    .. method:: chunk(max_size)

        Collects items into chunks of up to a given maximum size.
        Another :class:`AsyncIterator` is returned which collects items into
        :class:`list`\s of a given size. The maximum chunk size must be a positive integer.

        .. versionadded:: 1.6

        Collecting groups of users: ::

            async for leader, *users in reaction.users().chunk(3):
                ...

        .. warning::

            The last chunk collected may not be as large as ``max_size``.

        :param max_size: The size of individual chunks.
        :rtype: :class:`AsyncIterator`

    .. method:: map(func)

        This is similar to the built-in :func:`map <py:map>` function. Another
        :class:`AsyncIterator` is returned that executes the function on
        every element it is iterating over. This function can either be a
        regular function or a |coroutine_link|_.

        Creating a content iterator: ::

            def transform(message):
                return message.content

            async for content in channel.history().map(transform):
                message_length = len(content)

        :param func: The function to call on every element. Could be a |coroutine_link|_.
        :rtype: :class:`AsyncIterator`

    .. method:: filter(predicate)

        This is similar to the built-in :func:`filter <py:filter>` function. Another
        :class:`AsyncIterator` is returned that filters over the original
        async iterator. This predicate can be a regular function or a |coroutine_link|_.

        Getting messages by non-bot accounts: ::

            def predicate(message):
                return not message.author.bot

            async for elem in channel.history().filter(predicate):
                ...

        :param predicate: The predicate to call on every element. Could be a |coroutine_link|_.
        :rtype: :class:`AsyncIterator`

.. _discord-api-audit-logs:

Audit Log Data
----------------

Working with :meth:`Guild.audit_logs` is a complicated process with a lot of machinery
involved. The library attempts to make it easy to use and friendly. In order to accomplish
this goal, it must make use of a couple of data classes that aid in this goal.

AuditLogEntry
~~~~~~~~~~~~~~~

.. attributetable:: AuditLogEntry

.. autoclass:: AuditLogEntry
    :members:

AuditLogChanges
~~~~~~~~~~~~~~~~~

.. attributetable:: AuditLogChanges

.. class:: AuditLogChanges

    An audit log change set.

    .. attribute:: before

        The old value. The attribute has the type of :class:`AuditLogDiff`.

        Depending on the :class:`AuditLogActionCategory` retrieved by
        :attr:`~AuditLogEntry.category`\, the data retrieved by this
        attribute differs:

        +----------------------------------------+---------------------------------------------------+
        |                Category                |                    Description                    |
        +----------------------------------------+---------------------------------------------------+
        | :attr:`~AuditLogActionCategory.create` | All attributes are set to ``None``.               |
        +----------------------------------------+---------------------------------------------------+
        | :attr:`~AuditLogActionCategory.delete` | All attributes are set the value before deletion. |
        +----------------------------------------+---------------------------------------------------+
        | :attr:`~AuditLogActionCategory.update` | All attributes are set the value before updating. |
        +----------------------------------------+---------------------------------------------------+
        | ``None``                               | No attributes are set.                            |
        +----------------------------------------+---------------------------------------------------+

    .. attribute:: after

        The new value. The attribute has the type of :class:`AuditLogDiff`.

        Depending on the :class:`AuditLogActionCategory` retrieved by
        :attr:`~AuditLogEntry.category`\, the data retrieved by this
        attribute differs:

        +----------------------------------------+--------------------------------------------------+
        |                Category                |                   Description                    |
        +----------------------------------------+--------------------------------------------------+
        | :attr:`~AuditLogActionCategory.create` | All attributes are set to the created value      |
        +----------------------------------------+--------------------------------------------------+
        | :attr:`~AuditLogActionCategory.delete` | All attributes are set to ``None``               |
        +----------------------------------------+--------------------------------------------------+
        | :attr:`~AuditLogActionCategory.update` | All attributes are set the value after updating. |
        +----------------------------------------+--------------------------------------------------+
        | ``None``                               | No attributes are set.                           |
        +----------------------------------------+--------------------------------------------------+

AuditLogDiff
~~~~~~~~~~~~~

.. attributetable:: AuditLogDiff

.. class:: AuditLogDiff

    Represents an audit log "change" object. A change object has dynamic
    attributes that depend on the type of action being done. Certain actions
    map to certain attributes being set.

    Note that accessing an attribute that does not match the specified action
    will lead to an attribute error.

    To get a list of attributes that have been set, you can iterate over
    them. To see a list of all possible attributes that could be set based
    on the action being done, check the documentation for :class:`AuditLogAction`,
    otherwise check the documentation below for all attributes that are possible.

    .. container:: operations

        .. describe:: iter(diff)

            Returns an iterator over (attribute, value) tuple of this diff.

    .. attribute:: name

        A name of something.

        :type: :class:`str`

    .. attribute:: icon

        A guild's or role's icon.

        See also :attr:`Guild.icon` or :attr:`Role.icon`.

        :type: :class:`Asset`

    .. attribute:: splash

        The guild's invite splash. See also :attr:`Guild.splash`.

        :type: :class:`Asset`

    .. attribute:: discovery_splash

        The guild's discovery splash. See also :attr:`Guild.discovery_splash`.

        :type: :class:`Asset`

    .. attribute:: banner

        The guild's banner. See also :attr:`Guild.banner`.

        :type: :class:`Asset`

    .. attribute:: owner

        The guild's owner. See also :attr:`Guild.owner`

        :type: Union[:class:`Member`, :class:`User`]

    .. attribute:: region

        The guild's voice region. See also :attr:`Guild.region`.

        :type: :class:`str`

    .. attribute:: afk_channel

        The guild's AFK channel.

        If this could not be found, then it falls back to a :class:`Object`
        with the ID being set.

        See :attr:`Guild.afk_channel`.

        :type: Union[:class:`VoiceChannel`, :class:`Object`]

    .. attribute:: system_channel

        The guild's system channel.

        If this could not be found, then it falls back to a :class:`Object`
        with the ID being set.

        See :attr:`Guild.system_channel`.

        :type: Union[:class:`TextChannel`, :class:`Object`]


    .. attribute:: rules_channel

        The guild's rules channel.

        If this could not be found then it falls back to a :class:`Object`
        with the ID being set.

        See :attr:`Guild.rules_channel`.

        :type: Union[:class:`TextChannel`, :class:`Object`]


    .. attribute:: public_updates_channel

        The guild's public updates channel.

        If this could not be found then it falls back to a :class:`Object`
        with the ID being set.

        See :attr:`Guild.public_updates_channel`.

        :type: Union[:class:`TextChannel`, :class:`Object`]

    .. attribute:: afk_timeout

        The guild's AFK timeout. See :attr:`Guild.afk_timeout`.

        :type: :class:`int`

    .. attribute:: mfa_level

        The guild's MFA level. See :attr:`Guild.mfa_level`.

        :type: :class:`int`

    .. attribute:: widget_enabled

        The guild's widget has been enabled or disabled.

        :type: :class:`bool`

    .. attribute:: widget_channel

        The widget's channel.

        If this could not be found then it falls back to a :class:`Object`
        with the ID being set.

        :type: Union[:class:`abc.GuildChannel`, :class:`Object`]

    .. attribute:: verification_level

        The guild's verification level.

        See also :attr:`Guild.verification_level`.

        :type: :class:`VerificationLevel`

    .. attribute:: premium_progress_bar_enabled

        Whether the guild's premium progress bar is enabled.

        See also :attr:`Guild.premium_progress_bar_enabled`.

        :type: :class:`bool`

    .. attribute:: default_notifications

        The guild's default notification level.

        See also :attr:`Guild.default_notifications`.

        :type: :class:`NotificationLevel`

    .. attribute:: explicit_content_filter

        The guild's content filter.

        See also :attr:`Guild.explicit_content_filter`.

        :type: :class:`ContentFilter`

    .. attribute:: default_message_notifications

        The guild's default message notification setting.

        :type: :class:`int`

    .. attribute:: vanity_url_code

        The guild's vanity URL code.

        See also :meth:`Guild.vanity_invite`, :meth:`Guild.edit`, and :attr:`Guild.vanity_url_code`.

        :type: :class:`str`

    .. attribute:: preferred_locale

        The guild's preferred locale.

        :type: :class:`Locale`

    .. attribute:: position

        The position of a :class:`Role` or :class:`abc.GuildChannel`.

        :type: :class:`int`

    .. attribute:: type

        The type of channel/thread, sticker, webhook, integration (:class:`str`), or permission overwrite (:class:`int`).

        :type: Union[:class:`ChannelType`, :class:`StickerType`, :class:`WebhookType`, :class:`str`, :class:`int`]

    .. attribute:: topic

        The topic of a :class:`TextChannel`, :class:`StageChannel`, :class:`StageInstance` or :class:`ForumChannel`.

        See also :attr:`TextChannel.topic`, :attr:`StageChannel.topic`,
        :attr:`StageInstance.topic` or :attr:`ForumChannel.topic`.

        :type: :class:`str`

    .. attribute:: bitrate

        The bitrate of a :class:`VoiceChannel` or :class:`StageChannel`.

        See also :attr:`VoiceChannel.bitrate` or :attr:`StageChannel.bitrate`.

        :type: :class:`int`

    .. attribute:: overwrites

        A list of permission overwrite tuples that represents a target and a
        :class:`PermissionOverwrite` for said target.

        The first element is the object being targeted, which can either
        be a :class:`Member` or :class:`User` or :class:`Role`. If this object
        is not found then it is a :class:`Object` with an ID being filled and
        a ``type`` attribute set to either ``'role'`` or ``'member'`` to help
        decide what type of ID it is.

        :type: List[Tuple[Union[:class:`Member`, :class:`User`, :class:`Role`, :class:`Object`], :class:`PermissionOverwrite`]]

    .. attribute:: privacy_level

        The privacy level of the stage instance or guild scheduled event.

        :type: Union[:class:`StagePrivacyLevel`, :class:`GuildScheduledEventPrivacyLevel`]

    .. attribute:: roles

        A list of roles being added or removed from a member.

        If a role is not found then it is a :class:`Object` with the ID and name being
        filled in.

        :type: List[Union[:class:`Role`, :class:`Object`]]

    .. attribute:: nick

        The nickname of a member.

        See also :attr:`Member.nick`

        :type: Optional[:class:`str`]

    .. attribute:: deaf

        Whether the member is being server deafened.

        See also :attr:`VoiceState.deaf`.

        :type: :class:`bool`

    .. attribute:: mute

        Whether the member is being server muted.

        See also :attr:`VoiceState.mute`.

        :type: :class:`bool`

    .. attribute:: permissions

        The permissions of a role.

        See also :attr:`Role.permissions`.

        :type: :class:`Permissions`

    .. attribute:: colour
                   color

        The colour of a role.

        See also :attr:`Role.colour`

        :type: :class:`Colour`

    .. attribute:: hoist

        Whether the role is being hoisted or not.

        See also :attr:`Role.hoist`

        :type: :class:`bool`

    .. attribute:: mentionable

        Whether the role is mentionable or not.

        See also :attr:`Role.mentionable`

        :type: :class:`bool`

    .. attribute:: code

        The invite's code.

        See also :attr:`Invite.code`

        :type: :class:`str`

    .. attribute:: channel

        A guild channel.

        If the channel is not found then it is a :class:`Object` with the ID
        being set. In some cases the channel name is also set.

        :type: Union[:class:`abc.GuildChannel`, :class:`Object`]

    .. attribute:: inviter

        The user who created the invite.

        See also :attr:`Invite.inviter`.

        :type: Optional[:class:`User`]

    .. attribute:: max_uses

        The invite's max uses.

        See also :attr:`Invite.max_uses`.

        :type: :class:`int`

    .. attribute:: uses

        The invite's current uses.

        See also :attr:`Invite.uses`.

        :type: :class:`int`

    .. attribute:: max_age

        The invite's max age in seconds.

        See also :attr:`Invite.max_age`.

        :type: :class:`int`

    .. attribute:: temporary

        If the invite is a temporary invite.

        See also :attr:`Invite.temporary`.

        :type: :class:`bool`

    .. attribute:: allow
                   deny

        The permissions being allowed or denied.

        :type: :class:`Permissions`

    .. attribute:: id

        The ID of the object being changed.

        :type: :class:`int`

    .. attribute:: avatar

        The avatar of a member.

        See also :attr:`User.avatar`.

        :type: :class:`Asset`

    .. attribute:: slowmode_delay

        The number of seconds members have to wait before
        sending another message or creating another thread in the channel.

        See also :attr:`TextChannel.slowmode_delay`, :attr:`VoiceChannel.slowmode_delay`,
        :attr:`ForumChannel.slowmode_delay` or :attr:`Thread.slowmode_delay`.

        :type: :class:`int`

    .. attribute:: rtc_region

        The region for the voice or stage channel's voice communication.
        A value of ``None`` indicates automatic voice region detection.

        See also :attr:`VoiceChannel.rtc_region` or :attr:`StageChannel.rtc_region`.

        :type: :class:`str`

    .. attribute:: video_quality_mode

        The camera video quality for the voice or stage channel's participants.

        See also :attr:`VoiceChannel.video_quality_mode` or :attr:`StageChannel.video_quality_mode`.

        :type: :class:`VideoQualityMode`

    .. attribute:: user_limit

        The voice channel's user limit.

        See also :attr:`VoiceChannel.user_limit`.

        :type: :class:`int`

    .. attribute:: nsfw

        Whether the channel is marked as "not safe for work".

        See also :attr:`TextChannel.nsfw`, :attr:`VoiceChannel.nsfw` or :attr:`ForumChannel.nsfw`.

        :type: :class:`bool`

    .. attribute:: format_type

        The format type of a sticker being changed.

        See also :attr:`GuildSticker.format`

        :type: :class:`StickerFormatType`

    .. attribute:: emoji

        The name of the sticker's or role's emoji being changed.

        See also :attr:`GuildSticker.emoji` or :attr:`Role.emoji`.

        :type: :class:`str`

    .. attribute:: description

        The description of a guild, sticker or a guild scheduled event being changed.

        See also :attr:`Guild.description`, :attr:`GuildSticker.description`, :attr:`GuildScheduledEvent.description`

        :type: :class:`str`

    .. attribute:: available

        The availability of a sticker being changed.

        See also :attr:`GuildSticker.available`

        :type: :class:`bool`

    .. attribute:: archived

        The thread is now archived.

        :type: :class:`bool`

    .. attribute:: locked

        The thread is being locked or unlocked.

        :type: :class:`bool`

    .. attribute:: auto_archive_duration

        The thread's auto archive duration being changed.

        See also :attr:`Thread.auto_archive_duration`

        :type: :class:`int`

    .. attribute:: default_auto_archive_duration

        The default auto archive duration for newly created threads being changed.

        :type: :class:`int`

    .. attribute:: invitable

        Whether non-moderators can add other non-moderators to the thread.

        :type: :class:`bool`

    .. attribute:: timeout

        The datetime when the timeout expires, if any.

        :type: :class:`datetime.datetime`

    .. attribute:: entity_type

        The entity type of a guild scheduled event being changed.

        :type: :class:`GuildScheduledEventEntityType`

    .. attribute:: location

        The location of a guild scheduled event being changed.

        :type: :class:`str`

    .. attribute:: status

        The status of a guild scheduled event being changed.

        :type: :class:`GuildScheduledEventStatus`

    .. attribute:: image

        The cover image of a guild scheduled event being changed.

        :type: :class:`Asset`

    .. attribute:: command_permissions

        A mapping of target ID to guild permissions of an application command.

        Note that only changed permission entries are included,
        not necessarily all of the command's permissions.

        :type: Dict[:class:`int`, :class:`ApplicationCommandPermissions`]

    .. attribute:: application_id

        The ID of the application that created a webhook.

        :type: :class:`int`

    .. attribute:: flags

        The channel's flags.

        See also :attr:`abc.GuildChannel.flags` or :attr:`Thread.flags`.

        :type: :class:`ChannelFlags`

    .. attribute:: system_channel_flags

        The guild's system channel settings.

        See also :attr:`Guild.system_channel_flags`.

        :type: :class:`SystemChannelFlags`

    .. attribute:: enabled

        Whether something was enabled or disabled.

        :type: :class:`bool`

    .. attribute:: trigger_type

        The trigger type of an auto moderation rule being changed.

        :type: :class:`AutoModTriggerType`

    .. attribute:: event_type

        The event type of an auto moderation rule being changed.

        :type: :class:`AutoModEventType`

    .. attribute:: actions

        The list of actions of an auto moderation rule being changed.

        :type: List[:class:`AutoModAction`]

    .. attribute:: trigger_metadata

        The additional trigger metadata of an auto moderation rule being changed.

        :type: :class:`AutoModTriggerMetadata`

    .. attribute:: exempt_roles

        The list of roles that are exempt from an auto moderation rule being changed.

        If a role is not found then it is an :class:`Object` with the ID being set.

        :type: List[Union[:class:`Role`, :class:`Object`]]

    .. attribute:: exempt_channels

        The list of channels that are exempt from an auto moderation rule being changed.

        If a channel is not found then it is an :class:`Object` with the ID being set.

        :type: List[Union[:class:`abc.GuildChannel`, :class:`Object`]]

Webhook Support
------------------

disnake offers support for creating, editing, and executing webhooks through the :class:`Webhook` class.

Webhook
~~~~~~~~~

.. attributetable:: Webhook

.. autoclass:: Webhook()
    :members:
    :inherited-members:

WebhookMessage
~~~~~~~~~~~~~~~~

.. attributetable:: WebhookMessage

.. autoclass:: WebhookMessage()
    :members:

SyncWebhook
~~~~~~~~~~~~

.. attributetable:: SyncWebhook

.. autoclass:: SyncWebhook()
    :members:
    :inherited-members:

SyncWebhookMessage
~~~~~~~~~~~~~~~~~~~

.. attributetable:: SyncWebhookMessage

.. autoclass:: SyncWebhookMessage()
    :members:

.. _discord_api_abcs:

Abstract Base Classes
-----------------------

An :term:`abstract base class` (also known as an ``abc``) is a class that models can inherit
to get their behaviour. **Abstract base classes should not be instantiated**.
They are mainly there for usage with :func:`isinstance` and :func:`issubclass`\.

This library has a module related to abstract base classes, in which all the ABCs are subclasses of
:class:`typing.Protocol`.

Snowflake
~~~~~~~~~~

.. attributetable:: disnake.abc.Snowflake

.. autoclass:: disnake.abc.Snowflake()
    :members:

User
~~~~~

.. attributetable:: disnake.abc.User

.. autoclass:: disnake.abc.User()
    :members:

PrivateChannel
~~~~~~~~~~~~~~~

.. attributetable:: disnake.abc.PrivateChannel

.. autoclass:: disnake.abc.PrivateChannel()
    :members:

GuildChannel
~~~~~~~~~~~~~

.. attributetable:: disnake.abc.GuildChannel

.. autoclass:: disnake.abc.GuildChannel()
    :members:

Messageable
~~~~~~~~~~~~

.. attributetable:: disnake.abc.Messageable

.. autoclass:: disnake.abc.Messageable()
    :members:
    :exclude-members: history, typing

    .. automethod:: disnake.abc.Messageable.history
        :async-for:

    .. automethod:: disnake.abc.Messageable.typing
        :async-with:

Connectable
~~~~~~~~~~~~

.. attributetable:: disnake.abc.Connectable

.. autoclass:: disnake.abc.Connectable()



Localization
------------

The library uses the following types/methods to support localization.

Localized
~~~~~~~~~

.. autoclass:: Localized
    :members:
    :inherited-members:

LocalizationValue
~~~~~~~~~~~~~~~~~

.. autoclass:: LocalizationValue
    :members:
    :inherited-members:

LocalizationProtocol
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: LocalizationProtocol
    :members:

LocalizationStore
~~~~~~~~~~~~~~~~~~

.. autoclass:: LocalizationStore
    :members:
    :inherited-members:


Exceptions
------------

The following exceptions are thrown by the library.

.. autoexception:: DiscordException

.. autoexception:: ClientException

.. autoexception:: LoginFailure

.. autoexception:: NoMoreItems

.. autoexception:: HTTPException
    :members:

.. autoexception:: Forbidden

.. autoexception:: NotFound

.. autoexception:: DiscordServerError

.. autoexception:: InvalidData

.. autoexception:: WebhookTokenMissing

.. autoexception:: GatewayNotFound

.. autoexception:: ConnectionClosed

.. autoexception:: PrivilegedIntentsRequired

.. autoexception:: SessionStartLimitReached

.. autoexception:: InteractionException

.. autoexception:: InteractionResponded

.. autoexception:: InteractionNotResponded

.. autoexception:: InteractionTimedOut

.. autoexception:: ModalChainNotSupported

.. autoexception:: LocalizationKeyError

.. autoexception:: disnake.opus.OpusError

.. autoexception:: disnake.opus.OpusNotLoaded

Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`Exception`
        - :exc:`DiscordException`
            - :exc:`ClientException`
                - :exc:`InvalidData`
                - :exc:`LoginFailure`
                - :exc:`ConnectionClosed`
                - :exc:`PrivilegedIntentsRequired`
                - :exc:`SessionStartLimitReached`
                - :exc:`InteractionException`
                    - :exc:`InteractionResponded`
                    - :exc:`InteractionNotResponded`
                    - :exc:`InteractionTimedOut`
                    - :exc:`ModalChainNotSupported`
            - :exc:`NoMoreItems`
            - :exc:`GatewayNotFound`
            - :exc:`HTTPException`
                - :exc:`Forbidden`
                - :exc:`NotFound`
                - :exc:`DiscordServerError`
            - :exc:`LocalizationKeyError`
            - :exc:`WebhookTokenMissing`


Warnings
----------

.. autoclass:: DiscordWarning

.. autoclass:: ConfigWarning

.. autoclass:: SyncWarning

.. autoclass:: LocalizationWarning

Warning Hierarchy
~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :class:`DiscordWarning`
        - :class:`ConfigWarning`
        - :class:`SyncWarning`
        - :class:`LocalizationWarning`
