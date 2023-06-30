import string
import json


class Validator():

    def validate(self, key):
        with open("app/enigmacrypt/_src/validate_data.json", 'r') as f:
            validate_data_values = json.load(f)
            f.close()

        min_len = validate_data_values['max_min_len']['min']
        max_len = validate_data_values['max_min_len']['max']

        if (not key[0] in string.ascii_letters) or (not key[-1] in string.digits) or (not len(key) > min_len) or (not len(key) < max_len):
            return False

        return True


class Formatter():
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

    def format_key(self, key):
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

        return [digits_changed, alphabet_changed, self.inverted, self.inverted2]


if __name__ == '__main__':
    KEY = "t25169380473241B71181Mo662GuKhNazFAJMCpZqPyfRnctesQLvUDdSoWkrbxYVIHTigBXOmljEw3814145035"

    # formatter = Formatter()
    # digits, alphabet, inverted, inverted2 = formatter.format_key(KEY)
    # print(
    #     f"Digits: {digits} \nAlphabet: {alphabet} \nInverted: {inverted} \nInverted2: {inverted2}")

    validator = Validator()
    valid = validator.validate(KEY)

    print(valid)
