# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    try:
        str_0 = ':'
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Test function\n    :param int x: An integer\n    :param : A parameter with no type\n    :param z: A parameterwith no type nor name\n    :param type b: A parameter with no name\n    :yields: A generator\n    :yields: A generator with no type\n    :returns: A return object\n    :returns: A return with no type\n    :raises TypeError: This fails\n    :raises TypeError: This fails with no args\n    :raises: This fails with no type\n    '
        str_1 = None
        docstring_0 = module_0.parse(str_1)
        docstring_1 = module_0.parse(str_0)
    except BaseException:
        pass