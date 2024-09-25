from django.core.exceptions import ValidationError
from django.test import TestCase
from ..validators import validate_phone_number

class PhoneNumberValidatorTest(TestCase):
    def test_valid_phone_number(self):
        # A valid Kenyan phone number
        valid_number = "+254712345678"
        try:
            validate_phone_number(valid_number)
        except ValidationError:
            self.fail(f"{valid_number} should be considered valid.")

    def test_invalid_phone_number(self):
        # Invalid phone numbers
        invalid_numbers = [
            "0712345678",  # Missing '+254'
            "+25412345678",  # Too short (9 digits)
            "+2547123456789",  # Too long (more than 13 digits)
            "+254ABCD12345",  # Contains non-digits
        ]
        for number in invalid_numbers:
            with self.assertRaises(ValidationError):
                validate_phone_number(number)
