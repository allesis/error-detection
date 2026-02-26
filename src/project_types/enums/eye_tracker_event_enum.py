from enum import Enum


class EyeTrackerEventEnum(str, Enum):
    FIXATION = "fixation"
    SACCADE = "saccade"
    GLANCE = "glance"

    @classmethod
    def from_string(cls, s: str) -> EyeTrackerEventEnum:
        print("HERE")
        return cls[s.strip().lower()]
