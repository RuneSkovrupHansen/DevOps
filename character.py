class Character:

    # This class has no class docstring, which will cause pylint to raise a 
    # convention message, this can be disabled using the syntax below.
    # See link below for more information on message control.
    # https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html

    # pylint: disable=missing-class-docstring

    _MIN_LEVEL = 1
    _MAX_LEVEL = 100 

    _MIN_NAME_LENGTH = 1
    _MAX_NAME_LENGTH = 10

    def __init__(self) -> None:
        self.name = ""
        self.level = self._MIN_LEVEL

    def set_level(self, new_level) -> None:

        if new_level < self._MIN_LEVEL:
            self.level = self._MIN_LEVEL

        elif new_level > self._MAX_LEVEL:
            self.level = self._MAX_LEVEL

        else:
            self.level = new_level

    def level_up(self) -> None:

        if self.level < self._MAX_LEVEL:
            self.level += 1

    def set_name(self, new_name) -> bool:

        if len(new_name) < self._MIN_NAME_LENGTH or len(new_name) > self._MAX_NAME_LENGTH:
            return False 

        self.name = new_name
        return True


def main():

    #Example of manually testing set_level() funcitonality
    
    character = Character()

    character.set_level(-1)
    print(f"set_level(-1), chracter.level: {character.level}")
    # set_level(-1), chracter.level: 1

    character.set_level(150)
    print(f"set_level(150), chracter.level: {character.level}")
    # set_level(150), chracter.level: 100

if __name__ == "__main__":
    main()

