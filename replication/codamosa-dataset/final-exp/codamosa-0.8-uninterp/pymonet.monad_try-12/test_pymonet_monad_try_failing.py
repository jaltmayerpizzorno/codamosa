# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    try:
        bool_0 = True
        int_0 = 3624
        bool_1 = True
        try_0 = module_0.Try(int_0, bool_1)
        var_0 = try_0.map(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = ()
        int_0 = 413
        bool_0 = False
        try_0 = module_0.Try(int_0, bool_0)
        var_0 = try_0.get()
        try_1 = module_0.Try(try_0, bool_0)
        bytes_0 = b'\xe1-\xf6\x82\xc0\x98"N\xd8\x1bG\x82\x8a\xcb\x8a\xa2\xee'
        bool_1 = False
        try_2 = module_0.Try(bytes_0, bool_1)
        complex_0 = None
        var_1 = try_1.bind(complex_0)
        var_2 = try_1.on_fail(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = -3730.09
        bool_0 = True
        try_0 = module_0.Try(float_0, bool_0)
        str_0 = try_0.__str__()
        str_1 = '?Fm0\x0cu=+@rV<VCP2~Uk'
        var_0 = try_0.bind(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b'\xa0=\x7f\xc6W\xf0\xa6B\x9dU'
        bool_0 = True
        try_0 = module_0.Try(bytes_0, bool_0)
        float_0 = 1352.9
        bool_1 = False
        bool_2 = True
        try_1 = module_0.Try(bool_1, bool_2)
        var_0 = try_1.on_success(float_0)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'<\x03\x08\x0e\xbc/\xa5\xd2\xcd\x9d@\xc7\xf2z\xd5f\xf6\xc0|\x19'
        bool_0 = False
        str_0 = 'N|O#hTsSC'
        set_0 = {bool_0, str_0, str_0, bool_0}
        try_0 = module_0.Try(set_0, bool_0)
        var_0 = try_0.on_fail(bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '\n        If Maybe is empty return default_value, in other case.\n\n        :param default_value: value to return if Maybe is empty\n        :type default_value: Any\n        :returns: value of Maybe or default_value\n        :rtype: A\n        '
        bool_0 = True
        try_0 = module_0.Try(str_0, bool_0)
        list_0 = [try_0, bool_0, bool_0]
        bytes_0 = b''
        bool_1 = False
        try_1 = module_0.Try(bytes_0, bool_1)
        var_0 = try_1.filter(list_0)
        var_1 = try_0.filter(try_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        list_0 = [set_0]
        tuple_0 = (set_0, list_0, set_0)
        float_0 = -1339.397
        bool_1 = False
        try_0 = module_0.Try(float_0, bool_1)
        bytes_0 = None
        int_0 = -784
        dict_0 = {bytes_0: bytes_0, bytes_0: int_0}
        bool_2 = try_0.__eq__(try_0)
        var_0 = try_0.map(dict_0)
        var_1 = try_0.filter(tuple_0)
        bytes_1 = b'\xc6B\xa4v'
        var_2 = try_0.get_or_else(bytes_1)
        bool_3 = True
        try_1 = module_0.Try(tuple_0, bool_3)
        bool_4 = False
        try_2 = module_0.Try(dict_0, bool_4)
        bool_5 = True
        try_3 = module_0.Try(bytes_0, bool_5)
        var_3 = try_3.filter(tuple_0)
    except BaseException:
        pass