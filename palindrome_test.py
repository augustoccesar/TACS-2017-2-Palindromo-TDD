import unittest

from palindrome import is_palindrome


class IsPalindromeTest(unittest.TestCase):
    def test_palindrome_full_alphanumeric(self):
        self.assertTrue(is_palindrome('arara'))

    def test_not_palindrome_full_alphanumeric(self):
        self.assertFalse(is_palindrome('augusto'))

    def test_palindrome_with_dash_and_space(self):
        self.assertTrue(is_palindrome("ar-a-ra arara"))

    def test_not_palindrome_with_dash_and_space(self):
        self.assertFalse(is_palindrome("aug-usto cesar"))

    def test_assignment_defined_string_1(self):
        self.assertTrue(is_palindrome("Socorram-me subi no onibus em Marrocos"))

    def test_assignment_defined_string_2(self):
        self.assertTrue(is_palindrome("Anotaram a data da maratona"))


if __name__ == '__main__':
    unittest.main()
