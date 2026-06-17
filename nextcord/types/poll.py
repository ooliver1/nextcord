# SPDX-License-Identifier: MIT

from typing import List, Literal, Optional, TypedDict

from typing_extensions import NotRequired

from .emoji import PartialEmoji

LayoutType = Literal[1]


class PollMedia(TypedDict):
    text: NotRequired[str]
    emoji: NotRequired[PartialEmoji]


class PollCreateMedia(TypedDict):
    text: NotRequired[str]
    emoji: NotRequired[PartialEmoji]


class PollAnswer(TypedDict):
    answer_id: int
    poll_media: PollMedia


class PollCreateAnswer(TypedDict):
    poll_media: PollCreateMedia


class PollAnswerCount(TypedDict):
    id: int
    count: int
    me_voted: bool


class PollCreateRequest(TypedDict):
    question: PollMedia
    answers: List[PollCreateAnswer]
    duration: NotRequired[int]
    allow_multiselect: NotRequired[bool]
    layout_type: NotRequired[LayoutType]


class PollResults(TypedDict):
    is_finalized: bool
    answer_counts: List[PollAnswerCount]


class Poll(TypedDict):
    question: PollMedia
    answers: List[PollAnswer]
    expiry: Optional[str]
    allow_multiselect: bool
    layout_type: LayoutType
    results: NotRequired[PollResults]
