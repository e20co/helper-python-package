from unittest import TestCase
from helper.type_checking import check_value
from helper.type_checking import check_string


class TestTypeChecking(TestCase):

    def test_check_value__valid_string(self):
        value = "x7430x"
        value_name = "ID"
        value_type = str

        value_okay = check_value(value, value_name, value_type)
        self.assertTrue(value_okay)

    def test_check_value__valid_int(self):
        value = 1234
        value_name = "ID"
        value_type = int

        value_okay = check_value(value, value_name, value_type)
        self.assertTrue(value_okay)

    def test_check_value__string_none(self):
        value = None
        value_name = "ID"
        value_type = str

        expected_exception_message = "{} cannot be `None`.".format(value_name)

        with self.assertRaises(ValueError) as context_manager:
            check_value(value, value_name, value_type)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_check_value__int_none(self):
        value = None
        value_name = "ID"
        value_type = int

        expected_exception_message = "{} cannot be `None`.".format(value_name)

        with self.assertRaises(ValueError) as context_manager:
            check_value(value, value_name, value_type)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_check_value__wrong_type(self):
        value = 45
        value_name = "ID"
        value_type = str

        expected_exception_message = "{} has to be an instance of {} or a subclass of it and not {}.".format(value_name, type(value_type), type(value))

        with self.assertRaises(TypeError) as context_manager:
            check_value(value, value_name, type)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_check_string__valid(self):
        value = "x7430x"
        value_name = "ID"

        value_okay = check_string(value, value_name)
        self.assertTrue(value_okay)

    def test_check_string__string_empty(self):
        value = ""
        value_name = "ID"
        value_type = str

        expected_exception_message = "{} cannot be empty.".format(value_name)

        with self.assertRaises(ValueError) as context_manager:
            check_string(value, value_name)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_check_string__wrong_type(self):
        value = 123
        value_name = "ID"
        value_type = str

        expected_exception_message = "{} has to be an instance of {} or a subclass of it and not {}.".format(value_name, value_type, type(value))

        with self.assertRaises(TypeError) as context_manager:
            check_string(value, value_name)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))

    def test_check_string__string_none(self):
        value = None
        value_name = "ID"

        expected_exception_message = "{} cannot be `None`.".format(value_name)

        with self.assertRaises(ValueError) as context_manager:
            check_string(value, value_name)

        exception = context_manager.exception
        self.assertEqual(expected_exception_message, str(exception))
