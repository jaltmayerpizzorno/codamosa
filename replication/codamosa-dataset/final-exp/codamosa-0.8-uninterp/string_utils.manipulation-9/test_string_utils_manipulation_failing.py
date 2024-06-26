# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    try:
        str_0 = "\n    Checks if the string is a pangram (https://en.wikipedia.org/wiki/Pangram).\n\n    *Examples:*\n\n    >>> is_pangram('The quick brown fox jumps over the lazy dog') # returns true\n    >>> is_pangram('hello world') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if the string is a pangram, False otherwise.\n    "
        str_1 = module_0.prettify(str_0)
        str_2 = '1ak3^yz2QkE_]e}(.zj'
        str_3 = module_0.prettify(str_2)
        str_4 = 'is_isbn'
        int_0 = 698
        str_5 = module_0.roman_encode(int_0)
        str_6 = module_0.compress(str_4, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    Checks if the given string represents a valid ISBN 10 (International Standard Book Number).\n    By default hyphens in the string are ignored, so digits can be separated in different ways, by calling this\n    function with `normalize=False` only digit-only strings will pass the validation.\n\n    *Examples:*\n\n    >>> is_isbn_10(\'1506715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\') # returns true\n    >>> is_isbn_10(\'150-6715214\', normalize=False) # returns false\n\n    :param input_string: String to check.\n    :param normalize: True to ignore hyphens ("-") in the string (default), false otherwise.\n    :return: True if valid ISBN 10, false otherwise.\n    '
        bool_0 = module_0.booleanize(str_0)
        int_0 = -1996
        str_1 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'GBD\td&,R+v<BS<L+][\x0b`'
        str_1 = module_0.shuffle(str_0)
        int_0 = None
        str_2 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '6Y@|xH ]M_}%?h'
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = None
        str_1 = module_0.decompress(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'tm0HF#&\\DEuLN7-Z'
        str_1 = module_0.reverse(str_0)
        str_2 = '\n    Checks if a string is a valid number.\n\n    The number can be a signed (eg: +1, -2, -3.3) or unsigned (eg: 1, 2, 3.3) integer or double\n    or use the "scientific notation" (eg: 1e5).\n\n    *Examples:*\n\n    >>> is_number(\'42\') # returns true\n    >>> is_number(\'19.99\') # returns true\n    >>> is_number(\'-9.12\') # returns true\n    >>> is_number(\'1e3\') # returns true\n    >>> is_number(\'1 2 3\') # returns false\n\n    :param input_string: String to check\n    :type input_string: str\n    :return: True if the string represents a number, false otherwise\n    '
        str_3 = '-'
        int_0 = None
        str_4 = module_0.compress(str_2, str_3, int_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'I]}<p*MX53!gIz$zM'
        str_1 = module_0.decompress(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 3999
        bytes_0 = b'\x97\x17\x89\xd9\xe4\xa5\x8d\x9bB'
        str_0 = '^(?:2131|1800|35\\d{3})\\d{11}$'
        tuple_0 = (int_0, bytes_0, str_0)
        dict_0 = {}
        string_compressor_0 = module_0.__StringCompressor()
        tuple_1 = (tuple_0, tuple_0, dict_0, string_compressor_0)
        string_formatter_0 = module_0.__StringFormatter(tuple_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\n    Reformat a string by applying the following basic grammar and formatting rules:\n\n    - String cannot start or end with spaces\n    - The first letter in the string and the ones after a dot, an exclamation or a question mark must be uppercase\n    - String cannot have multiple sequential spaces, empty lines or punctuation (except for "?", "!" and ".")\n    - Arithmetic operators (+, -, /, \\*, =) must have one, and only one space before and after themselves\n    - One, and only one space should follow a dot, a comma, an exclamation or a question mark\n    - Text inside double quotes cannot start or end with spaces, but one, and only one space must come first and     after quotes (foo" bar"baz -> foo "bar" baz)\n    - Text inside round brackets cannot start or end with spaces, but one, and only one space must come first and     after brackets ("foo(bar )baz" -> "foo (bar) baz")\n    - Percentage sign ("%") cannot be preceded by a space if there is a number before ("100 %" -> "100%")\n    - Saxon genitive is correct ("Dave\' s dog" -> "Dave\'s dog")\n\n    *Examples:*\n\n    >>> prettify(\' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! \')\n    >>> # -> \'Unprettified string, like this one, will be "prettified". It\'s awesome!\'\n\n    :param input_string: String to manipulate\n    :return: Prettified string.\n    '
        str_1 = module_0.prettify(str_0)
        str_2 = module_0.reverse(str_1)
        str_3 = 'decompress'
        str_4 = module_0.shuffle(str_3)
        float_0 = 1497.131588
        string_formatter_0 = module_0.__StringFormatter(float_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '\n    Reformat a string by applying the following basic grammar and formatting rules:\n\n    - String cannot start or end with spaces\n    - The first letter in the string and the ones after a dot, an exclamation or a question mark must be uppercase\n    - String cannot have multiple sequential spaces, empty lines or punctuation (except for "?", "!" and ".")\n    - Arithmetic operators (+, -, /, \\*, =) must have one, and only one space before and after themselves\n    - One, and only one space should follow a dot, a comma, an exclamation or a question mark\n    - Text inside double quotes cannot start or end with spaces, but one, and only one space must come first and     after quotes (foo" bar"baz -> foo "bar" baz)\n    - Text inside round brackets cannot start or end with spaces, but one, and only one space must come first and     after brackets ("foo(bar )baz" -> "foo (bar) baz")\n    - Percentage sign ("%") cannot be preceded by a space if there is a number before ("100 %" -> "100%")\n    - Saxon genitive is correct ("Dave\' s dog" -> "Dave\'s dog")\n\n    *Examples:*\n\n    >>> prettify(\' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! \')\n    >>> # -> \'Unprettified string, like this one, will be "prettified". It\'s awesome!\'\n\n    :param input_string: String to manipulate\n    :return: Prettified string.\n    '
        str_1 = module_0.prettify(str_0)
        str_2 = None
        str_3 = module_0.reverse(str_2)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = None
        var_0 = module_0.camel_case_to_snake(list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'L'
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = module_0.prettify(str_0)
        string_compressor_0 = module_0.__StringCompressor()
        str_3 = '\n}#m{(nq(|~:G8e'
        int_0 = module_0.roman_decode(str_3)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        str_1 = module_0.strip_html(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = None
        bool_0 = module_0.booleanize(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '^[a-f\\d]{8}-[a-f\\d]{4}-[a-f\\d]{4}-[a-f\\d]{4}-[a-f\\d]{12}$'
        str_1 = module_0.slugify(str_0)
        int_0 = -1435
        str_2 = module_0.compress(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = -1996
        str_0 = 's\x0b'
        str_1 = module_0.strip_html(str_0)
        str_2 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = "B1~3'Mm\x0chCc D3x"
        str_1 = module_0.snake_case_to_camel(str_0)
        str_2 = '0=%Tj6q\x0b&BAyP%'
        int_0 = 1013
        str_3 = module_0.roman_encode(int_0)
        str_4 = module_0.slugify(str_3)
        str_5 = 'TVcnI7y79La0!T'
        str_6 = module_0.reverse(str_5)
        str_7 = module_0.compress(str_2)
        bool_0 = True
        str_8 = module_0.snake_case_to_camel(str_0, bool_0)
        str_9 = 'ZZVL'
        str_10 = '\n        :param input_data: Any received object\n        '
        str_11 = module_0.compress(str_9, str_10)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = "B1~3'Mm\x0chCc D3x"
        string_compressor_0 = module_0.__StringCompressor()
        str_1 = module_0.prettify(str_0)
        str_2 = '1yfR/eA\roB2mXDAL'
        str_3 = module_0.strip_html(str_2)
        int_0 = 1523
        str_4 = module_0.roman_encode(int_0)
        str_5 = '%xl9SUpH@vj'
        str_6 = module_0.slugify(str_5)
        str_7 = module_0.reverse(str_1)
        str_8 = module_0.compress(str_4)
        str_9 = module_0.compress(str_7)
        int_1 = module_0.roman_decode(str_8)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'is_number'
        str_1 = module_0.prettify(str_0)
        str_2 = module_0.slugify(str_0, str_0)
        str_3 = None
        str_4 = module_0.compress(str_1, str_3)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'R\tRj]1?\r""Q\\@'
        str_3 = '61'
        str_4 = module_0.reverse(str_3)
        str_5 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_6 = None
        str_7 = module_0.snake_case_to_camel(str_6)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'R\tRj]1?\r""Q\\@'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.reverse(str_1)
        str_5 = module_0.strip_margin(str_2)
        str_6 = ";*^Z,?:PS.1%n#K'}"
        str_7 = module_0.strip_html(str_6)
        int_0 = 1519
        str_8 = module_0.roman_encode(int_0)
        str_9 = module_0.slugify(str_2)
        str_10 = module_0.reverse(str_8)
        str_11 = 'SvcS'
        str_12 = module_0.compress(str_11)
        string_compressor_0 = module_0.__StringCompressor()
        str_13 = '}sUuDIqRp'
        str_14 = module_0.reverse(str_13)
        str_15 = '_'
        str_16 = module_0.strip_html(str_15)
        str_17 = None
        str_18 = module_0.shuffle(str_17)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = None
        str_1 = module_0.slugify(str_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'R\tRj]1?\r""Q\\@'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = ";*^Z,?:PS.1%n#K'}"
        str_6 = module_0.strip_html(str_5)
        int_0 = 1519
        str_7 = module_0.roman_encode(int_0)
        str_8 = ''
        str_9 = module_0.reverse(str_8)
        str_10 = module_0.compress(str_9)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = module_0.reverse(str_0)
        str_3 = module_0.strip_margin(str_1)
        int_0 = 1573
        str_4 = module_0.roman_encode(int_0)
        var_0 = module_0.camel_case_to_snake(str_2)
        str_5 = 'SvcS'
        str_6 = module_0.compress(str_5)
        str_7 = 'N^=+7+P'
        str_8 = module_0.snake_case_to_camel(str_7)
        str_9 = module_0.prettify(str_2)
        str_10 = 'is_credit_card'
        str_11 = module_0.snake_case_to_camel(str_10, str_5)
        bool_0 = module_0.booleanize(str_7)
        str_12 = 'strip_html'
        int_1 = module_0.roman_decode(str_12)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = 'R\tRj]1?\r""Q\\@'
        str_1 = module_0.reverse(str_0)
        bool_0 = module_0.booleanize(str_0)
        str_2 = module_0.strip_margin(str_0)
        str_3 = ";*^Z,?:PS.1%n#K'}"
        str_4 = module_0.strip_html(str_3)
        int_0 = 1519
        str_5 = module_0.roman_encode(int_0)
        str_6 = module_0.slugify(str_0)
        str_7 = '\n    Custom error raised when received object is not a string as expected.\n    '
        str_8 = module_0.slugify(str_7)
        str_9 = module_0.reverse(str_4)
        str_10 = '7Wt`7f[\x0c'
        str_11 = module_0.compress(str_10, str_10, int_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = 'kkh,'
        str_1 = module_0.reverse(str_0)
        str_2 = '\t;I62'
        bool_0 = module_0.booleanize(str_2)
        str_3 = None
        str_4 = module_0.strip_margin(str_3)
    except BaseException:
        pass

def test_case_27():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'R\tRj]1?\r""Q\\@'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = ";*^Z,?:PS.1%n#K'}"
        str_6 = module_0.strip_html(str_5)
        int_0 = 1541
        str_7 = module_0.roman_encode(int_0)
        str_8 = module_0.slugify(str_2)
        var_0 = module_0.camel_case_to_snake(str_3)
        str_9 = module_0.reverse(str_7)
        str_10 = 'N^=+7+P'
        str_11 = module_0.snake_case_to_camel(str_10)
        str_12 = 'SAXON_GENITIVE'
        str_13 = module_0.prettify(str_12)
        str_14 = module_0.compress(str_2)
        str_15 = '8Ual9.7\n3`;'
        bool_1 = module_0.booleanize(str_15)
        str_16 = module_0.reverse(str_6)
        str_17 = '#y\n^[.'
        str_18 = module_0.shuffle(str_17)
        int_1 = module_0.roman_decode(str_13)
    except BaseException:
        pass

def test_case_28():
    try:
        roman_numbers_0 = module_0.__RomanNumbers()
        str_0 = '"[~\x0cfZ9'
        var_0 = module_0.camel_case_to_snake(str_0)
        str_1 = 'j|yT5\\t2ZbT^@OYX)nM'
        bool_0 = False
        str_2 = module_0.snake_case_to_camel(str_1, bool_0)
        str_3 = 'd|%BTE'
        str_4 = module_0.decompress(str_3)
    except BaseException:
        pass

def test_case_29():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = '?ut&r3&^&.1*t\x0cQDWU%/'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = ''
        str_6 = module_0.strip_html(str_5)
        int_0 = 1568
        str_7 = module_0.roman_encode(int_0)
        str_8 = module_0.slugify(str_2)
        var_0 = module_0.camel_case_to_snake(str_3)
        str_9 = module_0.reverse(str_7)
        str_10 = 'SvcS'
        str_11 = module_0.compress(str_10)
        str_12 = 'N^=+7+P'
        str_13 = module_0.snake_case_to_camel(str_12)
        str_14 = 'SAXON_GENITIVE'
        str_15 = module_0.prettify(str_14)
        str_16 = 'is_credit_card'
        str_17 = module_0.snake_case_to_camel(str_16, str_6)
        str_18 = module_0.compress(str_12)
        bool_1 = module_0.booleanize(str_12)
        str_19 = module_0.reverse(str_5)
        str_20 = module_0.shuffle(str_11)
        str_21 = 'H\nq+\rv7zP\tyyL3:0O'
        int_1 = module_0.roman_decode(str_21)
    except BaseException:
        pass

def test_case_30():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = None
        str_3 = module_0.asciify(str_2)
    except BaseException:
        pass

def test_case_31():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'R\tRj]1?\r""Q\\@'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = ";*^Z,-?:PS.1%n#xK'}"
        str_6 = module_0.strip_html(str_5)
        int_0 = 1601
        str_7 = module_0.roman_encode(int_0)
        str_8 = module_0.slugify(str_2)
        var_0 = module_0.camel_case_to_snake(str_4)
        str_9 = 'SvcS'
        str_10 = module_0.compress(str_9)
        str_11 = 'N^=+7+P'
        str_12 = module_0.snake_case_to_camel(str_11)
        str_13 = 'SAXON_GENITIUD\x0bVE'
        str_14 = module_0.prettify(str_13)
        str_15 = '_credit_card'
        str_16 = module_0.snake_case_to_camel(str_15, str_6)
        str_17 = module_0.compress(str_11)
        bool_1 = module_0.booleanize(str_2)
        str_18 = module_0.reverse(str_2)
        str_19 = module_0.shuffle(str_5)
        int_1 = module_0.roman_decode(str_16)
    except BaseException:
        pass

def test_case_32():
    try:
        int_0 = 5061
        str_0 = module_0.roman_encode(int_0)
    except BaseException:
        pass

def test_case_33():
    try:
        str_0 = 'yes'
        str_1 = module_0.slugify(str_0)
        str_2 = 'diPq'
        str_3 = module_0.reverse(str_2)
        bool_0 = module_0.booleanize(str_2)
        str_4 = module_0.strip_margin(str_2)
        str_5 = ";*^Z,-?:PS.1%n#K'}"
        str_6 = module_0.strip_html(str_5)
        int_0 = 1601
        str_7 = module_0.roman_encode(int_0)
        str_8 = module_0.slugify(str_2)
        var_0 = module_0.camel_case_to_snake(str_4)
        str_9 = 'SvcS'
        str_10 = module_0.compress(str_9)
        str_11 = 'N^=+7+P'
        str_12 = module_0.snake_case_to_camel(str_11)
        str_13 = 'SAXON_GENITIUD\x0bVE'
        str_14 = module_0.prettify(str_13)
        str_15 = 'is_credit_card'
        str_16 = module_0.snake_case_to_camel(str_15, str_6)
        str_17 = module_0.compress(str_11)
        bool_1 = module_0.booleanize(str_2)
        str_18 = module_0.reverse(str_2)
        str_19 = module_0.shuffle(str_5)
        int_1 = module_0.roman_decode(str_16)
    except BaseException:
        pass

def test_case_34():
    try:
        str_0 = 'R\tRj]1?\r""Q\\@'
        str_1 = module_0.reverse(str_0)
        bool_0 = module_0.booleanize(str_0)
        str_2 = ";*^Z,-?:PS.1%n#K'}"
        str_3 = module_0.strip_html(str_2)
        int_0 = 1601
        str_4 = module_0.roman_encode(int_0)
        var_0 = module_0.camel_case_to_snake(str_1)
        str_5 = module_0.reverse(str_4)
        str_6 = 'SvcS'
        str_7 = module_0.compress(str_6)
        str_8 = 'N^=+7+P'
        str_9 = module_0.decompress(str_7)
        str_10 = module_0.snake_case_to_camel(str_8)
        str_11 = 'SAXON_GENITIVE'
        str_12 = module_0.prettify(str_11)
        str_13 = 'is_credit_card'
        str_14 = module_0.snake_case_to_camel(str_13, str_3)
        str_15 = module_0.compress(str_8)
        bool_1 = module_0.booleanize(str_0)
        str_16 = module_0.strip_html(str_5)
        str_17 = '3/k9'
        str_18 = module_0.reverse(str_17)
        str_19 = "\n    Checks if the string is an isogram (https://en.wikipedia.org/wiki/Isogram).\n\n    *Examples:*\n\n    >>> is_isogram('dermatoglyphics') # returns true\n    >>> is_isogram('hello') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if isogram, false otherwise.\n    "
        str_20 = module_0.shuffle(str_19)
        str_21 = 'UPPERCASE_FIRST_LETTER'
        int_1 = module_0.roman_decode(str_21)
    except BaseException:
        pass