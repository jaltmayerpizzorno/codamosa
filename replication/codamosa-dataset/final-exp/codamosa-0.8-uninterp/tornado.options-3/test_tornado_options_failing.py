# Automatically generated by Pynguin.
import tornado.options as module_0
import typing as module_1

def test_case_0():
    try:
        str_0 = '&XJ~\nz?|j|]'
        option_parser_0 = module_0.OptionParser()
        mockable_0 = option_parser_0.mockable()
        mockable_0.__setattr__(str_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '/input/tornado/options.py'
        module_0.parse_config_file(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '\x0bN'
        option_parser_0 = module_0.OptionParser()
        option_parser_0.__setitem__(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        option_parser_0 = module_0.OptionParser()
        option_parser_1 = module_0.OptionParser()
        dict_0 = option_parser_1.as_dict()
        iterator_0 = option_parser_1.__iter__()
        str_0 = 'rv\nO*Rw:\\6I'
        any_0 = option_parser_0.__getitem__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '/input/tornado/options.py'
        option_parser_0 = module_0.OptionParser()
        option_parser_0.parse_config_file(str_0)
        iterable_0 = option_parser_0.items()
        list_0 = option_parser_0.parse_command_line()
    except BaseException:
        pass

def test_case_5():
    try:
        optional_0 = None
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.as_dict()
        option_parser_0.run_parse_callbacks()
        list_0 = option_parser_0.parse_command_line(optional_0)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = module_0.parse_command_line()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'config.py'
        list_0 = [str_0]
        option_parser_0 = module_0.OptionParser()
        list_1 = option_parser_0.parse_command_line(list_0)
        option_parser_1 = module_0.OptionParser()
        option_parser_1.__setitem__(str_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        list_0 = module_0.parse_command_line()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/input/tornado/options.py'
        option_parser_0 = module_0.OptionParser()
        option_parser_0.parse_config_file(str_0)
        option_parser_1 = module_0.OptionParser()
        iterable_0 = option_parser_1.items()
        str_1 = '"]*/'
        mockable_0 = module_0._Mockable(option_parser_1)
        any_0 = mockable_0.__getattr__(str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'LT3G,+l_'
        option_parser_0 = module_0.OptionParser()
        mockable_0 = module_0._Mockable(option_parser_0)
        mockable_0.__delattr__(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = ',.h(AnWpm:_cEm\x0c|U'
        option_parser_0 = module_0.OptionParser()
        option_0 = module_0._Option(str_0, option_parser_0)
    except BaseException:
        pass

def test_case_12():
    try:
        option_parser_0 = module_0.OptionParser()
        iterator_0 = option_parser_0.__iter__()
        str_0 = '/input/tornado/log.py'
        bool_0 = True
        list_0 = [str_0]
        option_0 = module_0._Option(str_0, bool_0, bool_0, str_0, str_0, list_0)
        option_0.set(iterator_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bool_0 = True
        module_0.add_parse_callback(bool_0)
        str_0 = '/input/tornado/options.py'
        option_parser_0 = module_0.OptionParser()
        option_parser_0.parse_config_file(str_0)
        iterable_0 = option_parser_0.items()
        list_0 = option_parser_0.parse_command_line()
    except BaseException:
        pass

def test_case_14():
    try:
        option_parser_0 = module_0.OptionParser()
        str_0 = '--static_path=/path/to/static'
        list_0 = option_parser_0.parse_command_line(str_0)
    except BaseException:
        pass

def test_case_15():
    try:
        option_parser_0 = module_0.OptionParser()
        str_0 = 'static_path'
        iterable_0 = option_parser_0.items()
        option_parser_0.define(str_0, str_0)
        str_1 = '--static_path=/path/to/static'
        str_2 = [str_1, str_1, str_0]
        list_0 = option_parser_0.parse_command_line(str_2)
        text_i_o_0 = module_1.TextIO()
        option_parser_0.print_help(text_i_o_0)
        list_1 = option_parser_0.parse_command_line()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'd\\E]1 Z'
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.group_dict(str_0)
        str_1 = '/input/tornado/options.py'
        str_2 = 'LSi|\x0bTE'
        module_0.define(str_2, str_0, str_0)
        option_parser_0.parse_config_file(str_1)
        list_0 = option_parser_0.parse_command_line()
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = ']j\\Okbnx'
        module_0.define(str_0, str_0, str_0)
    except BaseException:
        pass

def test_case_18():
    try:
        option_parser_0 = module_0.OptionParser()
        iterator_0 = option_parser_0.__iter__()
        str_0 = '/input/tornado/log.py'
        option_parser_0.define(str_0)
        bool_0 = True
        list_0 = [str_0]
        option_0 = module_0._Option(str_0, bool_0, bool_0, str_0, str_0, list_0)
        option_0.set(iterator_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'R\x0b\n@DEj\rZn3\tc\nc='
        str_1 = 'V6~m3wO%[+N4r~w'
        bool_0 = True
        option_0 = module_0._Option(str_1, str_1, bool_0, str_1)
        any_0 = option_0.parse(str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        text_i_o_0 = module_1.TextIO()
        text_i_o_1 = text_i_o_0.__enter__()
        text_i_o_2 = text_i_o_0.__enter__()
        str_0 = ''
        option_parser_0 = module_0.OptionParser()
        dict_0 = option_parser_0.group_dict(str_0)
        option_parser_1 = module_0.OptionParser()
        option_parser_1.print_help(text_i_o_0)
        option_parser_2 = module_0.OptionParser()
        mockable_0 = option_parser_2.mockable()
        option_parser_3 = module_0.OptionParser()
        str_1 = '=+Qf3e\x0bG'
        mockable_0.__setattr__(str_1, option_parser_2)
    except BaseException:
        pass

def test_case_21():
    try:
        list_0 = []
        bool_0 = False
        option_parser_0 = module_0.OptionParser()
        list_1 = option_parser_0.parse_command_line(list_0, bool_0)
        option_parser_1 = module_0.OptionParser()
        str_0 = 'applcation'
        dict_0 = option_parser_1.group_dict(str_0)
        var_0 = lambda : dict_0
        option_parser_1.add_parse_callback(var_0)
        option_parser_1.define(str_0, str_0)
        str_1 = 'static_0pa\x0bh'
        option_parser_1.define(str_1, str_0)
        option_parser_1.__setattr__(str_0, dict_0)
    except BaseException:
        pass

def test_case_22():
    try:
        callable_0 = None
        option_parser_0 = module_0.OptionParser()
        option_parser_0.add_parse_callback(callable_0)
        iterable_0 = option_parser_0.items()
        dict_0 = option_parser_0.as_dict()
        module_0.print_help()
    except BaseException:
        pass

def test_case_23():
    try:
        list_0 = module_0.parse_command_line()
    except BaseException:
        pass

def test_case_24():
    try:
        list_0 = module_0.parse_command_line()
    except BaseException:
        pass

def test_case_25():
    try:
        option_parser_0 = module_0.OptionParser()
        str_0 = 'a|}pplication'
        dict_0 = option_parser_0.group_dict(str_0)
        option_parser_0.add_parse_callback(dict_0)
        option_parser_0.print_help()
        option_parser_0.define(str_0, str_0)
        option_parser_0.__setattr__(str_0, dict_0)
    except BaseException:
        pass