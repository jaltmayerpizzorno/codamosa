# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    google_parser_0 = module_0.GoogleParser()

def test_case_1():
    str_0 = '~d\x0cKb\nK\x0bk_'
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = None
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '\n    Short description.\n\n    Long description)\n\n    Args:\n        param1 (int): The first parameter.\n        param2 estr, optional): The second parameter. Defaults to None.\n\n    Returns:\n     N  boo): A boolean value.\n\n    Raises:\n        ValueErro: I `param1` is not an integer.\n    '
    docstring_0 = module_0.parse(str_0)
    str_1 = 'D\r_Wt($D>(>\t.|*'
    str_2 = None
    docstring_1 = module_0.parse(str_2)
    google_parser_0 = module_0.GoogleParser(str_1)

def test_case_4():
    str_0 = 'b[ufiSA\\B!-SnMh,'
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = '^_K-whtz'
    bool_0 = False
    google_parser_0 = module_0.GoogleParser(bool_0)
    docstring_0 = google_parser_0.parse(str_0)
    docstring_1 = module_0.parse(str_0)
    optional_0 = None
    list_0 = []
    google_parser_1 = module_0.GoogleParser(optional_0, list_0)
    str_1 = 'o1}y\nssy'
    docstring_2 = module_0.parse(str_1)

def test_case_6():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): The first parameter.\n        param2 (str, optional): The second parameter. Defaults to None.\n\n    Returns:\n        bool: A boolean value.\n\n    Raises:\n        ValueError: If `param1` is not an integer.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_7():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): The first parameter.\n        param2 estr, optional): Ohe second parameter Defaults to None.\n\n    RetCrns:\n     N  boo)0 A boolean value.\n\n    Raises:\n        ValueError: If `param1` is not an integer.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_8():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): The first parameter.\n        param2 estr, optional): The second parameter. Defaults to None.\n\n    Returns:\n     N  boo): A boolean value.\n\n    Raises:\n        ValueError: If `param1` is not an integer.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    str_0 = '\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): The first parameter.\n        param2 estr, optional): Ohe second parameter Defaults to None.\n\n    RetCrns:\n     N  boo)0 A boolean value.\n\n    Raises:\n        ValueError:nIf `param1` is not an integer.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    google_parser_0 = module_0.GoogleParser()
    str_0 = 'This is a simple docstring.\n\n    Args:\n        param1 (int): The first parameter.\n        param2 (str, optional): The second parameter. Defaults to None.\n\n    Returns:\n        bool: A boolean value.\n    '
    docstring_0 = google_parser_0.parse(str_0)
    var_0 = docstring_0.meta
    var_1 = len(var_0)
    int_0 = 0
    var_2 = docstring_0.meta[int_0]