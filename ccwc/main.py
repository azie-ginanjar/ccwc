import argparse
import os
import sys


def count_lines(text):
    return len(text.splitlines())


def count_words(text):
    return len(text.split())


def count_bytes(text):
    return len(text.encode('utf-8'))


def count_characters(text):
    return len(text)


def main():
    parser = argparse.ArgumentParser(description="ccwc: A wc-like tool in Python")
    parser.add_argument('filename', nargs='?', help="File to process")
    parser.add_argument('-l', '--lines', action='store_true', help="Count lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count words")
    parser.add_argument('-c', '--bytes', action='store_true', help="Count bytes")
    parser.add_argument('-m', '--chars', action='store_true', help="Count characters")

    args = parser.parse_args()

    # Read from file or stdin
    if args.filename:
        with open(args.filename, 'rb') as file:  # Open in binary mode
            binary_content = file.read()
            text = binary_content.decode('utf-8')  # Decode using UTF-8 or other appropriate encoding
    else:
        text = sys.stdin.read()

    lines = count_lines(text)
    words = count_words(text)
    chars = count_characters(text)

    result = ''

    show_all = not (args.bytes or args.lines or args.words or args.chars)

    if show_all:
        result += '{} {} {}'.format(lines, words, os.path.getsize(args.filename))
    else:
        if args.bytes:
            result += ' {}'.format(os.path.getsize(args.filename))

        if args.lines:
            result += ' {}'.format(lines)

        if args.words:
            result += ' {}'.format(words)

        if args.chars:
            result += ' {}'.format(chars)

    result += ' {}'.format(args.filename) if args.filename else ''

    return result.strip()


if __name__ == "__main__":
    main()
