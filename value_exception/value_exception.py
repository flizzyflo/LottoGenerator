


class ValueException(Exception):

    """Exception class to handle wrong input values for start value, end value and amount of required numbers."""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)