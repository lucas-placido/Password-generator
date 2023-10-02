import random
import string


class RandomPassword:
    def __init__(self) -> None:
        self.lowerLetters = string.ascii_lowercase
        self.upperLetters = string.ascii_uppercase
        self.digits = string.digits
        self.special_characters = "[](){}!?^~#%@,;/+-&*$"

    def validate_password(self, components, password):
        for i in components:
            if set(i).intersection(set(password)):
                continue
            else:
                return False
        return True

    def generate_password(
        self,
        length=12,
        upperLetters=True,
        lowerLetters=True,
        digits=True,
        special_characters=True,
        custom_characters="",
    ):
        options = {
            str(self.lowerLetters): lowerLetters,
            str(self.upperLetters): upperLetters,
            str(self.digits): digits,
            str(self.special_characters): special_characters,
        }
        if custom_characters:
            options[custom_characters] = True
        components = [key for key in options if options[key]]
        characters = "".join(components)

        while True:
            password = "".join([random.choice(characters) for i in range(length)])
            valid = self.validate_password(components, password)
            if valid:
                break
        return password


rp = RandomPassword()
if __name__ == "__main__":
    rp.generate_password()
