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
    log_formatter_0 = module_0.LogFormatter()
    str_0 = {log_formatter_0: log_formatter_0, log_formatter_0: log_formatter_0}
    var_0 = module_1.makeLogRecord(str_0)
    str_1 = log_formatter_0.format(var_0)

def test_case_4():
    logger_0 = None
    bytes_0 = b'\x11\xcf\x8f\xb0\x91o6Q\x19\xa6\xf5\xab\xc8\xef\x14\xe1'
    float_0 = 3379.13819
    list_0 = [logger_0, logger_0, logger_0, bytes_0]
    tuple_0 = (logger_0, bytes_0)
    log_record_0 = module_1.LogRecord(logger_0, bytes_0, logger_0, float_0, list_0, tuple_0, list_0)
    log_formatter_0 = module_0.LogFormatter()
    str_0 = log_formatter_0.format(log_record_0)