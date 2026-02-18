from dataclasses import dataclass
from project_types.enums.eye_tracker_event_enum import EyeTrackerEventEnum as EventEnum
from project_types.enums.eye_tracker_validity_enum import (
    EyeTrackerValidityEnum as ValidityEnum,
)

# Some of the fields do not share have the same name in the csv file
# Here we define the mapping between the two
# Left hand side should be name as it appears in class def
# Right hand side should be name as it appears in first row of csv file
EVENT_FIELD_TO_NAME_MAPPING = {
    "Recording": "Recording",
    "Participant": "Participant",
    "Timeline": "Timeline",
    "TOI": "TOI",
    "Interval": "Interval",
    "Media": "Media",
    "AOITag": "AOI_tag",
    "EventType": "Event_type",
    "Validity": "Validity",
    "EventIndex": "EventIndex",
    "Start": "Start",
    "Stop": "Stop",
    "Duration": "Duration",
    "AOI": "AOI",
    "HitProportion": "Hit_proportion",
    "FixationPointX": "FixationPointX",
    "FixationPointY": "FixationPointY",
    "AveragePupilDiameter": "Average_pupil_diameter",
    "SaccadeDirection": "Saccade_direction",
    "AverageVelocity": "Average_velocity",
    "PeakVelocity": "Peak_velocity",
    "SaccadeAmplitude": "Saccade_amplitude",
    "StartAOI": "Start_AOI",
    "LandingAOI": "Landing_AOI",
    "StartPositionX": "Start_position_X",
    "StartPositionY": "Start_position_Y",
    "LandingPositionX": "Landing_position_X",
    "LandingPositionY": "Landing_position_Y",
    "GlanceAOI": "Glance_AOI",
    "GlancePreviousAOI": "Glance_previous_AOI",
    "GlanceNextAOI": "Glance_next_AOI",
}


# TODO: AOIs are not really strings
# They can be more accurately modeled as a enum
# Since once we begin we should know all possible values
# If this can't be done programatically, we can probably
# do it by hard coding the values in a enum and using that
# This would be a less ideal, but still less fragile approach
@dataclass(frozen=True, kw_only=True)
class EyeTrackerEvent:
    Recording: str
    Participant: str
    Timeline: str
    TOI: str
    Interval: int
    Media: str
    AOITag: str
    EventType: EventEnum
    Validity: ValidityEnum
    EventIndex: int
    Start: int
    Stop: int
    Duration: int
    AOI: str
    HitProportion: int
    FixationPointX: float
    FixationPointY: float
    AveragePupilDiameter: float
    SaccadeDirection: float
    AverageVelocity: float
    PeakVelocity: float
    SaccadeAmplitude: float
    StartAOI: str
    LandingAOI: str
    StartPositionX: float
    StartPositionY: float
    LandingPositionX: float
    LandingPositionY: float
    GlanceAOI: str
    GlancePreviousAOI: str
    GlanceNextAOI: str

    @classmethod
    def from_dict(cls, d: dict) -> Self:
        """Construct a EyeTrackerEvent from a dict.
        Dict should contain an entry for each element of the struct,
        even if the entry is empty.
        Checks to ensure the dict represents a valid entry.
        Raises an error if the dict is not able to be parsed to the struct.
        """

        # Ensure dict is correct length
        if len(d) != len(cls.__dataclass_fields__):
            raise KeyError(
                f"HumanErrorEvent Dict param is of length {len(d)} expected length {len(cls.__dataclass_fields__)}"
            )

        # Ensure dict has all the correct fields
        for field in cls.__dataclass_fields__:
            try:
                d[EVENT_FIELD_TO_NAME_MAPPING[field]]
            except KeyError as e:
                raise KeyError(
                    f"The key {EVENT_FIELD_TO_NAME_MAPPING[field]} was not found in the provided dict:\n\t{dict}\nError:\n\t{e}"
                )
            except Exception as e:
                # Out of the ordinary error
                raise type(e)(
                    f"Error with parsing EyeTrackerEvent from dict:\n\t{d}\nError:\n\t{e}"
                )

        new_dict = dict(zip(cls.__dataclass_fields__, d.items()))

        return cls(**new_dict)
