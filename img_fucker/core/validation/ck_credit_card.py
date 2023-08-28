import asyncio

async def validate_credit_card_number(card_number: str) -> bool:
    """
    Validate the provided credit card number using the Luhn algorithm.

    This function takes a credit card number as input and checks its validity
    using the Luhn algorithm.

    Args:
        card_number (str): The credit card number to be validated.

    Returns:
        bool: True if the credit card number is valid, False otherwise.
    """
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        raise ValueError("Invalid credit card number format")

    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0

if __name__ == "__main__":
    try:
        card_number = input("Enter credit card number: ")
        if validate_credit_card_number(card_number):
            print("Valid credit card number.")
        else:
            print("Invalid credit card number.")
    except ValueError as e:
        print("Error:", e)
