from django.core.exceptions import ValidationError

def validate_phone_number(value):
    """
    Custom validator for phone numbers.
    Ensures the number starts with '+254' followed by 9 digits.
    """
    if not value.startswith("+254") or not value[4:].isdigit() or len(value) != 13:
        raise ValidationError("Invalid phone number format. Please use +254XXXXXXXXX.")


