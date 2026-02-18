import csv
from project_types.structs.eye_tracker_event_struct import EyeTrackerEvent


def main() -> None:
    eye_tracker_events: [EyeTrackerEvent] = []
    with open("test-data/sample.csv", mode="r") as file:
        csvFile: csv.DictReader = csv.DictReader(file)
        for line_dict in csvFile:
            event = EyeTrackerEvent.from_dict(line_dict)
            eye_tracker_events.append(event)

    for event in eye_tracker_events:
        print(event)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("error")
        print(e)
        exit(0)
