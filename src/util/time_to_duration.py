import re
import type_enforced
from project_types.errors.regex_match_error import RegexMatchError


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def time_to_duration(time_str: str) -> int:
    _TIME_REGEX_PATTERN: str = "^\\d\\d:\\d\\d:\\d\\d$"
    _TIME_REGEX: re.Pattern[anystr] = re.compile(_TIME_REGEX_PATTERN)
    regex_match = _TIME_REGEX.match(time_str)
    if regex_match is None:
        raise RegexMatchError(
            f"Failed to find match for pattern:\n\t{_TIME_REGEX_PATTERN}\nIn provided string:\n\t{time_str}"
        )

    if not regex_match.string == time_str:
        raise RegexMatchError(
            f"Provided time string:\n\t{time_str}\nIs not a valid time string"
        )

    hours = int(time_str[0:2])
    minutes = int(time_str[3:5])
    seconds = int(time_str[6:8])

    duration: int = (hours * 60 * 60) + (minutes * 60) + (seconds)
    return duration
