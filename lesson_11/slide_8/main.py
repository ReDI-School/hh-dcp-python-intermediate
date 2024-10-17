
def validate(number) -> bool:
    if number < 0:
        raise ValueError("Value must be greater than 0")
    return True

