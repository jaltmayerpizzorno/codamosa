# Automatically generated by Pynguin.
import tornado.util as module_0
import builtins as module_1

def test_case_0():
    try:
        object_dict_0 = module_0.ObjectDict()
        var_0 = object_dict_0.wrong
    except BaseException:
        pass

def test_case_1():
    try:
        gzip_decompressor_0 = module_0.GzipDecompressor()
        str_0 = '$jb3\nJ,1'
        object_dict_0 = module_0.ObjectDict()
        arg_replacer_0 = module_0.ArgReplacer(object_dict_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = b'F\r\xfe'
        bytes_1 = gzip_decompressor_0.decompress(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'J2EArd^s]cByaT6'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'urllib.missing_module'
        any_0 = module_0.import_object(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 2818.9205
        str_0 = 'q$'
        str_1 = 'U%>'
        str_2 = 'p'
        dict_0 = {str_0: float_0, str_1: str_1, str_2: float_0, str_2: str_1}
        str_3 = 'Dd+&w'
        module_0.exec_in(float_0, dict_0, str_3)
    except BaseException:
        pass

def test_case_6():
    try:
        list_0 = []
        base_exception_0 = module_1.BaseException(*list_0)
        object_dict_0 = module_0.ObjectDict()
        str_0 = 'A\tzXM\rf-\\KF_i/Z"\x0b'
        str_1 = module_0.re_unescape(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        configurable_0 = module_0.Configurable()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = None
        arg_replacer_0 = module_0.ArgReplacer(str_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        dict_0 = {}
        base_exception_0 = module_1.BaseException(**dict_0)
        optional_0 = module_0.errno_from_exception(base_exception_0)
        var_0 = module_0.timedelta_to_seconds(optional_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = "Qe'A\x0cLTD[K<"
        var_0 = module_0.raise_exc_info(str_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'urllib'
        base_exception_0 = module_1.BaseException()
        list_0 = [base_exception_0, str_0, base_exception_0]
        base_exception_1 = module_1.BaseException(*list_0)
        optional_0 = module_0.errno_from_exception(base_exception_1)
        str_1 = 'v?c(\rFl2^zo'
        any_0 = module_0.import_object(str_1)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        base_exception_0 = module_1.BaseException(*list_0)
        str_0 = '한국어'
        str_1 = '$jb3\nJ,1'
        dict_0 = {str_1: base_exception_0, str_0: list_0, str_1: str_0, str_0: base_exception_0}
        object_dict_0 = module_0.ObjectDict()
        gzip_decompressor_0 = module_0.GzipDecompressor()
        tuple_0 = (str_1, gzip_decompressor_0, dict_0)
        module_0.exec_in(str_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_13():
    try:
        base_exception_0 = module_1.BaseException()
        optional_0 = module_0.errno_from_exception(base_exception_0)
        str_0 = "ctIprrB\\'{6b}"
        str_1 = module_0.re_unescape(str_0)
        gzip_decompressor_0 = module_0.GzipDecompressor()
        bytes_0 = gzip_decompressor_0.flush()
        int_0 = 1102
        arg_replacer_0 = module_0.ArgReplacer(int_0, str_1)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'urllib'
        base_exception_0 = module_1.BaseException()
        optional_0 = module_0.errno_from_exception(base_exception_0)
        list_0 = [str_0, optional_0, base_exception_0]
        str_1 = '![\x0bFvq'
        object_dict_0 = module_0.ObjectDict()
        object_dict_0.__setattr__(str_1, list_0)
        var_0 = module_0.raise_exc_info(list_0)
    except BaseException:
        pass