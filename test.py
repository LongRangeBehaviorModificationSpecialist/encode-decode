


def hex_to_decimal(input_string: str) -> str:
    """Converts a hex string to signed, unsigned, and binary
    representations.

    Args:
        hex_str (str): Hex string (e.g. 'FFFF', '0xFF').

    Returns:
        dict: Contains 'signed' and 'unsigned' representations.
    """

    hex_str = input_string.strip().lower()

    if hex_str.startswith("0x"):
        hex_str = hex_str[2:]

    if not all(c in "0123456789abcdef" for c in hex_str):
        raise ValueError(f"Invalid hex string: '{hex_str}'")

    unsigned_value = int(hex_str, 16)
    bit_length = len(hex_str) * 4

    signed_value = unsigned_value

    if unsigned_value >= 2 ** (bit_length - 1):
        signed_value -= 2 ** bit_length

    decimal_results = {
        "signed" :   f"{signed_value:,}",
        "unsigned" : f"{unsigned_value:,}"
    }

    return decimal_results


if __name__ == "__main__":

    # decimal_results = hex_to_decimal("f40004")

    # fk, fv = list(results.items())[0]
    # sk, sv = list(results.items())[1]

    # (first_key, first_val), (second_key, second_val) = decimal_results.items()

    (first_key, first_val), (second_key, second_val) = hex_to_decimal("f40004").items()


    # Print the first item
    print(f"First item -> {first_key}: {first_val}")
    # Print the second item
    print(f"Second item -> {second_key}: {second_val}")
