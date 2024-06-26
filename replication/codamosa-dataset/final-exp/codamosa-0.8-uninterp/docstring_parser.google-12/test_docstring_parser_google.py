# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    pass

def test_case_1():
    google_parser_0 = module_0.GoogleParser()

def test_case_2():
    str_0 = '7<0>##oa9^ApU2Wd44'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = 'Brief summary.\n\n           Extended summary.\n\n           Returns:\n               Returns nothing.\n\n           Yields:\n               Yields something.\n\n           Raises:\n               KeyError: An exception.\n               ValueError: Another exception.\n\n           Examples:\n               Example usage.\n               >>> f(1)\n               1\n               >>> f(2)\n               5\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = None
    docstring_0 = module_0.parse(str_0)
    str_1 = 'Brief summary.\n\n           Extended summary.\n\n           Returns:\n               Returns nothing.\n\n           Yields:\n               Yields something.\n\n           Raises:\n               KeyError: An exception.\n              ValueError: Another exception.\n\n           Examples:\n               Example usage.\n               >>> f(1)\n               1\n               >>> f(2)\n               5\n    '
    docstring_1 = module_0.parse(str_1)

def test_case_5():
    str_0 = '\n    Test parsing Google-style docstrings.\n\n    This is the long description.\n    \n    Args:\n        arg1 (int): The first number.\n        arg2 (int): The second number.\n\n    Returns:\n        int: The return value.\n    '
    docstring_0 = module_0.parse(str_0)
    str_1 = ' '
    docstring_1 = module_0.parse(str_1)

def test_case_6():
    google_parser_0 = module_0.GoogleParser()
    str_0 = 'Computes the loss of a convolution operation.\n    Args:\n      conv_output: tensor, output of the convolution.\n      target: tensor, the target output values.\n      num_classes: the number of classes.\n      head_index: index of the head.\n      class_weights: tensor, containing the weights for each class.\n    Returns:\n      loss: scalar, the computed loss entry.\n    '
    docstring_0 = google_parser_0.parse(str_0)

def test_case_7():
    str_0 = '\n    Short description.\n\n    Long description.\n    Even longer description.\n\n    Args:\n        arg1 (str): Description for argument 1.\n        arg2 (str, optional): Description for argument 2.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '\n    Test parsing Google-style docstrings.\n\n    This is the long description.\n    \n    Args:\n        arg1 (int): The first number.\n        arg2 (int): The second number.\n\n    Returns:\n        int: The return value.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    str_0 = '\n    Method for getting some data.\n\n    Long description.\n\n    Arguments:\n        arg1 (int): first argument.\n        arg2 (int, optional): second argument. Defaults to 10.\n\n    Returns:\n        str: Some string.\n\n    Raises:\n        ValueError: If something goes wrong.\n\n    '
    google_parser_0 = module_0.GoogleParser()
    docstring_0 = google_parser_0.parse(str_0)
    var_0 = print(docstring_0)