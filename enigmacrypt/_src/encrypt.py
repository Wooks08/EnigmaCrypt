import random
import string
import json
import os


class Encrypter:
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
        min_len = 0
        max_len = 0

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

        min_len += 1
        max_len += 1

        # adding digits
        key_list.append(''.join(changed_digits))

        min_len += 10
        max_len += 10

        # control digits number 1
        control_dig_num1 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num1))

        max_len += 5

        # adding letter informing about text inversion
        if inverted:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        min_len += 1
        max_len += 1

        # control digits number 2
        control_dig_num2 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num2))

        max_len += 5

        # adding letter informing about text inversion2
        if inverted2:
            key_list.append(random.choice(string.ascii_lowercase))
        else:
            key_list.append(random.choice(string.ascii_uppercase))

        min_len += 1
        max_len += 1

        # control digits number 3
        control_dig_num3 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num3))

        max_len += 5

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

        min_len += 1
        max_len += 1

        # control digits number 4
        control_dig_num4 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num4))

        max_len += 5

        # adding alphabet
        key_list.append(''.join(changed_alphabet))

        min_len += len(changed_alphabet)
        max_len += len(changed_alphabet)

        # control digits number 5
        control_dig_num5 = random.randint(0, 5)
        key_list.extend(random.choice(string.digits)
                        for _ in range(control_dig_num5))

        max_len += 5

        # adding digits which inform about number of digits in each control number
        key_list.extend(str(control_dig_num) for control_dig_num in [
                        control_dig_num1, control_dig_num2, control_dig_num3, control_dig_num4, control_dig_num5])

        min_len += 5
        max_len += 5

        validate_data_values = {
            "max_min_len": {
                "min": min_len,
                "max": max_len
            },
        }

        with open("enigmacrypt/_src/validate_data.json", 'w') as f:
            json.dump(validate_data_values, f, indent=4)
            f.close()

        # returning key
        key = ''.join(key_list)
        return key

    # encoding method
    def encrypt(self, text: str):
        if not isinstance(text, str) and not isinstance(text, list):
            raise ValueError(
                f"Argument provided for encryption has to be a string. Argument of {type(text)} has been given instead")
        # checking args
        if text in ['', ' ']:
            raise ValueError(
                f"String provided for encryption has to contain any character other than ` `. `{text}` provided.")

        if isinstance(text, list):
            text_is_list = True
            text = ''.join(text)
        else:
            text_is_list = False

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
        encrypted_text_list = []
        for i, ch in enumerate(chars_in_text):
            if ch in self.letters:
                index_in_text = text.index(ch)
                if text[index_in_text - 1] == "\\":
                    continue
                else:
                    index = self.letters.index(ch)
                    encrypted_text_list.append(changed_alphabet[index])
            elif ch in self.digits:
                index = self.digits.index(ch)
                encrypted_text_list.append(changed_digits[index])
            else:
                encrypted_text_list.append(ch)

        encrypted_text = ''.join(encrypted_text_list)

        # deciding whether to invert text or not
        if random.choice([True, False]):
            encrypted_text = encrypted_text[::-1]
            inverted2 = True
        else:
            inverted2 = False

        # generating key
        key = self.generate_key(changed_digits, inverted,
                                inverted2, changed_alphabet)
        if text_is_list:
            encrypted_text = encrypted_text.split('\n')
            encrypted_text_file_list = [
                item + "\n" for item in encrypted_text if encrypted_text.index(item) < len(encrypted_text) - 1]
            encrypted_text_file_list.append(encrypted_text[-1])
            return [encrypted_text_file_list, key]
        else:
            return [encrypted_text, key]


if __name__ == '__main__':
    encrypter = Encrypter()
    _, key = encrypter.encrypt("lol")
    print(key)
