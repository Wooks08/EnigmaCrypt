import random
import string


class Encrypter():
    # getting letters and digit
    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits

    # method that randomize list of given chars
    def randomize(self, char_list: list):
        char_list = list(char_list)
        random.shuffle(char_list)
        return char_list

    def generate_key(self, changed_digits, inverted, inverted2, changed_alphabet):
        key_list = []
        # deciding whether to invert changed alphabet or not
        if random.choice([True, False]):
            changed_digits = changed_digits[::-1]
            inverted_digits = True
        else:
            inverted_digits = False

        # adding letter informing about digits inversion
        if inverted_digits:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        # adding digits
        key_list.append(''.join(changed_digits))

        # control digits number 1
        control_dig_num1 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num1))

        # adding letter informing about text inversion
        if inverted:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        # control digits number 2
        control_dig_num2 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num2))

        # adding letter informing about text inversion2
        if inverted2:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        # control digits number 3
        control_dig_num3 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num3))

        # deciding whether to invert changed alphabet or not
        if random.choice([True, False]):
            changed_alphabet = changed_alphabet[::-1]
            inverted_alphabet = True
        else:
            inverted_alphabet = False

        # adding letter informing about alphabet inversion
        if inverted_alphabet:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        # control digits number 4
        control_dig_num4 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num4))

        # adding alphabet
        key_list.append(''.join(changed_alphabet))

        # control digits number 5
        control_dig_num5 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num5))

        # adding digits which inform about number of digits in each control number
        key_list.extend(str(control_dig_num) for control_dig_num in [
                        control_dig_num1, control_dig_num2, control_dig_num3, control_dig_num4, control_dig_num5])

        # returning key
        key = ''.join(key_list)
        return key

    # encoding method
    def encrypt(self, text: str):
        if not isinstance(text, str):
            raise ValueError(
                f"Argument provided for encryption has to be a string. Argument of {type(text)} has been given instead")
        # checking args
        if text in ['', ' ']:
            raise ValueError(
                f"String provided for encryption has to contain any character other than ` `. `{text}` provided.    ")

        chars_in_text = [ch for ch in text]
        # deciding whether to invert text or not
        if random.choice([True, False]):
            chars_in_text = chars_in_text[::-1]
            inverted = True
        else:
            inverted = False

        # randomizing alphabet and digits
        changed_alphabet = self.randomize(self.letters)
        changed_digits = self.randomize(self.digits)

        # encoding
        encryptd_text_list = []
        for i, ch in enumerate(chars_in_text):
            if ch in self.letters:
                index = self.letters.index(ch)
                encryptd_text_list.append(changed_alphabet[index])
            elif ch in self.digits:
                index = self.digits.index(ch)
                encryptd_text_list.append(changed_digits[index])
            else:
                encryptd_text_list.append(ch)

        encryptd_text = ''.join(encryptd_text_list)

        # deciding whether to invert text or not
        if random.choice([True, False]):
            encryptd_text = encryptd_text[::-1]
            inverted2 = True
        else:
            inverted2 = False

        # generating key
        key = self.generate_key(changed_digits, inverted,
                                inverted2, changed_alphabet)
        return [encryptd_text, key]


if __name__ == '__main__':
    encrypter = Encrypter()
    encrypter.encrypt(12)
