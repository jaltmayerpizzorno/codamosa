# Automatically generated by Pynguin.
import flutils.objutils as module_0

def test_case_0():
    tuple_0 = None
    bool_0 = module_0.has_attrs(tuple_0)

def test_case_1():
    tuple_0 = ()
    bool_0 = module_0.has_any_callables(tuple_0)

def test_case_2():
    str_0 = '__class__'
    list_0 = [str_0]
    bool_0 = module_0.has_any_callables(str_0, *list_0)

def test_case_3():
    int_0 = -730
    str_0 = '&fV>"M_ehi^KO?wE'
    list_0 = [str_0]
    bool_0 = module_0.has_callables(int_0, *list_0)

def test_case_4():
    bytes_0 = b'4\xa5)j\xa8\r\xc2\xb9\xbf\x00\xcc\x80i\xa19\xc5\xf6\r\x9fi'
    bool_0 = module_0.has_callables(bytes_0)

def test_case_5():
    int_0 = -445
    bool_0 = module_0.is_list_like(int_0)

def test_case_6():
    list_0 = []
    str_0 = 'y"8X`\\?'
    list_1 = [str_0, str_0]
    bool_0 = module_0.has_any_callables(list_0, *list_1)
    bool_1 = module_0.has_attrs(list_0)

def test_case_7():
    str_0 = '__class__'
    list_0 = [str_0]
    complex_0 = None
    bool_0 = module_0.has_callables(complex_0, *list_0)