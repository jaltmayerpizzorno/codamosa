# Automatically generated by Pynguin.
import tornado.log as module_0
import logging as module_1

def test_case_0():
    pass

def test_case_1():
    log_formatter_0 = module_0.LogFormatter()

def test_case_2():
    module_0.enable_pretty_logging()

def test_case_3():
    none_type_0 = None
    str_0 = 'a{X.lYBT^*{^W|\x0bTfIo-'
    log_formatter_0 = module_0.LogFormatter(str_0)
    logger_0 = module_1.Logger(log_formatter_0)
    module_0.enable_pretty_logging(none_type_0, logger_0)
    dict_0 = {}
    var_0 = logger_0.exception(log_formatter_0)
    str_1 = 'PYC*1n]J'
    str_2 = None
    log_formatter_1 = module_0.LogFormatter(str_1, str_2, str_1, dict_0)
    log_formatter_2 = module_0.LogFormatter(dict_0)

def test_case_4():
    none_type_0 = None
    str_0 = 'a{X.lYBT^*{^W|\x0bTfIo-'
    log_formatter_0 = module_0.LogFormatter(str_0)
    logger_0 = module_1.Logger(log_formatter_0)
    module_0.enable_pretty_logging(none_type_0, logger_0)
    var_0 = logger_0.exception(log_formatter_0)

def test_case_5():
    int_0 = -2275
    none_type_0 = None
    str_0 = 'a{X.lYBT^*{^W|\x0bTfIo-'
    log_formatter_0 = module_0.LogFormatter(str_0)
    logger_0 = module_1.Logger(log_formatter_0)
    module_0.enable_pretty_logging(none_type_0, logger_0)
    int_1 = None
    set_0 = {int_1, int_0}
    var_0 = logger_0.warning(set_0)