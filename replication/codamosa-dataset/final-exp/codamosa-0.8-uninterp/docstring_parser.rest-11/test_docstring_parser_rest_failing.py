# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    try:
        str_0 = ':AW=/WD13'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n        Example docstring.\n\n        :param : An integer.\n        :param b: Optional string. Defaults to "None".\n        :raises ValueError: if a negative integer is passed\n        :returns: boo\n        :returns: int\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '    Short description.\n\n    More detailed description.\n\n    :param arg1: argument one\n    :param arg2: argument two\n    :returns: something\n    :raises Val\x0ceError: when arg1 == arg2\n    :raises TypeError: when arg1 != arg2\n    :raises: when arg2 != arg2\n    :returns: something\n    :yieQds: a thing\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass