# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    try:
        str_0 = ':fs5tveOM7\tC>-'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'W\x0c/{g\n:i@|Y8e('
        str_1 = '\t\t'
        docstring_0 = module_0.parse(str_1)
        docstring_1 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n    This is a short description of the function.\n\n    This is a long description of the function.\n    This is a long description of the function.\n\n    :param str arg1: Argument 1\n    :param: Argument 2\n    :returns: the return value\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass