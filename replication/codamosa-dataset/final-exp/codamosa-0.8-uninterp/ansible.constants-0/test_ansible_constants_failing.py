# Automatically generated by Pynguin.
import ansible.constants as module_0

def test_case_0():
    try:
        int_0 = -2765
        bytes_0 = b'\xe6\xa5\xea\xec@2'
        tuple_0 = ()
        float_0 = 1339.906
        deprecated_sequence_constant_0 = module_0._DeprecatedSequenceConstant(bytes_0, tuple_0, float_0)
        var_0 = deprecated_sequence_constant_0.__getitem__(int_0)
    except BaseException:
        pass