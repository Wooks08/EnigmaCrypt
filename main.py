import s_encoder
import s_decoder


class TextEncoder(s_encoder.Encoder):
    def encode(self, text):
        if not text:
            raise ValueError("Input text cannot be empty")
        if not isinstance(text, str):
            raise ValueError("Input must be a string")

        encoded_text, key = super().encode(text)

        return {'encoded_text': encoded_text, 'key': key}

    def __str__(self):
        return "TextEncoder"


class Decode():
    # getting user text
    def take_text(self):
        text = input("Type text to decode: ")
        key = input("Provide key: ")
        return text, key

    # encoding
    def decode(self):
        text, key = self.take_text()
        decoder = s_decoder.Decoder()
        decoded_text = decoder.decode(text, key)

        return decoded_text


class Main():
    def __init__(self):
        action = input("Select what you want to do: ")
        if action not in ['', None]:
            if action.lower() == 'encode':
                text = input("Type text to encode: ")
                encoder = TextEncoder()
                result = encoder.encode(text)
                print(f"Encoded text: {result['encoded_text']}")
                print(f"Key: {result['key']}")

            elif action.lower() == 'decode':
                decoder = Decode()
                decoded_text = decoder.decode()
                print(f"Decoded text: {decoded_text}")
            else:
                print("Invalid action selected.")


if __name__ == "__main__":
    Main()
