from ccwc.main import count_lines, count_words, count_bytes, count_characters, main

from unittest.mock import patch, mock_open


def test_count_lines():
    assert count_lines("Hello\nWorld") == 2
    assert count_lines("") == 0
    assert count_lines("Single line") == 1


def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("") == 0
    assert count_words("One") == 1


def test_count_bytes():
    assert count_bytes("Hello") == 5
    assert count_bytes("你好") == 6  # Assuming UTF-8 encoding
    assert count_bytes("") == 0


def test_count_characters():
    assert count_characters("Hello") == 5
    assert count_characters("你好") == 2
    assert count_characters("") == 0


def test_main_with_lines_option():
    test_args = ['ccwc', '-l', 'test.txt']
    test_data = b'Hello\nWorld'  # Note the 'b' prefix to denote a byte string
    with patch('sys.argv', test_args):
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            assert main() == '2 test.txt'

    test_args = ['ccwc', '-w', 'test.txt']
    with patch('sys.argv', test_args):
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            assert main() == '2 test.txt'

    test_args = ['ccwc', '-m', 'test.txt']
    with patch('sys.argv', test_args):
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            assert main() == '11 test.txt'

    test_args = ['ccwc', '-c', 'test.txt']
    with patch('sys.argv', test_args):
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            assert main() == '342190 test.txt'

    test_args = ['ccwc', 'test.txt']
    with patch('sys.argv', test_args):
        with patch('builtins.open', mock_open(read_data=test_data)) as mock_file:
            assert main() == '2 2 342190 test.txt'
