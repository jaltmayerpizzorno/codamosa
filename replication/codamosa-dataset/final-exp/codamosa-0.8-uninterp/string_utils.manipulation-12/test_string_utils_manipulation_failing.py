# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    try:
        int_0 = 37
        str_0 = module_0.roman_encode(int_0)
        var_0 = print(str_0)
        str_1 = '2020'
        str_2 = module_0.roman_encode(str_1)
        var_1 = print(str_2)
        int_1 = 4000
        str_3 = module_0.roman_encode(int_1)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'is_palindrome'
        str_1 = module_0.roman_encode(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '8!q!\ne#|f}\th{PKbl'
        str_1 = module_0.shuffle(str_0)
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        str_1 = module_0.shuffle(str_0)
        str_2 = '(?!"[^"]*)@+(?=[^"]*")|\\\\@'
        str_3 = None
        bool_0 = True
        str_4 = module_0.strip_html(str_2, bool_0)
        int_0 = -1468
        str_5 = module_0.compress(str_2, str_3, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 5564
        string_formatter_0 = module_0.__StringFormatter(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'x_w/{ un|'
        str_1 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_2 = module_0.strip_html(str_1, bool_0)
        str_3 = module_0.prettify(str_0)
        str_4 = module_0.asciify(str_3)
        str_5 = module_0.shuffle(str_4)
        dict_0 = {}
        string_formatter_0 = module_0.__StringFormatter(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_1 = 'x_w/{ un|'
        str_2 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_3 = module_0.strip_html(str_2, bool_0)
        str_4 = '\x0cD|7TnaF@'
        str_5 = module_0.snake_case_to_camel(str_0, str_4)
        str_6 = module_0.prettify(str_1)
        str_7 = module_0.asciify(str_6)
        str_8 = module_0.shuffle(str_7)
        str_9 = 'k{m'
        string_formatter_0 = module_0.__StringFormatter(str_9)
        str_10 = string_formatter_0.format()
        str_11 = string_formatter_0.format()
        str_12 = '3hPe+^D'
        str_13 = module_0.strip_margin(str_12)
        str_14 = None
        str_15 = module_0.reverse(str_14)
    except BaseException:
        pass

def test_case_7():
    try:
        tuple_0 = None
        bool_0 = False
        set_0 = {tuple_0, tuple_0, bool_0}
        list_0 = [set_0, bool_0]
        var_0 = module_0.camel_case_to_snake(list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        str_1 = module_0.shuffle(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = None
        str_1 = module_0.strip_html(str_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'DISCOVER'
        str_1 = module_0.strip_html(str_0)
        str_2 = None
        str_3 = module_0.slugify(str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'CY>)}?>{K\\^iD<As\\??O'
        str_1 = module_0.asciify(str_0)
        str_2 = None
        str_3 = 'Invalid input, only strings or integers are allowed'
        str_4 = module_0.strip_margin(str_3)
        bool_0 = module_0.booleanize(str_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '\rHo'
        str_1 = module_0.strip_margin(str_0)
        str_2 = 'random_string'
        str_3 = 'x_w/{ un|'
        str_4 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_5 = module_0.strip_html(str_4, bool_0)
        str_6 = '\x0cD|7TnaF@'
        str_7 = module_0.snake_case_to_camel(str_2, str_6)
        str_8 = module_0.prettify(str_3)
        roman_numbers_0 = module_0.__RomanNumbers()
        str_9 = module_0.slugify(str_4)
        str_10 = 'k{m'
        string_formatter_0 = module_0.__StringFormatter(str_10)
        str_11 = string_formatter_0.format()
        str_12 = module_0.reverse(str_8)
        str_13 = 'is_ip_v6'
        str_14 = module_0.strip_margin(str_13)
        str_15 = None
        str_16 = module_0.strip_margin(str_15)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = -1330
        str_0 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_1 = 'x_w/{ un|'
        str_2 = 'A\tVSk.'
        str_3 = module_0.asciify(str_2)
        str_4 = module_0.strip_html(str_0)
        str_5 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_6 = module_0.strip_html(str_5, bool_0)
        str_7 = module_0.prettify(str_1)
        str_8 = module_0.asciify(str_7)
        str_9 = module_0.shuffle(str_8)
        int_0 = module_0.roman_decode(str_9)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '&f1G~YiT^'
        str_1 = module_0.snake_case_to_camel(str_0, str_0)
        str_2 = None
        str_3 = module_0.asciify(str_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'c\nwKpRXKD'
        str_1 = module_0.asciify(str_0)
        str_2 = module_0.shuffle(str_1)
        int_0 = module_0.roman_decode(str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'hello worldk python rocks!'
        str_1 = module_0.compress(str_0)
        str_2 = module_0.decompress(str_1)
        str_3 = None
        str_4 = module_0.compress(str_3)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = ''
        str_1 = 'u.mNH:Kmd#!$%xq'
        int_0 = 2229
        str_2 = module_0.compress(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'AO. K^1-\nCn108E<c0eW'
        str_1 = "F:@)-'"
        int_0 = -2558
        str_2 = module_0.compress(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = None
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        int_0 = 275
        str_0 = module_0.roman_encode(int_0)
        str_1 = 'SA'
        str_2 = module_0.asciify(str_1)
        bytes_0 = None
        str_3 = '?'
        str_4 = module_0.compress(str_3)
        string_formatter_0 = module_0.__StringFormatter(bytes_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_1 = 'G\x0bA|+_6nU_u93cat'
        str_2 = 'AQE^<hrI\n)u,#)UVq1'
        str_3 = module_0.strip_html(str_2)
        str_4 = 'pqg)'
        str_5 = module_0.snake_case_to_camel(str_0, str_4)
        str_6 = 'Mf%d,'
        str_7 = module_0.prettify(str_6)
        dict_0 = {}
        roman_numbers_0 = module_0.__RomanNumbers(**dict_0)
        str_8 = '\rf!T\t 2G1{-E&w0'
        str_9 = module_0.asciify(str_8)
        str_10 = module_0.shuffle(str_8)
        str_11 = 'k{m'
        str_12 = '/R [nDW1H g"%J*a'
        string_formatter_0 = module_0.__StringFormatter(str_12)
        str_13 = string_formatter_0.format()
        str_14 = 'D'
        int_0 = module_0.roman_decode(str_14)
        str_15 = module_0.reverse(str_1)
        str_16 = 'w;'
        str_17 = module_0.compress(str_11, str_16, int_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'G\x0bA|+_6nU_u93cat'
        str_1 = module_0.strip_html(str_0)
        str_2 = None
        str_3 = module_0.snake_case_to_camel(str_2)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_1 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_2 = module_0.strip_html(str_1, bool_0)
        str_3 = '\x0cD|7TnaF@'
        str_4 = module_0.snake_case_to_camel(str_0, str_3)
        str_5 = module_0.prettify(str_1)
        str_6 = module_0.asciify(str_5)
        str_7 = module_0.shuffle(str_6)
        str_8 = 'k{m'
        string_formatter_0 = module_0.__StringFormatter(str_8)
        str_9 = 'vLBV|6>D'
        str_10 = 'K"5{19J%`9\x0bJ<'
        str_11 = module_0.strip_margin(str_10)
        str_12 = module_0.reverse(str_9)
        str_13 = "V'I'.TIpzc=\r)-#/\x0b"
        str_14 = 'n1\t5.v".\tqUqfHt\tcQ'
        int_0 = 1263
        str_15 = module_0.compress(str_13, str_14, int_0)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'x_w/{ un|'
        str_1 = 'G\x0bA|+_6nU_u93cat'
        bool_0 = True
        str_2 = module_0.strip_html(str_1, bool_0)
        str_3 = module_0.snake_case_to_camel(str_1, str_0)
        str_4 = module_0.prettify(str_0)
        roman_numbers_0 = module_0.__RomanNumbers()
        str_5 = '^3[47]\\d{13}$'
        str_6 = module_0.asciify(str_5)
        str_7 = '~\rmCqHLI6bX([hR'
        str_8 = module_0.shuffle(str_7)
        str_9 = 'xtXR#PW4FS9'
        string_formatter_0 = module_0.__StringFormatter(str_9)
        str_10 = string_formatter_0.format()
        str_11 = 'gU=D\t[?_\\@\tY/Q9V'
        str_12 = module_0.strip_margin(str_11)
        str_13 = '?H.'
        str_14 = module_0.reverse(str_13)
        str_15 = module_0.strip_margin(str_0)
        str_16 = '=y'
        str_17 = "]?g'<h/"
        int_0 = None
        str_18 = module_0.compress(str_16, str_17, int_0)
    except BaseException:
        pass