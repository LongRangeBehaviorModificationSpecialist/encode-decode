"""External configuration for menu items and application settings."""

from dataclasses import dataclass, field
from rich.console import Console
from typing import Dict, List, Callable, Any, Optional


c = Console()


@dataclass
class MenuItem:
    """Represents a single menu item configuration."""
    key: str
    label: str
    description: Optional[str] = None
    handler_name: Optional[str] = None  # Name of method to call

    def __post_init__(self):
        # Validate key is string and non-empty
        if not isinstance(self.key, str) or not self.key.strip():
            raise ValueError("Menu item key must be a non-empty string")


@dataclass
class AppConfig:
    """Central application configuration."""

    # Application metadata
    app_name: str = "DATA CONVERTER & ENCODER"
    version_source: str = "versions"  # Module to load version from

    # Display settings
    console_width: int = 80
    show_credits: bool = True
    credits_justify: str = "left"

    # Colors (Rich color codes)
    title_color: str = "dodger_blue1"
    header_style: str = "bold #2070b2"
    exit_text_color: str = "#d700d7"
    warning_color: str = "bright_yellow"
    success_color: str = "bright_green"

    # Continuation prompt settings
    continue_prompt_text: str = "Would you like to return to the main menu?"
    continue_prompt_default: str = "y"
    continue_prompt_choices: List[str] = field(
        default_factory=lambda: ["y", "n", ""]
    )
    show_separator_line: bool = True

    # Menu configuration
    menu_items: Dict[str, MenuItem] = field(default_factory=lambda: {
        "1": MenuItem(
            key="1",
            label="From ASCII",
            description="Convert ASCII text to various encodings",
            handler_name="ascii.run_ascii_convert"
        ),
        "2": MenuItem(
            key="2",
            label="From Base64",
            description="Convert Base64 encoded data",
            handler_name="base64.run_base64_convert"
        ),
        "3": MenuItem(
            key="3",
            label="From Binary",
            description="Convert binary string representations",
            handler_name="binary.run_binary_convert"
        ),
        "4": MenuItem(
            key="4",
            label="From Decimal (Integer)",
            description="Convert decimal integer values",
            handler_name="dec_int.run_dec_int_convert"
        ),
        "5": MenuItem(
            key="5",
            label="From Decimal (String)",
            description="Convert decimal string values",
            handler_name="dec_str.run_dec_str_convert"
        ),
        "6": MenuItem(
            key="6",
            label="From Hexadecimal",
            description="Convert hexadecimal values",
            handler_name="hexadecimal.run_hex_convert"
        ),
        "7": MenuItem(
            key="7",
            label="From Octal",
            description="Convert octal integer values",
            handler_name="octal.run_octal_convert"
        ),
        "8": MenuItem(
            key="8",
            label="Rotate String (Caesar Cipher)",
            description="Apply ROT cipher to strings",
            handler_name="rot_str.rotate_string"
        ),
        "9": MenuItem(
            key="9",
            label="From Morse Code -> ASCII",
            description="Decode Morse code to plain text",
            handler_name="morse_code.run_morse_code_convert"
        ),
    })

    # Special actions (exit, help, etc.)
    special_actions: Dict[str, str] = field(default_factory=lambda: {
        "q": "EXIT",
        "Q": "EXIT",
        "?": "HELP",
        "h": "HELP",
        "H": "HELP"
    })


def get_main_menu_text(config: AppConfig) -> List[str]:
    """Build the main menu text lines from configuration."""
    lines = []

    for key in sorted(config.menu_items.keys()):
        item = config.menu_items[key]
        lines.append(f"[white][{key}] {item.label}")

    return lines


def get_exit_message(config: AppConfig) -> str:
    """Return exit confirmation message."""
    return c.print(
        f"\n[{config.exit_text_color}]-> Exiting {config.app_name}... Goodbye!\n"
    )
