# Automatically generated by Pynguin.
import tornado.options as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'q2_yf/H&P6A'
    option_parser_0 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()
    option_parser_1 = module_0.OptionParser()
    option_parser_2 = module_0.OptionParser()
    mockable_0 = option_parser_0.mockable()
    bool_0 = option_parser_2.__contains__(str_0)
    iterable_0 = option_parser_2.items()

def test_case_2():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()

def test_case_3():
    str_0 = '/input/tornado/log.py'
    option_parser_0 = module_0.OptionParser()
    option_parser_0.parse_config_file(str_0)

def test_case_4():
    type_0 = None
    str_0 = '75me'
    option_0 = module_0._Option(str_0, str_0, str_0)
    option_0.set(type_0)

def test_case_5():
    bool_0 = None
    str_0 = "Z{qFl'}"
    list_0 = [str_0, str_0]
    list_1 = []
    option_0 = module_0._Option(str_0, list_0, str_0, list_1)
    option_0.set(bool_0)
    any_0 = option_0.value()

def test_case_6():
    option_parser_0 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()
    str_0 = "uUL^|'2"
    list_0 = [str_0]
    type_0 = module_1.type(*list_0)
    bool_0 = True
    str_1 = '#`,+PZ.Lm>c@\x0bG'
    str_2 = ',{nemt:4x'
    dict_0 = {str_1: str_2}
    option_parser_0.define(str_0, type_0, str_0, str_0, bool_0, str_0, dict_0)
    mockable_0 = option_parser_0.mockable()