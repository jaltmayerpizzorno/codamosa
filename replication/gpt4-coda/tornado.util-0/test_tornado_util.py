# Automatically generated by Pynguin.
import builtins as module_0
import tornado.util as module_1

def test_case_0():
    pass

def test_case_1():
    base_exception_0 = module_0.BaseException()
    optional_0 = module_1.errno_from_exception(base_exception_0)

def test_case_2():
    str_0 = "\x0cz]_r'C)I"
    var_0 = module_1.doctests()
    str_1 = module_1.re_unescape(str_0)

def test_case_3():
    var_0 = module_1.doctests()
    tuple_0 = None
    str_0 = '1'
    dict_0 = {}
    arg_replacer_0 = module_1.ArgReplacer(var_0, str_0)
    tuple_1 = arg_replacer_0.replace(str_0, tuple_0, dict_0)