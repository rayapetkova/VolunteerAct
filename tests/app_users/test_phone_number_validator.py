from django.core.exceptions import ValidationError
from django.test import TestCase
from VolunteerAct.app_users.validators import phone_number_validator


class TestPhoneNumberValidator(TestCase):
    def setUp(self):
        self.validator = phone_number_validator

    def test_valid_phone_number__success(self):
        phone_number = '0888888888'

        result = self.validator(phone_number)

        self.assertEquals('0888888888', result)

    def test_invalid_phone_number__error(self):
        phone_number = '08888jkdk'

        with self.assertRaises(ValidationError) as validation_err:
            self.validator(phone_number)

        self.assertEquals(str(validation_err.exception), "['Phone number needs to consist of only digits.']")
