# Automatically generated by Pynguin.
import docstring_parser.google as module_0

def test_case_0():
    try:
        str_0 = 'Sums two numbers.D        \n        Args:\n            a (int): firt number to add\n            b (int): second number to3add\n        Returns:\n         f  int: the sum\n        '
        docstring_0 = module_0.parse(str_0)
        google_parser_0 = module_0.GoogleParser()
        section_0 = None
        var_0 = google_parser_0.add_section(section_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Sums two numbers.D        \n        Args:\n           a (int): firt nuber to add\n            b (int): secInd number to3add\n        Returns:\n        f  int: the sum\n        '
        docstring_0 = module_0.parse(str_0)
    except BaseException:
        pass