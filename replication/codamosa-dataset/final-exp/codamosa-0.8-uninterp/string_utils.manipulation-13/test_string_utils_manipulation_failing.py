# Automatically generated by Pynguin.
import string_utils.manipulation as module_0

def test_case_0():
    try:
        int_0 = 3256
        str_0 = module_0.roman_encode(int_0)
        str_1 = None
        str_2 = '\n^h~kXX\nypegCI7f'
        str_3 = module_0.decompress(str_1, str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'the_snake_is_green'
        bool_0 = False
        str_1 = module_0.snake_case_to_camel(str_0, bool_0)
        str_2 = '12345'
        str_3 = module_0.prettify(str_2)
        str_4 = module_0.snake_case_to_camel(str_2)
        str_5 = module_0.snake_case_to_camel(str_4)
        str_6 = module_0.roman_encode(str_5)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'is_isbn_10'
        str_1 = module_0.roman_encode(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ']'
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '62]DG* tX&W_u4R_'
        str_1 = module_0.prettify(str_0)
        str_2 = ''
        int_0 = module_0.roman_decode(str_2)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'd:/3)z1eh%63\rSh'
        str_1 = module_0.decompress(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = None
        str_1 = module_0.decompress(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = "BJ:d^Z'3q-l#oaBe_-+"
        str_1 = '2i\t.{i\x0c'
        str_2 = module_0.shuffle(str_1)
        int_0 = None
        str_3 = module_0.compress(str_0, str_0, int_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '206\n\r6|f#1Y"`6P47$S'
        str_1 = module_0.decompress(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '\\//WU>M>yh~fB6_\x0c+'
        str_1 = ''
        str_2 = module_0.asciify(str_1)
        str_3 = module_0.slugify(str_0)
        str_4 = '^{}$'
        dict_0 = {str_4: str_4, str_4: str_4}
        string_formatter_0 = module_0.__StringFormatter(dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        float_0 = -725.72042
        var_0 = module_0.camel_case_to_snake(float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = None
        bool_0 = None
        str_1 = module_0.snake_case_to_camel(str_0, bool_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = None
        str_1 = module_0.shuffle(str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        str_1 = module_0.asciify(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'V'
        str_1 = 'Y j=#|'
        str_2 = 'lx'
        int_0 = module_0.roman_decode(str_2)
        str_3 = module_0.slugify(str_0)
        str_4 = module_0.prettify(str_1)
        str_5 = module_0.strip_margin(str_2)
        str_6 = module_0.compress(str_0)
        int_1 = module_0.roman_decode(str_0)
        str_7 = module_0.snake_case_to_camel(str_0)
        str_8 = module_0.roman_encode(int_1)
        str_9 = module_0.roman_encode(int_0)
        int_2 = -2706
        str_10 = module_0.roman_encode(int_2)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'l*dmi_\tlTV6r<h^;'
        str_1 = module_0.reverse(str_0)
        str_2 = '"xd6/nX^Yd/Ts:"\\'
        str_3 = 'G'
        int_0 = -354
        str_4 = module_0.compress(str_2, str_3, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'U'
        str_1 = 'OK=qr\n~'
        bool_0 = None
        str_2 = module_0.strip_html(str_1, bool_0)
        str_3 = module_0.prettify(str_0)
        int_0 = 595
        str_4 = module_0.compress(str_3, int_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 3263
        str_0 = module_0.roman_encode(int_0)
        str_1 = '(&7Q{%^rsO4k'
        str_2 = module_0.asciify(str_1)
        string_compressor_0 = module_0.__StringCompressor()
        str_3 = None
        bool_0 = module_0.booleanize(str_3)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '^TqJTleE|tu'
        bool_0 = True
        str_1 = module_0.strip_html(str_0, bool_0)
        str_2 = None
        str_3 = module_0.strip_html(str_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'ET\r|'
        bool_0 = module_0.booleanize(str_0)
        str_1 = "\n    Checks if the string is an isogram (https://en.wikipedia.org/wiki/Isogram).\n\n    *Examples:*\n\n    >>> is_isogram('dermatoglyphics') # returns true\n    >>> is_isogram('hello') # returns false\n\n    :param input_string: String to check.\n    :type input_string: str\n    :return: True if isogram, false otherwise.\n    "
        str_2 = module_0.shuffle(str_1)
        str_3 = module_0.prettify(str_1)
        list_0 = [str_0, str_1]
        string_formatter_0 = module_0.__StringFormatter(list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 3263
        str_0 = module_0.roman_encode(int_0)
        str_1 = '(&7Q{%^rsO4k'
        str_2 = module_0.asciify(str_1)
        string_compressor_0 = module_0.__StringCompressor()
        str_3 = None
        str_4 = module_0.strip_margin(str_3)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'This string     has     too     many     spaces in  between'
        string_formatter_0 = module_0.__StringFormatter(str_0)
        str_1 = string_formatter_0.format()
        str_2 = string_formatter_0.format()
        str_3 = 'Y\n3ETI'
        str_4 = string_formatter_0.format()
        int_0 = module_0.roman_decode(str_3)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = ''
        str_1 = module_0.decompress(str_0, str_0)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '^[^\\S\\r\\n]+'
        bool_0 = module_0.booleanize(str_0)
        str_1 = module_0.prettify(str_0)
        str_2 = module_0.snake_case_to_camel(str_1)
        str_3 = 'Fn&'
        int_0 = 2331
        str_4 = module_0.compress(str_0, str_3, int_0)
    except BaseException:
        pass

def test_case_24():
    try:
        int_0 = 407
        str_0 = module_0.roman_encode(int_0)
        str_1 = 'm@$G-+'
        str_2 = '?x|\tp`8 z'
        str_3 = module_0.slugify(str_1, str_2)
        str_4 = module_0.roman_encode(str_2)
    except BaseException:
        pass

def test_case_25():
    try:
        str_0 = None
        str_1 = module_0.slugify(str_0)
    except BaseException:
        pass

def test_case_26():
    try:
        str_0 = ''
        str_1 = module_0.asciify(str_0)
        str_2 = 'V'
        str_3 = '\x0bl$k\x0b%bB6<u8'
        str_4 = 'Y #|'
        str_5 = 'lx'
        int_0 = module_0.roman_decode(str_5)
        str_6 = module_0.slugify(str_0)
        str_7 = module_0.prettify(str_4)
        str_8 = module_0.strip_margin(str_3)
        str_9 = module_0.compress(str_2)
        int_1 = module_0.roman_decode(str_2)
        str_10 = module_0.snake_case_to_camel(str_2)
        str_11 = module_0.roman_encode(int_1)
        str_12 = None
        str_13 = module_0.reverse(str_12)
    except BaseException:
        pass

def test_case_27():
    try:
        int_0 = 859
        str_0 = module_0.roman_encode(int_0)
        tuple_0 = ()
        string_formatter_0 = module_0.__StringFormatter(tuple_0)
    except BaseException:
        pass

def test_case_28():
    try:
        str_0 = '[GS*:gVm'
        roman_numbers_0 = module_0.__RomanNumbers()
        int_0 = module_0.roman_decode(str_0)
    except BaseException:
        pass