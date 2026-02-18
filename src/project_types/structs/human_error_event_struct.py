from dataclasses import dataclass

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


@dataclass(frozen=True, kw_only=True)
class HumanErrorEvent:
    ErrorNumber: int
    StartTime: int
    EndTime: int
    Description: str
    Fix: int

    @classmethod
    def from_dict(cls, d: dict) -> Self:
        """Construct a HumanErrorEvent from a dict.
        Dict should contain an entry for each element of the struct,
        even if the entry is empty.
        Checks to ensure the dict represents a valid entry.
        If a fix time is not a valid int it will be replaced with `None`.
        Raises an error if the dict is not able to be parsed to the struct.
        """
        if len(d) != len(cls.__dataclass_fields__):
            raise KeyError(
                f"HumanErrorEvent Dict param is of length {len(d)} expected length {len(cls.__dataclass_fields__)}"
            )

        for field in cls.__dataclass_fields__:
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

        new_dict = dict(zip(cls.__dataclass_fields__, d.items()))

        return cls(**new_dict)
