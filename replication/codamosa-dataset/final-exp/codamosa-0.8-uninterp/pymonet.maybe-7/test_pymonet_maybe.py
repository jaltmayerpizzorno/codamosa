# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Vpfo:v$BUl".)x!'
    bool_0 = False
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.to_validation()

def test_case_2():
    object_0 = module_1.object()
    int_0 = 936
    bool_0 = True
    maybe_0 = module_0.Maybe(int_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)

def test_case_3():
    object_0 = module_1.object()
    float_0 = 1817.57
    bool_0 = True
    set_0 = {object_0}
    bytes_0 = b'\xfa\xa0'
    bool_1 = False
    maybe_0 = module_0.Maybe(bytes_0, bool_1)
    maybe_1 = module_0.Maybe(maybe_0, bool_0)
    var_0 = maybe_1.map(set_0)
    maybe_2 = module_0.Maybe(float_0, bool_0)
    var_1 = maybe_2.to_box()
    object_1 = module_1.object()
    bool_2 = maybe_2.__eq__(object_0)
    callable_0 = None
    var_2 = maybe_1.filter(callable_0)

def test_case_4():
    float_0 = 3653.795
    str_0 = '\n        If Maybe is empty return new empty Maybe, in other case\n        takes mapper function and returns result of mapper.\n\n        :param mapper: function to call with Maybe.value\n        :type mapper: Function(A) -> Maybe[B]\n        :returns: Maybe[B | None]\n        '
    object_0 = module_1.object()
    object_1 = module_1.object()
    bool_0 = True
    maybe_0 = module_0.Maybe(object_1, bool_0)
    maybe_1 = module_0.Maybe(maybe_0, bool_0)
    bool_1 = maybe_1.__eq__(object_0)
    bool_2 = True
    maybe_2 = module_0.Maybe(str_0, bool_2)
    var_0 = maybe_2.bind(float_0)

def test_case_5():
    float_0 = -1833.02557
    int_0 = -752
    bool_0 = True
    maybe_0 = module_0.Maybe(int_0, bool_0)
    var_0 = maybe_0.ap(float_0)
    str_0 = 'h<"F{/{?Sy\'vj4,/A6\n'
    bool_1 = False
    maybe_1 = module_0.Maybe(str_0, bool_1)
    var_1 = maybe_1.to_lazy()
    var_2 = maybe_1.to_lazy()

def test_case_6():
    var_0 = None
    list_0 = []
    float_0 = -3988.354711610684
    bool_0 = False
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_1 = maybe_0.to_lazy()
    object_0 = module_1.object()
    maybe_1 = module_0.Maybe(object_0, bool_0)
    var_2 = maybe_1.to_lazy()
    bool_1 = False
    maybe_2 = module_0.Maybe(list_0, bool_1)
    object_1 = module_1.object()
    bool_2 = maybe_2.__eq__(object_1)
    var_3 = maybe_2.get_or_else(var_0)

def test_case_7():
    object_0 = module_1.object()
    float_0 = 1817.57
    bool_0 = True
    set_0 = {object_0}
    bytes_0 = b'\xfa\xa0'
    bool_1 = False
    maybe_0 = module_0.Maybe(bytes_0, bool_1)
    maybe_1 = module_0.Maybe(maybe_0, bool_0)
    var_0 = maybe_1.map(set_0)
    maybe_2 = module_0.Maybe(float_0, bool_0)
    var_1 = maybe_2.to_box()
    int_0 = -3392
    bool_2 = True
    maybe_3 = module_0.Maybe(int_0, bool_2)
    object_1 = module_1.object()
    bool_3 = maybe_2.__eq__(object_0)
    var_2 = None
    var_3 = maybe_1.get_or_else(var_2)

def test_case_8():
    object_0 = module_1.object()
    float_0 = 1817.57
    bool_0 = True
    set_0 = {object_0}
    bytes_0 = b'\xfa\xa0'
    bool_1 = False
    maybe_0 = module_0.Maybe(bytes_0, bool_1)
    maybe_1 = module_0.Maybe(maybe_0, bool_0)
    var_0 = maybe_1.map(set_0)
    maybe_2 = module_0.Maybe(float_0, bool_0)
    var_1 = maybe_2.to_box()
    bool_2 = True
    maybe_3 = module_0.Maybe(object_0, bool_2)
    var_2 = maybe_2.to_try()
    bool_3 = True
    var_3 = maybe_3.to_validation()
    var_4 = maybe_3.map(object_0)
    maybe_4 = module_0.Maybe(maybe_3, bool_3)
    var_5 = maybe_4.to_either()

def test_case_9():
    int_0 = -751
    list_0 = [int_0, int_0, int_0]
    bool_0 = False
    maybe_0 = module_0.Maybe(list_0, bool_0)
    var_0 = maybe_0.to_box()
    bool_1 = True
    maybe_1 = module_0.Maybe(int_0, bool_1)
    var_1 = maybe_1.to_either()
    str_0 = None
    str_1 = '%y\r+Rs\x0ct5?xPshx,OO'
    dict_0 = {str_0: str_0, str_1: var_1}
    var_2 = maybe_1.filter(dict_0)
    str_2 = 'O%'
    callable_0 = None
    var_3 = maybe_1.map(callable_0)
    dict_1 = {str_2: int_0}
    var_4 = None
    var_5 = maybe_1.get_or_else(var_4)
    var_6 = maybe_1.get_or_else(var_4)
    var_7 = maybe_1.bind(dict_1)

def test_case_10():
    str_0 = 'O(M[9,%gX\rc|gG3'
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.to_box()
    object_0 = module_1.object()
    bool_1 = maybe_0.__eq__(object_0)

def test_case_11():
    str_0 = None
    str_1 = '[~x  BcIz'
    dict_0 = {str_0: str_0, str_0: str_0, str_1: str_1, str_0: str_0}
    bool_0 = True
    maybe_0 = module_0.Maybe(dict_0, bool_0)