# Automatically generated by Pynguin.
import ansible.module_utils.common.process as module_0

def test_case_0():
    try:
        bool_0 = True
        var_0 = module_0.get_bin_path(bool_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'C:\\WINDOWS\\system32'
        var_0 = module_0.get_bin_path(str_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = b'\x97\x18C[\x92\xdd\x03\x9c\x9b\xcd7\x84\xaa`\x07\x9a\xb3='
        var_0 = module_0.get_bin_path(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        bytes_0 = b"\x8c?%\xd0\x00'\x84\xf8\x1f\x9d\x99\x1c\xc3"
        var_0 = module_0.get_bin_path(bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = None
        float_0 = None
        dict_0 = {float_0: list_0, float_0: list_0, float_0: float_0}
        var_0 = module_0.get_bin_path(float_0, dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ''
        var_0 = module_0.get_bin_path(str_0)
    except BaseException:
        pass