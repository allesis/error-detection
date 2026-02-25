import re
import type_enforced
from project_types.errors.regex_match_error import RegexMatchError

TIME_REGEX_PATTERN: str = "^\\d\\d:\\d\\d:\\d\\d$"
TIME_REGEX: re.Pattern[anystr] = re.compile(TIME_REGEX_PATTERN)


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def time_to_duration(time_str: str) -> int:
    matched_str = TIME_REGEX.match(time_str)
    if matched_str is None:
        raise RegexMatchError(
            f"Failed to find match for pattern:\n\t{TIME_REGEX_PATTERN}\nIn provided string:\n\t{time_str}"
        )

    if not matched_str == time_str:
        raise RegexMatchError(
            f"Provided time string:\n\t{time_str}\nIs not a valid time string"
        )

    hours = int(time_str[0:2])
    minutes = int(time_str[3:5])
    seconds = int(time_str[6:8])

    print(hours)
    print(minutes)
    print(seconds)
    return 0
