# Automatically generated by Pynguin.
import pymonet.validation as module_0

def test_case_0():
    try:
        bytes_0 = b'&'
        list_0 = [bytes_0]
        str_0 = 'Xc.G~0^a3Kglq"@R'
        validation_0 = module_0.Validation(str_0, list_0)
        str_1 = 'lIbw1?'
        validation_1 = module_0.Validation(str_0, str_1)
        validation_2 = module_0.Validation(list_0, validation_1)
        var_0 = validation_2.__eq__(validation_0)
        tuple_0 = ()
        validation_3 = module_0.Validation(tuple_0, tuple_0)
        bool_0 = True
        var_1 = validation_3.map(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x020\xdc\x9b)\x10]\x8d\x14\xc9\xcf\x08~\xcb\xf0N\x17\xf6'
        int_0 = False
        tuple_0 = (bytes_0, int_0)
        validation_0 = module_0.Validation(bytes_0, tuple_0)
        var_0 = validation_0.__str__()
        str_0 = '`lrjK8y/]C8u'
        float_0 = 2012.42
        bytes_1 = b'\x9c`\xf4\xb8\xee\xb6\xa5\xa7^\xc3\x0fq\xac\x9fn'
        list_0 = [float_0, str_0]
        validation_1 = module_0.Validation(bytes_1, list_0)
        bool_0 = True
        var_1 = validation_1.__eq__(bool_0)
        var_2 = validation_1.to_either()
        var_3 = validation_1.bind(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        int_0 = -2275
        dict_0 = {}
        validation_0 = module_0.Validation(int_0, dict_0)
        var_0 = validation_0.__str__()
        set_0 = {bool_0, bool_0, bool_0}
        bool_1 = False
        tuple_0 = (bool_1,)
        str_0 = 'Callable[[U], Lazy[U, W]]'
        validation_1 = module_0.Validation(tuple_0, str_0)
        var_1 = validation_1.map(set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        validation_0 = module_0.Validation(bool_0, bool_0)
        var_0 = validation_0.to_try()
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        float_0 = 1842.451
        validation_0 = module_0.Validation(dict_0, float_0)
        var_0 = validation_0.is_fail()
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = -95.44
        list_0 = []
        set_0 = set()
        validation_0 = module_0.Validation(list_0, set_0)
        var_0 = validation_0.map(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '$wE!_z'
        bytes_0 = b'V(6\xd4\x1f\xae\xfc\\\xb1\x9f\xbd^\xfb_'
        float_0 = 293.565007
        validation_0 = module_0.Validation(bytes_0, float_0)
        var_0 = validation_0.bind(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = ''
        int_0 = 1120
        tuple_0 = (int_0,)
        set_0 = None
        bytes_0 = b'\xd9=\xcc\xb4N\x1a\xed'
        dict_0 = {tuple_0: int_0, tuple_0: tuple_0, set_0: str_0, bytes_0: set_0}
        validation_0 = module_0.Validation(str_0, dict_0)
        float_0 = -6112.26
        var_0 = validation_0.ap(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = False
        set_0 = set()
        validation_0 = module_0.Validation(bool_0, set_0)
        var_0 = validation_0.to_either()
        var_1 = validation_0.is_fail()
        var_2 = validation_0.to_try()
        int_0 = 489
        var_3 = validation_0.bind(int_0)
    except BaseException:
        pass

def test_case_9():
    try:
        tuple_0 = ()
        bool_0 = True
        validation_0 = module_0.Validation(tuple_0, bool_0)
        list_0 = [validation_0, tuple_0]
        str_0 = 'w^e2)'
        validation_1 = module_0.Validation(list_0, str_0)
        var_0 = validation_1.to_box()
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '`,l`ld4j&cFek\x0c\nmZf[H'
        str_1 = 'b e)*Et$efdwU!'
        bytes_0 = b'\xe5\x11\x12\\g\xd1\xc3\xd3\xf04y\x80\x98\x11\x07'
        validation_0 = module_0.Validation(str_1, bytes_0)
        complex_0 = None
        var_0 = validation_0.__eq__(validation_0)
        bytes_1 = b'X\xa2\x87\x83'
        validation_1 = module_0.Validation(bytes_1, str_0)
        list_0 = [complex_0, validation_1]
        bool_0 = True
        validation_2 = module_0.Validation(list_0, bool_0)
        var_1 = validation_2.__eq__(validation_0)
        float_0 = -1488.777656
        bool_1 = False
        float_1 = -156.0
        list_1 = [float_1, float_0]
        tuple_0 = (list_1,)
        validation_3 = module_0.Validation(tuple_0, str_0)
        validation_4 = module_0.Validation(validation_3, validation_3)
        tuple_1 = (float_1, validation_4)
        validation_5 = module_0.Validation(tuple_1, bool_1)
        var_2 = validation_5.__str__()
    except BaseException:
        pass