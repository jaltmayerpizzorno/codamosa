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
    str_0 = None
    optional_0 = None
    list_0 = None
    module_0.enable_pretty_logging()
    logger_0 = module_1.Logger(list_0)
    module_0.enable_pretty_logging(optional_0, logger_0)
    log_formatter_0 = module_0.LogFormatter(str_0)
    var_0 = logger_0.exception(log_formatter_0)
    log_formatter_1 = module_0.LogFormatter()