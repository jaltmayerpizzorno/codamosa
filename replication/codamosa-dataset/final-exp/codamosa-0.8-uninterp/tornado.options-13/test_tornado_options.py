# Automatically generated by Pynguin.
import tornado.options as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    option_parser_0 = module_0.OptionParser()
    str_0 = '~*nqKyK-=ur<|}l'
    bool_0 = option_parser_0.__contains__(str_0)
    option_parser_0.run_parse_callbacks()

def test_case_2():
    option_parser_0 = module_0.OptionParser()
    iterable_0 = option_parser_0.items()
    str_0 = '9'
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_3():
    option_parser_0 = module_0.OptionParser()
    str_0 = '9'
    dict_0 = option_parser_0.group_dict(str_0)

def test_case_4():
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.as_dict()

def test_case_5():
    str_0 = 'qR6i2G~;n#B~$l'
    str_1 = '/input/tornado/log.py'
    list_0 = [str_0, str_1]
    option_parser_0 = module_0.OptionParser()
    list_1 = option_parser_0.parse_command_line(list_0)

def test_case_6():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'b\x0bT~3[B vkw FPcu'
    dict_0 = option_parser_0.group_dict(str_0)
    option_parser_1 = module_0.OptionParser()
    int_0 = -316
    module_0.add_parse_callback(int_0)
    option_parser_2 = module_0.OptionParser()
    str_1 = '/input/tornado/log.py'
    bool_0 = False
    option_parser_2.parse_config_file(str_1, bool_0)
    mockable_0 = option_parser_1.mockable()
    iterable_0 = option_parser_2.items()

def test_case_7():
    str_0 = '\n\n##### In test_Option_value():'
    var_0 = print(str_0)
    bool_0 = False
    option_0 = module_0._Option(str_0, str_0, str_0, bool_0, str_0)
    option_0.set(var_0)

def test_case_8():
    str_0 = 'mbl!&A&aZ"j'
    str_1 = 'rH\rnwCU\n?vm'
    list_0 = []
    list_1 = [str_1]
    type_0 = module_1.type(*list_1)
    option_0 = module_0._Option(str_1, list_0, type_0, str_0)
    any_0 = option_0.parse(str_1)

def test_case_9():
    str_0 = 'mbl!&A&aZ"j'
    option_parser_0 = module_0.OptionParser()
    dict_0 = option_parser_0.group_dict(str_0)
    str_1 = 'rH\rnwCU\n?vm'
    list_0 = []
    dict_1 = option_parser_0.as_dict()
    list_1 = [str_1]
    type_0 = module_1.type(*list_1)
    option_0 = module_0._Option(str_1, list_0, type_0, str_0)
    any_0 = option_0.parse(str_1)
    optional_0 = None
    option_1 = module_0._Option(str_1, any_0, type_0, str_1, str_0, optional_0)
    option_0.set(str_1)

def test_case_10():
    option_parser_0 = module_0.OptionParser()
    mockable_0 = module_0._Mockable(option_parser_0)
    iterable_0 = option_parser_0.items()
    str_0 = 'T'
    str_1 = 'mbl!&A&aZ"j'
    str_2 = 'Content-Disposition'
    option_parser_1 = module_0.OptionParser()
    str_3 = ']M%'
    list_0 = [str_3, str_3]
    list_1 = option_parser_1.parse_command_line(list_0)
    dict_0 = option_parser_0.group_dict(str_0)
    list_2 = []
    dict_1 = option_parser_0.as_dict()
    list_3 = [str_2]
    type_0 = module_1.type(*list_3)
    option_0 = module_0._Option(str_2, list_2, type_0, str_0)
    any_0 = option_0.parse(str_2)
    option_0.set(str_0)
    str_4 = ' (viaU%s)'
    bool_0 = True
    none_type_0 = None
    option_1 = module_0._Option(str_4, str_3, str_3, bool_0, str_1, str_3, none_type_0)
    option_1.set(list_2)

def test_case_11():
    option_parser_0 = module_0.OptionParser()
    str_0 = 'port'
    int_0 = 8000
    str_1 = 'Port to listen on'
    option_parser_0.define(str_0, int_0, str_1)
    str_2 = 'log_to_stderr'
    bool_0 = False
    str_3 = 'Send log output to stderr (colorized if possible)'
    option_parser_0.define(str_2, bool_0, str_3)
    var_0 = list(option_parser_0)
    var_1 = len(var_0)