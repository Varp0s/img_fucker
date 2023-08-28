import unittest
import asyncio
from img_fucker.core.validation.ck_credit_card import validate_credit_card_number

class TestCreditCardValidation(unittest.IsolatedAsyncioTestCase):
    async def test_valid_credit_card(self):
        valid_card_numbers = [
            "4111 1111 1111 1111",
            "5500 0000 0000 0004",
            "6011 1111 1111 1117",
        ]
        
        for card_number in valid_card_numbers:
            result = await validate_credit_card_number(card_number)
            self.assertTrue(result)

    async def test_invalid_credit_card(self):
        invalid_card_numbers = [
            "1234 5678 9012 3456",
            "4111 1111 1111 1112",
            "6011 1111 1111 1111",
        ]
        
        for card_number in invalid_card_numbers:
            result = await validate_credit_card_number(card_number)
            self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
