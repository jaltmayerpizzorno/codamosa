# Automatically generated by Pynguin.
import flutes.structure as module_0

def test_case_0():
    pass

def test_case_1():
    bool_0 = False
    module_0.register_no_map_class(bool_0)

def test_case_2():
    str_0 = '(Z``+y:G}`,'
    dict_0 = {}
    int_0 = 532
    tuple_0 = (str_0, dict_0, int_0)
    var_0 = module_0.no_map_instance(tuple_0)

def test_case_3():
    str_0 = 'remove_prefix'
    tuple_0 = ()
    var_0 = module_0.map_structure(str_0, tuple_0)

def test_case_4():
    int_0 = -2224
    dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
    var_0 = module_0.no_map_instance(dict_0)
    str_0 = 'D^@!8"\x0cI)xUj^IY'
    list_0 = []
    tuple_0 = (list_0,)
    var_1 = module_0.map_structure(str_0, tuple_0)
    set_0 = set()
    list_1 = [var_1]
    var_2 = module_0.map_structure_zip(set_0, list_1)
    bytes_0 = b'0\xa1\xb4t\xe9'
    var_3 = module_0.no_map_instance(bytes_0)
    bytes_1 = b'%\x84!\x14\xe9a\x96\xda\xc3\xab'
    var_4 = module_0.no_map_instance(bytes_1)
    var_5 = module_0.no_map_instance(var_0)

def test_case_5():
    dict_0 = {}
    int_0 = 173
    tuple_0 = (int_0,)
    list_0 = [tuple_0, dict_0, dict_0, dict_0]
    var_0 = module_0.map_structure_zip(dict_0, list_0)

def test_case_6():
    int_0 = 1
    int_1 = 2
    int_2 = 3
    int_3 = [int_0, int_1, int_2]
    int_4 = 4
    int_5 = [int_1, int_2, int_4]
    int_6 = 5
    int_7 = [int_2, int_4, int_6]
    var_0 = lambda x, y, z: x + y + z
    int_8 = [int_3, int_5, int_7]
    str_0 = '=YUYgu:w<*7m*t'
    var_1 = module_0.no_map_instance(str_0)
    var_2 = module_0.map_structure_zip(var_0, int_8)
    str_1 = 'a'
    str_2 = 'b'
    type_0 = None
    module_0.register_no_map_class(type_0)
    int_9 = 6
    int_10 = {str_1: int_6, str_2: int_9}
    int_11 = 7
    int_12 = {str_1: int_6, str_2: int_11}
    int_13 = 8
    int_14 = {str_1: int_6, str_2: int_13}
    var_3 = lambda x, y, z: x + y + z
    int_15 = [int_10, int_12, int_14]
    var_4 = module_0.map_structure_zip(var_3, int_15)

def test_case_7():
    str_0 = 'first'
    str_1 = 'second'
    int_0 = 1
    int_1 = 2
    int_2 = {str_0: int_0, str_1: int_1}
    int_3 = 10
    int_4 = 20
    int_5 = {str_0: int_3, str_1: int_4}
    var_0 = lambda a, b: a + b
    int_6 = [int_2, int_5]
    var_1 = module_0.map_structure_zip(var_0, int_6)
    var_2 = type(int_2)
    var_3 = isinstance(var_1, var_2)