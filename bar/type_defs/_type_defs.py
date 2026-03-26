"""Public type definitions for bar."""

from enum import Enum
from typing import NewType, TypedDict

# Scalar aliases
JobId = NewType("JobId", str)
Score = float

# Enums
class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"


# TypedDicts
class JobResult(TypedDict):
    """Result payload for a completed job."""

    job_id: str
    status: str
    score: float


# Private — not exported
_InternalState = dict[str, object]
