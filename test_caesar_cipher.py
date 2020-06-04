from cypher import encrypt, decrypt, break_code


# def test_version():
#     assert __version__ == '0.1.0'

def test_encrypt_lower():
    actual = encrypt('abc', 1) 
    expected = 'bcd'
    assert actual == expected


def test_encrypt__lower_wrap():
    actual = encrypt('xyz', 1) 
    expected = 'yza'
    assert actual == expected

def test_encrypt_upper():
    actual = encrypt('ABC', 1) 
    expected = 'BCD'
    assert actual == expected


def test_encrypt_upper_wrap():
    actual = encrypt('XYZ', 1) 
    expected = 'YZA'
    assert actual == expected

def test_encrypt_non_string():
    actual = encrypt('X8Z', 1) 
    expected = 'Y8A'
    assert actual == expected


def test_break_code():
    encrypted = encrypt('It was the best of times, it was the worst of times.', 4)
    actual = break_code(encrypted) 
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected

def test_break_code_wrap():
    encrypted = encrypt('It was the best of times, it was the worst of times.', 30)
    actual = break_code(encrypted) 
    expected = 'It was the best of times, it was the worst of times.'
    assert actual == expected

def test_break_code_wonka():
    encrypted = encrypt('We are the dreams of makers and the makers of dreams 111', 11)
    actual = break_code(encrypted) 
    expected = 'We are the dreams of makers and the makers of dreams 111'
    assert actual == expected

def test_break_code_wonka_wrap():
    encrypted = encrypt('We are the dreams of makers and the makers of dreams 111', 30)
    actual = break_code(encrypted) 
    expected = 'We are the dreams of makers and the makers of dreams 111'
    assert actual == expected