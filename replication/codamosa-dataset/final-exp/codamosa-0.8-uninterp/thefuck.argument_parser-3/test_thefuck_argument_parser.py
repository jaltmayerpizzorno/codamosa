# Automatically generated by Pynguin.
import thefuck.argument_parser as module_0

def test_case_0():
    pass

def test_case_1():
    parser_0 = module_0.Parser()

def test_case_2():
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_usage()

def test_case_3():
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_help()

def test_case_4():
    parser_0 = module_0.Parser()
    str_0 = 'command'
    str_1 = [str_0]
    var_0 = parser_0.parse(str_1)
    str_2 = '--'
    str_3 = [str_0, str_2]
    var_1 = parser_0.parse(str_3)
    str_4 = [str_0]
    var_2 = parser_0.parse(str_4)
    str_5 = [parser_0, str_0, str_1]
    var_3 = parser_0.parse(str_5)