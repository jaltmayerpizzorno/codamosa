# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    var_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(var_0, bool_0)

def test_case_2():
    str_0 = 'e&\r9-9L-\' ER"k"pt$'
    bool_0 = False
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_3():
    object_0 = module_1.object()
    set_0 = set()
    bool_0 = True
    maybe_0 = module_0.Maybe(set_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)

def test_case_4():
    dict_0 = {}
    int_0 = 800
    bool_0 = True
    maybe_0 = module_0.Maybe(int_0, bool_0)
    var_0 = maybe_0.bind(dict_0)

def test_case_5():
    str_0 = ' '
    tuple_0 = (str_0,)
    bool_0 = True
    maybe_0 = module_0.Maybe(tuple_0, bool_0)
    var_0 = maybe_0.to_box()
    callable_0 = None
    var_1 = maybe_0.map(callable_0)
    var_2 = maybe_0.to_either()

def test_case_6():
    bytes_0 = b'\xf4W'
    str_0 = 'sADznNj,[_'
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.ap(bytes_0)

def test_case_7():
    str_0 = ')lZ'
    dict_0 = {str_0: str_0, str_0: str_0}
    float_0 = -247.14774
    bool_0 = True
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.filter(dict_0)

def test_case_8():
    str_0 = '\n        Transform Validation to Either.\n\n        :returns: Right monad with previous value when Validation has no errors, in other case Left with errors list\n        :rtype: Right[A] | Left[E]\n        '
    str_1 = 'ED&73u${OOX}ZW2r_'
    str_2 = 'gqy(3j'
    dict_0 = {str_0: str_0, str_1: str_0, str_2: str_2, str_0: str_0}
    bool_0 = False
    maybe_0 = module_0.Maybe(dict_0, bool_0)
    var_0 = maybe_0.to_either()
    object_0 = module_1.object()
    dict_1 = {}
    bool_1 = True
    maybe_1 = module_0.Maybe(dict_1, bool_1)
    var_1 = maybe_1.filter(object_0)
    bool_2 = True
    maybe_2 = module_0.Maybe(object_0, bool_2)
    var_2 = maybe_0.to_either()
    list_0 = [dict_0, dict_0]
    var_3 = maybe_0.get_or_else(list_0)
    var_4 = maybe_1.to_box()
    var_5 = maybe_2.to_box()

def test_case_9():
    str_0 = 'TAbD:'
    object_0 = module_1.object()
    tuple_0 = (str_0, object_0)
    float_0 = -3559.67
    bool_0 = True
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.get_or_else(tuple_0)
    maybe_1 = module_0.Maybe(bool_0, bool_0)
    var_1 = maybe_1.get_or_else(bool_0)

def test_case_10():
    bytes_0 = b'\xfb\x1e\xdf\xef\xa8'
    bool_0 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    list_0 = None
    var_0 = maybe_0.map(list_0)
    var_1 = maybe_0.to_box()
    var_2 = maybe_0.to_lazy()
    str_0 = '!X'
    bool_1 = False
    var_3 = None
    var_4 = maybe_0.get_or_else(var_3)
    maybe_1 = module_0.Maybe(str_0, bool_1)
    var_5 = maybe_1.to_try()

def test_case_11():
    bytes_0 = b'f]\r\xfbc\x04z+K\x04\xe8\xaf\xf3\xe7'
    bool_0 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_12():
    list_0 = []
    object_0 = module_1.object(*list_0)
    bytes_0 = b'/\x80\xf0y\x0f\x19\xe1\x9d'
    bool_0 = False
    var_0 = None
    bool_1 = False
    maybe_0 = module_0.Maybe(var_0, bool_1)
    maybe_1 = module_0.Maybe(bytes_0, bool_0)
    var_1 = maybe_1.to_validation()
    bool_2 = maybe_1.__eq__(object_0)
    var_2 = maybe_1.to_validation()

def test_case_13():
    int_0 = 1
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    maybe_1 = module_0.Maybe(int_0, bool_0)
    var_0 = maybe_0 == maybe_1
    maybe_2 = module_0.Maybe(int_0, bool_0)
    int_1 = 2
    maybe_3 = module_0.Maybe(int_1, bool_0)
    var_1 = maybe_2 == maybe_3
    maybe_4 = module_0.Maybe(int_0, bool_0)
    bool_1 = True
    maybe_5 = module_0.Maybe(bool_1, bool_1)
    var_2 = maybe_4 == maybe_5
    bool_2 = True
    maybe_6 = module_0.Maybe(bool_1, bool_2)
    bool_3 = True
    maybe_7 = module_0.Maybe(int_1, bool_3)
    var_3 = maybe_6 == maybe_7
    bool_4 = True
    maybe_8 = module_0.Maybe(bool_3, bool_4)
    maybe_9 = module_0.Maybe(bool_4, bool_0)
    var_4 = maybe_8 == maybe_9
    maybe_10 = module_0.Maybe(bool_4, bool_0)
    bool_5 = True
    maybe_11 = module_0.Maybe(int_1, bool_5)
    var_5 = maybe_10 == maybe_11