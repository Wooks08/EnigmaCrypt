import string


class Validator():
    def validate(self, key):
        if (not key[0] in string.ascii_letters) or (not key[-1] in string.digits) or (not len(key) > 71) or (not len(key) < 96):
            return False

        return True


if __name__ == '__main__':
    validator = Validator()
    valid = validator.validate(
        "t25169380473241B71181Mo662GuKhNazFAJMCpZqPyfRnctesQLvUDdSoWkrbxYVIHTigBXOmljEw3814145035")

    print(valid)
