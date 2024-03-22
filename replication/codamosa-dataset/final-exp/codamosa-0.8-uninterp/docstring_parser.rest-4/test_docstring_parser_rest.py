# Automatically generated by Pynguin.
import docstring_parser.rest as module_0
import inspect as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '\n    Docstring summary.\n    \n    Long description.\n    \n    :param a: A parameter.\n    :type a: int\n    :param b: Another parameter, defaults to None.\n    :type b: str\n    :param c: Yet another parameter, defaults to None.\n    :type c: str\n    :rtype: str\n    :return: Return description\n    :raises ValueError: raise description\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = 'Parse the numpy-style docstring into its components.\n\n        :returns: parsed docstring\n        '
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '-CNj%#@L*'
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = '\n    Short summary.\n\n    This is a long description.\n\n    :param a: This is a parameter description\n    :type a: integer\n    :param b: This is a parameter description that defaults to null\n      and is optional.\n    :type b: integer\n    :param c: This is a parameter description that defaults to 3.\n    :type c: integer\n    :param d: This is a parameter description.\n    :type d: integer\n    :param e: This is a parameter description that defaults to null.\n      It is optional.\n    :type e: integer\n    :param f: This is a parameter description.\n    :returns: integer\n    :raises Exception: An exception\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = None
    docstring_0 = module_0.parse(str_0)

def test_case_6():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    :param type arg1: description\n    :type arg1: type\n    :param arg2: description\n    :keyword type arg3: description\n    :keyword arg4: description\n    :returns: what is returned\n    :rtype: type\n    :rtype: desc\n    :returns: desc\n    :return: desc\n    :yields: what is yielded\n    :yields: desc\n    :yield: desc\n    :raises Exc: what exceptions are raised\n    :raises Exc: desc\n    :raise Exc: desc\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = 'This is a short description.\n\nThis is a long description.\n\n:param arg1: argument 1\n:type arg1: str\n:param arg2: argument 2\n:type arg2: int\n:param arg3: argument 3\n:type arg3: str or int\n:returns: return type\n:raises: raises error\n:param optional_arg: an optional argument\n:type optional_arg: str\n:param optional_arg_with_default: an optional argument with a default value\n:type optional_arg_with_default: str\n:param optional_arg_with_type_and_default: an optional argument with a default value and a type\n:type optional_arg_with_type_and_default: str\n:key arg4: argument 4\n:key arg5: argument 5\n:key arg6: argument 6\n'
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '\n        This function performs bread.\n\n        :param str name: The name of the bread.\n        :param str kind: The type of bread.\n        :param int crustiness: Hardness of the crust.\n        :param float weight: Weight of the bread, in Kg.\n        :param float? price: Price of the bread, in dollars. Defaults to 0.5.\n        :raises NotEnoughBreadError: When there is not enough bread.\n        :raises TypeError: When something goes wrong.\n        :returns: The bread object.\n        '
    docstring_0 = module_0.parse(str_0)
    var_0 = module_1.cleandoc(str_0)