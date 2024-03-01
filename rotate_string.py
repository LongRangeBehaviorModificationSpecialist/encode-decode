# !/usr/bin/env python3

import string
from rich.console import Console

from results import Results

# Make the console object
console = Console()


class RotateString:


    def rotate_string(self, input_string: str, n: int) -> str:
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        n = int(n)
        trans = str.maketrans(
            lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
        rotated_string = str.translate(input_string, trans)
        Results.print_results(self, results=rotated_string)


