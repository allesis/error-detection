from project_types.structs.eye_tracker_event_struct import EyeTrackerEvent
import type_enforced


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def process_marked_events(
    marked_events: list[tuple[EyeTrackerEvent, bool]],
) -> tuple[list[list[float]], list[bool]]:
    target_data = list(map(lambda x: x[1], marked_events))
    training_data = list(
        map(
            lambda marked_event: marked_event[0].to_list(),
            marked_events,
        )
    )

    return (training_data, target_data)
