# Automatically generated by Pynguin.
import flutils.objutils as module_0
import collections as module_1

def test_case_0():
    pass

def test_case_1():
    bytes_0 = b'LM^\xd1'
    bool_0 = module_0.has_any_attrs(bytes_0)

def test_case_2():
    bool_0 = None
    str_0 = '1|aejt#r~j\x0cX8NgQvl4'
    list_0 = [str_0]
    bool_1 = module_0.has_any_callables(bool_0, *list_0)

def test_case_3():
    set_0 = set()
    bool_0 = module_0.has_any_callables(set_0)

def test_case_4():
    bool_0 = False
    bool_1 = module_0.has_callables(bool_0)

def test_case_5():
    str_0 = '__class__'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_callables(str_0, *list_0)

def test_case_6():
    bool_0 = False
    str_0 = '7DLox>'
    str_1 = '\x0b'
    list_0 = [str_0, str_0, str_1, str_0]
    bool_1 = module_0.has_attrs(bool_0, *list_0)

def test_case_7():
    bytes_0 = b'LM^\xd1'
    bool_0 = module_0.has_any_attrs(bytes_0)
    str_0 = 'y2'
    list_0 = [str_0]
    bool_1 = module_0.has_callables(bool_0, *list_0)

def test_case_8():
    float_0 = -1885.8676
    bool_0 = module_0.is_list_like(float_0)

def test_case_9():
    bytes_0 = b'\x96S3\xee.Z\xc4>'
    list_0 = [bytes_0]
    str_0 = '\x0c3`y_]EN_O]\t\x0b}A\nD$'
    str_1 = '5C0CUT~V3ca`%!'
    str_2 = ')E'
    dict_0 = {str_0: str_0, str_1: bytes_0, str_1: bytes_0, str_2: list_0}
    tuple_0 = (bytes_0, list_0, list_0, dict_0)
    bool_0 = module_0.is_list_like(tuple_0)

def test_case_10():
    str_0 = '__class__'
    list_0 = [str_0, str_0]
    bool_0 = module_0.has_callables(str_0, *list_0)
    bool_1 = module_0.has_any_callables(bool_0, *list_0)

def test_case_11():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    list_0 = [tuple_0, bool_0]
    deque_0 = module_1.deque(*list_0)
    bool_1 = module_0.has_any_attrs(deque_0)
    str_0 = '__doc__'
    list_1 = [str_0, str_0]
    bool_2 = module_0.has_callables(str_0, *list_1)
    bool_3 = module_0.has_callables(bool_2)
    list_2 = [str_0]
    bool_4 = module_0.has_callables(str_0)
    list_3 = None
    bool_5 = module_0.is_list_like(list_3)
    bool_6 = module_0.has_any_callables(bool_0, *list_2)