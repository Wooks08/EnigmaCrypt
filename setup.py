from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.1'
DESCRIPTION = 'Encoding and decoding strings using keys'

# Setting up
setup(
    name="enigma-crypt",
    version=VERSION,
    author="WooksCode (Wojciech Karwowski)",
    author_email="<wookscode.kontakt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/Wooks08/EnigmaCrypt",
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'encode', 'decode', 'decoder',
              'encoder', 'string encryption', 'string decryption'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
