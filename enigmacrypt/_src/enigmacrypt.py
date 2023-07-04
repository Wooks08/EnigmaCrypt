from decrypt import Decrypter
from encrypt import Encrypter
from key import Validator, Formatter
from file_manage import File_Manage


class Decryption:
    def decrypt_string(self, text, key):
        decrypter = Decrypter()
        return decrypter.decrypt(text, key)

    def decrypt_file(self, fp, key):
        file_manage = File_Manage()
        file_lines = file_manage.read_file(fp)
        lines = self.decrypt_string(file_lines, key)
        print(lines)
        file_manage.write_file(fp, lines[0])


class Encryption:
    def encrypt_string(self, text):
        encrypter = Encrypter()
        return encrypter.encrypt(text)

    def encrypt_file(self, fp):
        file_manage = File_Manage()
        file_lines = file_manage.read_file(fp)
        lines, key = self.encrypt_string(file_lines)

        file_manage.write_file(fp, lines)
        return key


class Key:
    def validate(self, key):
        validator = Validator()
        return validator.validate(key)

    def key_info(self, key):
        formatter = Formatter()
        return formatter.format_key(key)
