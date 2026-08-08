# !/usr/bin/env python3
# DLU : 08-Aug-2026


import base64
from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import install
from results import Results


c = Console()
install(show_locals=True)


class DecimalInteger:


    def format_input(self, input: str):
        if "," in input:
            input = input.replace(",", "")
        return int(input)


    def decimal_to_binary(self, input: str) -> str:
        """Convert the decimal number to binary number."""
        return "{0:b}".format(input)


    def decimal_to_hexadecimal(self, input: str) -> str:
        """Convert the decimal number to hexadecimal number."""
        hex_str = hex(input)[2:]
        if len(hex_str) % 2 != 0:
            hex_str = "0" + hex_str
        pairs = [hex_str[i : i + 2] for i in range(0, len(hex_str), 2)]
        return "0x " + " ".join(pairs).upper()


    def decimal_to_octal(self, input: str) -> str:
        """Convert the decimal number to octal number."""
        return oct(input)


    def make_data_dict(self, input: str) -> None:
        results = {}
        results["Input Type"] = "Decimal (integer)"
        results["Input Value"] = f"{input}"
        results["binary"] = f"{self.decimal_to_binary(input=input)}"
        results["hexadecimal"] = f"{self.decimal_to_hexadecimal(input=input)}"
        results["octal"] = f"{self.decimal_to_octal(input=input)}"
        return results


    def run_dec_int_convert(self) -> None:
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)


class DecimalString:


    def decimal_to_ascii(self, input: str) -> str:
        try:
            return "".join(chr(int(c)) for c in input.split())

        except ValueError:
            c.print(
                "[red1][!] Error : Please ensure the input only contains "
                "numbers separated by spaces."
            )
        except OverflowError:
            c.print(
                "[red1][!] Error : One of the numbers is too large to be a "
                "valid ascii character."
            )


    def decimal_to_base64(self, input: str) -> str:
        byte_data = bytes(int(c) for c in input.split())
        return base64.b64encode(byte_data).decode("utf-8")


    def make_data_dict(self, input: str) -> None:
        results = {}
        results["Input Type"] = "Decimal (String)"
        results["Input Value"] = f"{input}"
        results["ascii"] = f"{self.decimal_to_ascii(input=input)}"
        results["base64"] = f"{self.decimal_to_base64(input=input)}"
        return results


    def run_dec_str_convert(self) -> None:
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)
