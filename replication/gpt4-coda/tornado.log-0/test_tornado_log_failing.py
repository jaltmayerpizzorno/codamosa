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
        bool_0 = False
        list_0 = [bool_0]
        logger_0 = module_1.Logger(list_0)
        module_0.enable_pretty_logging(list_0, logger_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'XSRF cookie does not match POST argument'
        module_0.enable_pretty_logging()
        bool_0 = True
        log_formatter_0 = module_0.LogFormatter(bool_0)
        optional_0 = None
        logger_0 = module_1.Logger(str_0)
        module_0.enable_pretty_logging(optional_0, logger_0)
        log_formatter_1 = module_0.LogFormatter(str_0)
        str_1 = log_formatter_1.format(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.enable_pretty_logging()
        str_0 = 'ynv'
        module_0.define_logging_options(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'XSRF cookie does not match POST argument'
        bool_0 = True
        str_1 = 'SRF cooki d\res ot match POST argument'
        bool_1 = None
        log_formatter_0 = module_0.LogFormatter(str_0, str_0, str_1, bool_1)
        module_0.enable_pretty_logging()
        log_formatter_1 = module_0.LogFormatter(bool_0)
        str_2 = log_formatter_1.format(log_formatter_1)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 1152.827945096803
        int_0 = 1038
        str_0 = '^\x0c'
        bool_0 = True
        log_record_0 = module_1.LogRecord(float_0, float_0, int_0, str_0, bool_0, str_0, str_0)
        log_formatter_0 = module_0.LogFormatter(str_0)
        str_1 = log_formatter_0.format(log_record_0)
    except BaseException:
        pass