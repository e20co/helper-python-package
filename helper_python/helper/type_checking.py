from typing import Any


def check_value(value: Any, value_name: str, value_type: Any) -> bool:
    """
    Check if a value is not `None` and a subclass of a given type.

    Args:
        value (Any): The value to check.
        value_name (str): The value name, which is used in the exception messages.
        value_type (Any): The type of the value.

    Returns:
        bool: `True` if the value is not `None` and a subclass of a given type,
              otherwise `False.`
    """
    value_okay = False

    if value is not None:
        if isinstance(value, value_type):
            value_okay = True
        else:
            message = "{} has to be an instance of {} or a subclass of it and not {}.".format(value_name, value_type, type(value))
            raise TypeError(message)
    else:
        message = "{} cannot be `None`.".format(value_name)
        raise ValueError(message)

    return value_okay


def check_string(value: str, value_name: str) -> bool:
    """
    Check if a string is not None, a string or subclass of it and not empty.

    Args:
        value (str): The value to check.
        value_name (str): The value name, which is used in the exception messages.

    Returns:
        bool: `True` if the string is not None, a subclass of string and not empty,
              otherwise `False`.
    """
    string_okay = False
    value_type = str

    if check_value(value, value_name, value_type):
        if value:
            string_okay = True
        else:
            message = "{} cannot be empty.".format(value_name)
            raise ValueError(message)

    return string_okay
