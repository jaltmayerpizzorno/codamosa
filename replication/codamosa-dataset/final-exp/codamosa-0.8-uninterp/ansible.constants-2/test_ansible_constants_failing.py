# Automatically generated by Pynguin.
import ansible.constants as module_0

def test_case_0():
    try:
        int_0 = 6003
        list_0 = [int_0, int_0, int_0, int_0, int_0]
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(list_0, list_0, list_0)
        var_0 = deprecated_sequence_constant_0.__getitem__(list_0)
    except BaseException:
        pass