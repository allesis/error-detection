from enum import Enum


class EyeTrackerValidityEnum(Enum):
    PARTIAL = "partial", 1
    WHOLE = "whole", 2

    @classmethod
    def from_str(self, s) -> EyeTrackerEventEnum:
        return self(s.strip().lower())
