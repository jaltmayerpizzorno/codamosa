# Automatically generated by Pynguin.
import thefuck.argument_parser as module_0

def test_case_0():
    pass

def test_case_1():
    parser_0 = module_0.Parser()

def test_case_2():
    list_0 = []
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_help()
    parser_1 = module_0.Parser()
    var_1 = parser_1.parse(list_0)
    var_2 = parser_1.print_usage()

def test_case_3():
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_usage()

def test_case_4():
    parser_0 = module_0.Parser()
    var_0 = parser_0.print_help()

def test_case_5():
    parser_0 = module_0.Parser()
    str_0 = '3-'
    var_0 = parser_0.parse(str_0)
    parser_1 = module_0.Parser()
    parser_2 = module_0.Parser()
    var_1 = parser_1.print_usage()
    var_2 = parser_2.print_help()