# !/usr/bin/env python3

from rich.console import Console

# Make the console object
console = Console()


class MorseCode:
    '''Python program to implement Morse Code Translator

    VARIABLE KEY
    'cipher' -> 'stores the morse translated form of the english string'
    'decipher' -> 'stores the english translated form of the morse string'
    'citext' -> 'stores morse code of a single character'
    'i' -> 'keeps count of the spaces between morse characters'
    'message' -> 'stores the string to be encoded or decoded'
    '''

    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = {
        'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
        'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---',
        'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--',
        'Z':'--..', '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
        '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'
        }


    def encode_morse_code(self, input_string: str) -> str:
        '''Conversion from Morse Code value to ASCII

        Args:
          str: ASCII encoded string
            One (1) space indicates different character
            Two (2) spaces indicates different word

        Returns:
          str: Morse Code string to convert
        '''
        cipher = ''
        input_string = input_string.upper()
        for c in input_string:
            if c != ' ':
                # Looks up the dictionary and adds the corresponding morse code
                # along with a space to separate morse codes for different
                # characters
                cipher += MorseCode.MORSE_CODE_DICT[c] + ' '
            else:
                cipher += ' '
        return cipher


    def decode_morse_code(self, input_string: str) -> str:
        '''Conversion from Morse Code value to ASCII.

        Args:
          str: Morse Code string to convert

        Returns:
          str: ASCII encoded string
        '''
        # Extra space added at the end to access the last morse code
        input_string += ' '
        decipher = ''
        citext = ''
        for c in input_string:
            # Checks for space
            if (c != ' '):
                # Counter to keep track of space
                i = 0
                # Storing morse code of a single character
                citext += c
            # In case of space
            else:
                # If i = 1 that indicates a new character
                i += 1
                # If i = 2 that indicates a new word
                if i == 2 :
                    # Adding space to separate words
                    decipher += ' '
                else:
                    # Accessing the keys using their values (reverse of encryption)
                    decipher += list(
                        MorseCode.MORSE_CODE_DICT.keys())[list(
                            MorseCode.MORSE_CODE_DICT.values()).index(citext)]
                    citext = ''
        return decipher