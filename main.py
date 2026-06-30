# !/usr/bin/env python3

import sys

from rich import box
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.traceback import install

from ascii_input import Ascii
from base64_input import Base64
from binary_input import Binary
from decimal_input import DecimalInteger, DecimalString
from hex_input import Hexadecimal
from morse_code import MorseCode
from octal_input import Octal
from rotate_string import RotateString

from results import Results


# Make the console object
c = Console()
install()


class Convert:


    def __init__(self):
        self.author = "mikes"
        self.version = "0.5.6"
        self.last_updated = "30-Jun-2026"
        self.input_type_dict = {
            1: "Ascii",
            2: "Base64",
            3: "Binary",
            4: "Decimal (Integer)",
            5: "Decimal (String)",
            6: "Hexadecimal",
            7: "Octal",
            8: "Morse Code"
        }


    def print_error_msg(self, e: str) -> str:
        return c.print(f"""[bold bright_red]
[!] There was an error during processing: {e}\n""")


    def get_input(self) -> str:
        input_string = Prompt.ask(f"""[bright_white]
[-] Enter the data you want to convert """)
        return input_string


    def get_cipher_shift_value(self) -> int:
        shift_value: int = Prompt.ask("""[bright_white]
[-] Enter a numeric value for the shift you want to use """)
        return shift_value


    def no_valid_yn_option(self) -> None:
        c.print("""[bold bright_red]
[!] You did not enter a valid choice ("y" or "n"). Please try again.""")


    def main(self) -> None:

        menu = {
            1: "From ASCII",
            2: "From Base64",
            3: "From Binary",
            4: "From Decimal (Integer)",
            5: "From Decimal (String)",
            6: "From Hexadecimal",
            7: "From Octal (Integer)",
            8: "Rotate String (Caesar Cipher)",
            9: "From Morse Code -> ASCII",
            "Q": "Exit Program"
        }

        main_menu = Table(
            title=f"[bold dodger_blue1]\nDATA CONVERTER & ENCODER, v.{self.version}",
            box=box.HEAVY_HEAD,
            show_header=False,
            header_style="bold #2070b2",
            show_lines=False,
            pad_edge=True,
            padding=(0, 5, 0, 1),
            caption=f"Written by: {self.author}. Last Updated: {self.last_updated}",
            caption_justify="left",
            expand=True)

        main_menu.add_row(
            "[khaki3][?] What type of encoding/decoding do you want to do?\n")
        for key, value in menu.items():
            main_menu.add_row(f"[bright_white]  [{key}]  {value}")

        # Add blank line at end of options
        main_menu.add_row()

        c.print(main_menu)

        input_option = Prompt.ask("[khaki3]\nENTER CHOICE").lower().strip()


        if input_option == "1":
            input_string = self.get_input()
            Ascii(input_string=input_string, results={}).print_ascii_output()


        elif input_option == "2":
            input_string = self.get_input()
            Base64(input_string=input_string, results={}).print_base64_output()


        elif input_option == "3":
            input_string = self.get_input()
            Binary(input_string=input_string, results={}).print_binary_output()


        elif input_option == "4":
            input_string = self.get_input()
            DecimalInteger(
                input_string=input_string,
                results={}).print_decimal_integer_output()


        elif input_option == "5":
            input_string = self.get_input()
            DecimalString(
                input_string=input_string,
                results={}).print_decimal_string_output()


        elif input_option == "6":
            input_string = self.get_input()
            Hexadecimal(
                input_string=input_string,
                results={}).print_hex_output()


        elif input_option == "7":
            input_string = self.get_input()
            Octal(
                input_string=input_string,
                results={}).print_octal_output()


        elif input_option == "8":
            try:
                input_string = self.get_input()
                n = self.get_cipher_shift_value()
                RotateString(input_string=input_string, n=n).rotate_string()
            except Exception as e:
                self.print_error_msg(e)
                return None


        elif input_option == "9":
            input_string = self.get_input()
            MorseCode(
                input_string=input_string,
                results={}).print_morse_code_output()


        elif input_option == "q":
            sys.exit(0)

        else:
            c.print(f"""[bold bright_red]\n
[!] Invalid choice entered. Please enter a valid option.""")
            self.main()


if __name__ == "__main__":
    # app = Convert().main()
    Convert().main()
