# !/usr/bin/env python3

import sys

from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

from ascii_input import ASCII
from base64_input import Base64
from binary_input import Binary
from decimal_input import Decimal
from hex_input import Hexadecimal
from morse_code import MorseCode
from octal_input import Octal
from rotate_string import RotateString

from results import Results


__author__ = "a/k/a bWlrZXNwb24="


# Make the console object
c = Console()
install()


class Convert:

    def __init__(self):
        self.version = "0.5.5"
        self.last_updated = "06-Apr-2026"

    def print_error_msg(self, e: str) -> str:
        return c.print(f"\n[red] There was an error during processing: {e}\n")

    def get_input(self, input_type: str) -> str:
        input_string = Prompt.ask(f"""[bright_white]
[+] Enter the data you want to convert from [bold khaki3]{input_type}[bright_white] """)
        return input_string

#     def get_binary_data_format(self) -> str:
#         choice: str = c.input("""[bright_white]
# Is the binary data separated with a space character every 8 bits (y/n)?
# >> """)
#         return choice.lower().strip()

    def get_cipher_shift_value(self) -> int:
        shift_value: int = c.input("""[bright_white]
[+] Enter a numeric value for the shift you want to use >> """)
        return shift_value

    def no_valid_yn_option(self) -> None:
        c.print("""[bold bright_red]
!!! You did not enter a valid choice (either "y" or "n"). Please try again.""")

    def main(self) -> None:

        menu = {
            1: "From ASCII",
            2: "From Base64",
            3: "From Binary",
            4: "From Decimal (Integer)",
            5: "From Hexadecimal",
            6: "From Octal (Integer)",
            7: "Rotate String (Caesar Cipher)",
            8: "Exit Program"
        }

        main_menu = Table(
            title=f"[bold dodger_blue1]\nDATA CONVERTER & ENCODER, v.{self.version}",
            box=box.HEAVY_HEAD,
            show_header=False,
            header_style="bold #2070b2",
            show_lines=False,
            pad_edge=True,
            padding=(0,5,0,1),
            caption=f"Last Updated: {self.last_updated}",
            caption_justify="left",
            expand=True)

        main_menu.add_row(
            "[khaki3][?] What type of encoding/decoding do you want to do?\n")
        for key, value in menu.items():
            main_menu.add_row(f"[bright_white]  [{key}]  {value}")

        # Add blank line at end of options
        main_menu.add_row()

        c.print(main_menu)

        input_option = c.input("""[bold khaki3]\nENTER CHOICE >> """).lower().strip()

        if input_option == "1":
            try:
                input_type = "ASCII"
                input_string = self.get_input(input_type=input_type)
                ascii = ASCII(results={}, data_type=input_type)
                ascii.print_ascii_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "2":
            try:
                input_type = "Base64"
                input_string = self.get_input(input_type=input_type)
                base64 = Base64(results={}, data_type=input_type)
                base64.print_base64_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "3":
            try:
                input_type = "Binary"
                input_string = self.get_input(input_type=input_type)
                binary = Binary(results={}, data_type=input_type)
                binary.print_binary_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "4":
            try:
                input_type = "Decimal"
                input_string = self.get_input(input_type=input_type)
                decimal = Decimal(results={}, data_type=input_type)
                decimal.print_decimal_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "5":
            try:
                input_type = "Hexadecimal"
                input_string = self.get_input(input_type=input_type)
                hex = Hexadecimal(results={}, data_type=input_type)
                hex.print_hex_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "6":
            try:
                input_type = "Octal"
                input_string = self.get_input(input_type=input_type)
                octal = Octal(results={}, data_type=input_type)
                octal.print_octal_output(input_string=input_string)
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "7":
            try:
                input_type="Rotate String"
                input_string = self.get_input(input_type=input_type)
                n = self.get_cipher_shift_value()
                rotate_string = RotateString(input_string=input_string, n=n)
                rotate_string.rotate_string()
            except Exception as e:
                self.print_error_msg(e)
                return None

        elif input_option == "8":
            sys.exit(0)

        else:
            c.print(f"""[bold bright_red]\n
[+] Invalid choice entered. Please enter a valid option.""")
            self.main()


if __name__ == "__main__":
    app = Convert().main()
    # app.main()
