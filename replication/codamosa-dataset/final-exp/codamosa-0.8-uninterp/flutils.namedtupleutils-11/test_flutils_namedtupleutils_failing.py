# Automatically generated by Pynguin.
import flutils.namedtupleutils as module_0
import types as module_1

def test_case_0():
    try:
        var_0 = None
        var_1 = module_0.to_namedtuple(var_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '_'
        str_1 = '<.5'
        str_2 = 'U7DysbKkn;{le-zD-'
        str_3 = '__module__'
        dict_0 = {str_1: str_1, str_2: str_0, str_3: str_1}
        simple_namespace_0 = module_1.SimpleNamespace(**dict_0)
        var_0 = module_0.to_namedtuple(simple_namespace_0)
        var_1 = module_0.to_namedtuple(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '_'
        var_0 = module_0.to_namedtuple(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'Test the function with a variety of inputs.'
        simple_namespace_0 = None
        bytes_0 = b'\x9f\xdb\r\xe9\x80\xcc5L\xfcE\x84\x0c\xb4-8\xcb\xd1\xd3\x9c/'
        dict_0 = {bytes_0: bytes_0, str_0: str_0, simple_namespace_0: str_0}
        str_1 = ';A\n?%)7azp]Q+b]B'
        dict_1 = {str_1: dict_0}
        float_0 = -1099.5
        bytes_1 = b'\xb96N\xae\x08\xc1\xe2\xb4\xf1'
        tuple_0 = (dict_1, float_0, bytes_1, dict_1)
        tuple_1 = (simple_namespace_0, dict_0, str_1, tuple_0)
        var_0 = module_0.to_namedtuple(tuple_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ' a'
        str_1 = 'b'
        int_0 = -10
        int_1 = 2
        int_2 = {str_0: int_0, str_1: int_1}
        var_0 = module_0.to_namedtuple(int_2)
        var_1 = repr(int_0)
        var_2 = str(var_0)
        var_3 = None
        var_4 = module_0.to_namedtuple(var_3)
    except BaseException:
        pass