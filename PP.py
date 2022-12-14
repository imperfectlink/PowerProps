"""
PP - PowerProps
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of the random keycaps as strings.

    :param kind: Optional "kind" of keycaps.
    :type kind: list[str] or None
    :raise pp.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["Capslock", "Spacebar", "Shift"]
