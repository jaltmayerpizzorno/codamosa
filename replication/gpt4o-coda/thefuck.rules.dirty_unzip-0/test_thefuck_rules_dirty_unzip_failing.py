# Automatically generated by Pynguin.
import thefuck.rules.dirty_unzip as module_0

def test_case_0():
    try:
        float_0 = 4184.749
        bytes_0 = b'\xc0\xc7\xd8\xd3\xa4x\x86'
        var_0 = module_0.side_effect(bytes_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = 4184.749
        var_0 = module_0.get_new_command(float_0)
    except BaseException:
        pass