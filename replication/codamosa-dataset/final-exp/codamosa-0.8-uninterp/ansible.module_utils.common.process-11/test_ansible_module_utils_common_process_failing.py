# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        int_0 = 3862
        var_0 = module_0.get_bin_path(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '*6"kO.C"9-%yiKDWs'
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'x|LsR_so-s(N'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '/bin/ls'
        var_0 = module_0.get_bin_path(str_0)
        str_1 = '/bin/invalid_exe'
        str_2 = 'expect %s%s or %s'
        var_1 = module_0.get_bin_path(str_2, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = "p\n7;t'$1A.Bn__G\\K"
        bool_0 = False
        tuple_0 = (bool_0,)
        var_0 = module_0.get_bin_path(str_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '/bin/ls'
        var_0 = module_0.get_bin_path(str_0)
        bool_0 = False
        float_0 = -3152.22
        set_0 = {bool_0, float_0}
        list_0 = [bool_0, set_0]
        tuple_0 = None
        tuple_1 = (tuple_0,)
        var_1 = module_0.get_bin_path(list_0, tuple_1)
    except BaseException:
        pass