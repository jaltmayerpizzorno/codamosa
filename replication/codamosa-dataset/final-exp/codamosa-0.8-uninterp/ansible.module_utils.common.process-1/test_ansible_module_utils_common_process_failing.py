# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        list_0 = None
        var_0 = module_0.get_bin_path(list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 't'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'l)p$8K!'
        bool_0 = False
        tuple_0 = (bool_0,)
        var_0 = module_0.get_bin_path(str_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ansible.module_utils'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        float_0 = None
        list_0 = [float_0, float_0, float_0, float_0]
        bytes_0 = b'4'
        var_0 = module_0.get_bin_path(float_0, list_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'true'
        var_0 = module_0.get_bin_path(str_0)
        str_1 = '/dev/null'
        var_1 = module_0.get_bin_path(str_1)
    except BaseException:
        pass