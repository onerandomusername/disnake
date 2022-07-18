.. currentmodule:: disnake

.. _discord_ui_kit:

Bot UI Kit
-------------

The library has helpers to help create component-based UIs.

View
~~~~~~~

.. attributetable:: disnake.ui.View

.. autoclass:: disnake.ui.View
    :members:

ActionRow
~~~~~~~~~~

.. attributetable:: disnake.ui.ActionRow

.. autoclass:: disnake.ui.ActionRow
    :members:

Item
~~~~~~~

.. attributetable:: disnake.ui.Item

.. autoclass:: disnake.ui.Item
    :members:

WrappedComponent
~~~~~~~~~~~~~~~~

.. attributetable:: disnake.ui.WrappedComponent

.. autoclass:: disnake.ui.WrappedComponent
    :members:

Button
~~~~~~~

.. attributetable:: disnake.ui.Button

.. autoclass:: disnake.ui.Button
    :members:
    :inherited-members:

.. autofunction:: disnake.ui.button(cls=disnake.ui.Button, *, style=ButtonStyle.secondary, label=None, disabled=False, custom_id=..., url=None, emoji=None, row=None)

Select
~~~~~~~

.. attributetable:: disnake.ui.Select

.. autoclass:: disnake.ui.Select
    :members:
    :inherited-members:

.. autofunction:: disnake.ui.select(cls=disnake.ui.Select, *, custom_id=..., placeholder=None, min_values=1, max_values=1, options=..., disabled=False, row=None)

Modal
~~~~~

.. attributetable:: disnake.ui.Modal

.. autoclass:: disnake.ui.Modal
    :members:

TextInput
~~~~~~~~~

.. attributetable:: disnake.ui.TextInput

.. autoclass:: disnake.ui.TextInput
    :members:
