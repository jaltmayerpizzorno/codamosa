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
    str_0 = "'TGTpkv"
    none_type_0 = None
    logger_0 = module_1.Logger(str_0)
    module_0.enable_pretty_logging(none_type_0, logger_0)
    log_formatter_0 = module_0.LogFormatter()
    var_0 = logger_0.exception(log_formatter_0)

def test_case_4():
    log_formatter_0 = module_0.LogFormatter()
    var_0 = {}
    var_1 = module_1.makeLogRecord(var_0)
    str_0 = log_formatter_0.format(var_1)