from decrypt import Decrypter
from encrypt import Encrypter
from key import Validator, Formatter


class Decryption():
    def decrypt(self, text, key):
        decrypter = Decrypter()
        return decrypter.decrypt(text, key)


class Encryption():
    def encrypt(self, text):
        encrypter = Encrypter()
        return encrypter.encrypt(text)


class Key():
    def validate(self, key):
        validator = Validator()
        return validator.validate(key)

    def key_info(self, key):
        formatter = Formatter()
        return formatter.format_key(key)
