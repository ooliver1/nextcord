# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING, Any, Callable, Coroutine, TypeVar, Union

if TYPE_CHECKING:
    from nextcord.application_command import ClientCog

    from ..interactions import Interaction

    T = TypeVar("T")
    InteractionT = TypeVar("InteractionT", bound=Interaction)
    CogT = TypeVar("CogT", bound=ClientCog)

    Coro = Coroutine[Any, Any, T]
    MaybeCoro = Union[T, Coro[T]]
    CoroFunc = Callable[..., Coro[Any]]
    ApplicationCheck = Callable[[InteractionT], MaybeCoro[bool]]
    ApplicationHook = Union[
        Callable[[CogT, InteractionT], Coro[Any]], Callable[[InteractionT], Coro[Any]]
    ]
    ApplicationErrorCallback = Union[
        Callable[[ClientCog, Interaction[Any], Exception], Coro[Any]],
        Callable[[Interaction[Any], Exception], Coro[Any]],
    ]
