# Automatically generated by Pynguin.
import thefuck.argument_parser as module_0

def test_case_0():
    try:
        str_0 = "sI,Aj'Q]'q\x0bVb"
        parser_0 = module_0.Parser()
        var_0 = parser_0.parse(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x14\xea\x06D`\x19'
        str_0 = 'QK#oV~CTidk!I\tjy'
        list_0 = [str_0, str_0, bytes_0, bytes_0]
        str_1 = '--'
        parser_0 = module_0.Parser()
        var_0 = parser_0.parse(str_1)
        parser_1 = module_0.Parser()
        var_1 = parser_1.parse(list_0)
        parser_2 = module_0.Parser()
        parser_3 = module_0.Parser()
        var_2 = parser_3.print_usage()
        var_3 = parser_2.print_usage()
        var_4 = parser_2.print_help()
        str_2 = 'l>7KVJPHs\x0bWZM/6cQ2LL'
        var_5 = parser_2.parse(str_2)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 550
        parser_0 = module_0.Parser()
        var_0 = parser_0.parse(int_0)
    except BaseException:
        pass

def test_case_3():
    try:
        parser_0 = module_0.Parser()
        tuple_0 = ()
        var_0 = parser_0.parse(tuple_0)
        var_1 = parser_0.print_help()
        parser_1 = module_0.Parser()
        var_2 = parser_1.print_usage()
        var_3 = parser_0.print_usage()
        var_4 = parser_0.print_usage()
        var_5 = parser_0.print_usage()
        var_6 = parser_0.print_usage()
        var_7 = parser_0.print_help()
        var_8 = parser_0.print_usage()
        var_9 = parser_0.print_help()
        var_10 = parser_1.print_usage()
        parser_2 = module_0.Parser()
        var_11 = parser_2.print_usage()
        var_12 = parser_1.print_usage()
        float_0 = 4047.18857
        var_13 = parser_0.parse(float_0)
    except BaseException:
        pass