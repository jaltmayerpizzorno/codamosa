# Automatically generated by Pynguin.
import tornado.util as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    object_dict_0 = module_0.ObjectDict()
    str_0 = 'o\x0b}*\x0bI@#Q9jeCOhZ'
    object_dict_0.__setattr__(str_0, str_0)

def test_case_2():
    gzip_decompressor_0 = module_0.GzipDecompressor()

def test_case_3():
    base_exception_0 = module_1.BaseException()
    optional_0 = module_0.errno_from_exception(base_exception_0)

def test_case_4():
    object_dict_0 = module_0.ObjectDict()
    list_0 = [object_dict_0, object_dict_0, object_dict_0]
    base_exception_0 = module_1.BaseException(*list_0)
    optional_0 = module_0.errno_from_exception(base_exception_0)

def test_case_5():
    base_exception_0 = module_1.BaseException()
    optional_0 = module_0.errno_from_exception(base_exception_0)
    var_0 = module_0.doctests()