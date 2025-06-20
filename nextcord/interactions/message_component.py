# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Tuple, cast

from .. import utils
from ..member import Member
from ..message import Message
from ..role import Role
from ..types import interactions as interaction_payloads
from ..user import User
from .base import (
    Interaction,
)

__all__ = ("MessageComponentInteraction",)

if TYPE_CHECKING:
    from ..state import ConnectionState
    from ..types.interactions import (
        ComponentInteractionData as InteractionData,
        MessageComponentInteraction as MessageComponentPayload,
    )

MISSING: Any = utils.MISSING


class MessageComponentInteraction(Interaction):
    """Represents the interaction for all messsage components.

    This interaction is a subclass of :class:`Interaction`.

    This interaction gets triggered by a :class:`nextcord.ui.View`.

    .. container:: operations

        .. describe:: x == y

            Checks if two interactions are equal.

        .. describe:: x != y

            Checks if two interactions are not equal.

        .. describe:: hash(x)

            Returns the interaction's hash.

    Attributes
    ----------
    message: :class:`Message`
        The message the component is attached to.
    component_id: :class:`str`
        The ID of the component that triggered the interaction.
    value: :class:`str`
        The value of the component that triggered the interaction.
    """

    __slots__: Tuple[str, ...] = (
        "message",
        "component_id",
        "value",
    )

    def __init__(self, *, data: MessageComponentPayload, state: ConnectionState) -> None:
        super().__init__(data=data, state=state)

    def _from_data(self, data: MessageComponentPayload) -> None:
        super()._from_data(data=data)

        self.data: InteractionData = data.get("data")
        self.component_id = self.data["custom_id"]
        self.value = self.data.get("values")

        message = data["message"]
        self.message = self._state._get_message(int(message["id"])) or Message(
            state=self._state, channel=self.channel, data=message  # type: ignore
        )

    def _resolve_users(self) -> list[User | Member]:
        """Returns a :class:`list` of resolved :class:`User` objects from the interaction data.
        If possible, it will return a :class:`list` of resolved :class:`Member` objects instead.


        Returns
        -------
        :class:`list`[:class:`User` | :class:`Member`]
            List of resolved users, or members if possible.
        """
        ret = []
        data = self.data
        data = cast(interaction_payloads.ApplicationCommandInteractionData, data)

        if "resolved" in data:
            # If we can, we will return Member objects instead of User.
            # If we don't have a guild object though, return User objects.
            if "members" in data["resolved"] and self.guild is not None:
                member_payloads = data["resolved"]["members"]
                # Because the payload is modified further down, a copy is made to avoid affecting methods or
                #  users that read from interaction.data further down the line.
                for member_id, member_payload in member_payloads.copy().items():
                    # If a member isn't in the cache, construct a new one.
                    if (
                        not (member := self.guild.get_member(int(member_id)))
                        and "users" in data["resolved"]
                    ):
                        user_payload = data["resolved"]["users"][member_id]
                        # This is required to construct the Member.
                        member_payload["user"] = user_payload
                        member = Member(data=member_payload, guild=self.guild, state=self._state)  # type: ignore

                    if member is not None:
                        ret.append(member)

            # If we have resolved members + guild, we don't want to go through the users. Hence, the elif.
            elif "users" in data["resolved"]:
                resolved_users_payload = data["resolved"]["users"]
                ret.extend(
                    [
                        self._state.create_user(user_payload)
                        for user_payload in resolved_users_payload.values()
                    ]
                )

        return ret

    def _resolve_messages(self) -> list[Message]:
        """Returns a :class:`list` of resolved :class:`Message` objects from the interaction data.

        Returns
        -------
        :class:`list`[:class:`Message`]
            A list of resolved messages.
        """
        ret = []
        data = self.data
        data = cast(interaction_payloads.ApplicationCommandInteractionData, data)

        if "resolved" in data and "messages" in data["resolved"]:
            message_payloads = data["resolved"]["messages"]
            for msg_id, msg_payload in message_payloads.items():
                if not (message := self._state._get_message(int(msg_id))):
                    message = Message(channel=self.channel, data=msg_payload, state=self._state)  # type: ignore

                ret.append(message)

        return ret

    def _resolve_roles(self) -> list[Role]:
        """Returns a :class:`list` of resolved :class:`Role` objects from the interaction data.

        Returns
        -------
        :class:`list`[:class:`Role`]
            A list of resolved roles.
        """
        ret = []
        data = self.data
        data = cast(interaction_payloads.ApplicationCommandInteractionData, data)

        if "resolved" in data and "roles" in data["resolved"]:
            role_payloads = data["resolved"]["roles"]
            for role_id, role_payload in role_payloads.items():
                # if True:  # Use this for testing payload -> Role
                if self.guild is None:
                    raise TypeError("self.guild cannot be None when resolving a Role")

                if not (role := self.guild.get_role(int(role_id))):
                    role = Role(guild=self.guild, state=self._state, data=role_payload)

                ret.append(role)

        return ret
