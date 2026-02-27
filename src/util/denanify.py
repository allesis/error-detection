import type_enforced
import math


@type_enforced.Enforcer(enabled=True, strict=True, clean_traceback=True)
def denanify(l: list[float]) -> list[float]:
    return list(map(lambda x: 0.0 if math.isnan(x) else x, l))
