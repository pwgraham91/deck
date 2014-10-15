from django.test import TestCase

class BasicMathTestCase(TestCase):
    def test_math(self):
        a = 1
        b = 1
        self.assertEqual(a+b, 2)

    def test_failing_case(self):
        a = 1
        b = 1
        self.assertEqual(a+b, 1)