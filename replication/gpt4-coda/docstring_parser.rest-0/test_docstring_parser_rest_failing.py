# Automatically generated by Pynguin.
import docstring_parser.rest as module_0
import docstring_parser.common as module_1

def test_case_0():
    try:
        str_0 = ':8MbWL(lEvqE}rhe\\_R'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'feFdQxYmz#\\E\t>6Zi\r\n:'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        docstring_0 = module_1.Docstring()
        str_0 = '\n    This is a short description.\n\n    This is a long description that goes into more detail.\n\n    :param str name: The name of the person.\n    :param :ge: The age of the person.\n    :type age: int, optional\n    :returns: The greeting message.\n    :rtype: str\n    :raises ValueError: If the name is empty.\n    '
        docstring_1 = module_0.parse(str_0)
    except BaseException:
        pass