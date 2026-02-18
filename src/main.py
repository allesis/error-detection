import sys
from pathlib import Path
import read_in_data

DATA_PATH: str = "test-data/train"


def main() -> None:
    eye_tracker_events = read_in_data.read_in_source_data(
        Path(f"{DATA_PATH}/source/{sys.argv[1]}")
    )
    human_error_events = read_in_data.read_in_target_data(
        Path(f"{DATA_PATH}/target/{sys.argv[1]}")
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(0)
