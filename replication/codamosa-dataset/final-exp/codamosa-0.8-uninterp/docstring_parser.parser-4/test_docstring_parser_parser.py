# Automatically generated by Pynguin.
import docstring_parser.parser as module_0
import docstring_parser.styles as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = '"I\r\rb!@JKS( '
    docstring_0 = module_0.parse(str_0)

def test_case_2():
    str_0 = 'x\n:\x0b),4f'
    docstring_0 = module_0.parse(str_0)

def test_case_3():
    str_0 = '6STe'
    style_0 = module_1.Style.google
    docstring_0 = module_0.parse(str_0, style_0)