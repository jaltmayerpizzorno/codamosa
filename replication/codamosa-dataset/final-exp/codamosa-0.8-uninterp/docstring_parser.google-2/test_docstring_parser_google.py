# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    pass

def test_case_1():
    google_parser_0 = module_0.GoogleParser()

def test_case_2():
    str_0 = '!\x0c*JYr?\\\\>0H_MX'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '    This is a test docstring.\n\n    Args:\n        param1 (str): The first parameter.\n        param2 (str): The second parameter.\n\n    Returns:\n        str: The return value. True for success, False oterwise.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    google_parser_0 = module_0.GoogleParser()
    str_0 = '\n        Short summary.\n        Longer description.\n\n        Args:\n            var1: Description for `var1`.\n            var2: Description for `var2`.\n\n        Returns:\n            Description of return value.\n            Description of return value.\n\n        Raises:\n            ValueError: Description of `ValueError` raised.\n            AttributeError: Description of `AttributeError` raised.\n\n        Examples:\n            Examples should be written in doctest format, and\n            should illustrate how to use the function.\n\n            >>> a=[1,2,3]\n            >>> print([x + 3 for x in a])\n            [4, 5, 6]\n    '
    str_1 = None
    docstring_0 = google_parser_0.parse(str_1)
    docstring_1 = google_parser_0.parse(str_0)

def test_case_5():
    str_0 = "    This is a test docstring.\n\n    Arsm\n        par&m1(str): The first parameter.\n        param2 (str): The second par'meter.\n\n    Returns:\n        str: The return value. True for success, False otherwise.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = '\n        Args:\n            a: a\n            b (optional): b\n            c (bool): c\n            d (:obj:`int`): d\n        Returns:\n            :obj:`bool`\n        Raises:\n            :obj:`ValueError`: if not valid\n        '
    google_parser_0 = module_0.GoogleParser()
    docstring_0 = google_parser_0.parse(str_0)

def test_case_7():
    str_0 = '    This is a test docstring.\n\n    Args:\n        param1 (sr): The first parameter.\n       para{2 (str): The second parameter.\n\n    Returns:\n       str: The return value. True for success, False otherwise.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '    This is a test docstring.\n\n    Args:\n        param1 str): The first parameter.\n        param2 (str): The second parameter.\n    Returns:\n        str: The return value. True for success, False otherwise.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    google_parser_0 = module_0.GoogleParser()
    str_0 = '\n    Short summary.\n\n    Longer summary.\n\n    Args:\n        name (str): Name of the staff. Defaults to None.\n        age (int, optional): Age of the staff.\n        salary (str?): Salary of the staff.\n\n    Returns:\n        str: Return value. Defaults to None.\n          Return value description.\n\n    Raises:\n        Exception: Error description.\n\n    '
    docstring_0 = google_parser_0.parse(str_0)

def test_case_10():
    str_0 = 'Title: Adds two numbers together.\nSummary: Adds two numbers together.\n\nDescription of the function.\n\nArguments:\n    x: The first number to add.\n    y: The second number to add.\n\nReturns:\n    The sum of x and y.\n\nExample:\n    Print the sum of 2 and 3:\n\n    >>> print(add(2, 3))\n    5\n'
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = '\n        Short summary.\n        Longer description.\n\n        Args:\n            var1: Description for `var1`.\n            var2: Description for `var2`.\n\n        Returns:\n            Description of return value.\n            Description of return value.\n\n        Raises:\n            ValueError: Description of `ValueError` raised.\n            AttributeError: Description of `AttributeError` raised.\n\n        Examples:\n            Examples should be written in doctest format, and\n            should illustrate how to use the function.\n\n            >>> a=[1,2,3]\n            >>> print([x + 3 for x in a])\n            [4, 5, 6]\n    '
    docstring_0 = module_0.parse(str_0)