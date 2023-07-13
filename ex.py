import time

from selenium import webdriver


from unittest import TestCase


class MyTests(TestCase):
    def test_one_plus_two(self):
        self.assertEqual(1 + 2, 3)