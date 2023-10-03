# SPDX-License-Identifier: MIT

from typing import List, TypedDict

from .appinfo import PartialAppInfo
from .guild import UnavailableGuild
from .user import User


class SessionStartLimit(TypedDict):
    total: int
    remaining: int
    reset_after: int
    max_concurrency: int


class Gateway(TypedDict):
    url: str


class GatewayBot(Gateway):
    shards: int
    session_start_limit: SessionStartLimit


class HasShardId(TypedDict):
    __shard_id__: int


class Ready(TypedDict):
    v: int
    user: User
    guilds: List[UnavailableGuild]
    session_id: str
    shard: List[int]
    application: PartialAppInfo


class ReadyWithShardId(Ready, HasShardId):
    pass
