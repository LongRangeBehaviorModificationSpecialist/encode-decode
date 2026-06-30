# !/usr/bin/env python3

import base64
from results import Results


class Binary:
    """
    Utility class for binary conversions.
    """


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def _validate(self) -> str:
        """
        Validates that the input is a non-empty binary string.

        Returns the cleaned string.
        """
        if not isinstance(self.input_string, str):
            raise TypeError("Input must be a string.")
        # Check for empty input value
        if not self.input_string:
            raise ValueError("Input can not be empty.")
        # Check to make sure the input consists of only 0 or 1
        if any (c not in "01" for c in self.input_string):
            raise ValueError("Binary input must be only 0 or 1.")
        clean_binary = self.input_string.replace(" ", "")
        if len(clean_binary) % 8 != 0:
            raise ValueError(
                f"Invalid binary length ({len(clean_binary)} bits). "
                f"The total number of bits must be evenly divisible by 8."
            )
        return self.input_string


    def binary_to_ascii(self) -> str:
        """
        Converts binary string to ascii representation.
        """
        self.input_string = self.input_string.replace(" ", "")
        list = []
        for i in range(0, len(self.input_string), 8):
            list.append(self.input_string[i:i+8])
        return "".join([chr(int(i, 2)) for i in list])


    def binary_to_base64(self) -> str:
        """
        Converts a binary string to base64 string.
        """
        binary_string = self._validate()
        # Pad binary string so length is multiple of 8
        padding_length = (8 - len(binary_string) % 8) % 8
        binary_string += "0" * padding_length
        # Convert binary string to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))
        # Encode to base64
        return base64.b64encode(byte_array).decode("utf-8")


    def binary_to_base32(self) -> str:
        """
        Converts a binary string to base32 string.
        """
        binary_string = self._validate()
        # Ensure the binary string is a multiple of 8 bits by padding
        # with leading zeros
        remainder = len(binary_string) % 8

        if remainder != 0:
            binary_string = binary_string.zfill(len(binary_string) + (8 - remainder))

        byte_list = []
        for i in range(0, len(binary_string), 8):
            byte_chunk = binary_string[i:i+8]
            byte_list.append(int(byte_chunk, 2))

        raw_bytes = bytes(byte_list)
        return base64.b32encode(raw_bytes).decode("ascii")


    def binary_to_decimal_int(self) -> int:
        """
        Converts a binary string to a decimal integer.
        """
        binary_string = self._validate()
        binary_string = binary_string.replace(" ", "")
        return f"{int(binary_string, 2):,}"


    def binary_to_decimal_char(self) -> str:
        """
        Converts each 8-bit byte chunk into its individual decimal
        value and returns them as a single space-seperated string.
        """
        binary_string = self._validate()
        clean_binary = binary_string.replace(" ", "")
        binary_bytes = [clean_binary[i:i+8] for i in range(0, len(clean_binary), 8)]
        return " ".join([str(int(b, 2)) for b in binary_bytes])


    def binary_to_hexadecimal(self) -> str:
        """
        Converts a binary string to a hexadecimal string.
        """
        binary_string = self._validate()
        decimal_value = int(binary_string, 2)
        hex_string = f"{decimal_value:X}"
        if len(hex_string) % 2 !=0:
            hex_string = "0" + hex_string
        return " ".join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))



    def binary_to_octal(self) -> str:
        """
        Converts a binary string to a octal string.
        """
        binary_string = self._validate()
        return oct(int(binary_string, 2))[2:]


    def make_data_dict(self) -> dict:
        self.results["type"] = "Binary"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Ascii"] = f"{self.binary_to_ascii()}"
        self.results["Base64"] = f"{self.binary_to_base64()}"
        self.results["Base32"] = f"{self.binary_to_base32()}"
        self.results["Decimal (int)"] = f"{self.binary_to_decimal_int()}"
        self.results["Decimal (char)"] = f"{self.binary_to_decimal_char()}"
        self.results["Hexadecimal"] = f"{self.binary_to_hexadecimal()}"
        self.results["Octal"] = f"{self.binary_to_octal()}"
        return self.results


    def print_binary_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)