# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    set_0 = {bool_0, bool_0}
    maybe_0 = module_0.Maybe(set_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_2():
    bool_0 = True
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    maybe_1 = module_0.Maybe(bool_0, bool_1)
    bool_2 = maybe_0.__eq__(maybe_1)
    maybe_2 = module_0.Maybe(bool_0, bool_1)
    maybe_3 = module_0.Maybe(bool_1, bool_1)
    bool_3 = maybe_2.__eq__(maybe_3)

def test_case_3():
    bool_0 = False
    bool_1 = True
    bool_2 = True
    maybe_0 = module_0.Maybe(bool_1, bool_2)
    callable_0 = None
    var_0 = maybe_0.bind(callable_0)
    var_1 = maybe_0.ap(bool_0)
    var_2 = maybe_0.to_lazy()

def test_case_4():
    int_0 = 864
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
    bool_0 = False
    bool_1 = True
    bytes_0 = b'\xa2\xab\xb0\xfc\xc2\xe5\xce;\x11\x14\xe7:\x08\xe2\xa1J'
    float_0 = 903.1737
    maybe_0 = module_0.Maybe(float_0, bool_1)
    var_0 = maybe_0.map(bytes_0)
    maybe_1 = module_0.Maybe(bool_0, bool_1)
    var_1 = maybe_1.ap(dict_0)

def test_case_5():
    bool_0 = True
    bool_1 = False
    str_0 = '<"kW:U'
    bytes_0 = b'7\x82\xea\x82\x88\xb2\x90z\xcfs\x9aU\xabu\x9a\xc4\x17\xd4\xcd'
    bool_2 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_2)
    var_0 = maybe_0.filter(str_0)
    maybe_1 = module_0.Maybe(bool_0, bool_1)
    maybe_2 = module_0.Maybe(bool_0, bool_1)
    bool_3 = maybe_1.__eq__(maybe_2)
    var_1 = None
    var_2 = maybe_1.get_or_else(var_1)
    maybe_3 = module_0.Maybe(bool_0, bool_1)
    var_3 = maybe_0.to_validation()
    maybe_4 = module_0.Maybe(bool_1, bool_1)
    bool_4 = maybe_3.__eq__(maybe_4)

def test_case_6():
    list_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(list_0, bool_0)
    list_1 = []
    bool_1 = None
    callable_0 = None
    bytes_0 = b'\xb9\xf2\x11R\xe9\xbb\x00\x8a\x02\t\x04\xf6\xea'
    float_0 = -290.3228
    bool_2 = True
    maybe_1 = module_0.Maybe(float_0, bool_2)
    var_0 = maybe_1.bind(bytes_0)
    dict_0 = {bool_1: bool_1}
    bool_3 = True
    maybe_2 = module_0.Maybe(dict_0, bool_3)
    var_1 = maybe_2.map(callable_0)
    maybe_3 = module_0.Maybe(list_1, bool_1)
    var_2 = maybe_3.to_either()

def test_case_7():
    object_0 = module_1.object()
    float_0 = -571.95
    bool_0 = True
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    var_0 = maybe_0.to_lazy()
    bytes_0 = b'D\xbf\x073'
    bytes_1 = b'zO\x10%\xfc\xa4\xe3'
    dict_0 = {}
    str_0 = 'Lt[_"\x0cXIpeu>:$yZ,Q#'
    str_1 = 'I@H}OA'
    dict_1 = {str_0: dict_0, str_0: bool_0, str_0: float_0, str_1: str_1}
    tuple_0 = (bytes_1, dict_0, dict_1)
    maybe_1 = module_0.Maybe(tuple_0, bool_0)
    var_1 = maybe_1.ap(bytes_0)
    maybe_2 = module_0.Maybe(float_0, bool_0)
    maybe_3 = module_0.Maybe(tuple_0, bool_0)
    var_2 = maybe_3.ap(bool_1)
    bool_2 = maybe_2.__eq__(object_0)

def test_case_8():
    var_0 = None
    list_0 = [var_0]
    bool_0 = False
    maybe_0 = module_0.Maybe(list_0, bool_0)
    bool_1 = True
    maybe_1 = module_0.Maybe(maybe_0, bool_1)
    var_1 = maybe_1.to_lazy()

def test_case_9():
    maybe_0 = None
    int_0 = -2582
    list_0 = [int_0, int_0, int_0, int_0]
    bool_0 = True
    tuple_0 = (list_0, bool_0)
    maybe_1 = module_0.Maybe(tuple_0, bool_0)
    var_0 = maybe_1.filter(maybe_0)
    set_0 = None
    var_1 = maybe_1.ap(set_0)
    str_0 = '4>Bk\tP'
    str_1 = 'Qs-v^\\'
    bool_1 = True
    maybe_2 = module_0.Maybe(str_1, bool_1)
    var_2 = maybe_2.to_lazy()
    var_3 = maybe_2.to_validation()
    var_4 = maybe_2.to_either()
    var_5 = maybe_2.ap(str_0)

def test_case_10():
    object_0 = module_1.object()
    bool_0 = False
    bool_1 = True
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    str_0 = 'tZ.)8%#\x0cqc$t~ka}_a'
    list_0 = [maybe_0, bool_1, str_0, bool_0]
    list_1 = [list_0, list_0, bool_1]
    bool_2 = True
    maybe_1 = module_0.Maybe(list_1, bool_2)
    bool_3 = maybe_1.__eq__(object_0)

def test_case_11():
    bool_0 = True
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    maybe_1 = module_0.Maybe(bool_0, bool_1)
    bool_2 = maybe_0.__eq__(maybe_1)
    maybe_2 = module_0.Maybe(bool_0, bool_1)
    var_0 = None
    maybe_3 = module_0.Maybe(var_0, bool_0)
    maybe_4 = module_0.Maybe(var_0, bool_0)
    bool_3 = maybe_3.__eq__(maybe_4)
    maybe_5 = module_0.Maybe(bool_0, bool_1)

def test_case_12():
    bool_0 = True
    bool_1 = False
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    maybe_1 = module_0.Maybe(bool_0, bool_1)
    bool_2 = maybe_0.__eq__(maybe_1)
    maybe_2 = module_0.Maybe(bool_0, bool_1)
    maybe_3 = module_0.Maybe(bool_1, bool_1)
    bool_3 = maybe_2.__eq__(maybe_3)
    var_0 = None
    maybe_4 = module_0.Maybe(var_0, bool_0)
    bool_4 = maybe_1.__eq__(maybe_4)
    maybe_5 = module_0.Maybe(bool_0, bool_1)