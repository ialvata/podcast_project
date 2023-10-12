"""
Module with utilities for db folder.
Includes:
    - Costume Exception classes
"""


class ConfigFormatError(Exception):
    def __init__(self, section, filename):
        """
        Class representing an error in the format of the config file for the database.
        """
        self.section = section
        self.filename = filename

    def __str__(self) -> str:
        return f"Section {self.section} not found in the {self.filename} file"


class ConfigEmptyError(Exception):
    """
    Class representing an error in the format of the config file for the database.
    """

    def __str__(self) -> str:
        return "This Config has no parameters"


class CursorNoneError(Exception):
    """
    Class triggered when cursor is not found.
    """

    def __str__(self) -> str:
        return "No cursor was found!"


class ConnectFirstError(Exception):
    """
    Class triggered when connect has been done yet, and we use other methods from db.
    """

    def __str__(self) -> str:
        return "Please do db.connect() first!"
