# Automatically generated by Pynguin.
import tornado.util as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'e-A>Z\nwM'
    dict_0 = {}
    object_dict_0 = module_0.ObjectDict(**dict_0)
    object_dict_0.__setattr__(str_0, str_0)
    timeout_error_0 = module_0.TimeoutError()

def test_case_2():
    gzip_decompressor_0 = module_0.GzipDecompressor()

def test_case_3():
    base_exception_0 = module_1.BaseException()
    optional_0 = module_0.errno_from_exception(base_exception_0)

def test_case_4():
    str_0 = '{[|hI\ra}Nl'
    str_1 = module_0.re_unescape(str_0)

def test_case_5():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    list_0 = [set_0]
    base_exception_0 = module_1.BaseException(*list_0)
    optional_0 = module_0.errno_from_exception(base_exception_0)

def test_case_6():
    int_0 = -27
    str_0 = 'hfo'
    str_1 = 'hi'
    str_2 = {str_0: str_0, str_0: str_0}
    var_0 = lambda *args, **kwargs: int_0
    arg_replacer_0 = module_0.ArgReplacer(var_0, str_1)
    tuple_0 = arg_replacer_0.replace(str_2, var_0, str_2)

def test_case_7():
    int_0 = 1
    str_0 = 'hfo'
    var_0 = [int_0, int_0, str_0]
    str_1 = 'zrg'
    str_2 = {str_0: str_1, str_1: str_1}
    var_1 = lambda *args, **kwargs: int_0
    arg_replacer_0 = module_0.ArgReplacer(var_1, str_1)
    tuple_0 = arg_replacer_0.replace(str_1, var_0, str_2)
    list_0 = [str_2, var_1]
    dict_0 = {str_0: list_0}
    any_0 = arg_replacer_0.get_old_value(int_0, dict_0)

def test_case_8():
    var_0 = lambda x: x
    str_0 = 'x'
    arg_replacer_0 = module_0.ArgReplacer(var_0, str_0)
    int_0 = 1
    int_1 = (int_0,)
    var_1 = {}
    any_0 = arg_replacer_0.get_old_value(int_1, var_1)
    var_2 = ()
    int_2 = 2
    int_3 = {str_0: int_2}
    any_1 = arg_replacer_0.get_old_value(var_2, int_3)
    var_3 = ()
    var_4 = {}
    any_2 = arg_replacer_0.get_old_value(var_3, var_4)
    var_5 = lambda x, y=2: x
    arg_replacer_1 = module_0.ArgReplacer(var_5, str_0)
    int_4 = (int_0,)
    var_6 = {}
    any_3 = arg_replacer_1.get_old_value(int_4, var_6)
    var_7 = ()
    int_5 = {str_0: int_2}
    any_4 = arg_replacer_1.get_old_value(var_7, int_5)
    var_8 = ()
    var_9 = {}
    any_5 = arg_replacer_1.get_old_value(var_8, var_9)
    var_10 = ()
    var_11 = {}
    any_6 = arg_replacer_1.get_old_value(var_10, var_11)
    str_1 = 'y'
    arg_replacer_2 = module_0.ArgReplacer(var_5, str_1)
    int_6 = (int_0,)
    var_12 = {}
    any_7 = arg_replacer_2.get_old_value(int_6, var_12)