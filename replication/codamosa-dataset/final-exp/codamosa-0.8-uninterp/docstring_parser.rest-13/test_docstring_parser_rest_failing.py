# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    try:
        str_0 = '\n    This is a short description.\n\n    This is a long\n    description.\n\n    :param x: This is a parameter.\n    :type x: str\n    :param y: This is another parameter.\n    :type y: bool\n\n    :param (str, bool) z: This is a tuple parameter.\n    :type z: (str, bool)\n\n    :returns: This is what is returned.\n    :rtype: str\n\n    :return: This is also what is returned.\n    :rtype: bool?\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    This is the short description.\n\n    This is the long\n    description. It is\n    split into\n    multiple\n    lines.\n    And it comes\n    before the meta\n    tags.\n\n    :key arg description\n    :key arg description\n    :key arg description\n\n    The long description continues\n    here'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\n    Converts a Python value to Json.\n    :param data: the Python value to convert to Json.\n    :returns: the correspondng Json value.\n    :raises\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Short desc.\n\n    Long desc7\n\n    :param type arg: arg desc with ``code``\n    :param int arg2: arg2 desc\n    :return: returns desc with ``code``\n    :raises type error: raises desc\n\n    Extended description.\n   '
        var_0 = print(str_0)
        var_1 = print()
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass