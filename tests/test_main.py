from ccwc.main import count_lines, count_words, count_bytes, count_characters


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
