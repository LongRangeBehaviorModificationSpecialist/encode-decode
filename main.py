# !/usr/bin/env python3

import sys
from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

from converters.ascii_input import Ascii
from converters.base64_input import Base64
from converters.binary_input import Binary
from converters.decimal_input import DecimalInteger, DecimalString
from converters.hex_input import Hexadecimal
from converters.morse_code import MorseCode
from converters.octal_input import Octal
from converters.rotate_string import RotateString

from versions import (
    __version__,
    __author__,
    __last_updated__,
    get_version_string
)

from ui.config import AppConfig, get_main_menu_text, get_exit_message

from results import Results


# Make the console object
c = Console()
install(show_locals=True, console=c)


class Main:


    def __init__(self):
        self.config = AppConfig()
        self._author = __author__
        self._version = __version__
        self._last_updated = __last_updated__
        self._version_banner = get_version_string(short=False)
        # Initialize subsystems
        self.ascii = Ascii()
        self.base64 = Base64()
        self.binary = Binary()
        self.dec_int = DecimalInteger()
        self.dec_str = DecimalString()
        self.hexadecimal = Hexadecimal()
        self.octal = Octal()
        self.morse_code = MorseCode()
        self.rot_str = RotateString()

        # Map handler names to actual method references
        self._handlers = {
            "ascii": self.ascii,
            "base64": self.base64,
            "binary": self.binary,
            "dec_int": self.dec_int,
            "dec_str": self.dec_str,
            "hexadecimal": self.hexadecimal,
            "octal": self.octal,
            "morse_code": self.morse_code,
            "rot_str": self.rot_str,
        }


    def _get_handler_by_name(self, handler_name: str):
        """Resolve handler name to actual object."""
        # Parse "module.method" format
        parts = handler_name.rsplit(".", 1)
        if len(parts) == 2:
            module_name, method_name = parts
            return getattr(self._handlers.get(module_name), method_name, None)
        return None


    def display_main_menu(self) -> None:
        """Render the main menu using configuration."""
        menu_table = Table(
            title=(
                f"[{self.config.title_color}]\n{self.config.app_name}, "
                f"v.{self._version}"
            ),
            box=box.HEAVY_HEAD,
            show_header=False,
            header_style=self.config.header_style,
            show_lines=False,
            pad_edge=True,
            padding=(0, 5, 0, 1),
            caption=(
                f"Written by: {self._author}  |  Last Updated: "
                f"{self._last_updated}"
            ),
            caption_justify=self.config.credits_justify,
            caption_style="grey58",
            expand=False,
        )

        menu_table.add_row(
            f"[{self.config.warning_color}]What type of encoding/decoding "
            "do you want to do?\n",
        )

        for line in get_main_menu_text(self.config):
            menu_table.add_row(line)

        menu_table.add_row()  # Blank line at end

        c.print(menu_table)


    def handle_selection(self, selection: str) -> bool:
        """Process user's menu selection.

        Args:
            selection: The user's input

        Returns:
            True if program should continue, False if it should exit.
        """
        normalized = selection.lower().strip()

        # Check for special actions
        if normalized in self.config.special_actions:
            action = self.config.special_actions[normalized]
            if action == "EXIT":
                c.print(get_exit_message(self.config))
                return False

        # Check for valid menu item
        if normalized not in [k.lower() for k in self.config.menu_items.keys()]:
            c.print(
                f"[{self.config.warning_color}][red1] Unknown choice -> "
                f"{selection}. Please enter a valid option or 'Q' to exit."
            )
            # Continue loop
            return True

        # Find the matching case-insensitive key
        actual_key = None
        for key in self.config.menu_items.keys():
            if key.lower() == normalized:
                actual_key = key
                break

        if actual_key:
            item = self.config.menu_items[actual_key]
            if item.handler_name:
                handler = self._get_handler_by_name(item.handler_name)
                if handler:
                    try:
                        # Run the converter
                        handler()
                        # --- NEW: Continuation Prompt ---
                        if not self._ask_continue():
                            c.print(get_exit_message(self.config))
                            return False
                        # --- End Continuation Prompt ---
                    except ValueError as e:
                        c.print(f"[red1]Validation Error: {e}")
                        c.print(f"[dim]Input may contain invalid characters.")
                        # Continue to menu instead of exiting

                    except Exception as e:
                        # NEW: Show full traceback for debugging
                        c.print(f"[red1]Unexpected Error: {type(e).__name__}: {e}")
                        c.print(f"[yellow3]Full traceback below:")
                        import traceback
                        c.print(traceback.format_exc())
                        c.print(f"[dim]Tip: Try simpler input or check the MorseCode module")

                        # Continue to menu instead of crashing
                        if not self._ask_continue():
                            c.print(get_exit_message(self.config))
                            return False

                else:
                    c.print(f"[red]Handler not found -> {item.handler_name}")
            else:
                c.print(f"[yellow3]No handler configured for '{item.label}'")

        # Continue loop
        return True


    def _ask_continue(self) -> bool:
        """Ask user if they want to continue to main menu."""
        if self.config.show_separator_line:
            c.print("\n\n[dim]" + "-" * 45)

        try:
            response = Prompt.ask(
                f"[{self.config.success_color}]"
                f"{self.config.continue_prompt_text}",
                choices=self.config.continue_prompt_choices,
                default=self.config.continue_prompt_default
            ).lower().strip()

            return response in ["y", "yes", ""]

        except (KeyboardInterrupt, EOFError):
            # Exit on interrupt during prompt
            return False


    def main(self) -> None:
        """Main application controller for the DATA CONVERTER utility.

        Orchestrates input/output operations and manages converter subsystems.
        Provides menu-driven interface for various encoding/decoding operations.
        """
        while True:
            self.display_main_menu()

            try:
                selection = Prompt.ask(
                    f"\n[{self.config.warning_color}]ENTER CHOICE"
                )

                if not self.handle_selection(selection):
                    break

            except KeyboardInterrupt:
                c.print(
                    f"\n\n[{self.config.warning_color}]-> Program interrupted "
                    "by user..."
                )
                c.print(get_exit_message(self.config))
                sys.exit(0)
            except EOFError:
                c.print("\n[red1]EOF received. Exiting...")
                sys.exit(0)


if __name__ != "__main__":
    pass


if __name__ == "__main__":
    try:
        app = Main()
        app.main()
    except KeyboardInterrupt:
        c.print("\n[yellow3]-> Program interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        c.print(f"[red1]Unexpected error -> {e}")
        sys.exit(1)

