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
        module_0.enable_pretty_logging()
        list_0 = []
        module_0.enable_pretty_logging(list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        log_formatter_0 = module_0.LogFormatter()
        log_formatter_1 = module_0.LogFormatter()
        module_0.enable_pretty_logging()
        module_0.define_logging_options(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'DEBUG'
        log_record_0 = module_1.LogRecord(str_0, str_0, str_0, str_0, str_0, str_0, str_0)
        log_formatter_0 = module_0.LogFormatter()
        str_1 = log_formatter_0.format(log_record_0)
    except BaseException:
        pass

def test_case_6():
    try:
        stream_handler_0 = module_1.StreamHandler()
        float_0 = None
        dict_0 = {float_0: stream_handler_0}
        list_0 = []
        bytes_0 = None
        str_0 = "@|HJi'd_'!4Ylg"
        dict_1 = {str_0: stream_handler_0}
        log_record_0 = module_1.LogRecord(stream_handler_0, float_0, dict_0, stream_handler_0, list_0, bytes_0, str_0, **dict_1)
        str_1 = 'u`G+;'
        bool_0 = True
        log_formatter_0 = module_0.LogFormatter(str_1, str_1, bool_0)
        str_2 = log_formatter_0.format(log_record_0)
    except BaseException:
        pass