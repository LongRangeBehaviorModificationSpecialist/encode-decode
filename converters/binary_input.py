# !/usr/bin/env python3
# DLU : 08-Aug-2026


import base64
from rich.traceback import install
from rich.prompt import Prompt
from results import Results


install(show_locals=True)


class Binary:
    """Utility class for binary conversions."""

    def _validate(self, input: str) -> str:
        """Validates that the input is a non-empty binary string.

        Returns the cleaned string.
        """
        if not isinstance(input, str):
            raise TypeError("Input must be a string.")
        # Check for empty input value
        if not input:
            raise ValueError("Input can not be empty.")
        # Check to make sure the input consists of only 0 or 1
        if any (c not in "01" for c in input):
            raise ValueError("Binary input must be only 0 or 1.")
        clean_binary = input.replace(" ", "")
        if len(clean_binary) % 8 != 0:
            raise ValueError(
                f"Invalid binary length ({len(clean_binary)} bits). The "
                "total number of bits must be evenly divisible by 8."
            )
        return input


    def binary_to_ascii(self, input: str) -> str:
        """Converts binary string to ascii representation."""
        input = input.replace(" ", "")
        list = []
        for i in range(0, len(input), 8):
            list.append(input[i : i + 8])
        return "".join([chr(int(i, 2)) for i in list])


    def binary_to_base64(self, input: str) -> str:
        """Converts a binary string to base64 string."""
        binary_string = self._validate(input=input)
        # Pad binary string so length is multiple of 8
        padding_length = (8 - len(binary_string) % 8) % 8
        binary_string += "0" * padding_length
        # Convert binary string to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i : i + 8]
            byte_array.append(int(byte, 2))
        # Encode to base64
        return base64.b64encode(byte_array).decode("utf-8")


    def binary_to_base32(self, input: str) -> str:
        """Converts a binary string to base32 string."""
        binary_string = self._validate(input=input)
        # Ensure the binary string is a multiple of 8 bits by padding
        # with leading zeros
        remainder = len(binary_string) % 8

        if remainder != 0:
            binary_string = (
                binary_string.zfill(len(binary_string) + (8 - remainder))
            )

        byte_list = []
        for i in range(0, len(binary_string), 8):
            byte_chunk = binary_string[i : i + 8]
            byte_list.append(int(byte_chunk, 2))

        raw_bytes = bytes(byte_list)
        return base64.b32encode(raw_bytes).decode("ascii")


    def binary_to_decimal_int(self, input: str) -> int:
        """Converts a binary string to a decimal integer."""
        binary_string = self._validate(input=input)
        binary_string = binary_string.replace(" ", "")
        return f"{int(binary_string, 2):,}"


    def binary_to_decimal_char(self, input: str) -> str:
        """Converts each 8-bit byte chunk into its individual decimal
        value and returns them as a single space-seperated string.
        """
        binary_string = self._validate(input=input)
        clean_binary = binary_string.replace(" ", "")
        binary_bytes = [
            clean_binary[i : i + 8]
            for i in range(0, len(clean_binary), 8)
        ]
        return " ".join([str(int(b, 2)) for b in binary_bytes])


    def binary_to_hexadecimal(self, input: str) -> str:
        """Converts a binary string to a hexadecimal string."""
        binary_string = self._validate(input=input)
        decimal_value = int(binary_string, 2)
        hex_string = f"{decimal_value:X}"
        if len(hex_string) % 2 !=0:
            hex_string = "0" + hex_string
        return " ".join(
            hex_string[i : i + 2] for i in range(0, len(hex_string), 2)
        )


    def binary_to_octal(self, input: str) -> str:
        """Converts a binary string to a octal string."""
        binary_string = self._validate(input=input)
        return oct(int(binary_string, 2))[2:]


    def make_data_dict(self, input: str) -> dict:
        results = {}
        results["Input Type"] = "Binary"
        results["Input Value"] = f"{input}"
        results["ascii"] = f"{self.binary_to_ascii(input=input)}"
        results["base64"] = f"{self.binary_to_base64(input=input)}"
        results["base32"] = f"{self.binary_to_base32(input=input)}"
        results["decimal (int)"] = f"{self.binary_to_decimal_int(input=input)}"
        results["decimal (char)"] = f"{self.binary_to_decimal_char(input=input)}"
        results["hexadecimal"] = f"{self.binary_to_hexadecimal(input=input)}"
        results["octal"] = f"{self.binary_to_octal(input=input)}"
        return results


    def run_binary_convert(self):
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)