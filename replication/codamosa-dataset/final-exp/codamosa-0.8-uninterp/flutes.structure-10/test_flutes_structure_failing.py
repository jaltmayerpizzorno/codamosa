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
        bool_0 = False
        var_0 = module_0.no_map_instance(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        var_0 = None
        list_0 = [var_0, var_0]
        var_1 = module_0.map_structure(list_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1388.287
        set_0 = {float_0}
        var_0 = module_0.map_structure(float_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -3657
        var_0 = module_0.map_structure(int_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'xj\nH'
        bytes_0 = b'Jl\x95;I\x9e\xef\x1a\xb7\xe7\xb5\xa8\xc1&'
        tuple_0 = (bytes_0,)
        int_0 = -389
        str_1 = 'dmx^x'
        int_1 = 1248
        str_2 = ''
        int_2 = 0
        int_3 = -598
        dict_0 = {tuple_0: int_0, str_1: int_1, str_2: int_2, int_1: int_3}
        list_0 = module_0.reverse_map(dict_0)
        set_0 = {str_0, str_0}
        bytes_1 = b'\x91\xea\xa0\xcb\x14~\xbf\rC\xd3\xb8BL@\xe9\x9b\x04'
        list_1 = [set_0, str_0, bytes_1, str_0]
        var_0 = module_0.map_structure_zip(list_1, list_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = False
        str_0 = '512'
        var_0 = module_0.map_structure_zip(bool_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        dict_0 = {}
        list_0 = module_0.reverse_map(dict_0)
        tuple_0 = ()
        list_1 = module_0.reverse_map(dict_0)
        bytes_0 = b'\x8e,*\x18\x04\xc2G\x04'
        list_2 = [list_1, dict_0, tuple_0, set_0]
        var_0 = module_0.map_structure(bytes_0, list_2)
    except BaseException:
        pass

def test_case_8():
    try:
        bytes_0 = b'\xa7\xd3\xbf1'
        str_0 = 'iE'
        tuple_0 = (str_0,)
        var_0 = module_0.map_structure(bytes_0, tuple_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '= \\-_WCBJ1="V4\n`{b\rB'
        var_0 = module_0.no_map_instance(str_0)
        str_1 = '\x0c$Y{*H\\?(lmAyC'
        var_1 = module_0.no_map_instance(var_0)
        set_0 = {str_1, var_1}
        var_2 = module_0.map_structure(str_1, set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        int_0 = -1241
        set_0 = None
        float_0 = None
        tuple_0 = (int_0, set_0, float_0)
        list_0 = [tuple_0]
        var_0 = module_0.map_structure_zip(int_0, list_0)
    except BaseException:
        pass

def test_case_11():
    try:
        tuple_0 = ()
        dict_0 = {tuple_0: tuple_0}
        list_0 = [dict_0, dict_0]
        var_0 = module_0.no_map_instance(list_0)
        list_1 = [var_0, var_0]
        var_1 = module_0.map_structure_zip(tuple_0, list_1)
    except BaseException:
        pass