# Automatically generated by Pynguin.
import tornado.options as module_0

def test_case_0():
    pass

def test_case_1():
    option_parser_0 = module_0.OptionParser()
    mockable_0 = option_parser_0.mockable()
    iterable_0 = option_parser_0.items()
    option_parser_1 = module_0.OptionParser()

def test_case_2():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'L'
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_3():
    str_0 = '--'
    list_0 = [str_0, str_0]
    bool_0 = False
    list_1 = module_0.parse_command_line(list_0, bool_0)

def test_case_4():
    option_parser_0 = module_0.OptionParser()
    option_parser_0.run_parse_callbacks()

def test_case_5():
    option_parser_0 = module_0.OptionParser()
    mockable_0 = module_0._Mockable(option_parser_0)

def test_case_6():
    str_0 = ''
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.group_dict(str_0)
    str_1 = '-logging=dbg'
    str_2 = "Vc/T'G.JV"
    optional_0 = None
    option_0 = module_0._Option(str_2, str_1, str_1, optional_0)
    option_0.set(optional_0)

def test_case_7():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()
    str_0 = '-logging=dbg'
    str_1 = "Vc/T'G.JV"
    optional_0 = None
    option_0 = module_0._Option(str_1, str_0, str_0, optional_0)
    option_0.set(optional_0)