# Automatically generated by Pynguin.
import flutils.codecs.raw_utf8_escape as module_0
import collections as module_1
import codecs as module_2

def test_case_0():
    try:
        bytes_0 = b"'\xca\xd4\xc5\x89Q\x0c\xca\xab/\xc8\xb2\x07\xb4"
        str_0 = 'q\x0c-102RF){:t\n\n'
        tuple_0 = module_0.encode(str_0)
        tuple_1 = module_0.encode(str_0, str_0)
        tuple_2 = module_0.decode(bytes_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\xc0\x01\xd3\x03\x14'
        int_0 = 42
        tuple_0 = (bytes_0, int_0)
        user_string_0 = module_1.UserString(tuple_0)
        tuple_1 = module_0.encode(user_string_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'/\xdf\xd0\xd2\xe9`Y\xd6\xa5\t\xe8\xc5wR\x9b\x8d)Ws'
        tuple_0 = module_0.decode(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'eutf8h'
        dict_0 = {}
        tuple_0 = module_0.decode(dict_0, str_0)
        var_0 = module_2.getdecoder(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        module_0.register()
        tuple_0 = ()
        tuple_1 = module_0.decode(tuple_0)
        module_0.register()
        byte_string_0 = None
        tuple_2 = module_0.decode(byte_string_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'eutf8h'
        var_0 = module_2.getdecoder(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        user_string_0 = module_1.UserString(bool_0)
        tuple_0 = module_0.encode(user_string_0)
        module_0.register()
        str_0 = 'gXjDA\\Q?6WBpO~y`w'
        bytes_0 = b"'\xca\xd4\xc5\x89Q\x0c\xca\xab/\xc8\xb2\x07\xb4"
        str_1 = 'q\x0c-102PF){:t\n\n'
        tuple_1 = module_0.encode(str_0)
        tuple_2 = module_0.encode(user_string_0, str_1)
        tuple_3 = None
        user_string_1 = module_1.UserString(tuple_3)
        tuple_4 = module_0.decode(bytes_0, user_string_1)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        str_0 = "Convert a camel-cased string to a string containing words separated\n    with underscores.\n\n    Args:\n        text (str): The camel-cased string to convert.\n\n    :rtype: :obj:`str`\n\n    Example:\n        >>> from flutils.strutils import camel_to_underscore\n        >>> camel_to_underscore('FooBar')\n        'foo_bar'\n    "
        int_0 = 1741
        tuple_0 = (str_0, int_0)
        bytes_0 = b'\xf7#\xfbN\x1a\xba\x89'
        tuple_1 = (bool_0, dict_0, tuple_0, bytes_0)
        user_string_0 = module_1.UserString(tuple_1)
        str_1 = 'YW'
        tuple_2 = module_0.encode(user_string_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        user_string_0 = module_1.UserString(bool_0)
        tuple_0 = module_0.encode(user_string_0)
        str_0 = "Convert the given ``text`` into a string of escaped UTF8 hexadecimal.\n\n    Args:\n         text (:obj:`str`): The string to convert.\n\n    :rtype:\n        :obj:`str`\n\n            A string with each character of the given ``text`` converted\n            into an escaped UTF8 hexadecimal.\n\n    Example:\n        >>> from flutils.strutils import as_literal_utf8\n        >>> t = '1.★ 🛑'\n        >>> as_escaped_utf8_literal(t)\n        '\\\\x31\\\\x2e\\\\xe2\\\\x98\\\\x85\\\\x20\\\\xf0\\\\x9f\\\\x9b\n        \\\\x91'\n    "
        bytes_0 = b"'\xca\xd4\xc5\x89Q\x0c\xca\xab/\xc8\xb2\x07\xb4"
        str_1 = 'q\x0c-102PF){:t\n\n'
        module_0.register()
        tuple_1 = module_0.encode(str_1)
        tuple_2 = module_0.encode(str_0, str_0)
        tuple_3 = module_0.decode(bytes_0)
    except BaseException:
        pass