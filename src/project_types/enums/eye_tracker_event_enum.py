from enum import Enum


class EyeTrackerEventEnum(Enum):
    FIXATION = "fixation", 1
    SACCADE = "saccade", 2
    GLANCE = "glance", 3

    @classmethod
    def from_str(self, s) -> EyeTrackerEventEnum:
        return self(s.strip().lower())
