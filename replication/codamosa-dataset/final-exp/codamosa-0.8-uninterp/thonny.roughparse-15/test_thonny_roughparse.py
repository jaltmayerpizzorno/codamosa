# Automatically generated by Pynguin.
import thonny.roughparse as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = -706.3345
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0}
    rough_parser_0 = module_0.RoughParser(float_0, dict_0)

def test_case_2():
    str_0 = ''
    list_0 = [str_0]
    rough_parser_0 = module_0.RoughParser(str_0, list_0)
    var_0 = rough_parser_0.set_str(str_0)
    var_1 = rough_parser_0.get_last_open_bracket_pos()

def test_case_3():
    str_0 = ''
    list_0 = [str_0]
    rough_parser_0 = module_0.RoughParser(str_0, list_0)
    var_0 = rough_parser_0.set_str(str_0)
    var_1 = rough_parser_0.is_block_opener()