# Automatically generated by Pynguin.
import flutes.structure as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.no_map_instance(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -123.41
        tuple_0 = (float_0,)
        set_0 = {tuple_0, float_0, tuple_0}
        var_0 = module_0.map_structure(tuple_0, set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'ATe'
        list_0 = None
        var_0 = module_0.map_structure(str_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = -810.4263
        str_0 = '\tZq=[{'
        var_0 = module_0.map_structure_zip(float_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 1496
        bool_0 = False
        var_0 = module_0.map_structure_zip(int_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bytes_0 = b'\x94\xa3\x9b\x8f\xe0\xd6\x0b\xa3'
        list_0 = [bytes_0, bytes_0]
        var_0 = module_0.map_structure(bytes_0, list_0)
    except BaseException:
        pass

def test_case_6():
    try:
        var_0 = None
        bool_0 = False
        tuple_0 = ()
        set_0 = {var_0, var_0, tuple_0, tuple_0}
        var_1 = module_0.map_structure(bool_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        dict_0 = {}
        str_0 = 'hG\ro[+M t3X1^'
        dict_1 = {}
        list_0 = module_0.reverse_map(dict_1)
        list_1 = module_0.reverse_map(dict_1)
        var_0 = module_0.map_structure(str_0, dict_0)
        str_1 = ' \x0c'
        set_0 = None
        var_1 = module_0.map_structure_zip(str_1, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        float_0 = -123.41
        tuple_0 = (float_0,)
        list_0 = [tuple_0, tuple_0]
        var_0 = module_0.map_structure_zip(float_0, list_0)
    except BaseException:
        pass

def test_case_9():
    try:
        set_0 = set()
        tuple_0 = ()
        list_0 = [tuple_0]
        var_0 = module_0.map_structure_zip(set_0, list_0)
        str_0 = 'register_ipython_excepthook'
        set_1 = None
        var_1 = module_0.map_structure(str_0, set_1)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = 3
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        str_0 = 'hG\ro[+M t3X1^'
        var_0 = None
        dict_1 = {}
        list_0 = module_0.reverse_map(dict_1)
        dict_2 = {var_0: int_0}
        list_1 = module_0.reverse_map(dict_2)
        var_1 = module_0.map_structure(str_0, dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        set_0 = set()
        tuple_0 = ()
        list_0 = [tuple_0]
        var_0 = module_0.map_structure_zip(set_0, list_0)
        int_0 = 1361
        var_1 = module_0.map_structure(list_0, set_0)
        var_2 = None
        int_1 = 784
        int_2 = -14
        dict_0 = {var_2: int_2, var_2: int_0}
        list_1 = module_0.reverse_map(dict_0)
        dict_1 = {var_2: int_1, var_2: int_2}
        list_2 = module_0.reverse_map(dict_1)
        str_0 = 'register_ipython_excepthook'
        set_1 = None
        set_2 = {tuple_0, set_1}
        var_3 = module_0.map_structure(str_0, set_2)
    except BaseException:
        pass

def test_case_12():
    try:
        set_0 = set()
        float_0 = 0.1
        list_0 = [set_0]
        var_0 = module_0.map_structure_zip(float_0, list_0)
    except BaseException:
        pass

def test_case_13():
    try:
        int_0 = 1
        int_1 = 2
        str_0 = 'a'
        var_0 = [int_0, int_1, str_0]
        var_1 = module_0.no_map_instance(var_0)
        var_2 = module_0.no_map_instance(var_1)
        var_3 = lambda x: x + int_0
        var_4 = module_0.map_structure(var_3, var_2)
    except BaseException:
        pass