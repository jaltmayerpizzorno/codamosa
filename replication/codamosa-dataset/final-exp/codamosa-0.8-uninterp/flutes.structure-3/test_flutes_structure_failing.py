# Automatically generated by Pynguin.
import flutes.structure as module_0

def test_case_0():
    try:
        dict_0 = None
        list_0 = module_0.reverse_map(dict_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        var_0 = module_0.no_map_instance(dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = -3556
        list_0 = [int_0]
        var_0 = module_0.no_map_instance(list_0)
        bytes_0 = b'\x16\x00\xba\x1d\xecv\x00\x0cA\xb1z\xf9YS\x91\x06'
        var_1 = module_0.no_map_instance(bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = ''
        list_0 = [str_0]
        var_0 = module_0.map_structure(str_0, list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        dict_0 = {}
        str_0 = '+>4'
        var_0 = module_0.no_map_instance(str_0)
        bytes_0 = b''
        set_0 = None
        tuple_0 = (dict_0, dict_0, bytes_0, set_0)
        var_1 = module_0.map_structure_zip(str_0, tuple_0)
        var_2 = module_0.map_structure(str_0, tuple_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = None
        set_0 = {float_0}
        var_0 = module_0.map_structure(float_0, set_0)
    except BaseException:
        pass

def test_case_6():
    try:
        int_0 = 2
        str_0 = '+}Yy clGh"/A'
        var_0 = module_0.map_structure(int_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        str_0 = 'd'
        var_0 = module_0.map_structure_zip(set_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xae'
        list_0 = []
        var_0 = module_0.map_structure(bytes_0, list_0)
        dict_0 = {}
        var_1 = None
        int_0 = 1916
        dict_1 = {var_1: int_0, var_1: int_0, var_1: int_0}
        list_1 = module_0.reverse_map(dict_1)
        str_0 = '+<!'
        var_2 = module_0.no_map_instance(str_0)
        str_1 = "Argument '"
        bytes_1 = b'+\xad\x02hq\x830\xba\x0b?\xa8>y\xa6'
        var_3 = module_0.no_map_instance(list_1)
        set_0 = None
        tuple_0 = (dict_0, dict_0, bytes_1, set_0)
        var_4 = module_0.map_structure_zip(str_1, tuple_0)
        int_1 = 1989
        var_5 = module_0.map_structure(tuple_0, int_1)
    except BaseException:
        pass

def test_case_9():
    try:
        float_0 = -281.0
        dict_0 = {float_0: float_0, float_0: float_0}
        var_0 = module_0.map_structure(dict_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0}
        str_0 = 's6@T'
        list_0 = [set_0, set_0, str_0, bool_0]
        list_1 = [list_0, bool_0, bool_0]
        tuple_0 = (str_0, list_0)
        var_0 = module_0.map_structure(list_1, tuple_0)
    except BaseException:
        pass

def test_case_11():
    try:
        int_0 = 3
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        tuple_0 = (dict_0,)
        list_0 = [tuple_0]
        var_0 = module_0.map_structure_zip(int_0, list_0)
    except BaseException:
        pass

def test_case_12():
    try:
        float_0 = -280.8285837245025
        dict_0 = {}
        var_0 = None
        int_0 = 1916
        dict_1 = {var_0: int_0, var_0: int_0, var_0: int_0}
        list_0 = module_0.reverse_map(dict_1)
        str_0 = '+<!'
        var_1 = module_0.no_map_instance(str_0)
        str_1 = "Argument '"
        bytes_0 = b'+\xad\x02hq\x830\xba\x0b?\xa8>y\xa6'
        set_0 = None
        tuple_0 = (dict_0, dict_0, bytes_0, set_0)
        var_2 = module_0.map_structure_zip(str_1, tuple_0)
        tuple_1 = (list_0,)
        list_1 = [var_1, float_0, tuple_1, dict_0]
        var_3 = module_0.map_structure_zip(float_0, list_1)
    except BaseException:
        pass

def test_case_13():
    try:
        var_0 = None
        int_0 = 1916
        dict_0 = {var_0: int_0, var_0: int_0, var_0: int_0}
        list_0 = module_0.reverse_map(dict_0)
        str_0 = '<'
        var_1 = module_0.no_map_instance(str_0)
        set_0 = {var_1, str_0}
        var_2 = module_0.map_structure(list_0, set_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = None
        set_0 = {int_0}
        list_0 = [set_0, set_0]
        int_1 = -2841
        var_0 = module_0.map_structure_zip(int_1, list_0)
    except BaseException:
        pass