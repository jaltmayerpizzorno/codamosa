# Automatically generated by Pynguin.
import pymonet.monad_try as module_0

def test_case_0():
    try:
        list_0 = None
        bool_0 = True
        try_0 = module_0.Try(bool_0, bool_0)
        var_0 = try_0.map(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '\n    In mathematics, a semigroup is an algebraic structure\n    consisting of a set together with an associative binary operation.\n    A semigroup generalizes a monoid in that there might not exist an identity element.\n    It also (originally) generalized a group (a monoid with all inverses)\n    to a type where every element did not have to have an inverse, this the name semigroup.\n    '
        list_0 = [str_0]
        str_1 = ''
        str_2 = '\x0cHNL\n\x0bQLl\n'
        bool_0 = True
        try_0 = module_0.Try(str_2, bool_0)
        bytes_0 = b'FL\xa4\xd5\xc4\xd3*\xc5\x0b\x9c'
        bool_1 = True
        try_1 = module_0.Try(bytes_0, bool_1)
        float_0 = 1320.0
        bool_2 = False
        try_2 = module_0.Try(float_0, bool_2)
        try_3 = module_0.Try(try_1, bool_1)
        str_3 = try_3.__str__()
        tuple_0 = (str_1,)
        bool_3 = False
        try_4 = module_0.Try(tuple_0, bool_3)
        var_0 = try_4.bind(list_0)
        var_1 = try_4.on_fail(tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = False
        bytes_0 = b'\x98\xbe\x96\xf3\xccX\x87\r6K\x8aW\xda\xea\xc3\x89}60\xfc'
        bool_1 = False
        try_0 = module_0.Try(bytes_0, bool_1)
        var_0 = try_0.filter(bool_0)
        bool_2 = True
        try_1 = module_0.Try(bool_2, bool_2)
        var_1 = try_1.get()
        str_0 = try_1.__str__()
        str_1 = 'YCB^^\n'
        bool_3 = try_1.__eq__(str_1)
        str_2 = ''
        var_2 = try_1.bind(str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = False
        bool_1 = False
        dict_0 = {bool_1: bool_1, bool_0: bool_0}
        bool_2 = False
        try_0 = module_0.Try(dict_0, bool_2)
        var_0 = try_0.get()
        int_0 = -1862
        tuple_0 = None
        tuple_1 = (bool_0, bool_1, int_0, tuple_0)
        list_0 = []
        bool_3 = True
        try_1 = module_0.Try(list_0, bool_3)
        var_1 = try_1.on_success(tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'M\x82q\x8d\x91-\xaf\\.K\x92\x0f\xb5.'
        bool_0 = True
        bool_1 = False
        try_0 = module_0.Try(bytes_0, bool_1)
        var_0 = try_0.on_fail(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        set_0 = set()
        str_0 = ']-Z!7'
        bool_0 = False
        try_0 = module_0.Try(bool_0, bool_0)
        var_0 = try_0.filter(str_0)
        bool_1 = True
        try_1 = module_0.Try(str_0, bool_1)
        var_1 = try_1.filter(set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'R06!'
        dict_0 = {str_0: str_0, str_0: str_0}
        float_0 = 292.231589
        str_1 = '\x0b\r*[_"*^G]dx*%'
        set_0 = None
        tuple_0 = (str_1, dict_0, set_0)
        bool_0 = False
        try_0 = module_0.Try(tuple_0, bool_0)
        var_0 = try_0.filter(float_0)
        bool_1 = False
        try_1 = module_0.Try(float_0, bool_1)
        var_1 = try_1.get()
        str_2 = try_1.__str__()
        bool_2 = try_1.__eq__(try_1)
        str_3 = try_1.__str__()
        var_2 = try_0.on_success(dict_0)
        str_4 = 'X|+:t8n'
        bool_3 = True
        try_2 = module_0.Try(str_4, bool_3)
        str_5 = 'j'
        var_3 = try_2.filter(str_5)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'R06!'
        dict_0 = {str_0: str_0, str_0: str_0}
        float_0 = 292.231589
        str_1 = '\x0b\r*[_"*^G]dx*%'
        set_0 = None
        tuple_0 = (str_1, dict_0, set_0)
        bool_0 = False
        try_0 = module_0.Try(tuple_0, bool_0)
        var_0 = try_0.filter(float_0)
        bool_1 = True
        var_1 = try_0.get()
        bool_2 = False
        str_2 = try_0.__str__()
        try_1 = module_0.Try(dict_0, bool_2)
        bool_3 = try_0.__eq__(try_1)
        int_0 = -2
        str_3 = try_1.__str__()
        var_2 = try_1.on_success(dict_0)
        str_4 = 'X|+:t8n'
        try_2 = module_0.Try(str_4, bool_1)
        bytes_0 = b''
        var_3 = try_0.map(bytes_0)
        var_4 = try_2.bind(int_0)
    except BaseException:
        pass