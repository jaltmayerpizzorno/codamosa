# Automatically generated by Pynguin.
import ansible.constants as module_0

def test_case_0():
    try:
        int_0 = -1984
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(int_0, int_0, int_0)
        var_0 = deprecated_sequence_constant_0.__len__()
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = None
        bool_0 = False
        str_0 = '|UYkxde6'
        bytes_0 = b'\xa4t\xa4D\x11'
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(bool_0, str_0, bytes_0)
        var_0 = deprecated_sequence_constant_0.__getitem__(float_0)
    except BaseException:
        pass