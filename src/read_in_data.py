import csv
from pathlib import Path
from os.path import splitext
from project_types.errors.file_type_error import FileTypeError
from project_types.structs.eye_tracker_event_struct import EyeTrackerEvent
from project_types.structs.human_error_event_struct import HumanErrorEvent


def read_in_source_data(file_path: Path) -> [EyeTrackingEvent]:
    """Reads in the csv file located at file_path
    and returns an array of `EyeTrackerEvent`s parsed from the file
    """
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(
            f"Could not open file located at path: {file_path}\nPlease ensure this file exists."
        )

    _, file_ext = splitext(file_path)
    if not file_ext == ".csv":
        raise FileTypeError(
            f"Provide file with path:\n\t{file_path}\nDoes not have correct file extension of '.csv'\n\tFound `{file_ext}`"
        )

    eye_tracker_events: [EyeTrackerEvent] = []
    with open(file_path, mode="r") as file:
        csvFile: csv.DictReader = csv.DictReader(file)
        for line_dict in csvFile:
            tracking_event: EyeTrackerEvent = EyeTrackerEvent.from_dict(line_dict)
            eye_tracker_events.append(tracking_event)

    return eye_tracker_events


def read_in_target_data(file_path: Path) -> [HumanErrorEvent]:
    """Reads in the csv file located at file_path
    and returns an array of `HumanErrorEvent`s parsed from the file
    """
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(
            f"Could not open file located at path: {file_path}\nPlease ensure this file exists."
        )

    _, file_ext = splitext(file_path)
    if not file_ext == ".csv":
        raise FileTypeError(
            f"Provide file with path:\n\t{file_path}\nDoes not have correct file extension of '.csv'\n\tFound `{file_ext}`"
        )

    human_error_events: [HumanErrorEvent] = []

    with open(file_path, mode="r") as file:
        csvFile: csv.DictReader = csv.DictReader(file)
        for line_dict in csvFile:
            error_event: HumanErrorEvent = HumanErrorEvent.from_dict(line_dict)
            human_error_events.append(error_event)

    return human_error_events
