# Automatically generated by Pynguin.
import docstring_parser.rest as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    :param x: bla\n    :param y: bla\n    :returns: bla\n    :rtype: str\n    :raises ValueError: bla\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = 'warnings'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Gparam x: bla\n    :para4 y: bla\n    :retusns: bla\n    :rtype: str\n    1raise:*ValueError: bla\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = '59U\rIn\tY\nCz:+V\nu+[w!'
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = None
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = '    This is a test docstring.\n\n    :param arg: An argument\n    :type arg: str\n    :returns: This is a return\n    :rtype: str\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = '\n    test\n    :type x: int\n    :type y: str\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '    This is the Summary.\n\n    :param str arg1: This is the 1st argument.\n    :param int arg2: This is the 2nd argument.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Gparam x: bla\n    :param y: bla\n    :returns: bla\n    :rtype: str\n    :raise:*ValueError: bla\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    str_0 = '    this docstring does not have a blank after short description\n    The short description.\n    The long description.\n    With a blank after it.\n    :arg int x: The x coordinate.\n    :arg int y: The y coordinate.\n    :raises np.NumpyError: when x or y is negative.\n    :raises ValueError: when x or y is too large.\n    :returns: a point (x, y)\n    :yields int: an int\n    :returns: a point (x, y)\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = 'This is a description.\n\n*:param cls: a particular class.\n:param verbose: Output progress messages, defaults to False.\n:returns: The number of images in the directory.\n:raises ValueError: If the directory does not exist.\n    '
    docstring_0 = module_0.parse(str_0)
    var_0 = print(str_0)