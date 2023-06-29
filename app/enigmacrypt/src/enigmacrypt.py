from decrypt import Decrypter
from encrypt import Encrypter


class Decryption():
    def decrypt(self, text, key):
        decrypter = Decrypter()
        return decrypter.decrypt(text, key)


class Encryption():
    def encrypt(self, text):
        encrypter = Encrypter()
        return encrypter.encrypt(text)
