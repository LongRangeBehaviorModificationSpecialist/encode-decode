# !/usr/bin/env python3

from rich import box, print
from rich.console import Console
from rich.table import Table

from ascii_input import ASCII
from base64_input import Base64
from binary_input import Binary
from decimal_input import Decimal
from hex_input import Hexadecimal
from morse_code import MorseCode
from octal_input import Octal
from rotate_string import RotateString

from results import Results


__author__ = 'a/k/a bWlrZXNwb24='
__last_updated__ = '2024-03-01'

# Make the console object
console = Console()


class Convert:


    def get_input(self, input_type: str) -> str:
        input_string: str = console.input(f'''[bright_white]
[-] Enter the data you want to encode from [bold khaki3]{input_type}[bright_white]:
>>> ''')
        return input_string


    def get_binary_data_format(self) -> str:
        choice: str = console.input('''[bright_white]
Is the binary data separated with a space character every 8 bits (y/n)?
>>> ''')
        return choice.lower().strip()


    def get_cipher_shift_value(self) -> int:
        shift_value: int = console.input('''[bright_white]
[-] Enter the value of the shift you want to use:
>>> ''')
        return shift_value


    def no_valid_yn_option(self) -> None:
        console.print('''[bold bright_red]
!!! You did not enter a valid choice (either `y` or `n`). Please try again.''')


    def main(self) -> None:

        menu_row_dict = {
            'A':'From ASCII',
            'B':'From Base64',
            'C':'From Binary',
            'D':'From Decimal',
            'E':'From Hexadecimal',
            'F':'From Octal (integer -> Binary, Decimal, & Hex)',
            'G':'Rotate String (Caesar Cipher)'}

        main_menu =Table(
            title='[bold dodger_blue1]\nDATA CONVERTER / ENCODER, v.0.5.3',
            box=box.HEAVY_HEAD,
            show_header=False,
            header_style='bold #2070b2',
            show_lines=False,
            pad_edge=True,
            padding=(0,5,0,1),
            caption=f'Last Updated: {__last_updated__}',
            caption_justify='left',
            expand=True)
        main_menu.add_row(
            '[khaki3][-] What type of encoding/decoding do you want to do?\n')
        for key, value in menu_row_dict.items():
            main_menu.add_row(f'[bright_white]  [{key}]  {value}')

        # Add blank line at end of options
        main_menu.add_row()

        print(main_menu)

        input_type: str = console.input('''[bold khaki3]\nENTER CHOICE >>> ''')
        input_type = input_type.lower().strip()


        if input_type == 'a':

            input_string = self.get_input(self, input_type='ASCII')
            output = Results.set_output_type(self)

            if output== 'p':
                ASCII.print_ascii_output_panels(self, input_string)
            elif output == 't':
                ASCII.print_ascii_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'b':

            input_string = self.get_input(self, input_type='Base64')
            output = Results.set_output_type(self)

            if output == 'p':
                Base64.print_base64_output_panels(self, input_string)
            elif output == 't':
                Base64.print_base64_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'c':

            choice = self.get_binary_data_format(self)
            input_string = self.get_input(self,input_type='Binary')

            output = Results.set_output_type(self)

            if choice == 'y' and output == 'p':
                Binary.print_binary_separated_output_panels(self, input_string)
            elif choice == 'n' and output == 'p':
                Binary.print_binary_combined_output_panels(self, input_string)
            elif choice == 'y' and output == 't':
                Binary.print_binary_separated_output_table(self, input_string)
            elif choice == 'n' and output == 't':
                Binary.print_binary_combined_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'd':

            input_string = self.get_input(self, input_type='Decimal')
            output = Results.set_output_type(self)

            if output == 'p':
                Decimal.print_decimal_output_panels(self, input_string)
            elif output == 't':
                Decimal.print_decimal_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'e':

            input_string = self.get_input(self, input_type='Hexadecimal')
            output = Results.set_output_type(self)

            if output == 'p':
                Hexadecimal.print_hex_output_panels(self, input_string)
            elif output == 't':
                Hexadecimal.print_hex_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'f':

            input_string = self.get_input(self, input_type='Octal')
            output = Results.set_output_type(self)

            if output == 'p':
                Octal.print_octal_output_panels(self, input_string)
            elif output == 't':
                Octal.print_octal_output_table(self, input_string)
            else:
                self.no_valid_yn_option(self)
                self.main(self)


        elif input_type == 'g':

            input_string = self.get_input(self, input_type='Rotate String')
            n = self.get_cipher_shift_value(self)
            RotateString.rotate_string(self, input_string, n)


        else:
            console.print(f'''[bold bright_red]\n
[-] Invalid choice entered. Please enter a valid option.''')
            self.main(self)


if __name__ == '__main__':
    Convert.main(Convert)
