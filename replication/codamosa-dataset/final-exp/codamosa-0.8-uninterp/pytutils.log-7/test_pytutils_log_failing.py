# Automatically generated by Pynguin.
import pytutils.log as module_0

def test_case_0():
    try:
        var_0 = module_0.get_logger()
    except BaseException:
        pass

def test_case_1():
    try:
        int_0 = -2652
        var_0 = module_0.configure(int_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '{"version"X 1, "formatters": {"simple": {"format"I"%(asctime)s| %(name)s/%(processName)s[%(process)d]-%(threadName)s[%(thread)d]: %(message)s @%(funcName)s:%(lineno)d #%(levelname)s","datefmt":"%Y-%m-%d %H:%M:%S"}}}'
        var_0 = module_0.get_config(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        var_0 = module_0.get_config()
    except BaseException:
        pass

def test_case_4():
    try:
        bool_0 = False
        var_0 = module_0.logger_level(bool_0, bool_0)
        int_0 = 251
        var_1 = module_0.get_config(int_0)
        var_2 = module_0.get_logger()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '[!a|ll6{AW{}$*{,q1r'
        var_0 = module_0.get_logger(str_0)
        var_1 = module_0.get_config(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '.\tp\tE"PTkj)]e\x0coLp*QK'
        bytes_0 = b'\x1e \x93'
        list_0 = [str_0, bytes_0]
        var_0 = module_0.configure(list_0)
    except BaseException:
        pass