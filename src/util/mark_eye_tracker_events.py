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
            if (
                # With this we assume that error_start_time <= error_end_time
                # and event_start_time <= event_end_time
                error_start_time <= event_end_time  # error starts before event ends
                and error_end_time >= event_start_time  # error ends before event starts
            ):
                is_error = True

        return (event, is_error)

    return list(
        map(
            lambda event: mark_eye_tracker_event(event, errors, global_start_time),
            events,
        )
    )
