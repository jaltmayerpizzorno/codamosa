# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    pass

def test_case_1():
    google_parser_0 = module_0.GoogleParser()

def test_case_2():
    str_0 = "\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n    Returns:\n        bool: Description of return value.\n    "
    google_parser_0 = module_0.GoogleParser()
    list_0 = [str_0, google_parser_0, str_0]
    section_0 = module_0.Section(*list_0)
    google_parser_1 = module_0.GoogleParser()
    docstring_0 = module_0.parse(str_0)
    var_0 = google_parser_1.add_section(section_0)

def test_case_3():
    str_0 = 'fhd>m'
    docstring_0 = module_0.parse(str_0)

def test_case_4():
    str_0 = "'\ncv8IX#o+TiW@"
    docstring_0 = module_0.parse(str_0)

def test_case_5():
    str_0 = None
    docstring_0 = module_0.parse(str_0)
    str_1 = "\n    Shor deGcription.\n\n    Long de-cription\n\n    Args:\n        param1Q(int): Description of param1.\n        param2 (str: Descri1tion of param2. DefaultsSo 'default'.i\n    Returns:\n       bool:iDescription of return value.\n    "
    docstring_1 = module_0.parse(str_1)

def test_case_6():
    str_0 = "\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n    Returns:\n        bool: Description of return value.\n    "
    str_1 = "d9W<NXs+\tY>V?'Cfqw"
    google_parser_0 = module_0.GoogleParser(str_1)
    docstring_0 = google_parser_0.parse(str_0)

def test_case_7():
    str_0 = ' '
    docstring_0 = module_0.parse(str_0)
    str_1 = "\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n    Returns:\n        bool: Description of return value.\n    "
    docstring_1 = module_0.parse(str_1)

def test_case_8():
    str_0 = "\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n    Returns:\n        bool: Description of return value.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_9():
    str_0 = "\n    Short description.\n\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n   Returns:\n        bool: Description of return value.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_10():
    str_0 = "\n    Short description.\n\n    Long descript%on.\n\n    Args:\n        param1 (int): Description oP param1.\n        paraH2 (s\x0cr): Description of paa\x0c2. D6faults to 'default'.\n\n    Returns:\n        bool Description of return value.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_11():
    str_0 = "\n    Short description./\n    Long description.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str): Description of param2. Defaults to 'default'.\n\n    Retur\rs:\n        bool: Description of return value.\n    "
    docstring_0 = module_0.parse(str_0)

def test_case_12():
    str_0 = '\n    Shor deGcription.\n\n    LongJdescription.\n\n    Args:\n        param1 (int): Description of param1.\n        param2 (str):"Description of param2. Defaults Oo \'default\'.\n\n    Returns:\n        bool: Description of return value.\n    '
    docstring_0 = module_0.parse(str_0)

def test_case_13():
    str_0 = 'HKw8aoJt?c7mE]\n\x0c'
    docstring_0 = module_0.parse(str_0)