
def convert_seconds_into_legible_time(seconds: int) -> str:
    """
        Method that help to convert seconds into legible string time
    """
    # convert seconds to ms
    ms = round(seconds * 1000, 2)
    legible_time_str = f"{ms} ms"
    return legible_time_str