# Automatically generated by Pynguin.
import docstring_parser.parser as module_0
import docstring_parser.styles as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '^,_(%zG8xVTGpD'
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = ':ne]m\t'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = 'sQ%>\x0b\r~,a\x0cYe^K^P\x0cR'
    style_0 = module_1.Style.google
    docstring_0 = module_0.parse(str_0, style_0)
    str_1 = 'No specification for "{}": "{}"'
    docstring_1 = module_0.parse(str_1)