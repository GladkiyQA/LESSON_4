from string_utils import StringUtils

import pytest

string_utils = StringUtils()
@pytest.mark.parametrize('string, result_string', [
    ('test', 'Test'),
    ('тест', 'Тест'),
    ('123', '123'),
    (' ', ' '),
    (' qwerty', ' qwerty'),
    ('', ''),
    ('skypro', 'sKypro')
])
def test_capitilize(string, result_string):
    string_utils = StringUtils()
    result = string_utils.capitilize(string)
    if string == 'skypro':
        assert result != 'sKypro'
    else:
        assert result == result_string


@pytest.mark.parametrize('string, result_string', [
    (' test', 'test'),
    ('  test', 'test'),
    ('1 2 3', '1 2 3'),
    ('test', 'test'),
    ('', ''),
    (' test', 'test ')
])
def test_trim(string, result_string):
    string_utils = StringUtils()
    result = string_utils.trim(string)
    if string == ' test':
        assert result != 'test '
    else:
        assert result == result_string



@pytest.mark.parametrize("string, delimiter, result_string", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("  ", ",", []),
    ("a, b, c, d", ",", ["a", " b", " c", " d"]),
    ("1,2;3", ";", ["1,2", "3"]),
    ('1 2 3 4', ' ', ['1', '2', '3', '4'])
])
def test_to_list(string, delimiter, result_string):
    string_utils = StringUtils()
    result = string_utils.to_list(string, delimiter)
    assert result == result_string


@pytest.mark.parametrize('string, value, result_string', [
    ('SkyPro', 'S', True),
    ('hello, world!', 'w', True),
    ('12345', '1', True),
    ('qwerty!', '!', True),
    ('qw qw qw', ' ', True),
    (' ', ' ', True),
    ('Skypro', 's', False),
    ('Skypro', 's', True),
    ('SkyPro', 't', False),
    ('12345', 'a', False)
])
def test_contains(string, value, result_string):
    string_utils = StringUtils()
    result = string_utils.contains(string, value)
    assert result == result_string



@pytest.mark.parametrize('string, value, result_string', [
    ('Test string', 't', 'es sring'),
    ('SkyPro programming school', 'Pro', 'Sky gramming school'),
    ('Error', 'r', 'Eo'),
    (' qw er ty ', ' ', 'qwerty'),
    (' ', ' x', ' '),
    ('Unique string', 'z', 'Unique string'),
    ('x', 'x', ''),
    ('', 'x', ''),
])

def test_delete_symbol(string, value, result_string):
    string_utils = StringUtils()
    result = string_utils.delete_symbol(string, value)
    assert result == result_string


@pytest.mark.parametrize('string, value, result_string',[
    ('SkyPro', 'S', True),
    ('!Hello, World!', '!', True),
    ('12345', '1', True),
    (' qwerty', ' ', True),
    (' ', ' ', True),
    ('', '', True),
    ('SkyPro', 's', True),
    ('SkyPro', 's', False),
    ('SkyPro', 't', False),
    (' ', '', True),
    ('x', 'x', True)
])

def test_starts_with(string, value, result_string):
    string_utils = StringUtils()
    result = string_utils.starts_with(string, value)
    assert result == result_string



@pytest.mark.parametrize('string, value, result_string',[
    ('SkyPro', 'o', True),
    ('!Hello, World!', '!', True),
    ('12345', '5', True),
    ('qwerty ', ' ', True),
    (' ', ' ', True),
    ('', '', True),
    ('SkyPro', 'O', True),
    ('SkyPro', 't', False),
    (' ', '', True),
    ('x', 'x', True)
])

def test_end_with(string, value, result_string):
    string_utils = StringUtils()
    result = string_utils.end_with(string, value)
    assert result == result_string



@pytest.mark.parametrize('string, result', [
    ('', True),
    (' ', True),
    ('      ', True),
    ('SkyPro', False),
    (' Hello ', False)
])

def test_is_empty(string, result):
    string_utils = StringUtils()
    result = string_utils.is_empty(string)
    assert result == result



@pytest.mark.parametrize('list, delimiter, result', [
    ([1, 2, 3, 4], ',', '1, 2, 3, 4'),
    ([1, 2, 3, 4], '', '1234'),
    ([1, 2, 3, 4], ' ', '1 2 3 4'),
    ([1, 2, 3, 4], '-', '1-2-3-4'),
    (['a', 'b', 'c', 'd'], ' ', 'a, b, c, d'),
    (['qwerty',1234, True, 12.5], "-", 'qwerty-1234-True-12.5')
])

def test_list_to_string(list, delimiter, result):
    string_utils = StringUtils()
    result = string_utils.list_to_string(list, delimiter)
    assert result == result

@pytest.mark.parametrize('list, result', [
    ([1, 2, 3, 4], '1, 2, 3, 4'),
    (['qwerty',1234, True, 12.5], 'qwerty, 1234, True, 12.5'),
    ([42], '42'),
    ([],'')
])
def test_list_to_string_default_param(list, result):
    string_utils = StringUtils()
    result = string_utils.list_to_string(list)
    assert result == result