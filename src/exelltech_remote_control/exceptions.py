class ExelltechError(Exception):
    """Base exception for this library."""


class CommunicationError(ExelltechError):
    """Raised when a command could not be sent to or acknowledged by the device."""
