import string


class Decrypter():
    digits = string.digits
    letters = string.ascii_letters

    def __init__(self):
        self.inverted = None
        self.inverted2 = None
        self.list_key = None

    def remove_control_digits(self, control_digits: int):
        if control_digits != 0:
            self.list_key = self.list_key[int(control_digits):]

    def inverted_checker(self, letter: str, to_remove: bool = True):
        if to_remove:
            self.list_key.remove(letter)

        if letter.islower():
            return True
        else:
            return False

    def formatting_key(self, key):
        # checking if digits are inverted
        self.list_key = list(key)

        # control digits
        control_dig_num1 = int(self.list_key[-5])
        control_dig_num2 = int(self.list_key[-4])
        control_dig_num3 = int(self.list_key[-3])
        control_dig_num4 = int(self.list_key[-2])
        control_dig_num5 = int(self.list_key[-1])

        digits_inverted = self.inverted_checker(self.list_key[0], False)

        # extracting digits
        digits_changed = self.list_key[1:11]
        if digits_inverted:
            digits_changed = digits_changed[::-1]

        self.list_key = self.list_key[11:]

        # first control digits
        self.remove_control_digits(control_dig_num1)

        # is inverted
        self.inverted = self.inverted_checker(self.list_key[0])

        # second control digits
        self.remove_control_digits(control_dig_num2)

        # is inverted2
        self.inverted2 = self.inverted_checker(self.list_key[0])

        # third control digits
        self.remove_control_digits(control_dig_num3)

        # checking if alphabet is inverted
        inverted_alphabet = self.inverted_checker(self.list_key[0])

        # fourth control digits
        self.remove_control_digits(control_dig_num4)

        # extracting alphabet
        alphabet_changed = self.list_key[:52]

        if inverted_alphabet:
            alphabet_changed = alphabet_changed[::-1]

        # return values
        digits_changed = ''.join(digits_changed)
        alphabet_changed = ''.join(alphabet_changed)

        return [digits_changed, alphabet_changed]

    def decrypt(self, text, key):
        changed_digits, changed_alphabet = self.formatting_key(key)

        list_text = list(text)

        if self.inverted:
            list_text = list_text[::-1]
        if self.inverted2:
            list_text = list_text[::-1]

        list_text = [Decrypter.digits[changed_digits.index(ch)] if ch in Decrypter.digits else Decrypter.letters[changed_alphabet.index(
            ch)] if ch in Decrypter.letters else ch for ch in list_text]

        decrypted_text = ''.join(list_text)

        return decrypted_text
