# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Optional, Tuple, Union

from .. import utils
from ..types.snowflake import Snowflake
from .base import (
    Interaction,
)

__all__ = ("ApplicationCommandInteraction", "ApplicationAutocompleteInteraction")

if TYPE_CHECKING:
    from ..application_command import (
        BaseApplicationCommand,
        SlashApplicationSubcommand,
        SlashOptionData,
    )
    from ..state import ConnectionState
    from ..types.interactions import (
        ApplicationAutocompleteInteraction as ApplicationAutocompletePayload,
        ApplicationCommandInteraction as ApplicationCommandPayload,
        ApplicationCommandInteractionData as InteractionData,
        ApplicationCommandInteractionDataOption as OptionsPayload,
    )

MISSING: Any = utils.MISSING


class ApplicationCommandInteraction(Interaction):
    """Represents the interaction for all application commands.

    Subclass of :class:`Interaction`.

    .. container:: operations

        .. describe:: x == y

            Checks if two interactions are equal.

        .. describe:: x != y

            Checks if two interactions are not equal.

        .. describe:: hash(x)

            Returns the interaction's hash.

    Attributes
    ----------
    application_command: Union[:class:`SlashApplicationSubcommand`, :class:`BaseApplicationCommand`]
        The application command that triggered the interaction.
    app_command_name: :class:`str`
        The name of the application command that triggered the interaction.
    app_command_id: :class:`int`
        The ID of the application command that triggered the interaction.
    options: List[:class:`SlashOptionData`]
        The application command options that have been given a value.
    """

    __slots__: Tuple[str, ...] = (
        "application_command",
        "app_command_name",
        "app_command_id",
        "options",
    )

    def __init__(self, *, data: ApplicationCommandPayload, state: ConnectionState) -> None:
        super().__init__(data=data, state=state)

        self.application_command: Optional[
            Union[SlashApplicationSubcommand, BaseApplicationCommand]
        ] = None

    def _from_data(self, data: ApplicationCommandPayload) -> None:
        super()._from_data(data=data)

        self.data: InteractionData = data.get("data")
        self.app_command_name: str = self.data["name"]
        self.app_command_id: Snowflake = self.data["id"]

        options = self.data.get("options")
        self.options: List[SlashOptionData] = (
            self._get_application_options(options) if options else []
        )

    def _set_application_command(
        self, app_cmd: Union[SlashApplicationSubcommand, BaseApplicationCommand]
    ) -> None:
        self.application_command = app_cmd

    def _get_application_options(self, options: List[OptionsPayload]) -> List[SlashOptionData]:
        if len(options) == 0:
            # return empty list if no options exist
            return []

        # iterate through options to get inputs
        # The option data gets nested 1x for each subcommand level
        # E.x. "/parent child subcommand" has 2 subcommands -> options get nested 2x
        while "options" in options[0]:
            options = options[0]["options"]  # type: ignore - Key exists only for one type -> accounted for by while loop

            if not options:
                # return empty list if no options exist
                return []

        from ..application_command import (  # Importing here due to circular import issues
            SlashOptionData,
        )

        return [SlashOptionData(option) for option in options]


class ApplicationAutocompleteInteraction(Interaction):
    """Represents the interaction for Autocompletes.

    This interaction is a subclass of :class:`Interaction`.

    .. container:: operations

        .. describe:: x == y

            Checks if two interactions are equal.

        .. describe:: x != y

            Checks if two interactions are not equal.

        .. describe:: hash(x)

            Returns the interaction's hash.

    Attributes
    ----------
    application_command: Union[SlashApplicationSubcommand, BaseApplicationCommand]
        The application command that triggered the interaction.
    app_command_name: :class:`str`
        The name of the application command that triggered the interaction.
    app_command_id: :class:`int`
        The application command ID that triggered the interaction.
    focused_option: :class:`SlashOptionData`
        The option the autocomplete is for.
    options: List[SlashOptionData]
        The application command options that have been given a value.
    """

    __slots__: Tuple[str, ...] = (
        "application_command",
        "app_command_name",
        "app_command_id",
        "options",
    )

    def __init__(self, *, data: ApplicationAutocompletePayload, state: ConnectionState) -> None:
        super().__init__(data=data, state=state)

        self.application_command: Optional[
            Union[SlashApplicationSubcommand, BaseApplicationCommand]
        ] = None

    def _from_data(self, data: ApplicationCommandPayload) -> None:
        super()._from_data(data=data)
        self.data: InteractionData = data.get("data")

        self.app_command_name: str = self.data["name"]
        self.app_command_id: Snowflake = self.data["id"]

        options = self.data.get("options")
        self.options: List[SlashOptionData] = (
            self._get_application_options(options) if options else []
        )

    def _set_application_command(
        self, app_cmd: Union[SlashApplicationSubcommand, BaseApplicationCommand]
    ) -> None:
        self.application_command = app_cmd

    def _get_application_options(self, options: List[OptionsPayload]) -> List[SlashOptionData]:
        if len(options) == 0:
            # return empty list if no options exist
            return []

        # iterate through options to get inputs
        # The option data gets nested 1x for each subcommand level
        # E.x. "/parent child subcommand" has 2 subcommands -> options get nested 2x
        while "options" in options[0]:
            options = options[0]["options"]  # type: ignore - Key exists only for one type -> accounted for by while loop

            if not options:
                # return empty list if no options exist
                return []

        from ..application_command import (  # Importing here due to circular import issues
            SlashOptionData,
        )

        return [SlashOptionData(option) for option in options]

    @property
    def focused_option(self) -> Optional[SlashOptionData]:
        """The application command option the autocomplete was called for."""
        return next((option for option in self.options if option.focused), None)
