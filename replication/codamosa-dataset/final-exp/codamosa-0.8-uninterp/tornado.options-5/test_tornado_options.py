# Automatically generated by Pynguin.
import tornado.options as module_0
import typing as module_1
import builtins as module_2

def test_case_0():
    pass

def test_case_1():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'name'
    option_parser_0.define(str_0, str_0)
    mockable_0 = module_0._Mockable(option_parser_0)
    var_0 = setattr(mockable_0, str_0, str_0)

def test_case_2():
    str_0 = '=mqMRG#5qcB'
    option_parser_0 = module_0.OptionParser()
    bool_0 = option_parser_0.__contains__(str_0)
    option_parser_1 = module_0.OptionParser()
    dict_0 = option_parser_1.as_dict()

def test_case_3():
    option_parser_0 = module_0.OptionParser()
    str_0 = "\n[tC:ck,kGhs'^,Bmc9l"
    dict_0 = None
    option_parser_0.define(str_0, str_0, str_0, dict_0)
    option_parser_0.__setitem__(str_0, dict_0)

def test_case_4():
    option_parser_0 = module_0.OptionParser()
    iterable_0 = option_parser_0.items()

def test_case_5():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'H@LN_4'
    dict_0 = option_parser_0.group_dict(str_0)
    set_0 = option_parser_0.groups()
    option_parser_1 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()

def test_case_6():
    str_0 = None
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_7():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()

def test_case_8():
    option_parser_0 = module_0.OptionParser()
    callable_0 = None
    str_0 = ';c!7yz&TCCjctAJ_(\nsT'
    module_0.define(str_0, str_0)
    module_0.add_parse_callback(callable_0)
    mockable_0 = module_0._Mockable(option_parser_0)

def test_case_9():
    option_parser_0 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()

def test_case_10():
    option_parser_0 = None
    mockable_0 = module_0._Mockable(option_parser_0)

def test_case_11():
    str_0 = '#1'
    bool_0 = False
    list_0 = None
    list_1 = [bool_0]
    text_i_o_0 = module_1.TextIO()
    option_parser_0 = module_0.OptionParser()
    option_parser_0.print_help(text_i_o_0)
    type_0 = module_2.type(*list_1)
    bool_1 = None
    option_0 = module_0._Option(str_0, list_0, type_0, str_0, bool_1)
    any_0 = option_0.parse(str_0)

def test_case_12():
    str_0 = '#1'
    bool_0 = False
    list_0 = None
    list_1 = [bool_0]
    type_0 = module_2.type(*list_1)
    option_0 = module_0._Option(str_0, list_0, type_0, str_0, bool_0)
    any_0 = option_0.parse(str_0)

def test_case_13():
    str_0 = '/input/tornado/options.py'
    option_parser_0 = module_0.OptionParser()
    option_parser_0.parse_config_file(str_0)
    option_parser_1 = module_0.OptionParser()