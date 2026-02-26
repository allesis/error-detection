import type_enforced
from dataclasses import dataclass
from project_types.errors.regex_match_error import RegexMatchError
from util.time_to_duration import time_to_duration

# Some of the fields do not share have the same name in the csv file
# Here we define the mapping between the two
# Left hand side should be name as it appears in class def
# Right hand side should be name as it appears in first row of csv file
EVENT_FIELD_TO_NAME_MAPPING = {
    "ErrorNumber": "Error #",
    "StartTime": "Time start",
    "EndTime": "Time end",
    "Description": "Description",
    "Fix": "Fix",
}


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
@dataclass(frozen=True, kw_only=True)
class HumanErrorEvent:
    ErrorNumber: int
    StartTime: int
    EndTime: int
    Description: str
    Fix: int
    ErrorIsFixed: bool

    @classmethod
    def from_dict(cls, d: dict) -> HumanErrorEvent:
        """Construct a HumanErrorEvent from a dict.
        Dict should contain an entry for each element of the struct,
        even if the entry is empty.
        Checks to ensure the dict represents a valid entry.
        If a fix time is not a valid int it will be replaced with `None`.
        Raises an error if the dict is not able to be parsed to the struct.
        """

        def convert_dict_typing(d: dict) -> dict:
            """Updates the typing of the provided dict
            to align with classes typing.
            This mapping is as follows:
                ErrorNumber: int -> int (No change)
                StartTime: str -> int (maps time in hh:mm:ss format to milliseconds)
                EndTime: str -> int (maps time in hh:mm:ss format to milliseconds)
                Description: str -> str (No change)
                Fix: str -> int (maps time in hh:mm:ss format to milliseconds; maps to -1 if str is not in hh:mm:ss format)
                ErrorIsFixed: gone -> bool (Should not be present in original dict; if True if Fix is mapped successfully, False otherwise)
            """

            type_corrected_dict: dict = d
            type_corrected_dict.update({"Description": d.pop("Description")})

            type_corrected_dict.update({"ErrorNumber": int(d.pop("ErrorNumber"))})

            try:
                type_corrected_dict.update(
                    {"StartTime": time_to_duration(d.pop("StartTime"))}
                )
                type_corrected_dict.update(
                    {"EndTime": time_to_duration(d.pop("EndTime"))}
                )
            except RegexMatchError as e:
                raise RuntimeError(f"Failed to read in target data\n{e}")

            fix_time = d.pop("Fix")
            if fix_time == "DNF":
                type_corrected_dict.update({"Fix": -1})
                type_corrected_dict["ErrorIsFixed"] = False
            else:
                type_corrected_dict.update({"Fix": time_to_duration(fix_time)})
                type_corrected_dict["ErrorIsFixed"] = True

        class_fields: dict[str] = cls.__dataclass_fields__.copy()
        class_fields.pop("ErrorIsFixed")

        if len(d) != len(class_fields):
            raise KeyError(
                f"HumanErrorEvent Dict param is of length {len(d)} expected length {len(cls.__dataclass_fields__)}"
            )

        for field in class_fields:
            try:
                d[EVENT_FIELD_TO_NAME_MAPPING[field]]
            except KeyError:
                raise KeyError(
                    f"The key {EVENT_FIELD_TO_NAME_MAPPING[field]} was not found in the provided dict:\n\t{dict}\nError:\n\t{e}"
                )
            except Exception as e:
                # Out of the ordinary error
                raise type(e)(
                    f"Error with parsing EyeTrackerEvent from dict:\n\t{d}\nError:\n\t{e}"
                )

        name_corrected_dict: dict = dict(
            zip(class_fields, map(lambda x: x[1], d.items()))
        )

        type_corrected_dict: dict = name_corrected_dict

        convert_dict_typing(type_corrected_dict)

        # `new_dict` is now a valid dict to parse to
        return cls(**type_corrected_dict)
