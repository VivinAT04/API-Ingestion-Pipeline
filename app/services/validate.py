def validate_record(record: dict) -> bool:
    if not record:
        return False

    if "source" not in record:
        return False

    return True