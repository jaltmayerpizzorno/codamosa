# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    string_compressor_0 = module_0.__StringCompressor()

def test_case_1():
    int_0 = 1318
    str_0 = module_0.roman_encode(int_0)

def test_case_2():
    int_0 = 1291
    str_0 = module_0.roman_encode(int_0)

def test_case_3():
    int_0 = 1910
    str_0 = '(tz(CniAml/55[\\At'
    str_1 = module_0.asciify(str_0)
    str_2 = module_0.roman_encode(int_0)
    roman_numbers_0 = module_0.__RomanNumbers()
    str_3 = module_0.prettify(str_2)

def test_case_4():
    str_0 = ":4'3MI{36]qW:G%\x0cP M"
    str_1 = module_0.compress(str_0)

def test_case_5():
    str_0 = 'L4]F:IT~Ac(y/T\\'
    str_1 = module_0.prettify(str_0)

def test_case_6():
    str_0 = 'hello world'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()
    str_2 = 'hello   world'
    string_formatter_1 = module_0.__StringFormatter(str_2)
    str_3 = string_formatter_1.format()
    str_4 = 'hello,world'
    string_formatter_2 = module_0.__StringFormatter(str_4)
    str_5 = string_formatter_2.format()
    str_6 = 'contact me at email@example.com for more info'
    string_formatter_3 = module_0.__StringFormatter(str_6)
    str_7 = string_formatter_3.format()

def test_case_7():
    str_0 = 'Xed7VB~HD%\t\t\rZJ.~-'
    var_0 = module_0.camel_case_to_snake(str_0)
    str_1 = 'step'
    bool_0 = False
    str_2 = 'ygE00 o9'
    str_3 = module_0.snake_case_to_camel(str_1, bool_0, str_2)

def test_case_8():
    str_0 = 'the_snake_is_green'
    str_1 = module_0.snake_case_to_camel(str_0)

def test_case_9():
    str_0 = '\x0badh2,HJm'
    str_1 = module_0.shuffle(str_0)

def test_case_10():
    str_0 = "hJDl]'hA7&J!m "
    str_1 = module_0.strip_html(str_0)

def test_case_11():
    str_0 = 'b<Y.#x3=u:\r_?[v['
    str_1 = module_0.reverse(str_0)
    dict_0 = {}
    string_compressor_0 = module_0.__StringCompressor(**dict_0)
    str_2 = '\n    Checks if the given string represents a valid ISBN (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn(\'9780312498580\') # returns true\n    >>> is_isbn(\'1506715214\') # returns true\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN (10 or 13), false otherwise.\n    '
    str_3 = module_0.asciify(str_2)

def test_case_12():
    str_0 = ")r9n\\G'6!/bL"
    str_1 = 'JCB'
    str_2 = '"6FDJS\''
    str_3 = module_0.snake_case_to_camel(str_2)
    bool_0 = module_0.booleanize(str_0)
    str_4 = 'T,'
    str_5 = module_0.prettify(str_4)
    str_6 = module_0.strip_html(str_5)
    str_7 = module_0.slugify(str_0, str_1)
    str_8 = '.'
    str_9 = module_0.prettify(str_8)
    str_10 = "}X]b~aT8'("
    bool_1 = False
    str_11 = module_0.snake_case_to_camel(str_10, bool_1, str_7)

def test_case_13():
    str_0 = '\n    Checks if the given string contains HTML/XML tags.\n\n    By design, this function matches ANY type of tag, so don\'t expect to use it\n    as an HTML validator, its goal is to detect "malicious" or undesired tags in the text.\n\n    *Examples:*\n\n    >>> contains_html(\'my string is <strong>bold</strong>\') # returns true\n    >>> contains_html(\'my string is not bold\') # returns false\n\n    :param input_string: Text to check\n    :type input_string: str\n    :return: True if string contains html, false otherwise.\n    '
    str_1 = module_0.strip_margin(str_0)

def test_case_14():
    str_0 = 'hello world'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()
    str_2 = 'hello   world'
    string_formatter_1 = module_0.__StringFormatter(str_2)
    str_3 = string_formatter_1.format()
    str_4 = 'hello, world!'
    string_formatter_2 = module_0.__StringFormatter(str_4)
    str_5 = string_formatter_2.format()
    str_6 = 'check out this link: https://example.com'
    string_formatter_3 = module_0.__StringFormatter(str_6)
    str_7 = string_formatter_3.format()
    str_8 = 'contact me at email@example.com'
    string_formatter_4 = module_0.__StringFormatter(str_8)
    str_9 = string_formatter_4.format()

def test_case_15():
    str_0 = ")r9n\\G'6!/bL"
    str_1 = 'JCB'
    str_2 = '"6FDJS\''
    str_3 = module_0.snake_case_to_camel(str_2)
    bool_0 = module_0.booleanize(str_0)
    str_4 = 'T,'
    str_5 = module_0.prettify(str_4)
    str_6 = module_0.slugify(str_0, str_1)
    str_7 = '.'
    str_8 = module_0.prettify(str_7)
    bool_1 = False
    str_9 = 'SPACES_AROUND'
    str_10 = module_0.snake_case_to_camel(str_9, bool_1)
    str_11 = module_0.slugify(str_10)

def test_case_16():
    str_0 = 'B_g\x0bQf#e7 '
    str_1 = module_0.compress(str_0)
    int_0 = 1904
    str_2 = module_0.roman_encode(int_0)
    str_3 = module_0.snake_case_to_camel(str_1)
    str_4 = module_0.shuffle(str_2)
    str_5 = '$;BnBuY!i=M"rc]vv9q'
    str_6 = module_0.snake_case_to_camel(str_5)
    int_1 = module_0.roman_decode(str_4)
    str_7 = '4Y'
    bool_0 = False
    str_8 = module_0.strip_html(str_4, bool_0)
    str_9 = module_0.prettify(str_7)
    str_10 = module_0.slugify(str_0, str_6)
    str_11 = module_0.decompress(str_1)