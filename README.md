# EnigmaCrypt
EnigmaCrypt is a Python package that provides a simple and secure way to encrypt and decrypt strings. It uses a unique encryption algorithm and generates a key that can be used to decode the encrypted string.

## Installation
To install EnigmaCrypt, you can use pip:

```pip install enigmacrypt```

## Usage
Here's a simple example of how to use EnigmaCrypt to encrypt and decrypt a string:

```python
from enigmacrypt import Encryption, Decryption

# Create an instance of Encryption
encryption = Encryption()

# Encrypt a string
encrypted_string, key = encryption.encrypt("Hello, World!")

# Create an instance of Decryption
decryption = Decryption()

# Decrypt the string using the generated key
decrypted_string = decryption.decrypt(encrypted_string, key)

print(decrypted_string)  # Output: Hello, World!
```

## Contributing
Contributions are welcome! If you have any bug reports, feature requests, or suggestions, please open an issue on the GitHub repository. If you'd like to contribute code, you can fork the repository and create a pull request with your changes.

## License
EnigmaCrypt is licensed under the MIT License.

## Contact
If you have any questions or need support, you can reach out to the project maintainer at wookscode.contact@gmail.com.

## Acknowledgments
EnigmaCrypt works by shuffling the alphabet and digits in random order and then generating quite complex key to show crucial information for decryption process

## Disclaimer
Please note that EnigmaCrypt is provided as-is and is not responsible for any security breaches or issues that may arise from its usage. It is always recommended to use additional security measures and best practices when handling sensitive information.
