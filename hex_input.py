# !/usr/bin/env python3

import binascii

from results import Results
from morse_code import MorseCode


class Hexadecimal:


    def __init__(self, data_type, results):
        self.data_type = data_type
        self.results = results


    def hex_to_ascii(self, input_string: str) -> str:
        hex_string = input_string.replace(" ", "")
        string = binascii.unhexlify(hex_string)
        ascii_string = string.decode()
        return ascii_string


    def hex_to_base64(self, input_string: str) -> str:
        hex_string = input_string.replace(" ", "")
        hex_bytes = binascii.unhexlify(hex_string)
        base64_string = binascii.b2a_base64(hex_bytes).decode()
        return base64_string


    def hex_to_binary(self, input_string: str) -> str:
        ascii_string = Hexadecimal.hex_to_ascii(self, input_string)
        n = [x for x in ascii_string]
        binary_string = " ".join([bin(ord(x))[2:].zfill(8) for x in n])
        return binary_string


    def hex_to_decimal(self, input_string: str) -> str:
        # Remove any spaces if present
        hex_string = input_string.replace(" ", "")
        # First, convert the HEX string to ASCII string
        ascii_string = binascii.unhexlify(hex_string)
        s = ascii_string.decode()
        # Conversion to DECIMAL string from ASCII
        d = [ord(i) for i in s]
        decimal_string = " ".join(str(x) for x in d)
        return decimal_string


    def hex_to_morse_code(self, input_string: str) -> str:
        hex_string = input_string.replace(" ", "")
        morse_code_string = MorseCode.encode_morse_code(self,
            input_string=hex_string)
        return morse_code_string


    def hex_convert_all(self, input_string: str) -> None:
        self.results["type"] = "Hexadecimal"
        self.results["user_input"] = f"{input_string}"
        self.results["ASCII"] = f"{self.hex_to_ascii(input_string)}"
        self.results["Base64"] = f"{self.hex_to_base64(input_string)}"
        self.results["Binary"] = f"{self.hex_to_binary(input_string)}"
        self.results["Decimal"] = f"{self.hex_to_decimal(input_string)}"
        return self.results


    def print_hex_output(self, input_string: str) -> None:
        output = self.hex_convert_all(input_string)
        Results.print_results_table(self,
                                    data_type=self.data_type,
                                    results_dict=output)
