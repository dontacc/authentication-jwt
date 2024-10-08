from django.core.validators import RegexValidator


class PhoneNumberValidator(RegexValidator):
    regex = r"^[0][9]\d{9}$"
    message = "Please enter valid phone number"
