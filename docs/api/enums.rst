.. currentmodule:: disnake

.. _discord-api-enums:

Enumerations
-------------

The API provides some enumerations for certain types of strings to avoid the API
from being stringly typed in case the strings change in the future.

All enumerations are subclasses of an internal class which mimics the behaviour
of :class:`enum.Enum`.

.. class:: ChannelType

    Specifies the type of channel.

    .. attribute:: text

        A text channel.
    .. attribute:: voice

        A voice channel.
    .. attribute:: private

        A private text channel. Also called a direct message.
    .. attribute:: group

        A private group text channel.
    .. attribute:: category

        A category channel.
    .. attribute:: news

        A guild news channel.

    .. attribute:: stage_voice

        A guild stage voice channel.

        .. versionadded:: 1.7

    .. attribute:: news_thread

        A news thread.

        .. versionadded:: 2.0

    .. attribute:: public_thread

        A public thread.

        .. versionadded:: 2.0

    .. attribute:: private_thread

        A private thread.

        .. versionadded:: 2.0

    .. attribute:: guild_directory

        A student hub channel.

        .. versionadded:: 2.1

    .. attribute:: forum

        A channel of only threads.

        .. versionadded:: 2.5

.. class:: MessageType

    Specifies the type of :class:`Message`. This is used to denote if a message
    is to be interpreted as a system message or a regular message.

    .. container:: operations

      .. describe:: x == y

          Checks if two messages are equal.
      .. describe:: x != y

          Checks if two messages are not equal.

    .. attribute:: default

        The default message type. This is the same as regular messages.
    .. attribute:: recipient_add

        The system message when a user is added to a group private
        message or a thread.
    .. attribute:: recipient_remove

        The system message when a user is removed from a group private
        message or a thread.
    .. attribute:: call

        The system message denoting call state, e.g. missed call, started call,
        etc.
    .. attribute:: channel_name_change

        The system message denoting that a channel's name has been changed.
    .. attribute:: channel_icon_change

        The system message denoting that a channel's icon has been changed.
    .. attribute:: pins_add

        The system message denoting that a pinned message has been added to a channel.
    .. attribute:: new_member

        The system message denoting that a new member has joined a Guild.

    .. attribute:: premium_guild_subscription

        The system message denoting that a member has "nitro boosted" a guild.
    .. attribute:: premium_guild_tier_1

        The system message denoting that a member has "nitro boosted" a guild
        and it achieved level 1.
    .. attribute:: premium_guild_tier_2

        The system message denoting that a member has "nitro boosted" a guild
        and it achieved level 2.
    .. attribute:: premium_guild_tier_3

        The system message denoting that a member has "nitro boosted" a guild
        and it achieved level 3.
    .. attribute:: channel_follow_add

        The system message denoting that an announcement channel has been followed.

        .. versionadded:: 1.3
    .. attribute:: guild_stream

        The system message denoting that a member is streaming in the guild.

        .. versionadded:: 1.7
    .. attribute:: guild_discovery_disqualified

        The system message denoting that the guild is no longer eligible for Server
        Discovery.

        .. versionadded:: 1.7
    .. attribute:: guild_discovery_requalified

        The system message denoting that the guild has become eligible again for Server
        Discovery.

        .. versionadded:: 1.7
    .. attribute:: guild_discovery_grace_period_initial_warning

        The system message denoting that the guild has failed to meet the Server
        Discovery requirements for one week.

        .. versionadded:: 1.7
    .. attribute:: guild_discovery_grace_period_final_warning

        The system message denoting that the guild has failed to meet the Server
        Discovery requirements for 3 weeks in a row.

        .. versionadded:: 1.7
    .. attribute:: thread_created

        The system message denoting that a thread has been created. This is only
        sent if the thread has been created from an older message. The period of time
        required for a message to be considered old cannot be relied upon and is up to
        Discord.

        .. versionadded:: 2.0
    .. attribute:: reply

        The system message denoting that the author is replying to a message.

        .. versionadded:: 2.0
    .. attribute:: application_command

        The system message denoting that an application (or "slash") command was executed.

        .. versionadded:: 2.0
    .. attribute:: guild_invite_reminder

        The system message sent as a reminder to invite people to the guild.

        .. versionadded:: 2.0
    .. attribute:: thread_starter_message

        The system message denoting the message in the thread that is the one that started the
        thread's conversation topic.

        .. versionadded:: 2.0
    .. attribute:: context_menu_command

        The system message denoting that a context menu command was executed.

        .. versionadded:: 2.3
    .. attribute:: auto_moderation_action

        The system message denoting that an auto moderation action was executed.

        .. versionadded:: 2.5

.. class:: UserFlags

    Represents Discord User flags.

    .. attribute:: staff

        The user is a Discord Employee.
    .. attribute:: partner

        The user is a Discord Partner.
    .. attribute:: hypesquad

        The user is a HypeSquad Events member.
    .. attribute:: bug_hunter

        The user is a Bug Hunter.
    .. attribute:: mfa_sms

        The user has SMS recovery for Multi Factor Authentication enabled.
    .. attribute:: premium_promo_dismissed

        The user has dismissed the Discord Nitro promotion.
    .. attribute:: hypesquad_bravery

        The user is a HypeSquad Bravery member.
    .. attribute:: hypesquad_brilliance

        The user is a HypeSquad Brilliance member.
    .. attribute:: hypesquad_balance

        The user is a HypeSquad Balance member.
    .. attribute:: early_supporter

        The user is an Early Supporter.
    .. attribute:: team_user

        The user is a Team User.
    .. attribute:: system

        The user is a system user (i.e. represents Discord officially).
    .. attribute:: has_unread_urgent_messages

        The user has an unread system message.
    .. attribute:: bug_hunter_level_2

        The user is a Bug Hunter Level 2.
    .. attribute:: verified_bot

        The user is a Verified Bot.
    .. attribute:: verified_bot_developer

        The user is an Early Verified Bot Developer.
    .. attribute:: discord_certified_moderator

        The user is a Discord Certified Moderator.
    .. attribute:: http_interactions_bot

        The user is a bot that only uses HTTP interactions.

        .. versionadded:: 2.3
    .. attribute:: spammer

        The user is marked as a spammer.

        .. versionadded:: 2.3

.. class:: ActivityType

    Specifies the type of :class:`Activity`. This is used to check how to
    interpret the activity itself.

    .. attribute:: unknown

        An unknown activity type. This should generally not happen.
    .. attribute:: playing

        A "Playing" activity type.
    .. attribute:: streaming

        A "Streaming" activity type.
    .. attribute:: listening

        A "Listening" activity type.
    .. attribute:: watching

        A "Watching" activity type.
    .. attribute:: custom

        A custom activity type.
    .. attribute:: competing

        A competing activity type.

        .. versionadded:: 1.5

.. class:: PartyType

    Represents the type of a voice channel activity/application.

    .. attribute:: poker

        The "Poker Night" activity.
    .. attribute:: betrayal

        The "Betrayal.io" activity.
    .. attribute:: fishing

        The "Fishington.io" activity.
    .. attribute:: chess

        The "Chess In The Park" activity.
    .. attribute:: letter_tile

        The "Letter Tile" activity.
    .. attribute:: word_snack

        The "Word Snacks" activity.
    .. attribute:: doodle_crew

        The "Doodle Crew" activity.
    .. attribute:: checkers

        The "Checkers In The Park" activity.

        .. versionadded:: 2.3
    .. attribute:: spellcast

        The "SpellCast" activity.

        .. versionadded:: 2.3
    .. attribute:: watch_together

        The "Watch Together" activity, a Youtube application.

        .. versionadded:: 2.3
    .. attribute:: sketch_heads

        The "Sketch Heads" activity.

        .. versionadded:: 2.4
    .. attribute:: ocho

        The "Ocho" activity.

        .. versionadded:: 2.4

.. class:: ApplicationCommandType

    Represents the type of an application command.

    .. versionadded:: 2.1

    .. attribute:: chat_input

        Represents a slash command.
    .. attribute:: user

        Represents a user command from the context menu.
    .. attribute:: message

        Represents a message command from the context menu.

.. class:: ApplicationCommandPermissionType

    Represents the type of a permission of an application command.

    .. versionadded:: 2.5

    .. attribute:: role

        Represents a permission that affects roles.
    .. attribute:: user

        Represents a permission that affects users.
    .. attribute:: channel

        Represents a permission that affects channels.

.. class:: InteractionType

    Specifies the type of :class:`Interaction`.

    .. versionadded:: 2.0

    .. attribute:: ping

        Represents Discord pinging to see if the interaction response server is alive.
    .. attribute:: application_command

        Represents an application command interaction.
    .. attribute:: component

        Represents a component based interaction, i.e. using the Discord Bot UI Kit.
    .. attribute:: application_command_autocomplete

        Represents an application command autocomplete interaction.
    .. attribute:: modal_submit

        Represents a modal submit interaction.

.. class:: InteractionResponseType

    Specifies the response type for the interaction.

    .. versionadded:: 2.0

    .. attribute:: pong

        Pongs the interaction when given a ping.

        See also :meth:`InteractionResponse.pong`
    .. attribute:: channel_message

        Respond to the interaction with a message.

        See also :meth:`InteractionResponse.send_message`
    .. attribute:: deferred_channel_message

        Responds to the interaction with a message at a later time.

        See also :meth:`InteractionResponse.defer`
    .. attribute:: deferred_message_update

        Acknowledges the component interaction with a promise that
        the message will update later (though there is no need to actually update the message).

        See also :meth:`InteractionResponse.defer`
    .. attribute:: message_update

        Responds to the interaction by editing the message.

        See also :meth:`InteractionResponse.edit_message`
    .. attribute:: application_command_autocomplete_result

        Responds to the autocomplete interaction with suggested choices.

        See also :meth:`InteractionResponse.autocomplete`
    .. attribute:: modal

        Responds to the interaction by displaying a modal.

        See also :meth:`InteractionResponse.send_modal`

.. class:: ComponentType

    Represents the component type of a component.

    .. versionadded:: 2.0

    .. attribute:: action_row

        Represents the group component which holds different components in a row.
    .. attribute:: button

        Represents a button component.
    .. attribute:: select

        Represents a select component.
    .. attribute:: text_input

        Represents a text input component.

.. class:: OptionType

    Represents the type of an option.

    .. versionadded:: 2.1

    .. attribute:: sub_command

        Represents a sub command of the main command or group.
    .. attribute:: sub_command_group

        Represents a sub command group of the main command.
    .. attribute:: string

        Represents a string option.
    .. attribute:: integer

        Represents an integer option.
    .. attribute:: boolean

        Represents a boolean option.
    .. attribute:: user

        Represents a user option.
    .. attribute:: channel

        Represents a channel option.
    .. attribute:: role

        Represents a role option.
    .. attribute:: mentionable

        Represents a role + user option.
    .. attribute:: number

        Represents a float option.
    .. attribute:: attachment

        Represents an attachment option.

        .. versionadded:: 2.4


.. class:: ButtonStyle

    Represents the style of the button component.

    .. versionadded:: 2.0

    .. attribute:: primary

        Represents a blurple button for the primary action.
    .. attribute:: secondary

        Represents a grey button for the secondary action.
    .. attribute:: success

        Represents a green button for a successful action.
    .. attribute:: danger

        Represents a red button for a dangerous action.
    .. attribute:: link

        Represents a link button.

    .. attribute:: blurple

        An alias for :attr:`primary`.
    .. attribute:: grey

        An alias for :attr:`secondary`.
    .. attribute:: gray

        An alias for :attr:`secondary`.
    .. attribute:: green

        An alias for :attr:`success`.
    .. attribute:: red

        An alias for :attr:`danger`.
    .. attribute:: url

        An alias for :attr:`link`.

.. class:: TextInputStyle

    Represents a style of the text input component.

    .. versionadded:: 2.4

    .. attribute:: short

        Represents a single-line text input component.
    .. attribute:: paragraph

        Represents a multi-line text input component.
    .. attribute:: single_line

        An alias for :attr:`short`.
    .. attribute:: multi_line

        An alias for :attr:`paragraph`.
    .. attribute:: long

        An alias for :attr:`paragraph`.


.. class:: VerificationLevel

    Specifies a :class:`Guild`\'s verification level, which is the criteria in
    which a member must meet before being able to send messages to the guild.

    .. container:: operations

        .. versionadded:: 2.0

        .. describe:: x == y

            Checks if two verification levels are equal.
        .. describe:: x != y

            Checks if two verification levels are not equal.
        .. describe:: x > y

            Checks if a verification level is higher than another.
        .. describe:: x < y

            Checks if a verification level is lower than another.
        .. describe:: x >= y

            Checks if a verification level is higher or equal to another.
        .. describe:: x <= y

            Checks if a verification level is lower or equal to another.

    .. attribute:: none

        No criteria set.
    .. attribute:: low

        Member must have a verified email on their Discord account.
    .. attribute:: medium

        Member must have a verified email and be registered on Discord for more
        than five minutes.
    .. attribute:: high

        Member must have a verified email, be registered on Discord for more
        than five minutes, and be a member of the guild itself for more than
        ten minutes.
    .. attribute:: highest

        Member must have a verified phone on their Discord account.

.. class:: NotificationLevel

    Specifies whether a :class:`Guild` has notifications on for all messages or mentions only by default.

    .. container:: operations

        .. versionadded:: 2.0

        .. describe:: x == y

            Checks if two notification levels are equal.
        .. describe:: x != y

            Checks if two notification levels are not equal.
        .. describe:: x > y

            Checks if a notification level is higher than another.
        .. describe:: x < y

            Checks if a notification level is lower than another.
        .. describe:: x >= y

            Checks if a notification level is higher or equal to another.
        .. describe:: x <= y

            Checks if a notification level is lower or equal to another.

    .. attribute:: all_messages

        Members receive notifications for every message regardless of them being mentioned.
    .. attribute:: only_mentions

        Members receive notifications for messages they are mentioned in.

.. class:: ContentFilter

    Specifies a :class:`Guild`\'s explicit content filter, which is the machine
    learning algorithms that Discord uses to detect if an image contains
    pornography or otherwise explicit content.

    .. container:: operations

        .. versionadded:: 2.0

        .. describe:: x == y

            Checks if two content filter levels are equal.
        .. describe:: x != y

            Checks if two content filter levels are not equal.
        .. describe:: x > y

            Checks if a content filter level is higher than another.
        .. describe:: x < y

            Checks if a content filter level is lower than another.
        .. describe:: x >= y

            Checks if a content filter level is higher or equal to another.
        .. describe:: x <= y

            Checks if a content filter level is lower or equal to another.

    .. attribute:: disabled

        The guild does not have the content filter enabled.
    .. attribute:: no_role

        The guild has the content filter enabled for members without a role.
    .. attribute:: all_members

        The guild has the content filter enabled for every member.

.. class:: Status

    Specifies a :class:`Member` 's status.

    .. attribute:: online

        The member is online.
    .. attribute:: offline

        The member is offline.
    .. attribute:: idle

        The member is idle.
    .. attribute:: dnd

        The member is "Do Not Disturb".
    .. attribute:: do_not_disturb

        An alias for :attr:`dnd`.
    .. attribute:: invisible

        The member is "invisible". In reality, this is only used in sending
        a presence a la :meth:`Client.change_presence`. When you receive a
        user's presence this will be :attr:`offline` instead.
    .. attribute:: streaming

        The member is live streaming to Twitch.

        .. versionadded:: 2.3


.. class:: AuditLogAction

    Represents the type of action being done for a :class:`AuditLogEntry`\,
    which is retrievable via :meth:`Guild.audit_logs`.

    .. attribute:: guild_update

        The guild has updated. Things that trigger this include:

        - Changing the guild vanity URL
        - Changing the guild invite splash
        - Changing the guild AFK channel or timeout
        - Changing the guild voice server region
        - Changing the guild icon, banner, or discovery splash
        - Changing the guild moderation settings
        - Changing things related to the guild widget

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Guild`.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.afk_channel`
        - :attr:`~AuditLogDiff.system_channel`
        - :attr:`~AuditLogDiff.afk_timeout`
        - :attr:`~AuditLogDiff.default_message_notifications`
        - :attr:`~AuditLogDiff.explicit_content_filter`
        - :attr:`~AuditLogDiff.mfa_level`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.owner`
        - :attr:`~AuditLogDiff.splash`
        - :attr:`~AuditLogDiff.discovery_splash`
        - :attr:`~AuditLogDiff.icon`
        - :attr:`~AuditLogDiff.banner`
        - :attr:`~AuditLogDiff.vanity_url_code`
        - :attr:`~AuditLogDiff.preferred_locale`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.rules_channel`
        - :attr:`~AuditLogDiff.public_updates_channel`
        - :attr:`~AuditLogDiff.widget_enabled`
        - :attr:`~AuditLogDiff.widget_channel`
        - :attr:`~AuditLogDiff.verification_level`
        - :attr:`~AuditLogDiff.premium_progress_bar_enabled`
        - :attr:`~AuditLogDiff.system_channel_flags`

    .. attribute:: channel_create

        A new channel was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        either a :class:`abc.GuildChannel` or :class:`Object` with an ID.

        A more filled out object in the :class:`Object` case can be found
        by using :attr:`~AuditLogEntry.after`.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.overwrites`
        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.bitrate`
        - :attr:`~AuditLogDiff.rtc_region`
        - :attr:`~AuditLogDiff.video_quality_mode`
        - :attr:`~AuditLogDiff.default_auto_archive_duration`
        - :attr:`~AuditLogDiff.user_limit`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.nsfw`

    .. attribute:: channel_update

        A channel was updated. Things that trigger this include:

        - The channel name or topic was changed
        - The channel bitrate was changed

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`abc.GuildChannel` or :class:`Object` with an ID.

        A more filled out object in the :class:`Object` case can be found
        by using :attr:`~AuditLogEntry.after` or :attr:`~AuditLogEntry.before`.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.position`
        - :attr:`~AuditLogDiff.overwrites`
        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.bitrate`
        - :attr:`~AuditLogDiff.rtc_region`
        - :attr:`~AuditLogDiff.video_quality_mode`
        - :attr:`~AuditLogDiff.default_auto_archive_duration`
        - :attr:`~AuditLogDiff.user_limit`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.nsfw`

    .. attribute:: channel_delete

        A channel was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        an :class:`Object` with an ID.

        A more filled out object can be found by using the
        :attr:`~AuditLogEntry.before` object.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.overwrites`
        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.bitrate`
        - :attr:`~AuditLogDiff.rtc_region`
        - :attr:`~AuditLogDiff.video_quality_mode`
        - :attr:`~AuditLogDiff.default_auto_archive_duration`
        - :attr:`~AuditLogDiff.user_limit`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.nsfw`

    .. attribute:: overwrite_create

        A channel permission overwrite was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`abc.GuildChannel` or :class:`Object` with an ID.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        either a :class:`Role` or :class:`Member`. If the object is not found
        then it is a :class:`Object` with an ID being filled, a name, and a
        ``type`` attribute set to either ``'role'`` or ``'member'`` to help
        dictate what type of ID it is.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.deny`
        - :attr:`~AuditLogDiff.allow`
        - :attr:`~AuditLogDiff.id`
        - :attr:`~AuditLogDiff.type`

        .. versionchanged:: 2.6
            :attr:`~AuditLogDiff.type` for this action is now an :class:`int`.

    .. attribute:: overwrite_update

        A channel permission overwrite was changed, this is typically
        when the permission values change.

        See :attr:`overwrite_create` for more information on how the
        :attr:`~AuditLogEntry.target` and :attr:`~AuditLogEntry.extra` fields
        are set.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.deny`
        - :attr:`~AuditLogDiff.allow`
        - :attr:`~AuditLogDiff.id`
        - :attr:`~AuditLogDiff.type`

        .. versionchanged:: 2.6
            :attr:`~AuditLogDiff.type` for this action is now an :class:`int`.

    .. attribute:: overwrite_delete

        A channel permission overwrite was deleted.

        See :attr:`overwrite_create` for more information on how the
        :attr:`~AuditLogEntry.target` and :attr:`~AuditLogEntry.extra` fields
        are set.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.deny`
        - :attr:`~AuditLogDiff.allow`
        - :attr:`~AuditLogDiff.id`
        - :attr:`~AuditLogDiff.type`

        .. versionchanged:: 2.6
            :attr:`~AuditLogDiff.type` for this action is now an :class:`int`.

    .. attribute:: kick

        A member was kicked.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`User` who got kicked.

        When this is the action, :attr:`~AuditLogEntry.changes` is empty.

    .. attribute:: member_prune

        A member prune was triggered.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        set to ``None``.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with two attributes:

        - ``delete_members_days``: An integer specifying how far the prune was.
        - ``members_removed``: An integer specifying how many members were removed.

        When this is the action, :attr:`~AuditLogEntry.changes` is empty.

    .. attribute:: ban

        A member was banned.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`User` who got banned.

        When this is the action, :attr:`~AuditLogEntry.changes` is empty.

    .. attribute:: unban

        A member was unbanned.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`User` who got unbanned.

        When this is the action, :attr:`~AuditLogEntry.changes` is empty.

    .. attribute:: member_update

        A member has updated. This triggers in the following situations:

        - A nickname was changed
        - They were server muted or deafened (or it was undone)
        - They were timed out

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who got updated.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.nick`
        - :attr:`~AuditLogDiff.mute`
        - :attr:`~AuditLogDiff.deaf`
        - :attr:`~AuditLogDiff.timeout`

    .. attribute:: member_role_update

        A member's role has been updated. This triggers when a member
        either gains a role or loses a role.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who got the role.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.roles`

    .. attribute:: member_move

        A member's voice channel has been updated. This triggers when a
        member is moved to a different voice channel.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with two attributes:

        - ``channel``: A :class:`TextChannel` or :class:`Object` with the channel ID where the members were moved.
        - ``count``: An integer specifying how many members were moved.

        .. versionadded:: 1.3

    .. attribute:: member_disconnect

        A member's voice state has changed. This triggers when a
        member is force disconnected from voice.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with one attribute:

        - ``count``: An integer specifying how many members were disconnected.

        .. versionadded:: 1.3

    .. attribute:: bot_add

        A bot was added to the guild.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` which was added to the guild.

        .. versionadded:: 1.3

    .. attribute:: role_create

        A new role was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Role` or a :class:`Object` with the ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.colour`
        - :attr:`~AuditLogDiff.mentionable`
        - :attr:`~AuditLogDiff.hoist`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.permissions`
        - :attr:`~AuditLogDiff.icon`
        - :attr:`~AuditLogDiff.emoji`

    .. attribute:: role_update

        A role was updated. This triggers in the following situations:

        - The name has changed
        - The permissions have changed
        - The colour has changed
        - Its hoist/mentionable state has changed

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Role` or a :class:`Object` with the ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.colour`
        - :attr:`~AuditLogDiff.mentionable`
        - :attr:`~AuditLogDiff.hoist`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.permissions`
        - :attr:`~AuditLogDiff.icon`
        - :attr:`~AuditLogDiff.emoji`

    .. attribute:: role_delete

        A role was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.colour`
        - :attr:`~AuditLogDiff.mentionable`
        - :attr:`~AuditLogDiff.hoist`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.permissions`
        - :attr:`~AuditLogDiff.icon`
        - :attr:`~AuditLogDiff.emoji`

    .. attribute:: invite_create

        An invite was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Invite` that was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.max_age`
        - :attr:`~AuditLogDiff.code`
        - :attr:`~AuditLogDiff.temporary`
        - :attr:`~AuditLogDiff.inviter`
        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.uses`
        - :attr:`~AuditLogDiff.max_uses`

    .. attribute:: invite_update

        An invite was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Invite` that was updated.

    .. attribute:: invite_delete

        An invite was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Invite` that was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.max_age`
        - :attr:`~AuditLogDiff.code`
        - :attr:`~AuditLogDiff.temporary`
        - :attr:`~AuditLogDiff.inviter`
        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.uses`
        - :attr:`~AuditLogDiff.max_uses`

    .. attribute:: webhook_create

        A webhook was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Webhook` or :class:`Object` with the webhook ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.application_id`
        - :attr:`~AuditLogDiff.avatar`

        .. versionchanged:: 2.6
            Added :attr:`~AuditLogDiff.application_id`.

        .. versionchanged:: 2.6
            :attr:`~AuditLogDiff.type` for this action is now a :class:`WebhookType`.

        .. versionchanged:: 2.6
            Added support for :class:`Webhook` instead of plain :class:`Object`\s.

    .. attribute:: webhook_update

        A webhook was updated. This trigger in the following situations:

        - The webhook name changed
        - The webhook channel changed

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Webhook` or :class:`Object` with the webhook ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.avatar`

        .. versionchanged:: 2.6
            Added support for :class:`Webhook` instead of plain :class:`Object`\s.

    .. attribute:: webhook_delete

        A webhook was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the webhook ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.application_id`
        - :attr:`~AuditLogDiff.avatar`

        .. versionchanged:: 2.6
            Added :attr:`~AuditLogDiff.application_id`.

        .. versionchanged:: 2.6
            :attr:`~AuditLogDiff.type` for this action is now a :class:`WebhookType`.

    .. attribute:: emoji_create

        An emoji was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Emoji` or :class:`Object` with the emoji ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`

    .. attribute:: emoji_update

        An emoji was updated. This triggers when the name has changed.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Emoji` or :class:`Object` with the emoji ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`

    .. attribute:: emoji_delete

        An emoji was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the emoji ID.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`

    .. attribute:: message_delete

        A message was deleted by a moderator. Note that this
        only triggers if the message was deleted by someone other than the author.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who had their message deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with two attributes:

        - ``count``: An integer specifying how many messages were deleted.
        - ``channel``: A :class:`TextChannel` or :class:`Object` with the channel ID where the message got deleted.

    .. attribute:: message_bulk_delete

        Messages were bulk deleted by a moderator.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`TextChannel` or :class:`Object` with the ID of the channel that was purged.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with one attribute:

        - ``count``: An integer specifying how many messages were deleted.

        .. versionadded:: 1.3

    .. attribute:: message_pin

        A message was pinned in a channel.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who had their message pinned.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with two attributes:

        - ``channel``: A :class:`TextChannel` or :class:`Object` with the channel ID where the message was pinned.
        - ``message_id``: the ID of the message which was pinned.

        .. versionadded:: 1.3

    .. attribute:: message_unpin

        A message was unpinned in a channel.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who had their message unpinned.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with two attributes:

        - ``channel``: A :class:`TextChannel` or :class:`Object` with the channel ID where the message was unpinned.
        - ``message_id``: the ID of the message which was unpinned.

        .. versionadded:: 1.3

    .. attribute:: integration_create

        A guild integration was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`PartialIntegration` or :class:`Object` with the integration ID
        of the integration which was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.type`

        .. versionadded:: 1.3

        .. versionchanged:: 2.6
            Added support for :class:`PartialIntegration` instead of plain :class:`Object`\s.

    .. attribute:: integration_update

        A guild integration was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`PartialIntegration` or :class:`Object` with the integration ID
        of the integration which was updated.

        .. versionadded:: 1.3

        .. versionchanged:: 2.6
            Added support for :class:`PartialIntegration` instead of plain :class:`Object`\s.

    .. attribute:: integration_delete

        A guild integration was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the integration ID of the integration which was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.type`

        .. versionadded:: 1.3

    .. attribute:: guild_scheduled_event_create

        A guild scheduled event was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`GuildScheduledEvent` or :class:`Object` with the ID of the event
        which was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.privacy_level`
        - :attr:`~AuditLogDiff.status`
        - :attr:`~AuditLogDiff.entity_type`
        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.location`
        - :attr:`~AuditLogDiff.image`

        .. versionadded:: 2.3

    .. attribute:: guild_scheduled_event_update

        A guild scheduled event was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`GuildScheduledEvent` or :class:`Object` with the ID of the event
        which was updated.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.privacy_level`
        - :attr:`~AuditLogDiff.status`
        - :attr:`~AuditLogDiff.entity_type`
        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.location`
        - :attr:`~AuditLogDiff.image`

        .. versionadded:: 2.3

    .. attribute:: guild_scheduled_event_delete

        A guild scheduled event was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the ID of the event which was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.privacy_level`
        - :attr:`~AuditLogDiff.status`
        - :attr:`~AuditLogDiff.entity_type`
        - :attr:`~AuditLogDiff.channel`
        - :attr:`~AuditLogDiff.location`
        - :attr:`~AuditLogDiff.image`

        .. versionadded:: 2.3

    .. attribute:: stage_instance_create

        A stage instance was started.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`StageInstance` or :class:`Object` with the ID of the stage
        instance which was created.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with one attribute:

        - ``channel``: The :class:`StageChannel` or :class:`Object` with the channel ID where the stage instance was started.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.privacy_level`

        .. versionadded:: 2.0

    .. attribute:: stage_instance_update

        A stage instance was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`StageInstance` or :class:`Object` with the ID of the stage
        instance which was updated.

        See :attr:`stage_instance_create` for more information on how the
        :attr:`~AuditLogEntry.extra` field is set.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.privacy_level`

        .. versionadded:: 2.0

    .. attribute:: stage_instance_delete

        A stage instance was ended.

        See :attr:`stage_instance_create` for more information on how the
        :attr:`~AuditLogEntry.extra` field is set.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.topic`
        - :attr:`~AuditLogDiff.privacy_level`

        .. versionadded:: 2.0

    .. attribute:: sticker_create

        A sticker was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`GuildSticker` or :class:`Object` with the ID of the sticker
        which was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.emoji`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.format_type`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.available`

        .. versionadded:: 2.0

    .. attribute:: sticker_update

        A sticker was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`GuildSticker` or :class:`Object` with the ID of the sticker
        which was updated.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.emoji`
        - :attr:`~AuditLogDiff.description`

        .. versionadded:: 2.0

    .. attribute:: sticker_delete

        A sticker was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the ID of the sticker which was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.emoji`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.format_type`
        - :attr:`~AuditLogDiff.description`
        - :attr:`~AuditLogDiff.available`

        .. versionadded:: 2.0

    .. attribute:: thread_create

        A thread was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Thread` or :class:`Object` with the ID of the thread which
        was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.archived`
        - :attr:`~AuditLogDiff.locked`
        - :attr:`~AuditLogDiff.auto_archive_duration`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.invitable`
        - :attr:`~AuditLogDiff.flags`

        .. versionadded:: 2.0

    .. attribute:: thread_update

        A thread was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Thread` or :class:`Object` with the ID of the thread which
        was updated.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.archived`
        - :attr:`~AuditLogDiff.locked`
        - :attr:`~AuditLogDiff.auto_archive_duration`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.invitable`
        - :attr:`~AuditLogDiff.flags`

        .. versionadded:: 2.0

    .. attribute:: thread_delete

        A thread was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the ID of the thread which was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.archived`
        - :attr:`~AuditLogDiff.locked`
        - :attr:`~AuditLogDiff.auto_archive_duration`
        - :attr:`~AuditLogDiff.type`
        - :attr:`~AuditLogDiff.slowmode_delay`
        - :attr:`~AuditLogDiff.invitable`
        - :attr:`~AuditLogDiff.flags`

        .. versionadded:: 2.0

    .. attribute:: application_command_permission_update

        The permissions of an application command were updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`ApplicationCommand`, :class:`PartialIntegration`, or :class:`Object`
        with the ID of the command whose permissions were updated or the application ID
        if these are application-wide permissions.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with one attribute:

        - ``integration``: The :class:`PartialIntegration` or :class:`Object` with the application ID of the associated application.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.command_permissions`

        .. versionadded:: 2.5

        .. versionchanged:: 2.6
            Added support for :class:`PartialIntegration`, and added ``integration`` to :attr:`~AuditLogEntry.extra`.

    .. attribute:: automod_rule_create

        An auto moderation rule was created.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`AutoModRule` or :class:`Object` with the ID of the auto moderation rule which
        was created.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.enabled`
        - :attr:`~AuditLogDiff.trigger_type`
        - :attr:`~AuditLogDiff.event_type`
        - :attr:`~AuditLogDiff.actions`
        - :attr:`~AuditLogDiff.trigger_metadata`
        - :attr:`~AuditLogDiff.exempt_roles`
        - :attr:`~AuditLogDiff.exempt_channels`

        .. versionadded:: 2.6

    .. attribute:: automod_rule_update

        An auto moderation rule was updated.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`AutoModRule` or :class:`Object` with the ID of the auto moderation rule which
        was updated.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.enabled`
        - :attr:`~AuditLogDiff.trigger_type`
        - :attr:`~AuditLogDiff.event_type`
        - :attr:`~AuditLogDiff.actions`
        - :attr:`~AuditLogDiff.trigger_metadata`
        - :attr:`~AuditLogDiff.exempt_roles`
        - :attr:`~AuditLogDiff.exempt_channels`

        .. versionadded:: 2.6

    .. attribute:: automod_rule_delete

        An auto moderation rule was deleted.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Object` with the ID of the auto moderation rule which
        was deleted.

        Possible attributes for :class:`AuditLogDiff`:

        - :attr:`~AuditLogDiff.name`
        - :attr:`~AuditLogDiff.enabled`
        - :attr:`~AuditLogDiff.trigger_type`
        - :attr:`~AuditLogDiff.event_type`
        - :attr:`~AuditLogDiff.actions`
        - :attr:`~AuditLogDiff.trigger_metadata`
        - :attr:`~AuditLogDiff.exempt_roles`
        - :attr:`~AuditLogDiff.exempt_channels`

        .. versionadded:: 2.6

    .. attribute:: automod_block_message

        A message was blocked by an auto moderation rule.

        When this is the action, the type of :attr:`~AuditLogEntry.target` is
        the :class:`Member` or :class:`User` who had their message blocked.

        When this is the action, the type of :attr:`~AuditLogEntry.extra` is
        set to an unspecified proxy object with these attributes:

        - ``channel``: A :class:`~abc.GuildChannel`, :class:`Thread` or :class:`Object` with the channel ID where the message got blocked.
        - ``rule_name``: A :class:`str` with the name of the rule that matched.
        - ``rule_trigger_type``: A :class:`AutoModTriggerType` value with the trigger type of the rule.

.. class:: AuditLogActionCategory

    Represents the category that the :class:`AuditLogAction` belongs to.

    This can be retrieved via :attr:`AuditLogEntry.category`.

    .. attribute:: create

        The action is the creation of something.

    .. attribute:: delete

        The action is the deletion of something.

    .. attribute:: update

        The action is the update of something.

.. class:: TeamMembershipState

    Represents the membership state of a team member retrieved through :func:`Client.application_info`.

    .. versionadded:: 1.3

    .. attribute:: invited

        Represents an invited member.

    .. attribute:: accepted

        Represents a member currently in the team.

.. class:: WebhookType

    Represents the type of webhook that can be received.

    .. versionadded:: 1.3

    .. attribute:: incoming

        Represents a webhook that can post messages to channels with a token.

    .. attribute:: channel_follower

        Represents a webhook that is internally managed by Discord, used for following channels.

    .. attribute:: application

        Represents a webhook that is used for interactions or applications.

        .. versionadded:: 2.0

.. class:: ExpireBehaviour

    Represents the behaviour the :class:`Integration` should perform
    when a user's subscription has finished.

    There is an alias for this called ``ExpireBehavior``.

    .. versionadded:: 1.4

    .. attribute:: remove_role

        This will remove the :attr:`StreamIntegration.role` from the user
        when their subscription is finished.

    .. attribute:: kick

        This will kick the user when their subscription is finished.

.. class:: DefaultAvatar

    Represents the default avatar of a Discord :class:`User`

    .. attribute:: blurple

        Represents the default avatar with the color blurple.
        See also :attr:`Colour.blurple`
    .. attribute:: grey

        Represents the default avatar with the color grey.
        See also :attr:`Colour.greyple`
    .. attribute:: gray

        An alias for :attr:`grey`.
    .. attribute:: green

        Represents the default avatar with the color green.
        See also :attr:`Colour.green`
    .. attribute:: orange

        Represents the default avatar with the color orange.
        See also :attr:`Colour.orange`
    .. attribute:: red

        Represents the default avatar with the color red.
        See also :attr:`Colour.red`

.. class:: StickerType

    Represents the type of sticker.

    .. versionadded:: 2.0

    .. attribute:: standard

        Represents a standard sticker that all Nitro users can use.

    .. attribute:: guild

        Represents a custom sticker created in a guild.

.. class:: StickerFormatType

    Represents the type of sticker images.

    .. versionadded:: 1.6

    .. attribute:: png

        Represents a sticker with a png image.

    .. attribute:: apng

        Represents a sticker with an apng image.

    .. attribute:: lottie

        Represents a sticker with a lottie image.

.. class:: InviteTarget

    Represents the invite type for voice channel invites.

    .. versionadded:: 2.0

    .. attribute:: unknown

        The invite doesn't target anyone or anything.

    .. attribute:: stream

        A stream invite that targets a user.

    .. attribute:: embedded_application

        A stream invite that targets an embedded application.

.. class:: VideoQualityMode

    Represents the camera video quality mode for voice channel participants.

    .. versionadded:: 2.0

    .. attribute:: auto

        Represents auto camera video quality.

    .. attribute:: full

        Represents full camera video quality.

.. class:: StagePrivacyLevel

    Represents a stage instance's privacy level.

    .. versionadded:: 2.0

    .. attribute:: public

        The stage instance can be joined by external users.

        .. deprecated:: 2.5

            Public stages are no longer supported by discord.

    .. attribute:: closed

        The stage instance can only be joined by members of the guild.

    .. attribute:: guild_only

        Alias for :attr:`.closed`

.. class:: NSFWLevel

    Represents the NSFW level of a guild.

    .. versionadded:: 2.0

    .. container:: operations

        .. describe:: x == y

            Checks if two NSFW levels are equal.
        .. describe:: x != y

            Checks if two NSFW levels are not equal.
        .. describe:: x > y

            Checks if a NSFW level is higher than another.
        .. describe:: x < y

            Checks if a NSFW level is lower than another.
        .. describe:: x >= y

            Checks if a NSFW level is higher or equal to another.
        .. describe:: x <= y

            Checks if a NSFW level is lower or equal to another.

    .. attribute:: default

        The guild has not been categorised yet.

    .. attribute:: explicit

        The guild contains NSFW content.

    .. attribute:: safe

        The guild does not contain any NSFW content.

    .. attribute:: age_restricted

        The guild may contain NSFW content.

.. class:: GuildScheduledEventEntityType

    Represents the type of a guild scheduled event entity.

    .. versionadded:: 2.3

    .. attribute:: stage_instance

        The guild scheduled event will take place in a stage channel.

    .. attribute:: voice

        The guild scheduled event will take place in a voice channel.

    .. attribute:: external

        The guild scheduled event will take place in a custom location.

.. class:: GuildScheduledEventStatus

    Represents the status of a guild scheduled event.

    .. versionadded:: 2.3

    .. attribute:: scheduled

        Represents a scheduled event.

    .. attribute:: active

        Represents an active event.

    .. attribute:: completed

        Represents a completed event.

    .. attribute:: canceled

        Represents a canceled event.

    .. attribute:: cancelled

        An alias for :attr:`canceled`.

        .. versionadded:: 2.6

.. class:: GuildScheduledEventPrivacyLevel

    Represents the privacy level of a guild scheduled event.

    .. versionadded:: 2.3

    .. attribute:: guild_only

        The guild scheduled event is only for a specific guild.

.. class:: ThreadArchiveDuration

    Represents the automatic archive duration of a thread in minutes.

    .. versionadded:: 2.3

    .. attribute:: hour

        The thread will archive after an hour of inactivity.

    .. attribute:: day

        The thread will archive after a day of inactivity.

    .. attribute:: three_days

        The thread will archive after three days of inactivity.

    .. attribute:: week

        The thread will archive after a week of inactivity.

.. class:: WidgetStyle

    Represents the supported widget image styles.

    .. versionadded:: 2.5

    .. attribute:: shield

        A shield style image with a Discord icon and the online member count.

    .. attribute:: banner1

        A large image with guild icon, name and online member count and a footer.

    .. attribute:: banner2

        A small image with guild icon, name and online member count.

    .. attribute:: banner3

        A large image with guild icon, name and online member count and a footer,
        with a "Chat Now" label on the right.

    .. attribute:: banner4

        A large image with a large Discord logo, guild icon, name and online member count,
        with a "Join My Server" label at the bottom.

.. class:: Locale

    Represents supported locales by Discord.

    .. versionadded:: 2.5

    .. attribute:: bg

        The ``bg`` (Bulgarian) locale.

    .. attribute:: cs

        The ``cs`` (Czech) locale.

    .. attribute:: da

        The ``da`` (Danish) locale.

    .. attribute:: de

        The ``de`` (German) locale.

    .. attribute:: el

        The ``el`` (Greek) locale.

    .. attribute:: en_GB

        The ``en_GB`` (English, UK) locale.

    .. attribute:: en_US

        The ``en_US`` (English, US) locale.

    .. attribute:: es_ES

        The ``es_ES`` (Spanish) locale.

    .. attribute:: fi

        The ``fi`` (Finnish) locale.

    .. attribute:: fr

        The ``fr`` (French) locale.

    .. attribute:: hi

        The ``hi`` (Hindi) locale.

    .. attribute:: hr

        The ``hr`` (Croatian) locale.

    .. attribute:: it

        The ``it`` (Italian) locale.

    .. attribute:: ja

        The ``ja`` (Japanese) locale.

    .. attribute:: ko

        The ``ko`` (Korean) locale.

    .. attribute:: lt

        The ``lt`` (Lithuanian) locale.

    .. attribute:: hu

        The ``hu`` (Hungarian) locale.

    .. attribute:: nl

        The ``nl`` (Dutch) locale.

    .. attribute:: no

        The ``no`` (Norwegian) locale.

    .. attribute:: pl

        The ``pl`` (Polish) locale.

    .. attribute:: pt_BR

        The ``pt_BR`` (Portuguese) locale.

    .. attribute:: ro

        The ``ro`` (Romanian) locale.

    .. attribute:: ru

        The ``ru`` (Russian) locale.

    .. attribute:: sv_SE

        The ``sv_SE`` (Swedish) locale.

    .. attribute:: th

        The ``th`` (Thai) locale.

    .. attribute:: tr

        The ``tr`` (Turkish) locale.

    .. attribute:: uk

        The ``uk`` (Ukrainian) locale.

    .. attribute:: vi

        The ``vi`` (Vietnamese) locale.

    .. attribute:: zh_CN

        The ``zh_CN`` (Chinese, China) locale.

    .. attribute:: zh_TW

        The ``zh_TW`` (Chinese, Taiwan) locale.

.. class:: AutoModActionType

    Represents the type of action an auto moderation rule will take upon execution.

    .. versionadded:: 2.6

    .. attribute:: block_message

        The rule will prevent matching messages from being posted.

    .. attribute:: send_alert_message

        The rule will send an alert to a specified channel.

    .. attribute:: timeout

        The rule will timeout the user that sent the message.

        .. note::
            This action type is only available for rules with trigger type
            :attr:`~AutoModTriggerType.keyword`, and :attr:`~Permissions.moderate_members`
            permissions are required to use it.

.. class:: AutoModEventType

    Represents the type of event/context an auto moderation rule will be checked in.

    .. versionadded:: 2.6

    .. attribute:: message_send

        The rule will apply when a member sends or edits a message in the guild.

.. class:: AutoModTriggerType

    Represents the type of content that can trigger an auto moderation rule.

    .. versionadded:: 2.6

    .. attribute:: keyword

        The rule will filter messages based on a custom keyword list.

        This trigger type requires additional :class:`metadata <AutoModTriggerMetadata>`.

    .. attribute:: harmful_link

        The rule will filter messages containing malicious links.

    .. attribute:: spam

        The rule will filter messages suspected of being spam.

    .. attribute:: keyword_preset

        The rule will filter messages based on predefined lists containing commonly flagged words.

        This trigger type requires additional :class:`metadata <AutoModTriggerMetadata>`.
