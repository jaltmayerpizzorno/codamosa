# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    bool_0 = True
    try_0 = module_0.Try(bool_0, bool_0)

def test_case_1():
    int_0 = None
    str_0 = '-&u187vS'
    bool_0 = False
    try_0 = module_0.Try(str_0, bool_0)
    bool_1 = try_0.__eq__(int_0)

def test_case_2():
    list_0 = []
    bool_0 = True
    try_0 = module_0.Try(list_0, bool_0)
    str_0 = try_0.__str__()

def test_case_3():
    float_0 = -323.655256
    float_1 = -2454.57
    bool_0 = False
    try_0 = module_0.Try(float_1, bool_0)
    var_0 = try_0.map(float_0)

def test_case_4():
    str_0 = 'UEn{oi\x0c1^'
    float_0 = 1184.64906
    bool_0 = False
    try_0 = module_0.Try(float_0, bool_0)
    var_0 = try_0.on_success(str_0)

def test_case_5():
    dict_0 = {}
    int_0 = -3066
    bytes_0 = b'\xe7\x18\nj\xe8\xc1\xda\x7f\xa2'
    bool_0 = False
    try_0 = module_0.Try(bytes_0, bool_0)
    try_1 = module_0.Try(try_0, bool_0)
    bool_1 = False
    try_2 = module_0.Try(int_0, bool_1)
    var_0 = try_2.filter(dict_0)

def test_case_6():
    float_0 = -280.3
    bytes_0 = b'&R\x06`\xc6\xeb\xd9R\xe3\x11^\xdax\x9aI\x9cd\xb1\x0b'
    int_0 = 3531
    bool_0 = True
    try_0 = module_0.Try(int_0, bool_0)
    bool_1 = try_0.__eq__(bytes_0)
    bytes_1 = b'\x08\xfa`\x85\xd0{#\xc4!'
    set_0 = {bytes_1}
    str_0 = ''
    float_1 = -3327.417096
    bool_2 = False
    tuple_0 = (str_0, float_1, bool_2)
    list_0 = [float_0, set_0, tuple_0]
    bytes_2 = b'\x83w~\xf1\x90\xc1\xbe\xa0\n\xe1\xa6\x85\xe4\xb2\xd1'
    bool_3 = False
    bool_4 = False
    try_1 = module_0.Try(bool_4, bool_3)
    str_1 = try_1.__str__()
    try_2 = module_0.Try(bytes_2, bool_3)
    var_0 = try_2.get_or_else(list_0)
    list_1 = [bytes_1, bytes_1, bytes_1, set_0]
    bool_5 = False
    try_3 = module_0.Try(list_1, bool_5)
    bool_6 = False
    try_4 = module_0.Try(try_3, bool_6)
    bool_7 = try_4.__eq__(float_0)

def test_case_7():
    dict_0 = {}
    bool_0 = False
    bool_1 = True
    try_0 = module_0.Try(bool_0, bool_1)
    var_0 = try_0.get_or_else(dict_0)