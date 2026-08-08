"""Application version and metadata management."""

# Single source of truth for version info
__version__ = "0.5.6"
__author__ = "mikes"
__last_updated__ = "08-Aug-2026"
__license__ = "MIT"
__description__ = "DATA CONVERTER & ENCODER Utility"


def get_version_info() -> dict:
    """Return complete version information as a dictionary."""
    return {
        "version": __version__,
        "author": __author__,
        "last_updated": __last_updated__,
        "license": __license__,
        "description": __description__
    }


def get_version_string(short: bool = False) -> str:
    """Return formatted version string.

    Args:
        short: If True, return only version number (e.g., "0.5.6")
               If False, return full banner (e.g., "DATA CONVERTER v0.5.6")

    Returns:
        Formatted version string
    """
    if short:
        return __version__
    return f"DATA CONVERTER v{__version__}"