# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Tuple

from .. import utils
from ..message import Message
from .base import (
    Interaction,
)

__all__ = ("ModalSubmitInteraction",)

if TYPE_CHECKING:
    from ..state import ConnectionState
    from ..types.interactions import (
        ModalSubmitInteraction as ModalSubmitPayload,
        ModalSubmitInteractionData as InteractionData,
    )

MISSING: Any = utils.MISSING


class ModalSubmitInteraction(Interaction):
    """Represents the interaction for all modal submits.

    This interaction is a subclass of :class:`Interaction`.

    This interaction is triggered by a :class:`nextcord.ui.Modal`

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
        The message the modal was called from.
    modal_id: :class:`int`
        The ID of the modal that triggered the interaction.
    """

    __slots__: Tuple[str, ...] = (
        "modal_id",
        "message",
    )

    def __init__(self, *, data: ModalSubmitPayload, state: ConnectionState) -> None:
        super().__init__(data=data, state=state)

    def _from_data(self, data: ModalSubmitPayload) -> None:
        super()._from_data(data=data)

        self.data: InteractionData = data.get("data")
        self.modal_id = self.data["custom_id"]
        self.message: Optional[Message]

        try:
            message = data["message"]
            self.message = self._state._get_message(int(message["id"])) or Message(
                state=self._state, channel=self.channel, data=message  # type: ignore
            )
        except KeyError:
            self.message = None
