# Automatically generated by Pynguin.
import tornado.util as module_0
import builtins as module_1

def test_case_0():
    try:
        str_0 = 'IX)Xs60{IFXfs;v5ta'
        object_dict_0 = module_0.ObjectDict()
        any_0 = object_dict_0.__getattr__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x99\x9aH\xbf\x1aX\tz\x04\x1a\xb6\x9a\x0f\xfaF\xff\xb3\x87'
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_1 = gzip_decompressor_0.decompress(bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = gzip_decompressor_0.flush()
        str_0 = 'tornado.test_utils'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '}63E9t10Znk  '
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 2
        base_exception_0 = module_1.BaseException()
        optional_0 = module_0.errno_from_exception(base_exception_0)
        str_0 = 'hello'
        var_0 = [int_0, int_0, str_0]
        str_1 = 'arg3'
        str_2 = 'arg4'
        str_3 = 'h7'
        str_4 = 'bye'
        str_5 = {str_1: str_3, str_2: str_4}
        var_1 = None
        var_2 = lambda *args, **kwargs: str_0
        str_6 = 'rg1'
        arg_replacer_0 = module_0.ArgReplacer(var_2, str_6)
        tuple_0 = ()
        str_7 = ';Fsqx=gf'
        int_1 = -1506
        str_8 = 'f,{3p'
        str_9 = "HeXm+CU\x0c'"
        dict_0 = {str_7: int_1, str_8: str_2, str_9: var_0}
        tuple_1 = arg_replacer_0.replace(tuple_0, str_6, dict_0)
        str_10 = 'new'
        tuple_2 = arg_replacer_0.replace(str_10, var_0, str_5)
        list_0 = [var_1, var_2]
        set_0 = None
        dict_1 = {str_3: str_6, str_0: str_7, str_2: set_0}
        module_0.exec_in(str_0, dict_1)
        dict_2 = {str_0: list_0}
        gzip_decompressor_0 = module_0.GzipDecompressor()
        str_11 = module_0.re_unescape(str_3)
        any_0 = arg_replacer_0.get_old_value(int_1, dict_2)
        any_1 = module_0.import_object(str_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\tJA76I;{R;GMdwK'
        str_1 = '9v>IH-#hA/lG\ny_'
        str_2 = 'B'
        dict_0 = {str_1: str_1, str_2: str_0}
        timeout_error_0 = module_0.TimeoutError()
        module_0.exec_in(str_0, dict_0, timeout_error_0)
    except BaseException:
        pass

def test_case_6():
    try:
        configurable_0 = None
        tuple_0 = (configurable_0,)
        gzip_decompressor_0 = module_0.GzipDecompressor()
        tuple_1 = (tuple_0, gzip_decompressor_0)
        var_0 = module_0.raise_exc_info(tuple_1)
    except BaseException:
        pass

def test_case_7():
    try:
        base_exception_0 = None
        optional_0 = module_0.errno_from_exception(base_exception_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'y$\\K{}g0<y'
        str_1 = module_0.re_unescape(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'i=b~;\\)B'
        str_1 = module_0.re_unescape(str_0)
        base_exception_0 = module_1.BaseException()
        optional_0 = module_0.errno_from_exception(base_exception_0)
        object_dict_0 = module_0.ObjectDict()
        arg_replacer_0 = module_0.ArgReplacer(object_dict_0, str_1)
    except BaseException:
        pass

def test_case_10():
    try:
        var_0 = module_0.doctests()
        list_0 = [var_0]
        str_0 = "O_s|*QA?~,')p&Cm"
        dict_0 = {str_0: var_0}
        configurable_0 = module_0.Configurable(*list_0, **dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '0'
        int_0 = 1973
        arg_replacer_0 = module_0.ArgReplacer(int_0, str_0)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'{k\xcdX'
        var_0 = module_0.timedelta_to_seconds(bytes_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\x97g\xa9\xc3\x132|-\x04\x10b~\xaf\xd1C\xa3\x97j@'
        str_0 = '8whH>;+2e9=/RRaex76'
        dict_0 = {str_0: bytes_0, str_0: bytes_0}
        complex_0 = None
        module_0.exec_in(bytes_0, dict_0, complex_0)
    except BaseException:
        pass

def test_case_14():
    try:
        configurable_0 = None
        gzip_decompressor_0 = module_0.GzipDecompressor()
        list_0 = [configurable_0, configurable_0, gzip_decompressor_0, gzip_decompressor_0]
        var_0 = module_0.raise_exc_info(list_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'a.b.c.d'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'tornado.test_utils'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        int_0 = 2
        str_0 = 'arg3'
        str_1 = 'arg4'
        str_2 = 'h7'
        str_3 = 'bye'
        str_4 = {str_0: str_2, str_1: str_3}
        var_0 = lambda *args, **kwargs: int_0
        object_dict_0 = module_0.ObjectDict()
        any_0 = object_dict_0.__getattr__(str_4)
    except BaseException:
        pass