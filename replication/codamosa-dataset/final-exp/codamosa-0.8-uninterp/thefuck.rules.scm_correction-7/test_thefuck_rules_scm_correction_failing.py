# Automatically generated by Pynguin.
import thefuck.rules.scm_correction as module_0

def test_case_0():
    try:
        list_0 = None
        bytes_0 = b'V\xebI\xf9^\xecK\xc2\xb9(\xc0\xc4\xe8p\xbeS/\x1c\x8e\xc2'
        list_1 = [list_0, bytes_0, list_0, bytes_0]
        var_0 = module_0.get_new_command(list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 472.0
        var_0 = module_0.get_new_command(float_0)
    except BaseException:
        pass