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
    str_0 = '%(color)s%(levelname)s%(end_color)s %(message)s'
    log_formatter_0 = module_0.LogFormatter(str_0)
    str_1 = {str_0: str_0}
    var_0 = module_1.makeLogRecord(str_1)
    str_2 = log_formatter_0.format(var_0)