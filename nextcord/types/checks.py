# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING, Any, Callable, Coroutine, TypeVar, Union

if TYPE_CHECKING:
    from nextcord.application_command import ClientCog

    from ..interactions import Interaction

    T = TypeVar("T")

    Coro = Coroutine[Any, Any, T]
    MaybeCoro = Union[T, Coro[T]]
    CoroFunc = Callable[..., Coro[Any]]
    ApplicationCheck = Union[
        Callable[[ClientCog, Interaction[Any]], MaybeCoro[bool]],
        Callable[[Interaction[Any]], MaybeCoro[bool]],
    ]
    ApplicationHook = Union[
        Callable[[ClientCog, Interaction[Any]], Coro[Any]], Callable[[Interaction[Any]], Coro[Any]]
    ]
    ApplicationErrorCallback = Union[
        Callable[[ClientCog, Interaction[Any], Exception], Coro[Any]],
        Callable[[Interaction[Any], Exception], Coro[Any]],
    ]
