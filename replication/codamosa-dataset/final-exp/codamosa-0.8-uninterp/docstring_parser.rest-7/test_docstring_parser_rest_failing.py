# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    try:
        str_0 = 'Python function.\n\n:param x: This is x.\n:param str name: This is name.\n:raises TypeError: When there is a type error.\n:return: This is a return.\n:returns: This is also a return.\n:yield int: This is a yield.\n:yields int: This is also a yield.\n:returns int name: This is a return with a name and a type.\n:yields: This is a yield type.\n:other: This is other.\n:return: This return has a\n  multi-line\n  description.\n:returns: This return also has a\n  multi-line\n  description.\n'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = ':&b<'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'J*jWsMhV0gb&&XX*3#a'
        docstring_0 = module_0.parse(str_0)
        str_1 = 'v4\x0b)GKwd6-\\1yOlvx'
        str_2 = 'raises'
        docstring_1 = module_0.parse(str_2)
        docstring_2 = module_0.parse(str_2)
        docstring_3 = module_0.parse(str_0)
        docstring_4 = module_0.parse(str_1)
        str_3 = 'argument'
        docstring_5 = module_0.parse(str_3)
        docstring_6 = module_0.parse(str_1)
        str_4 = ',u>\r\t<+4bqTjXz'
        str_5 = 'y~WS\x0b\\iwpxVlz'
        docstring_7 = module_0.parse(str_5)
        docstring_8 = module_0.parse(str_4)
        docstring_9 = module_0.parse(str_0)
        docstring_10 = module_0.parse(str_1)
        docstring_11 = module_0.parse(str_2)
        docstring_12 = module_0.parse(str_1)
        docstring_13 = module_0.parse(str_1)
        docstring_14 = module_0.parse(str_1)
        docstring_15 = module_0.parse(str_3)
        str_6 = 'XYsUcUK6@~Ezy9$=g'
        docstring_16 = module_0.parse(str_6)
        str_7 = '>el[*'
        docstring_17 = module_0.parse(str_7)
        str_8 = '${d\x0cHt>zG\n:C'
        docstring_18 = module_0.parse(str_8)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ':para: a text.'
        docstring_0 = module_0.parse(str_0)
        str_1 = ':param: a text.'
        docstring_1 = module_0.parse(str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\n        this is a docstring.\n\n        very long description\n        ends with a blank line.\n\n        :param arg1: description of parameter arg1\n        :param arg2: description of parameter arg2\n        :type arg2: int\n        :param arg3, arg4: description of arg3 and arg4\n        :returns: None\n        :rtype: None\n        :raises: Exception\n        :raises ValueError, TypeError: description of raises\n        :yields: value\n        :yields ValueError: description of yields ValueError\n        '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass