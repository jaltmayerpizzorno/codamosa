# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)

def test_case_2():
    bool_0 = False
    maybe_0 = module_0.Maybe(bool_0, bool_0)

def test_case_3():
    bool_0 = False
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    object_0 = module_1.object()
    bool_1 = maybe_0.__eq__(object_0)

def test_case_4():
    str_0 = '\n        Applies the function inside the Lazy[A] structure to another applicative type for notempty Lazy.\n        For empty returns copy of itself\n\n        :param applicative: applicative contains function\n        :type applicative: Lazy[Function(A) -> B]\n        :returns: new Lazy with result of contains function\n        :rtype: Lazy[B]\n        '
    object_0 = module_1.object()
    bool_0 = True
    maybe_0 = module_0.Maybe(object_0, bool_0)
    var_0 = maybe_0.ap(str_0)

def test_case_5():
    str_0 = '<*j<\x0bAY*sjYx'
    str_1 = '0H](n'
    dict_0 = {str_0: str_0, str_1: str_1, str_1: str_0, str_0: str_1}
    bool_0 = True
    callable_0 = None
    list_0 = []
    maybe_0 = module_0.Maybe(list_0, bool_0)
    var_0 = maybe_0.map(callable_0)
    maybe_1 = module_0.Maybe(dict_0, bool_0)
    var_1 = maybe_1.to_lazy()
    callable_1 = None
    var_2 = maybe_1.to_lazy()
    var_3 = maybe_1.bind(callable_1)

def test_case_6():
    str_0 = 'Ke.S@\rY<RfDt'
    set_0 = set()
    bool_0 = True
    maybe_0 = module_0.Maybe(set_0, bool_0)
    var_0 = maybe_0.bind(str_0)

def test_case_7():
    str_0 = 'Y}>tSS'
    dict_0 = {str_0: str_0, str_0: str_0}
    bool_0 = True
    maybe_0 = module_0.Maybe(dict_0, bool_0)
    var_0 = None
    var_1 = maybe_0.filter(var_0)
    var_2 = maybe_0.to_box()

def test_case_8():
    list_0 = None
    bool_0 = False
    bool_1 = True
    maybe_0 = module_0.Maybe(bool_0, bool_1)
    var_0 = maybe_0.get_or_else(list_0)

def test_case_9():
    list_0 = []
    object_0 = module_1.object()
    bool_0 = False
    maybe_0 = module_0.Maybe(object_0, bool_0)
    var_0 = maybe_0.to_either()
    str_0 = '\nsd*"p?2\r,-t:e'
    bool_1 = False
    maybe_1 = module_0.Maybe(str_0, bool_1)
    bool_2 = maybe_1.__eq__(object_0)
    bool_3 = True
    maybe_2 = module_0.Maybe(list_0, bool_3)

def test_case_10():
    bytes_0 = b'\xb7\xa9'
    bool_0 = False
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    var_0 = maybe_0.to_box()

def test_case_11():
    bytes_0 = b'\xb7\xa9'
    bool_0 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    var_0 = maybe_0.to_box()

def test_case_12():
    str_0 = ''
    bool_0 = False
    object_0 = None
    int_0 = -703
    maybe_0 = module_0.Maybe(int_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)
    maybe_1 = module_0.Maybe(str_0, bool_0)
    bool_2 = False
    maybe_2 = module_0.Maybe(bool_2, bool_0)
    var_0 = maybe_2.to_either()
    var_1 = maybe_2.to_lazy()
    var_2 = maybe_2.to_either()

def test_case_13():
    bytes_0 = b'o,`}\x83\xb6\xb0Y|\xca7\xcb\x85\xda;\x02n'
    bool_0 = True
    float_0 = -1198.423537
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.to_lazy()
    maybe_1 = module_0.Maybe(bytes_0, bool_0)
    var_1 = maybe_1.to_box()
    var_2 = maybe_1.to_lazy()
    var_3 = maybe_1.to_try()
    var_4 = maybe_1.to_try()
    var_5 = maybe_1.to_validation()

def test_case_14():
    str_0 = 't6jq9LqS'
    str_1 = '\n        Transform Maybe to Try.\n\n        :returns: successfully Try with previous value when Maybe is not empty, othercase not successfully Try with None\n        :rtype: Try[A]\n        '
    dict_0 = {str_0: str_0, str_1: str_0, str_1: str_0}
    bool_0 = False
    maybe_0 = module_0.Maybe(dict_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_15():
    float_0 = -2869.42
    bool_0 = True
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.to_try()
    bool_1 = False
    var_1 = maybe_0.get_or_else(bool_1)
    bytes_0 = b'\x17\x8ako\xc2\x05\xa3P\xd6\x19\x91'
    var_2 = maybe_0.bind(bytes_0)
    var_3 = None
    var_4 = maybe_0.get_or_else(var_3)

def test_case_16():
    int_0 = 1
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    maybe_1 = module_0.Maybe(int_0, bool_0)
    maybe_2 = module_0.Maybe(int_0, bool_0)
    var_0 = maybe_1 == maybe_2
    int_1 = 2
    maybe_3 = module_0.Maybe(int_1, bool_0)
    var_1 = maybe_0 != maybe_3
    bool_1 = True
    maybe_4 = module_0.Maybe(int_0, bool_1)
    var_2 = maybe_0 != maybe_4
    maybe_5 = module_0.Maybe(bool_1, bool_0)
    var_3 = maybe_0 == maybe_5
    maybe_6 = module_0.Maybe(bool_1, bool_0)
    bool_2 = True
    maybe_7 = module_0.Maybe(bool_1, bool_2)