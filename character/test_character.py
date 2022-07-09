#!/bin/python3
import unittest
from character import Character

"""In the current setup all tests are contained within a single
test case, 'TestCharacter', however, it could be beneficial to
split the test case into two.

By splitting the test case into 'TestCharacterName' and
'TestCharacterLevel', the respective functionality could be tested
independently. Additionally, if the test fixture required to test
each functionality was different, no unnecessary setup would have
to be performed."""


class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character = Character()

    def tearDown(self):
        self.character = None

    def test_set_level_valid(self):

        new_level = 20
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, new_level)

    def test_set_level_below_min(self):

        new_level = Character._MIN_LEVEL - 10
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, Character._MIN_LEVEL)

    def test_set_level_above_max(self):

        new_level = Character._MAX_LEVEL + 10
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, Character._MAX_LEVEL)

    def test_level_up_valid_test(self):

        no_level_ups = 10
        for _ in range(no_level_ups):
            self.character.level_up()

        self.assertEqual(self.character.level, Character._MIN_LEVEL + no_level_ups)

    def test_level_up_above_max(self):

        for _ in range(Character._MAX_LEVEL + 10):
            self.character.level_up()

        self.assertEqual(self.character.level, Character._MAX_LEVEL)

    def test_set_name_valid(self):

        # Create new name with min length
        new_name = "a" * self.character._MIN_NAME_LENGTH

        ret = self.character.set_name(new_name)

        self.assertTrue(ret)  # Check that methods returns true
        self.assertEqual(self.character.name, new_name)  # Check that name has changed

    def test_set_name_invalid(self):

        original_name = self.character.name

        # Create new name with max length + 1
        new_name = "a" * (self.character._MAX_NAME_LENGTH+1)

        ret = self.character.set_name(new_name)

        ret = True

        self.assertFalse(ret)  # Check that methods returns false
        self.assertEqual(self.character.name, original_name)  # Check that name has not changed


if __name__ == "__main__":
    unittest.main()
