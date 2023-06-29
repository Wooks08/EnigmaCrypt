import random
import string


class Encoder():
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

        # adding digit informing about digits inversion
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

        # adding digit informing about text inversion
        if inverted:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        # control digits number 2
        control_dig_num2 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num2))

        # adding digit informing about text inversion2
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

        # adding digit informing about alphabet inversion
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
    def encode(self, text):
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
        encoded_text_list = []
        for i, ch in enumerate(chars_in_text):
            if ch in self.letters:
                index = self.letters.index(ch)
                encoded_text_list.append(changed_alphabet[index])
            elif ch in self.digits:
                index = self.digits.index(ch)
                encoded_text_list.append(changed_digits[index])
            else:
                encoded_text_list.append(ch)

        encoded_text = ''.join(encoded_text_list)

        # deciding whether to invert text or not
        if random.choice([True, False]):
            encoded_text = encoded_text[::-1]
            inverted2 = True
        else:
            inverted2 = False

        # generating key
        key = self.generate_key(changed_digits, inverted,
                                inverted2, changed_alphabet)
        return [encoded_text, key]
