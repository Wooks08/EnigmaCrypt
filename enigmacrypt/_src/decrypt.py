import string
from key import Validator, Formatter


class InvalidKeyError(Exception):
    def __init__(self, value):
        self.value = value


def raiseInvalidKeyError():
    raise InvalidKeyError(
        "Provided key is invalid. Check it and try again.")


class Decrypter:
    digits = string.digits
    letters = string.ascii_letters

    def decrypt(self, text, key):
        if (not isinstance(text, str) and not isinstance(text, list)) or (not isinstance(key, str)):
            raise ValueError(
                f"Argument with text to decryption has to be string or list and argument with encryption key has to be a string. Types provided: \n- text argument: {type(text)} \n- key argument: {type(key)}.")

        if text in ['', ' '] or key in ['', ' ']:
            raise ValueError(
                f"Arguments have to contain any character other than ` `. String: `{text}`, key: `{key}` provided.")

        if isinstance(text, list):
            text_is_list = True
        else:
            text_is_list = False

        if text_is_list:
            text = ''.join(text)

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

        decrypted_text = []
        for ch in list_text:
            if ch in Decrypter.digits:
                digit = Decrypter.digits[changed_digits.index(ch)]
                decrypted_text.append(digit)
            elif ch in Decrypter.letters:
                if not list_text.index(ch) - 1 == '\\':
                    letter = Decrypter.letters[changed_alphabet.index(ch)]
                    decrypted_text.append(letter)
            else:
                decrypted_text.append(ch)

        decrypted_text = ''.join(decrypted_text)

        if text_is_list:
            decrypted_text = decrypted_text.split('\n')
            decrypted_text_file_list = [
                item + "\n" for item in decrypted_text if decrypted_text.index(item) < len(decrypted_text) - 1]
            decrypted_text_file_list.append(decrypted_text[-1])
            return [decrypted_text_file_list]
        else:
            return decrypted_text


if __name__ == "__main__":
    decrypter = Decrypter()
    text = decrypter.decrypt(
        "a", "t25169380473241B71181Mo662GuKhNazFAJMCpZqPyfRnctesQLvUDdSoWkrbxYVIHTigBXOmljEw3814145035")
    print(text)
