# Automatically generated by Pynguin.
import tornado.log as module_0

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
        float_0 = -1307.2
        str_0 = 'iIptF@TT;aMbf'
        module_0.enable_pretty_logging()
        dict_0 = {str_0: float_0}
        log_formatter_0 = module_0.LogFormatter(str_0)
        str_1 = log_formatter_0.format(dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 60.0
        module_0.enable_pretty_logging(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'Union[Future[List], Future[Dict]]'
        log_formatter_0 = module_0.LogFormatter(str_0)
        str_1 = '#c_x%-'
        bool_0 = True
        log_formatter_1 = module_0.LogFormatter(str_1, bool_0)
        module_0.define_logging_options(log_formatter_0)
    except BaseException:
        pass