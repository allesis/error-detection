from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class HumanErrorEvent:
    ErrorNumber: int
    StartTime: int
    EndTime: int
    Description: str
    Fix: int
