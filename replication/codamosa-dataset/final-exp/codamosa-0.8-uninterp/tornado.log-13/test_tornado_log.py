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
    str_0 = 'o\x0c2AHM^pT2=+i=1@'
    str_1 = '3QY8rKh]\x0cUO3(mI'
    dict_0 = {}
    log_formatter_0 = module_0.LogFormatter(str_0, str_0, str_1, dict_0)

def test_case_4():
    log_formatter_0 = module_0.LogFormatter()
    str_0 = 'some message'
    str_1 = {str_0: str_0}
    var_0 = module_1.makeLogRecord(str_1)
    str_2 = log_formatter_0.format(var_0)

def test_case_5():
    str_0 = 'unittest'
    var_0 = module_1.getLogger(str_0)
    var_1 = None
    module_0.enable_pretty_logging(var_1, var_0)
    str_1 = 'debug'
    var_2 = module_1.debug(str_1)
    str_2 = 'info'
    var_3 = module_1.info(str_2)
    str_3 = 'warning'
    var_4 = module_1.warning(str_3)
    str_4 = 'error'
    var_5 = module_1.error(str_4)
    str_5 = 'fatal'
    var_6 = module_1.fatal(str_5)