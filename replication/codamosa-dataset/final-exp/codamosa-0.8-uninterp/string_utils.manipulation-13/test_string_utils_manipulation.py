# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    string_compressor_0 = module_0.__StringCompressor()

def test_case_1():
    str_0 = 'abc'
    str_1 = module_0.compress(str_0)
    str_2 = module_0.decompress(str_1)

def test_case_2():
    str_0 = ''
    string_formatter_0 = module_0.__StringFormatter(str_0)

def test_case_3():
    str_0 = "L/jny'UhI{!.\\AgKV_f"
    str_1 = module_0.prettify(str_0)

def test_case_4():
    str_0 = 'PIuAcw'
    str_1 = module_0.reverse(str_0)

def test_case_5():
    str_0 = '\n    Convert a snake case string into a camel case one.\n    (The original string is returned if is not a valid snake case string)\n\n    *Example:*\n\n    >>> snake_case_to_camel(\'the_snake_is_green\') # returns \'TheSnakeIsGreen\'\n\n    :param input_string: String to convert.\n    :type input_string: str\n    :param upper_case_first: True to turn the first letter into uppercase (default).\n    :type upper_case_first: bool\n    :param separator: Sign to use as separator (default to "_").\n    :type separator: str\n    :return: Converted string\n    '
    var_0 = module_0.camel_case_to_snake(str_0)

def test_case_6():
    str_0 = '\n    Checks if a string is a valid ip v6.\n\n    *Examples:*\n\n    >>> is_ip_v6(\'2001:db8:85a3:0000:0000:8a2e:370:7334\') # returns true\n    >>> is_ip_v6(\'2001:db8:85a3:0000:0000:8a2e:370:?\') # returns false (invalid "?")\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if a v6 ip, false otherwise.\n    '
    str_1 = module_0.shuffle(str_0)
    str_2 = "'PWG"
    str_3 = module_0.snake_case_to_camel(str_2)

def test_case_7():
    str_0 = "%3K'%IzdBUw"
    str_1 = module_0.shuffle(str_0)

def test_case_8():
    str_0 = 'g/>N\r_l8q}pqoZvD'
    str_1 = module_0.strip_html(str_0)

def test_case_9():
    str_0 = '`gZTk\t8f+U=URla'
    str_1 = module_0.slugify(str_0)

def test_case_10():
    str_0 = '".\\Ck6*h68iL&@W'
    bool_0 = module_0.booleanize(str_0)

def test_case_11():
    str_0 = 'ukP*W!\t$v{*fe-hE~b'
    str_1 = module_0.strip_margin(str_0)

def test_case_12():
    str_0 = '^TqJTleE|tu'
    bool_0 = True
    str_1 = module_0.strip_html(str_0, bool_0)
    str_2 = 'p{6(,N#`$'
    str_3 = module_0.strip_html(str_2)
    str_4 = module_0.prettify(str_3)
    str_5 = '"*67gz~T%P{{~s9~C(w'
    str_6 = module_0.strip_margin(str_5)
    str_7 = module_0.compress(str_4)
    str_8 = ''
    str_9 = module_0.slugify(str_8)

def test_case_13():
    str_0 = '[.wq'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = 'the_snake_is_green'
    str_2 = module_0.snake_case_to_camel(str_1)
    str_3 = string_formatter_0.format()
    bool_0 = False
    str_4 = module_0.snake_case_to_camel(str_1, bool_0)

def test_case_14():
    str_0 = 'This string     has     too     many     spaces in  between'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()
    str_2 = string_formatter_0.format()
    str_3 = string_formatter_0.format()
    str_4 = "This is a string with an email. Send an email to admin@google.com, he's waiting for you!"
    string_formatter_1 = module_0.__StringFormatter(str_4)
    str_5 = string_formatter_1.format()

def test_case_15():
    str_0 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
    bool_0 = False
    str_1 = module_0.strip_html(str_0, bool_0)
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_2 = '\n    Compress the given string by returning a shorter one that can be safely used in any context (like URL) and\n    restored back to its original state using `decompress()`.\n\n    **Bear in mind:**\n    Besides the provided `compression_level`, the compression result (how much the string is actually compressed\n    by resulting into a shorter string) depends on 2 factors:\n\n    1. The amount of data (string size): short strings might not provide a significant compression result    or even be longer than the given input string (this is due to the fact that some bytes have to be embedded    into the compressed string in order to be able to restore it later on)\n    2. The content type: random sequences of chars are very unlikely to be successfully compressed, while the best    compression result is obtained when the string contains several recurring char sequences (like in the example).\n\n    Behind the scenes this method makes use of the standard Python\'s zlib and base64 libraries.\n\n    *Examples:*\n\n    >>> n = 0 # <- ignore this, it\'s a fix for Pycharm (not fixable using ignore comments)\n    >>> # "original" will be a string with 169 chars:\n    >>> original = \' \'.join([\'word n{}\'.format(n) for n in range(20)])\n    >>> # "compressed" will be a string of 88 chars\n    >>> compressed = compress(original)\n\n    :param input_string: String to compress (must be not empty or a ValueError will be raised).\n    :type input_string: str\n    :param encoding: String encoding (default to "utf-8").\n    :type encoding: str\n    :param compression_level: A value between 0 (no compression) and 9 (best compression), default to 9.\n    :type compression_level: int\n    :return: Compressed string.\n    '
    str_3 = module_0.slugify(str_2)
    str_4 = string_formatter_0.format()

def test_case_16():
    str_0 = 'This string     has     too     many     spaces in  between'
    string_formatter_0 = module_0.__StringFormatter(str_0)
    str_1 = string_formatter_0.format()
    str_2 = 'string with url http://www.google.com'
    string_formatter_1 = module_0.__StringFormatter(str_2)
    str_3 = string_formatter_1.format()
    str_4 = 'Hello! @user! What do you think about Kevin from @googledevs?'
    string_formatter_2 = module_0.__StringFormatter(str_4)
    str_5 = string_formatter_2.format()
    str_6 = "This is a string with an email. Send an email to admin@google.com, he's waiting for you!"
    string_formatter_3 = module_0.__StringFormatter(str_6)
    str_7 = string_formatter_3.format()

def test_case_17():
    str_0 = 'qE'
    str_1 = module_0.asciify(str_0)
    str_2 = 'lx'
    int_0 = module_0.roman_decode(str_2)
    str_3 = module_0.slugify(str_0)
    str_4 = module_0.prettify(str_3)
    str_5 = module_0.strip_margin(str_4)
    str_6 = module_0.compress(str_3)
    str_7 = module_0.snake_case_to_camel(str_0)
    str_8 = module_0.roman_encode(int_0)
    var_0 = module_0.camel_case_to_snake(str_1)

def test_case_18():
    str_0 = 'the_snake_is_green'
    str_1 = module_0.snake_case_to_camel(str_0)
    bool_0 = False
    str_2 = module_0.snake_case_to_camel(str_0, bool_0)
    str_3 = 'the-snake-is-green'
    str_4 = '-'
    str_5 = module_0.snake_case_to_camel(str_3, str_4)

def test_case_19():
    str_0 = 'a_low_case_string'
    str_1 = module_0.snake_case_to_camel(str_0)
    bool_0 = False
    str_2 = module_0.snake_case_to_camel(str_0, bool_0)
    str_3 = '_not_a_snake_string_'
    str_4 = module_0.snake_case_to_camel(str_1)
    bool_1 = False
    str_5 = module_0.snake_case_to_camel(str_3, bool_1)