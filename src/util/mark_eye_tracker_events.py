from project_types.structs.eye_tracker_event_struct import EyeTrackerEvent
from project_types.structs.human_error_event_struct import HumanErrorEvent
import type_enforced


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def mark_eye_tracker_events(
    events: list[EyeTrackerEvent], errors: list[HumanErrorEvent]
) -> list[tuple[EyeTrackerEvent, bool]]:
    """Takes a list of events and a list of errors and returns a list of tuples indicating if each event was part of an error"""
    global_start_time = events[0].Start

    def mark_eye_tracker_event(
        event: EyeTrackerEvent, errors: lis[HumanErrorEvent], global_start_time: int
    ) -> tuple[EyeTrackerEvent, bool]:
        is_error = False

        event_start_time = (event.Start - global_start_time) / 1000
        event_end_time = (event.Stop - global_start_time) / 1000
        for error in errors:
            error_start_time = error.StartTime
            error_end_time = error.EndTime
            if error_end_time < event_start_time or event_end_time < error_start_time:
                # FIX: Bad reverse logic, we should have the opposite check
                is_error = False
            else:
                is_error = True

        return (event, is_error)

    return list(
        map(
            lambda event: mark_eye_tracker_event(event, errors, global_start_time),
            events,
        )
    )
