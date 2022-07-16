#!/bin/python3
import unittest
import json

import character

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
        self.character = character.Character()

    def tearDown(self):
        self.character = None

    def test_set_level_valid(self):

        new_level = 20
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, new_level)

    def test_set_level_below_min(self):

        new_level = character.Character._MIN_LEVEL - 10
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, character.Character._MIN_LEVEL)

    def test_set_level_above_max(self):

        new_level = character.Character._MAX_LEVEL + 10
        self.character.set_level(new_level)

        self.assertEqual(self.character.level, character.Character._MAX_LEVEL)

    def test_level_up_valid_test(self):

        no_level_ups = 10
        for _ in range(no_level_ups):
            self.character.level_up()

        self.assertEqual(self.character.level, character.Character._MIN_LEVEL + no_level_ups)

    def test_level_up_above_max(self):

        for _ in range(character.Character._MAX_LEVEL + 10):
            self.character.level_up()

        self.assertEqual(self.character.level, character.Character._MAX_LEVEL)

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

        self.assertFalse(ret)  # Check that methods returns false
        self.assertEqual(self.character.name, original_name)  # Check that name has not changed

    def test_export_to_json(self):

        # Valid values
        name = "a" * (self.character._MAX_NAME_LENGTH)
        level = self.character._MAX_LEVEL

        self.character.set_name(name)
        self.character.set_level(level)

        ret, character_json = self.character.export_to_json()

        self.assertTrue(ret)

        json_dict = json.loads(character_json)

        self.assertTrue("name" in json_dict)
        self.assertEqual(json_dict.get("name"), name)

        self.assertTrue("level" in json_dict)
        self.assertEqual(json_dict.get("level"), level)

    def test_export_to_json_invalid_name(self):

        # Name is too long
        name = "a" * (self.character._MAX_NAME_LENGTH+1)

        self.character.set_name(name)
        ret, character_json = self.character.export_to_json()

        self.assertFalse(ret)
        self.assertEqual(character_json, "")

    def test_import_from_json(self):

        name = "a" * (self.character._MAX_NAME_LENGTH)
        level = self.character._MAX_LEVEL

        character_dict = {
            "name": name,
            "level": level
        }

        self.character.import_from_json(json.dumps(character_dict))

        self.assertEqual(self.character.name, name)
        self.assertEqual(self.character.level, level)

    def test_export_import(self):

        name = "a" * (self.character._MAX_NAME_LENGTH)
        level = self.character._MAX_LEVEL

        self.character.set_name(name)
        self.character.set_level(level)

        _, character_json = self.character.export_to_json()

        # Create new character and import
        new_character = character.Character()
        new_character.import_from_json(character_json)

        # Check that name and level are equal
        self.assertEqual(self.character.name, new_character.name)
        self.assertEqual(self.character.level, new_character.level)


if __name__ == "__main__":
    unittest.main()
