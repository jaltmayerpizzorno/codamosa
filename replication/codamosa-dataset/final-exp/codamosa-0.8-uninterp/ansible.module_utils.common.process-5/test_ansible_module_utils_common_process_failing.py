# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        str_0 = 'jYn_^'
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bool_0 = True
        bytes_0 = b'\x83\x13\xb9\xb4\x80\x0e\xe2P\x19\xa4'
        var_0 = module_0.get_bin_path(bool_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 3184
        list_0 = [int_0]
        bool_0 = False
        dict_0 = {int_0: list_0, int_0: bool_0, int_0: int_0}
        set_0 = set()
        tuple_0 = (bool_0, dict_0, set_0)
        var_0 = module_0.get_bin_path(list_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = []
        bool_0 = False
        var_0 = module_0.get_bin_path(list_0, bool_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        int_0 = 6
        set_0 = {str_0, int_0, str_0, int_0}
        var_0 = module_0.get_bin_path(int_0, set_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        bytes_0 = b'\x94(e'
        str_0 = ' assemble a file from a directory of fragments '
        list_0 = [bool_0]
        int_0 = None
        tuple_0 = (str_0, int_0)
        var_0 = module_0.get_bin_path(bytes_0, list_0, tuple_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass