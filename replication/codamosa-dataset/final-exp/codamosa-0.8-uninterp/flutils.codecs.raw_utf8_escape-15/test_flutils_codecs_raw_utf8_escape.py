# Automatically generated by Pynguin.
import flutils.codecs.raw_utf8_escape as module_0

def test_case_0():
    module_0.register()

def test_case_1():
    str_0 = "'Et@v4'#hNq\nO#g^^G"
    tuple_0 = module_0.encode(str_0)

def test_case_2():
    str_0 = "Convert the given ``text`` into a string of escaped UTF8 hexadecimal.\n\n    Args:\n         text (:obj:`str`): The string to convert.\n\n    :rtype:\n        :obj:`str`\n\n            A string with each character of the given ``text`` converted\n            into an escaped UTF8 hexadecimal.\n\n    Example:\n        >>> from flutils.strutils import as_literal_utf8\n        >>> t = '1.★ 🛑'\n        >>> as_escaped_utf8_literal(t)\n        '\\\\x31\\\\x2e\\\\xe2\\\\x98\\\\x85\\\\x20\\\\xf0\\\\x9f\\\\x9b\n        \\\\x91'\n    "
    tuple_0 = module_0.encode(str_0)