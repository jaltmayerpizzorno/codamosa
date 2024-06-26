# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    try:
        str_0 = 'the_snake_is_green'
        string_compressor_0 = module_0.__StringCompressor()
        int_0 = 1460
        str_1 = module_0.compress(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_4 = module_0.snake_case_to_camel(str_3, str_3)
        tuple_0 = ()
        string_formatter_0 = module_0.__StringFormatter(tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'the_snake_is_green'
        string_compressor_0 = module_0.__StringCompressor()
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = module_0.snake_case_to_camel(str_0)
        int_0 = 5076
        str_3 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '&nX\x0c%(\nX?g/JwMesE'
        str_1 = module_0.roman_encode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Ec[\\\x0b:Cwge'
        str_1 = '2Z2_rH\x0b|+CQ'
        str_2 = module_0.reverse(str_1)
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '16b^1!bNL(O(8$'
        str_1 = module_0.strip_margin(str_0)
        str_2 = module_0.compress(str_1)
        str_3 = ''
        str_4 = module_0.slugify(str_3)
        int_0 = module_0.roman_decode(str_4)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "N}<FAutbw$'e&"
        str_1 = module_0.decompress(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        str_1 = module_0.reverse(str_0)
        str_2 = module_0.decompress(str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'Kmo^~SYt:#7Ig?6m'
        str_1 = module_0.compress(str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        string_formatter_0 = module_0.__StringFormatter(bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        list_0 = None
        var_0 = module_0.camel_case_to_snake(list_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'Ec[\\\x0b:Cwge'
        str_1 = module_0.slugify(str_0)
        str_2 = '2Z2_rH\x0b|+CQ'
        str_3 = module_0.reverse(str_2)
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'k3\r'
        str_1 = module_0.strip_margin(str_0)
        str_2 = '$;v\x0cH\'8&OB0#<V6C"*7\x0b'
        str_3 = '?>dncEv$]9?jPyl+Wq=_'
        str_4 = module_0.slugify(str_3)
        str_5 = module_0.strip_margin(str_2)
        int_0 = -2773
        str_6 = 'U4e)!]['
        bool_0 = module_0.booleanize(str_6)
        str_7 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'the_snake_is_green'
        string_compressor_0 = module_0.__StringCompressor()
        str_1 = module_0.snake_case_to_camel(str_0)
        int_0 = 1438
        str_2 = module_0.roman_encode(int_0)
        str_3 = None
        str_4 = module_0.compress(str_3)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = ''
        bool_0 = module_0.booleanize(str_0)
        str_1 = 'piq@6J@o8&'
        int_0 = -2975
        str_2 = 'Na'
        var_0 = module_0.camel_case_to_snake(str_2)
        str_3 = 'yQ1*T:9eP]}'
        str_4 = module_0.snake_case_to_camel(str_3, str_1)
        str_5 = module_0.compress(str_1, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = None
        str_1 = module_0.slugify(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = None
        bool_0 = module_0.booleanize(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = "]c\tP03?)'"
        str_1 = module_0.prettify(str_0)
        str_2 = '&tPdseNcg'
        bool_0 = module_0.booleanize(str_2)
        str_3 = module_0.reverse(str_1)
        bool_1 = module_0.booleanize(str_3)
        roman_numbers_0 = module_0.__RomanNumbers()
        str_4 = 'u?>>$bC'
        int_0 = module_0.roman_decode(str_4)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'W"aq""*7X~\x0b5c+XCD}6'
        int_0 = 307
        str_1 = module_0.compress(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        list_0 = []
        roman_numbers_0 = module_0.__RomanNumbers(*list_0)
        roman_numbers_1 = module_0.__RomanNumbers()
        str_0 = ' Z4-<^If5jk;\\'
        str_1 = "\n    Checks if a string is formatted as camel case.\n\n    A string is considered camel case when:\n\n    - it's composed only by letters ([a-zA-Z]) and optionally numbers ([0-9])\n    - it contains both lowercase and uppercase letters\n    - it does not start with a number\n\n    *Examples:*\n\n    >>> is_camel_case('MyString') # returns true\n    >>> is_camel_case('mystring') # returns false\n\n    :param input_string: String to test.\n    :type input_string: str\n    :return: True for a camel case string, false otherwise.\n    "
        int_0 = -2232
        str_2 = module_0.compress(str_0, str_1, int_0)
    except BaseException:
        pass

def test_case_19():
    try:
        int_0 = 2163
        str_0 = 'Ch+{p\\wmx9|uum'
        str_1 = module_0.asciify(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = module_0.strip_margin(str_1)
        str_4 = None
        str_5 = module_0.asciify(str_4)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'F<{4q,{P'
        str_1 = 'qJEJp-@ML7@eA}A7GO>'
        bool_0 = module_0.booleanize(str_1)
        str_2 = module_0.strip_html(str_0)
        int_0 = 2169
        str_3 = module_0.roman_encode(int_0)
        str_4 = module_0.prettify(str_2)
        str_5 = '5bZ2&BNqO\t\x0b07J6c'
        str_6 = module_0.decompress(str_5)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = None
        str_1 = module_0.strip_html(str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'NWM'
        str_1 = module_0.reverse(str_0)
        int_0 = 6
        str_2 = 'Ch+{p\\wmx9|uum'
        str_3 = module_0.asciify(str_2)
        str_4 = module_0.roman_encode(int_0)
        str_5 = module_0.shuffle(str_2)
        str_6 = '\n    Checks whether the given string represents an integer or not.\n\n    An integer may be signed or unsigned or use a "scientific notation".\n\n    *Examples:*\n\n    >>> is_integer(\'42\') # returns true\n    >>> is_integer(\'42.0\') # returns false\n\n    :param input_string: String to check\n    :type input_string: str\n    :return: True if integer, false otherwise\n    '
        list_0 = [str_6, int_0, str_2, str_6]
        str_7 = 'ApGhH['
        str_8 = module_0.snake_case_to_camel(str_7)
        var_0 = module_0.camel_case_to_snake(str_6, list_0)
        str_9 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
        str_10 = module_0.compress(str_4)
        str_11 = module_0.prettify(str_6)
        str_12 = module_0.strip_html(str_9)
        str_13 = None
        str_14 = module_0.strip_margin(str_13)
    except BaseException:
        pass

def test_case_23():
    try:
        int_0 = 6
        str_0 = 'Ch+{p\\wmx9|uum'
        str_1 = module_0.asciify(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = module_0.strip_margin(str_1)
        str_4 = module_0.snake_case_to_camel(str_2)
        str_5 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
        str_6 = module_0.compress(str_2)
        str_7 = ' '
        str_8 = module_0.prettify(str_7)
        bool_0 = True
        str_9 = module_0.strip_html(str_5, bool_0)
        str_10 = module_0.strip_html(str_8)
        str_11 = "2~sl |w?F`vh'aiql"
        str_12 = module_0.shuffle(str_11)
        str_13 = '}m\x0c1/AB!iE]5VE'
        str_14 = module_0.reverse(str_13)
        str_15 = module_0.compress(str_8)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'the_snake_is_green'
        str_1 = module_0.snake_case_to_camel(str_0, str_0)
        str_2 = None
        str_3 = module_0.snake_case_to_camel(str_2)
    except BaseException:
        pass

def test_case_25():
    try:
        int_0 = 6
        str_0 = 'Ch+{p\\wmx9|uum'
        str_1 = module_0.asciify(str_0)
        str_2 = module_0.roman_encode(int_0)
        str_3 = module_0.strip_margin(str_1)
        str_4 = module_0.snake_case_to_camel(str_2)
        str_5 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
        str_6 = module_0.compress(str_2)
        str_7 = ' '
        str_8 = module_0.prettify(str_7)
        bool_0 = True
        str_9 = module_0.strip_html(str_5, bool_0)
        str_10 = module_0.strip_html(str_8)
        str_11 = '3]sO=r@N"JdR)1`\rZh'
        str_12 = module_0.strip_margin(str_11)
        str_13 = None
        str_14 = module_0.shuffle(str_13)
    except BaseException:
        pass

def test_case_26():
    try:
        int_0 = 6
        str_0 = module_0.roman_encode(int_0)
        str_1 = module_0.shuffle(str_0)
        str_2 = '\n    Checks whether the given string represents an integer or not.\n\n    An integer may be signed or unsigned or use a "scientific notation".\n\n    *Examples:*\n\n    >>> is_integer(\'42\') # returns true\n    >>> is_integer(\'42.0\') # returns false\n\n    :param input_string: String to check\n    :type input_string: str\n    :return: True if integer, false otherwise\n    '
        list_0 = [str_2, int_0, str_2, str_2]
        str_3 = 'ApGhH['
        str_4 = module_0.snake_case_to_camel(str_3)
        var_0 = module_0.camel_case_to_snake(str_2, list_0)
        str_5 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
        str_6 = module_0.compress(str_0)
        str_7 = module_0.prettify(str_2)
        str_8 = module_0.strip_html(str_5)
        bool_0 = False
        str_9 = module_0.strip_html(str_4, bool_0)
        str_10 = '('
        str_11 = module_0.strip_html(str_10)
        str_12 = None
        str_13 = module_0.reverse(str_12)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'er[Y'
        str_1 = module_0.prettify(str_0)
        int_0 = 2159
        str_2 = 'Ch+{p\\wmx9|uum'
        str_3 = module_0.asciify(str_2)
        str_4 = module_0.roman_encode(int_0)
        str_5 = module_0.strip_margin(str_3)
        str_6 = module_0.prettify(str_5)
        str_7 = '@+ K9.o%GAj\\-Q'
        str_8 = module_0.slugify(str_7)
        str_9 = module_0.snake_case_to_camel(str_4)
        str_10 = '^[a-zA-Z]*([a-z]+[A-Z]+|[A-Z]+[a-z]+)[a-zA-Z\\d]*$'
        str_11 = module_0.compress(str_4)
        str_12 = module_0.reverse(str_7)
        str_13 = module_0.prettify(str_1)
        str_14 = module_0.strip_html(str_10)
        str_15 = module_0.strip_html(str_14)
        str_16 = module_0.shuffle(str_14)
        int_1 = module_0.roman_decode(str_13)
    except BaseException:
        pass

def test_case_28():
    try:
        string_compressor_0 = module_0.__StringCompressor()
        str_0 = '?$ZPqLdjx?gOPM'
        str_1 = module_0.snake_case_to_camel(str_0)
        int_0 = 1460
        str_2 = module_0.compress(str_0)
        str_3 = module_0.roman_encode(int_0)
        str_4 = module_0.decompress(str_2)
        int_1 = module_0.roman_decode(str_3)
        str_5 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        str_6 = module_0.snake_case_to_camel(str_5, str_5)
        tuple_0 = ()
        string_formatter_0 = module_0.__StringFormatter(tuple_0)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'P'
        str_1 = ")xvD8oY;yR{b\rH}j'a"
        int_0 = None
        str_2 = module_0.compress(str_1, str_0, int_0)
    except BaseException:
        pass