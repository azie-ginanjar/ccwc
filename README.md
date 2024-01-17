# CCWC - Custom Word Count
## Overview

`ccwc` is a Python-based command-line utility that mimics the basic functionality of the Unix wc command. It is designed to count lines, words, bytes, and characters in a text file or standard input.


## Features
- Count the number of lines in a text (-l option)
- Count the number of words in a text (-w option)
- Count the number of bytes in a text (-c option)
- Count the number of characters in a text (-m option)

## Installation

To install `ccwc`, clone this repository and use Poetry to install the package:
```bash
git clone https://github.com/yourusername/ccwc.git
cd ccwc
poetry install
```

## Usage

To use `ccwc`, run the following command in your terminal:
```bash
ccwc [options] [filename]
```

If no filename is specified, `ccwc` will read from standard input.

### Options
- `-l`, `--lines`: Count the number of lines
- `-w`, `--words`: Count the number of words
- `-c`, `--bytes`: Count the number of bytes
- `-m`, `--chars`: Count the number of characters

### Examples

Count the number of lines in example.txt:
```bash
ccwc -l example.txt
```

Count the number of words in example.txt:
```bash
ccwc -w example.txt
```

Count the number of lines, words, and bytes in standard input:
```bash
cat example.txt | ccwc -l -w -c
```

## Development

To contribute to `ccwc`, you can fork the repository and then clone your fork. After making your changes, submit a pull request.

## Testing
To run unit test, run the following command in your terminal
```bash
poetry run pytest
```

## License
This project is licensed under the MIT License.

## Acknowledgments
Mention any individuals or projects that helped inspire or contribute to this tool.