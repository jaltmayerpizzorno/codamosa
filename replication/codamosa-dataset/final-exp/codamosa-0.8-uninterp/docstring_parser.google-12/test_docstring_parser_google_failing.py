# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    try:
        section_0 = None
        google_parser_0 = module_0.GoogleParser()
        var_0 = google_parser_0.add_section(section_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '=HGQQ:Tr'
        str_1 = 'R'
        google_parser_0 = module_0.GoogleParser(str_1)
        list_0 = [str_1, str_1, str_0]
        section_0 = module_0.Section(*list_0)
        var_0 = google_parser_0.add_section(section_0)
        docstring_0 = google_parser_0.parse(str_0)
        str_2 = 's'
        google_parser_1 = module_0.GoogleParser()
        docstring_1 = google_parser_1.parse(str_2)
        google_parser_2 = module_0.GoogleParser()
        google_parser_3 = module_0.GoogleParser()
        docstring_2 = google_parser_3.parse(str_2)
        section_1 = module_0.Section()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Brief summary.\n\n           Extended summary.\n\n           Returns:\n               Returns nothing.\n\n           Yields:\n               Yields something.\n\n           Raises:\n               KeyError: An exception.\n               ValueError: Another exception.\n\n           Examples:\n               Example usage.\n               >>> f(1)\n               1\n               >>> f(2)\n               5\n    '
        docstring_0 = module_0.parse(str_0)
        section_type_0 = module_0.SectionType.MULTIPLE
        google_parser_0 = module_0.GoogleParser(section_type_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\n    This is a test.\n    Blah blah blah.\n    blah blah blah\n\n    Args:\n        haha: a test \n\n    Returns:\n        Return a test.\n    \n    Raises:\n        Error.\n    '
        google_parser_0 = module_0.GoogleParser()
        list_0 = []
        list_1 = []
        google_parser_1 = module_0.GoogleParser(list_0, list_1)
        docstring_0 = google_parser_0.parse(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Brief summary.\n\n           Extended summary.\n\n           Returns:\n               Returns nothing.\n\n           Yields:\n               Yields something.\n\n           Raises:\n               KeyError: An exception.\n               ValueError: Another except=on.\n\n           Ehamples:\n               Example usage.\n               >>> f(1)\n               1\n               >>> f(2)\n               5\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Brief summary.\n\n           Extended summary.\n\n           Returns:\n               Returns not+ing.\n\n           Yields:\n               Yields something.\n\n          Raises:\n               KeyError: An exception.\n               ValueError:6Another exception.\n\n           Examples:\n               Example usage.\n               >>> f(1)\n               1\n               >>> f(2)\n               5\n    '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = "Xyz\n    Xyz is something.\n    Args:\n    x [int] - Description for x\n    y [str] - Description for y. Defaults to 'default'.\n    z [int] - Description for z\n    Raises:\n    TypeError - Description\n    ZeroDivisionError - Description\n    Example:\n    Exmaple explanation\n    "
        google_parser_0 = module_0.GoogleParser()
        docstring_0 = google_parser_0.parse(str_0)
    except BaseException:
        pass