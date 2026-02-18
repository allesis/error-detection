import csv
import sys
from project_types.structs.eye_tracker_event_struct import EyeTrackerEvent
from project_types.structs.human_error_event_struct import HumanErrorEvent

DATA_PATH: str = "test-data/train"


def main() -> None:
    eye_tracker_events: [EyeTrackerEvent] = []
    human_error_events: [HumanErrorEvent] = []
    with open(f"{DATA_PATH}/source/{sys.argv[1]}", mode="r") as file:
        csvFile: csv.DictReader = csv.DictReader(file)
        for line_dict in csvFile:
            tracking_event: EyeTrackerEvent = EyeTrackerEvent.from_dict(line_dict)
            eye_tracker_events.append(tracking_event)

    with open(f"{DATA_PATH}/target/{sys.argv[1]}", mode="r") as file:
        csvFile: csv.DictReader = csv.DictReader(file)
        for line_dict in csvFile:
            error_event: HumanErrorEvent = HumanErrorEvent.from_dict(line_dict)
            human_error_events.append(error_event)

    print(
        f"Read in {len(eye_tracker_events)} tracking events\nRead in {len(human_error_events)} error events"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(0)
