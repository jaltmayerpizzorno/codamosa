# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    try_0 = module_0.Try(bool_0, bool_0)

def test_case_2():
    float_0 = -4753.2281
    bool_0 = True
    try_0 = module_0.Try(float_0, bool_0)
    float_1 = 1618.2837
    bool_1 = True
    try_1 = module_0.Try(float_1, bool_1)
    var_0 = try_1.get_or_else(try_0)
    float_2 = -2212.3
    bool_2 = True
    list_0 = []
    bool_3 = True
    try_2 = module_0.Try(list_0, bool_3)
    var_1 = try_2.on_fail(bool_2)
    set_0 = {float_2, float_2}
    bool_4 = True
    tuple_0 = ()
    try_3 = module_0.Try(tuple_0, bool_4)
    try_4 = module_0.Try(set_0, bool_4)
    int_0 = -2678
    str_0 = "w+~H_ud+Ayw'\x0bw(}k$"
    tuple_1 = (int_0, str_0)
    list_1 = [tuple_1]
    list_2 = [list_1, list_1, int_0]
    bool_5 = False
    try_5 = module_0.Try(list_2, bool_5)
    bool_6 = try_5.__eq__(try_4)
    bool_7 = try_2.__eq__(set_0)
    var_2 = try_2.get_or_else(bool_5)
    int_1 = False
    try_6 = module_0.Try(int_1, bool_3)

def test_case_3():
    int_0 = 1478
    bytes_0 = b'\xa2\x07\xa8*\x03\x06\xd2F\xfdtw\xc0Q\xc0\xfb;'
    bool_0 = False
    try_0 = module_0.Try(bytes_0, bool_0)
    bool_1 = True
    try_1 = module_0.Try(try_0, bool_1)
    bool_2 = try_1.__eq__(int_0)

def test_case_4():
    str_0 = 'a#e{x1O0\r~dx-\x0b&Wq@!r'
    float_0 = -2400.3
    bool_0 = False
    try_0 = module_0.Try(float_0, bool_0)
    str_1 = try_0.__str__()
    set_0 = {str_0}
    bool_1 = True
    try_1 = module_0.Try(set_0, bool_1)
    str_2 = try_1.__str__()

def test_case_5():
    bytes_0 = b'-6\x9c\xa0\x1fz0\x88w\x8c\x81'
    int_0 = -2534
    bool_0 = False
    try_0 = module_0.Try(int_0, bool_0)
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: try_0}
    list_0 = [bytes_0, bytes_0, dict_0]
    bool_1 = False
    bool_2 = True
    float_0 = -1268.618
    var_0 = try_0.on_success(float_0)
    tuple_0 = (list_0, bool_1, bool_2)
    bool_3 = True
    try_1 = module_0.Try(tuple_0, bool_3)
    bool_4 = True
    try_2 = module_0.Try(bytes_0, bool_4)
    str_0 = try_2.__str__()

def test_case_6():
    str_0 = 'eb}|c5 "=YV'
    str_1 = '~\x0cr-zAm6I{eX1[R5~'
    list_0 = [str_1]
    bool_0 = True
    try_0 = module_0.Try(list_0, bool_0)
    var_0 = try_0.on_fail(str_0)

def test_case_7():
    float_0 = -519.33549
    str_0 = '\n        :param constructor_fn: function to call during fold method call\n        :type constructor_fn: Function() -> A\n        '
    bool_0 = False
    try_0 = module_0.Try(str_0, bool_0)
    var_0 = try_0.filter(float_0)

def test_case_8():
    str_0 = "Yv&<IH,=fL/7A'T}[%x&"
    bool_0 = True
    try_0 = module_0.Try(str_0, bool_0)
    var_0 = try_0.get()

def test_case_9():
    int_0 = -583
    float_0 = 1646.46
    set_0 = None
    bool_0 = True
    bool_1 = False
    try_0 = module_0.Try(bool_0, bool_1)
    var_0 = try_0.filter(set_0)
    int_1 = -1678
    tuple_0 = ()
    try_1 = module_0.Try(tuple_0, bool_1)
    bool_2 = try_1.__eq__(int_1)
    bool_3 = False
    try_2 = module_0.Try(bool_3, bool_3)
    var_1 = try_2.map(float_0)
    bytes_0 = b'\xce?'
    var_2 = try_2.map(bytes_0)
    bytes_1 = b'\x16\x19'
    bool_4 = True
    try_3 = module_0.Try(bytes_1, bool_4)
    str_0 = try_3.__str__()
    var_3 = try_3.get_or_else(bytes_0)
    bool_5 = False
    try_4 = module_0.Try(float_0, bool_5)
    str_1 = '\n        Transform Either to Try.\n\n        :returns: resolved Try monad with previous value. Right is resolved successfully, Left not.\n        :rtype: Box[A]\n        '
    str_2 = try_2.__str__()
    var_4 = try_1.bind(str_1)
    var_5 = try_4.get_or_else(int_0)