"""Public type definitions for foo."""

from typing import NewType, TypedDict

# Scalar aliases
UserId = NewType("UserId", int)
EventName = str

# TypedDicts
class EventRecord(TypedDict):
    """A raw event row."""

    user_id: int
    event: str
    ts: float


class UserProfile(TypedDict):
    """Minimal user profile."""

    user_id: int
    name: str
    active: bool


# Private — not exported
_RawRow = dict[str, object]
