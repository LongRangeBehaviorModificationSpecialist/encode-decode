# !/usr/bin/env python3

from rich.console import Console
from rich.traceback import install

from results import Results


c = Console()
install()


class MorseCode:
    """
    Python program to implement Morse Code Translator

        VARIABLE KEY
        "cipher"     -> "stores the morse translated form of the english string"
        "decipher"   -> "stores the english translated form of the morse string"
        "ciphertext" -> "stores morse code of a single character"
        "i"          -> "keeps count of the spaces between morse characters"
        "message"    -> "stores the string to be encoded or decoded"
    """

    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {
        "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".",
        "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---",
        "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---",
        "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
        "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--",
        "Z":"--..", "1":".----", "2":"..---", "3":"...--",
        "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..",
        "9":"----.", "0":"-----", ", ":"--..--", ".":".-.-.-",
        "?":"..--..", "/":"-..-.", "-":"-....-", "(":"-.--.", ")":"-.--.-",
        "=":"-...-"
    }


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def is_valid_morse(self) -> str:
        """
        Validates that the input contains valid morse code characters.
        """
        if not self.input_string or self.input_string.isspace():
            return False
        allowed_characters = {".", "-", " "}
        if set(self.input_string).issubset(allowed_characters):
            return True
        else:
            return False


    def encode_morse_code(self) -> str:
        """
        Conversion from Morse Code value to ascii

        Args:
            str: ascii encoded string
                One (1) space indicates different character
                Two (2) spaces indicates different word

        Returns:
            str: Morse Code string to convert
        """
        cipher = ""
        self.input_string = self.input_string.upper()
        for letter in self.input_string:
            if letter != " ":
                # Looks up the dictionary and adds the corresponding morse code
                # along with a space to separate morse codes for different
                # characters
                cipher += f"""{MorseCode.MORSE_CODE_DICT[letter] + " "}"""
            else:
                cipher += " "
        return cipher


    def decode_morse_code(self) -> str:
        """
        Conversion from Morse Code value to ascii.

        Args:
            str: Morse code string to convert

        Returns:
            str: ascii encoded string
        """
        # Extra space added at the end to access the last morse code
        if self.is_valid_morse():

            self.input_string += " "
            decipher = ""
            ciphertext = ""
            for entry in self.input_string:
                # Checks for space
                if (entry != " "):
                    # Counter to keep track of space
                    i = 0
                    # Storing morse code of a single character
                    ciphertext += entry
                # In case of space
                else:
                    # If i = 1 that indicates a new character
                    i += 1
                    # If i = 2 that indicates a new word
                    if i == 2 :
                        # Adding space to separate words
                        decipher += " "
                    else:
                        # Accessing the keys using their values (reverse of encryption)
                        decipher += list(
                            MorseCode.MORSE_CODE_DICT.keys())[list(
                                MorseCode.MORSE_CODE_DICT.values()).index(ciphertext)]
                        ciphertext = ""
            return decipher
        else:
            c.print("""[red]
[!] The data containes not valid morse code characters. Check the data and \
try again.""")


    def make_data_dict(self) -> dict:
        self.results["type"] = "Morse Code"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Ascii"] = f"{self.decode_morse_code()}"
        return self.results


    def print_morse_code_output(self) -> None:
        output = self.make_data_dict()
        Results.print_results_table(self, results_dict=output)


"""

Morse Code : -- .. -.- .  ... .--. --- -.

"""
