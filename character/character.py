import typing
import json


class Character:

    # This class has no class docstring, which will cause pylint to raise a
    # convention message, this can be disabled using the syntax below.
    # See link below for more information on message control.
    # https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html

    # pylint: disable=missing-class-docstring

    """Character class.

    Simple implementation of a character class with
    levels, name, and setter functions.

    The class also contains a number of private
    constant members which define the limits for the
    setter methods.

    Attributes:
        _MIN_LEVEL (int): The minimum level of a character
        _MAX_LEVEL (int): The maximum level of a character
        _MIN_NAME_LENGTH (int): The minimum length of a character name
        _MAX_NAME_LENGTH (int): The maximum length of a character name
    """

    _MIN_LEVEL = 1
    _MAX_LEVEL = 100

    _MIN_NAME_LENGTH = 1
    _MAX_NAME_LENGTH = 10

    def __init__(self) -> None:
        self.name = ""
        self.level = self._MIN_LEVEL

    def __repr__(self) -> str:
        return f"Character, {self.name = }, {self.level = }"

    def set_level(self, new_level) -> None:
        """Set the character level.

        If new_level is below the minimum level it is
        set to the minimum level.
        If new_level is above the maximum level it is
        set to the maximum level.

        Args:
            new_level (int): The level which the 
                character should be set to.

        Returns:
            None.
        """

        if new_level < self._MIN_LEVEL:
            self.level = self._MIN_LEVEL

        elif new_level > self._MAX_LEVEL:
            self.level = self._MAX_LEVEL

        else:
            self.level = new_level

    def level_up(self) -> None:
        """Level up the character.

        Increments the characters level by one.

        Returns:
            None.
        """

        if self.level < self._MAX_LEVEL:
            self.level += 1

    def _is_name_valid(self, new_name) -> bool:
        """Check if name is valid.

        A name is valid the length of the name is within
        the boundaries defined by the class members.

        Returns:
            (bool): True if the name is valid, otherwise
                False.
        """

        if len(new_name) < self._MIN_NAME_LENGTH or len(new_name) > self._MAX_NAME_LENGTH:
            return False

        return True

    def set_name(self, new_name) -> bool:
        """Set the character name.

        If the length of the name is below the minimum
        length, it is not set.
        If the length of the name is above the maximum
        length, it is not set.

        Args:
            new_name (str): The new name.

        Returns:
            (bool): True if successful, otherwise False.
        """

        if not self._is_name_valid(new_name):
            return False

        self.name = new_name
        return True

    def import_from_json(self, character_json) -> bool:
        """Import character from JSON.

        The JSON must contain all required keys, and each
        key must have a valid value, other wise the import
        fails.

        Args:
            character_json (str): JSON string representing the
                character.

        Returns:
            (bool): True if successful, otherwise False.
        """

        character_dict = json.loads(character_json)

        # Check that dict contains all required keywords
        keys = ["name", "level"]
        if not all(k in character_dict for k in keys):
            return False

        # Check that name is valid
        name = character_dict.get("name")
        if not self._is_name_valid(name):
            return False
        self.set_name(name)

        level = character_dict.get("level")
        self.set_level(level)

        return True

    def export_to_json(self) -> typing.Tuple[bool, str]:
        """Export character to JSON.

        A character can only be exported if the name is valid.

        Returns:
            (bool): True if successful, otherwise False.
            (str): JSON string representing the character
                if successful, otherwise empty string.
        """

        if not self._is_name_valid(self.name):
            print("Name is not valid")
            return False, ""

        character_dict = {
            "name": self.name,
            "level": self.level
        }

        return True, json.dumps(character_dict)


def main():

    # Example of manually testing set_level() functionality

    character = Character()

    character.set_level(-1)
    print(f"set_level(-1), character.level: {character.level}")
    # set_level(-1), character.level: 1

    character.set_level(150)
    print(f"set_level(150), character.level: {character.level}")
    # set_level(150), character.level: 100

    character.set_name("Rune")

    _, c_json = character.export_to_json()
    print(c_json)
    rune = Character()
    rune.import_from_json(c_json)
    print(rune)

    name = "a" * (Character._MAX_NAME_LENGTH)
    level = Character._MAX_LEVEL

    character_json = f'"name": "{name}", "level": {level}'

    rune.import_from_json(character_json)


if __name__ == "__main__":
    main()
