# Automatically generated by Pynguin.
import tornado.log as module_0
import logging as module_1

def test_case_0():
    try:
        log_formatter_0 = module_0.LogFormatter()
        str_0 = log_formatter_0.format(log_formatter_0)
    except BaseException:
        pass

def test_case_1():
    try:
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_2():
    try:
        module_0.define_logging_options()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = None
        bool_0 = True
        log_formatter_0 = module_0.LogFormatter(str_0, str_0, bool_0)
        set_0 = {log_formatter_0, log_formatter_0, bool_0}
        list_0 = [set_0, bool_0]
        module_0.enable_pretty_logging(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = None
        list_0 = [bool_0, bool_0]
        module_0.enable_pretty_logging(bool_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        int_0 = -2275
        none_type_0 = None
        str_0 = 'a{X.lYBT^*{^W|\x0bTfIo-'
        log_formatter_0 = module_0.LogFormatter(str_0)
        logger_0 = module_1.Logger(log_formatter_0)
        module_0.enable_pretty_logging(none_type_0, logger_0)
        int_1 = None
        set_0 = {int_1, int_0}
        var_0 = logger_0.warning(set_0)
        str_1 = '#s9Dd[*y5bgP1\x0cLo'
        dict_0 = {}
        var_1 = logger_0.addHandler(logger_0)
        log_formatter_1 = module_0.LogFormatter(str_1, dict_0)
        var_2 = logger_0.exception(log_formatter_1)
    except BaseException:
        pass