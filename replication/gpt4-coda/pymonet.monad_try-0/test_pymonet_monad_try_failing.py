# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    try:
        int_0 = None
        list_0 = [int_0, int_0, int_0]
        bool_0 = True
        float_0 = 3140.44
        try_0 = module_0.Try(float_0, bool_0)
        try_1 = module_0.Try(list_0, bool_0)
        float_1 = 1250.58
        bool_1 = True
        try_2 = module_0.Try(float_1, bool_1)
        try_3 = module_0.Try(try_1, bool_0)
        tuple_0 = ()
        bool_2 = try_1.__eq__(tuple_0)
        var_0 = try_3.get()
        bytes_0 = b'^\xb3W\x0c'
        set_0 = {bytes_0, bytes_0}
        bool_3 = True
        try_4 = module_0.Try(set_0, bool_3)
        var_1 = try_4.map(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 529.11522
        bool_0 = True
        try_0 = module_0.Try(float_0, bool_0)
        var_0 = try_0.get()
        var_1 = try_0.get()
        var_2 = try_0.bind(try_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '89&<t1\nF'
        bool_0 = True
        try_0 = module_0.Try(str_0, bool_0)
        var_0 = try_0.on_success(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xcb`\x06\x9c\x02\xf9-E\x7f\xc6'
        bool_0 = True
        try_0 = module_0.Try(bytes_0, bool_0)
        str_0 = try_0.__str__()
        str_1 = try_0.__str__()
        bool_1 = False
        try_1 = module_0.Try(bool_1, bool_1)
        str_2 = try_1.__str__()
        float_0 = 108.6591
        var_0 = try_1.on_fail(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = 1030.0
        bytes_0 = b'\xfb\xd9\xa8(,v\x9f\xb5W\xbd\xc0`1\xa1r'
        bool_0 = True
        try_0 = module_0.Try(bytes_0, bool_0)
        var_0 = try_0.filter(float_0)
    except BaseException:
        pass