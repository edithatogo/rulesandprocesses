from __future__ import annotations

from datetime import date, timedelta
from typing import Iterable


def _is_summer_exclusion(day: date) -> bool:
    return (day.month == 12 and day.day >= 25) or (day.month == 1 and day.day <= 15)


def add_working_days(
    start: date,
    n: int,
    holidays: Iterable[date] | None = None,
    include_oia_summer_exclusion: bool = True,
) -> date:
    blocked_days = set(holidays or [])
    current = start
    remaining = n
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() >= 5:
            continue
        if current in blocked_days:
            continue
        if include_oia_summer_exclusion and _is_summer_exclusion(current):
            continue
        remaining -= 1
    return current
