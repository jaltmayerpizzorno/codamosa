# Automatically generated by Pynguin.
import ansible.modules.replace as module_0

def test_case_0():
    try:
        int_0 = 100
        dict_0 = {int_0: int_0}
        set_0 = {int_0}
        var_0 = module_0.write_changes(int_0, dict_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = -2048.597818
        str_0 = '\x0c4]rHWuF2q)leTd6'
        int_0 = 127
        var_0 = module_0.check_file_attrs(float_0, str_0, int_0)
    except BaseException:
        pass