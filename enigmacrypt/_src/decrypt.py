import string
from key import Validator, Formatter


class InvalidKeyError(Exception):
    def __init__(self, value):
        self.value = value


def raiseInvalidKeyError():
    raise InvalidKeyError(
        "Provided key is invalid. Check it and try again.")


class Decrypter():
    digits = string.digits
    letters = string.ascii_letters

    def decrypt(self, text, key):
        if not isinstance(text, str) or not isinstance(key, str):
            raise ValueError(
                f"Argument with text to decryption and argument with encryption key have to be a string. Types provided: \n- text argument: {type(text)} \n- key argument: {type(key)}.")

        if text in ['', ' '] or key in ['', ' ']:
            raise ValueError(
                f"Arguments have to contain any character other than ` `. String: `{text}`, key: `{key}` provided.")

        validator = Validator()
        if not validator.validate(key):
            raiseInvalidKeyError()

        formatter = Formatter()
        changed_digits, changed_alphabet, inverted, inverted2 = formatter.format_key(
            key)

        list_text = list(text)

        if inverted:
            list_text = list_text[::-1]
        if inverted2:
            list_text = list_text[::-1]

        list_text = [Decrypter.digits[changed_digits.index(ch)] if ch in Decrypter.digits else Decrypter.letters[changed_alphabet.index(
            ch)] if ch in Decrypter.letters else ch for ch in list_text]

        decrypted_text = ''.join(list_text)

        return decrypted_text


if __name__ == "__main__":
    decrypter = Decrypter()
    text = decrypter.decrypt(
        "a", "t25169380473241B71181Mo662GuKhNazFAJMCpZqPyfRnctesQLvUDdSoWkrbxYVIHTigBXOmljEw3814145035")
    print(text)
