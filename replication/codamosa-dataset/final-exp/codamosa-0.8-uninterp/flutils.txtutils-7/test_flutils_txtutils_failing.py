# Automatically generated by Pynguin.
import flutils.txtutils as module_0

def test_case_0():
    try:
        str_0 = 'eY:rAS&8z!4'
        str_1 = 'unicode_escape'
        bool_0 = False
        str_2 = 'y1T6OjLce19'
        bool_1 = True
        int_0 = 174
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(str_1, str_1, bool_1, bool_1, max_lines=int_0)
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, int_0, max_lines=int_0)
        bool_2 = False
        ansi_text_wrapper_2 = module_0.AnsiTextWrapper(str_0, str_2, bool_2, bool_0, bool_1, max_lines=int_0)
        str_3 = ansi_text_wrapper_1.fill(str_2)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '~U>A0f^yiJPwk\t` l'
        int_0 = 2867
        str_1 = 'k`JOG@\\BozJS'
        bool_0 = False
        bool_1 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_1, bool_0, bool_0, bool_1, bool_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = "The given 'cmd', %r, must be of type: str, bytes, list or tuple.  Got: %r"
        bool_0 = False
        bool_1 = False
        bool_2 = True
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_1, bool_2)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        str_0 = '`]T[Q-.;WsCeDgPeO'
        float_0 = 1017.9
        tuple_0 = (dict_0, str_0, bool_0, float_0)
        dict_1 = {bool_0: tuple_0, float_0: tuple_0}
        int_0 = module_0.len_without_ansi(dict_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        bool_0 = True
        int_0 = -1525
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, max_lines=int_0, placeholder=str_0)
        str_1 = ansi_text_wrapper_0.fill(str_0)
        str_2 = '"'
        str_3 = ansi_text_wrapper_0.fill(str_2)
        str_4 = ansi_text_wrapper_0.fill(str_0)
        list_0 = ansi_text_wrapper_0.wrap(str_1)
        str_5 = 'GoKb\\KgI}'
        str_6 = ansi_text_wrapper_0.fill(str_5)
        sequence_0 = None
        int_1 = module_0.len_without_ansi(sequence_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$'
        bool_0 = True
        int_0 = 18
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, str_0, bool_0, bool_0, int_0, max_lines=int_0)
        str_1 = 'FKpuk)F'
        list_0 = ansi_text_wrapper_0.wrap(str_1)
        str_2 = "Convert the given ``text``  into a string of escaped Unicode\n    hexadecimal.\n\n    Args:\n         text (:obj:`str`): The string to convert.\n\n    :rtype:\n        :obj:`str`\n\n            A string with each character of the given ``text`` converted\n            into an escaped Python literal.\n\n    Example:\n        >>> from flutils.strutils import as_escaped_unicode_literal\n        >>> t = '1.★ 🛑'\n        >>> as_literal(t)\n        '\\\\x31\\\\x2e\\\\u2605\\\\x20\\\\U0001f6d1'\n    "
        str_3 = ansi_text_wrapper_0.fill(str_2)
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, int_0, max_lines=int_0)
        str_4 = ansi_text_wrapper_1.fill(str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '\x1b[38;5;209mfoobar\x1b[0m'
        bool_0 = False
        int_0 = -1324
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(bool_0, bool_0, int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '1\rd%XG=Pcky:'
        bool_0 = True
        int_0 = 18
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, str_0, bool_0, bool_0, int_0, max_lines=int_0)
        list_0 = ansi_text_wrapper_0.wrap(str_0)
        str_1 = 'Fq\n'
        str_2 = ansi_text_wrapper_0.fill(str_1)
        str_3 = 'A module that manages attributes pointing to lazy-loaded-modules\n    and lazy-loaded-module-attributes.\n    '
        list_1 = ansi_text_wrapper_0.wrap(str_3)
        bool_1 = False
        ansi_text_wrapper_1 = module_0.AnsiTextWrapper(bool_1, max_lines=int_0)
        str_4 = '=Pcky:{'
        str_5 = ansi_text_wrapper_1.fill(str_4)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        int_0 = 2614
        str_0 = '/46Rl(y\x0cXg'
        bool_1 = False
        bool_2 = None
        bool_3 = True
        bool_4 = False
        str_1 = 'y\x0bQSPN]rwk<PRu*tBv6s'
        ansi_text_wrapper_0 = module_0.AnsiTextWrapper(int_0, str_0, bool_0, bool_1, bool_2, bool_3, bool_2, bool_4, placeholder=str_1)
        str_2 = ',"6'
        list_0 = ansi_text_wrapper_0.wrap(str_2)
        str_3 = "Convert the given ``text``  into a string of escapedDUnicode\n    hexadecimal.\n\n    Args:\n         text (:obj:`str`): The string to convert.\n\n    :rtype:\n        :obj:`str`\n\n            A string with each character of the given ``text`` converted\n            into an escaped Python literal.3\n    Example:\n        >>> from flutils.strutilsYimport as_escaped_unicode_literal\n        >>> t = '1.★ 🛑'\n        >>> as_literal(t)\n        '\\\\x31\\\\x2e\\\\u2605\\\\x20\\\\U0001f6d1'\n    "
        list_1 = ansi_text_wrapper_0.wrap(str_3)
        str_4 = 'C'
        str_5 = ansi_text_wrapper_0.fill(str_4)
        str_6 = None
        list_2 = ansi_text_wrapper_0.wrap(str_6)
    except BaseException:
        pass