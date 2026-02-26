import sys
import type_enforced
import read_in_data
from pathlib import Path
from util.mark_eye_tracker_events import mark_eye_tracker_events
from util.process_marked_events import process_marked_events

DATA_PATH: str = "data/train"


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def main() -> None:
    eye_tracker_events = read_in_data.read_in_source_data(
        Path(f"{DATA_PATH}/source/{sys.argv[1]}")
    )
    human_error_events = read_in_data.read_in_target_data(
        Path(f"{DATA_PATH}/target/{sys.argv[1]}")
    )

    marked_eye_tracker_events = mark_eye_tracker_events(
        eye_tracker_events, human_error_events
    )

    (train_data, target_data) = process_marked_events(marked_eye_tracker_events)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Encountered an error:\n\t{e}")
        exit(0)
