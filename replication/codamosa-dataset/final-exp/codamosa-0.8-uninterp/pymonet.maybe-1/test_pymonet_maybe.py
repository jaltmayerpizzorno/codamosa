# Automatically generated by Pynguin.
import pymonet.maybe as module_0
import builtins as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = -2006.10511
    bool_0 = False
    maybe_0 = module_0.Maybe(float_0, bool_0)

def test_case_2():
    object_0 = module_1.object()
    bool_0 = True
    maybe_0 = module_0.Maybe(bool_0, bool_0)
    bool_1 = maybe_0.__eq__(object_0)

def test_case_3():
    float_0 = -1886.4615
    bool_0 = True
    maybe_0 = module_0.Maybe(float_0, bool_0)
    list_0 = [maybe_0]
    var_0 = maybe_0.bind(list_0)
    var_1 = maybe_0.to_try()

def test_case_4():
    var_0 = None
    bool_0 = False
    maybe_0 = module_0.Maybe(var_0, bool_0)
    tuple_0 = ()
    bool_1 = True
    maybe_1 = module_0.Maybe(tuple_0, bool_1)
    var_1 = maybe_1.map(maybe_0)

def test_case_5():
    int_0 = -1906
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    float_0 = 94.0
    bool_1 = True
    maybe_1 = module_0.Maybe(float_0, bool_1)
    var_0 = maybe_1.ap(maybe_0)
    str_0 = 'aPU"P%\r'
    str_1 = "Yd'\nG"
    str_2 = '%D0Kks'
    dict_0 = {str_0: str_0, str_1: str_1, str_2: str_1}
    bool_2 = True
    maybe_2 = module_0.Maybe(dict_0, bool_2)
    var_1 = maybe_2.to_box()

def test_case_6():
    dict_0 = {}
    str_0 = '[Qx'
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    var_0 = maybe_0.filter(dict_0)
    int_0 = 943
    list_0 = [maybe_0]
    bool_1 = False
    maybe_1 = module_0.Maybe(list_0, bool_1)
    var_1 = maybe_1.get_or_else(int_0)

def test_case_7():
    float_0 = 2142.38
    var_0 = None
    list_0 = [float_0]
    bool_0 = True
    object_0 = module_1.object()
    float_1 = 1050.3728
    bool_1 = True
    maybe_0 = module_0.Maybe(float_1, bool_1)
    bool_2 = maybe_0.__eq__(object_0)
    maybe_1 = module_0.Maybe(list_0, bool_0)
    var_1 = maybe_1.get_or_else(var_0)
    bool_3 = True
    maybe_2 = module_0.Maybe(float_0, bool_3)
    var_2 = maybe_2.to_validation()

def test_case_8():
    str_0 = ''
    bool_0 = True
    maybe_0 = module_0.Maybe(str_0, bool_0)
    object_0 = module_1.object()
    bool_1 = maybe_0.__eq__(object_0)
    var_0 = maybe_0.to_either()

def test_case_9():
    dict_0 = {}
    float_0 = 2353.13
    bool_0 = False
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.to_try()
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    float_1 = 1572.8338
    tuple_0 = (list_0, float_1)
    bool_1 = True
    maybe_1 = module_0.Maybe(tuple_0, bool_1)
    var_1 = maybe_1.to_either()
    bool_2 = True
    bool_3 = False
    var_2 = maybe_1.to_validation()
    maybe_2 = module_0.Maybe(bool_2, bool_3)
    var_3 = maybe_2.to_lazy()

def test_case_10():
    str_0 = "JJ<>s[7oFP7`>R\rN'sL"
    bytes_0 = b'\xdc'
    bool_0 = True
    maybe_0 = module_0.Maybe(bytes_0, bool_0)
    var_0 = maybe_0.to_lazy()
    set_0 = {str_0, str_0, str_0}
    bool_1 = False
    var_1 = maybe_0.to_either()
    maybe_1 = module_0.Maybe(set_0, bool_1)
    bool_2 = True
    var_2 = maybe_0.filter(bool_2)
    var_3 = maybe_1.to_either()
    str_1 = '2X\x0c,Tq@OSq8XM'
    bool_3 = False
    maybe_2 = module_0.Maybe(str_1, bool_3)
    var_4 = maybe_2.to_validation()

def test_case_11():
    float_0 = -2006.10511
    bool_0 = False
    maybe_0 = module_0.Maybe(float_0, bool_0)
    var_0 = maybe_0.to_try()

def test_case_12():
    list_0 = []
    object_0 = module_1.object(*list_0)
    bytes_0 = b'\x10\x95\x92Di\x930K\x82\x96\x83s\x8c^'
    tuple_0 = (list_0, object_0, list_0, bytes_0)
    bool_0 = False
    maybe_0 = module_0.Maybe(tuple_0, bool_0)
    var_0 = maybe_0.to_validation()

def test_case_13():
    complex_0 = None
    bool_0 = True
    maybe_0 = module_0.Maybe(complex_0, bool_0)
    var_0 = maybe_0.to_validation()

def test_case_14():
    int_0 = 5
    bool_0 = False
    maybe_0 = module_0.Maybe(int_0, bool_0)
    maybe_1 = module_0.Maybe(int_0, bool_0)
    maybe_2 = module_0.Maybe(int_0, bool_0)
    var_0 = None
    maybe_3 = module_0.Maybe(var_0, bool_0)
    var_1 = maybe_2 == maybe_3
    maybe_4 = module_0.Maybe(int_0, bool_0)
    bool_1 = True
    maybe_5 = module_0.Maybe(int_0, bool_1)
    var_2 = maybe_4 == maybe_5
    maybe_6 = module_0.Maybe(var_0, bool_1)
    maybe_7 = module_0.Maybe(var_0, bool_1)
    maybe_8 = module_0.Maybe(var_0, bool_1)
    maybe_9 = module_0.Maybe(var_0, bool_0)
    var_3 = maybe_8 == maybe_9

def test_case_15():
    int_0 = 5
    bool_0 = True
    maybe_0 = module_0.Maybe(int_0, bool_0)
    maybe_1 = module_0.Maybe(int_0, bool_0)
    maybe_2 = module_0.Maybe(int_0, bool_0)
    var_0 = None
    maybe_3 = module_0.Maybe(var_0, bool_0)
    var_1 = maybe_2 == maybe_3
    maybe_4 = module_0.Maybe(int_0, bool_0)
    bool_1 = False
    maybe_5 = module_0.Maybe(int_0, bool_1)
    var_2 = maybe_4 == maybe_5
    maybe_6 = module_0.Maybe(var_0, bool_1)
    maybe_7 = module_0.Maybe(var_0, bool_1)
    maybe_8 = module_0.Maybe(var_0, bool_1)
    maybe_9 = module_0.Maybe(var_0, bool_0)
    var_3 = maybe_8 == maybe_9