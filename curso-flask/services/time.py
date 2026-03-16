from datetime import datetime, timezone

def now_utc():
    """Return timezone-aware current UTC datetime."""
    return datetime.now()


def parse_datetime(value: str):
    """Try parsing a date/time string into a timezone-aware datetime (UTC).

    Supports several common formats. Returns None if parsing fails or
    if `value` is falsy.
    """
    if not value:
        return None
    formats = ("%Y-%m-%d", "%Y-%m-%d %H:%M", "%d/%m/%y", "%d/%m/%y %H:%M")
    for fmt in formats:
        try:
            dt = datetime.strptime(value, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None