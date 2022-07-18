.. currentmodule:: disnake


.. _discord_api_data:

Data Classes
--------------

Some classes are just there to be data containers, this lists them.

Unlike :ref:`models <discord_api_models>` you are allowed to create
most of these yourself, even if they can also be used to hold attributes.

Nearly all classes here have :ref:`py:slots` defined which means that it is
impossible to have dynamic attributes to the data classes.

The only exception to this rule is :class:`Object`, which is made with
dynamic attributes in mind.


Object
~~~~~~~

.. attributetable:: Object

.. autoclass:: Object
    :members:

Embed
~~~~~~

.. attributetable:: Embed

.. autoclass:: Embed
    :members:

AllowedMentions
~~~~~~~~~~~~~~~~~

.. attributetable:: AllowedMentions

.. autoclass:: AllowedMentions
    :members:

MessageReference
~~~~~~~~~~~~~~~~~

.. attributetable:: MessageReference

.. autoclass:: MessageReference
    :members:

InteractionReference
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: InteractionReference

.. autoclass:: InteractionReference
    :members:

PartialMessage
~~~~~~~~~~~~~~~~~

.. attributetable:: PartialMessage

.. autoclass:: PartialMessage
    :members:

ApplicationCommand
~~~~~~~~~~~~~~~~~~

.. attributetable:: ApplicationCommand

.. autoclass:: ApplicationCommand()
    :members:

SlashCommand
~~~~~~~~~~~~

.. attributetable:: SlashCommand

.. autoclass:: SlashCommand()
    :members:
    :inherited-members:

UserCommand
~~~~~~~~~~~

.. attributetable:: UserCommand

.. autoclass:: UserCommand()
    :members:
    :inherited-members:

MessageCommand
~~~~~~~~~~~~~~

.. attributetable:: MessageCommand

.. autoclass:: MessageCommand()
    :members:
    :inherited-members:

Option
~~~~~~

.. attributetable:: Option

.. autoclass:: Option()
    :members:

OptionChoice
~~~~~~~~~~~~

.. attributetable:: OptionChoice

.. autoclass:: OptionChoice()
    :members:

SelectOption
~~~~~~~~~~~~~

.. attributetable:: SelectOption

.. autoclass:: SelectOption
    :members:

Intents
~~~~~~~~~~

.. attributetable:: Intents

.. autoclass:: Intents
    :members:

MemberCacheFlags
~~~~~~~~~~~~~~~~~~

.. attributetable:: MemberCacheFlags

.. autoclass:: MemberCacheFlags
    :members:

ApplicationFlags
~~~~~~~~~~~~~~~~~

.. attributetable:: ApplicationFlags

.. autoclass:: ApplicationFlags
    :members:

ChannelFlags
~~~~~~~~~~~~

.. attributetable:: ChannelFlags

.. autoclass:: ChannelFlags
    :members:

AutoModKeywordPresets
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoModKeywordPresets

.. autoclass:: AutoModKeywordPresets
    :members:

AutoModTriggerMetadata
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoModTriggerMetadata

.. autoclass:: AutoModTriggerMetadata
    :members:

AutoModAction
~~~~~~~~~~~~~~

.. attributetable:: AutoModAction

.. autoclass:: AutoModAction()
    :members:

AutoModBlockMessageAction
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoModBlockMessageAction

.. autoclass:: AutoModBlockMessageAction
    :members:

AutoModSendAlertAction
~~~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoModSendAlertAction

.. autoclass:: AutoModSendAlertAction
    :members:

AutoModTimeoutAction
~~~~~~~~~~~~~~~~~~~~~

.. attributetable:: AutoModTimeoutAction

.. autoclass:: AutoModTimeoutAction
    :members:

File
~~~~~

.. attributetable:: File

.. autoclass:: File
    :members:

Colour
~~~~~~

.. attributetable:: Colour

.. autoclass:: Colour
    :members:

BaseActivity
~~~~~~~~~~~~~~

.. attributetable:: BaseActivity

.. autoclass:: BaseActivity
    :members:

Activity
~~~~~~~~~

.. attributetable:: Activity

.. autoclass:: Activity
    :members:

Game
~~~~~

.. attributetable:: Game

.. autoclass:: Game
    :members:

Streaming
~~~~~~~~~~~

.. attributetable:: Streaming

.. autoclass:: Streaming
    :members:

CustomActivity
~~~~~~~~~~~~~~~

.. attributetable:: CustomActivity

.. autoclass:: CustomActivity
    :members:

Permissions
~~~~~~~~~~~~

.. attributetable:: Permissions

.. autoclass:: Permissions
    :members:

PermissionOverwrite
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: PermissionOverwrite

.. autoclass:: PermissionOverwrite
    :members:

ShardInfo
~~~~~~~~~~~

.. attributetable:: ShardInfo

.. autoclass:: ShardInfo()
    :members:

SessionStartLimit
~~~~~~~~~~~~~~~~~

.. attributetable:: SessionStartLimit

.. autoclass:: SessionStartLimit()
    :members:

SystemChannelFlags
~~~~~~~~~~~~~~~~~~~~

.. attributetable:: SystemChannelFlags

.. autoclass:: SystemChannelFlags()
    :members:

MessageFlags
~~~~~~~~~~~~

.. attributetable:: MessageFlags

.. autoclass:: MessageFlags()
    :members:

PublicUserFlags
~~~~~~~~~~~~~~~

.. attributetable:: PublicUserFlags

.. autoclass:: PublicUserFlags()
    :members:
