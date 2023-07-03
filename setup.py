from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    LONG_DESCRIPTION = f.read()

VERSION = '0.0.4'
DESCRIPTION = 'Encoding and decoding strings using keys'

# Setting up
setup(
    name="enigmacrypt",
    version=VERSION,
    author="WooksCode (Wojciech Karwowski)",
    author_email="<wookscode.kontakt@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/Wooks08/EnigmaCrypt",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.07",
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    keywords=['python', 'encode', 'decode', 'decoder',
              'encoder', 'string encryption', 'string decryption'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
