from django.core.exceptions import ValidationError
from django.test import TestCase
from VolunteerAct.app_users.validators import first_name_validator


class TestFirstNameValidator(TestCase):
    def setUp(self):
        self.validator = first_name_validator

    def test_valid_first_name__success(self):
        first_name = 'Test'

        result = self.validator(first_name)

        self.assertEquals('Test', result)

    def test_invalid_first_name__error(self):
        first_name = '1234'

        with self.assertRaises(ValidationError) as validation_err:
            self.validator(first_name)

        self.assertEquals(str(validation_err.exception), "['First name needs to contain only alphabetic symbols.']")
