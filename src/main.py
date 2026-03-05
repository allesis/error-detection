import sys
import traceback
from sklearn.decomposition import PCA
import numpy
import type_enforced
import read_in_data
from pathlib import Path
from util.mark_eye_tracker_events import mark_eye_tracker_events
from util.process_marked_events import process_marked_events
from util.denanify import denanify
from util.plot import plot_results
from sklearn.neighbors import KNeighborsClassifier

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

    denanned_training_data = numpy.array(list(map(lambda l: denanify(l), train_data)))
    numpified_target_data = numpy.array(list(map(lambda b: 1 if b else 0, target_data)))

    test_eye_tracker_events = read_in_data.read_in_source_data(
        Path(f"{DATA_PATH}/source/{sys.argv[2]}")
    )
    test_human_error_events = read_in_data.read_in_target_data(
        Path(f"{DATA_PATH}/target/{sys.argv[2]}")
    )

    test_marked_eye_tracker_events = mark_eye_tracker_events(
        test_eye_tracker_events, test_human_error_events
    )
    (test_data, _) = process_marked_events(test_marked_eye_tracker_events)
    denanned_test_data = numpy.array(list(map(lambda l: denanify(l), test_data)))

    model_classes = [KNeighborsClassifier]

    for model_class in model_classes:
        model = model_class()

        model.fit(denanned_training_data, numpified_target_data)
        prediction: numpy.ndarray = model.predict(denanned_test_data)

        plot_results(denanned_test_data, prediction, name=f"test-plot.svg")


if __name__ == "__main__":
    try:
        main()
    except:
        print(traceback.format_exc())
        exit(0)
