# Automatically generated by Pynguin.
import ansible.utils.context_objects as module_0
import ansible.module_utils.common.collections as module_1

def test_case_0():
    try:
        int_0 = 1024
        c_l_i_args_0 = module_0.CLIArgs(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        set_0 = None
        tuple_0 = (set_0,)
        float_0 = -1708.0301
        int_0 = None
        bytes_0 = b'\xa8\xec\xdd\xff\xdb\xe7\xb0r\x93T$rm}\x80&\x0f\x057'
        dict_0 = {float_0: tuple_0, int_0: set_0, bytes_0: set_0}
        c_l_i_args_0 = module_0.CLIArgs(dict_0)
        a_b_c_singleton_0 = module_0._ABCSingleton(float_0, float_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'hnner_ke8'
        str_1 = 'HFtg-@v!^vh_YOIO['
        set_0 = {str_0, str_0, str_1, str_0}
        dict_0 = {str_1: str_1, str_0: set_0}
        immutable_dict_0 = module_1.ImmutableDict(**dict_0)
        c_l_i_args_0 = module_0.CLIArgs(immutable_dict_0)
        str_2 = 'inner_value'
        c_l_i_args_1 = module_0.CLIArgs(str_2)
    except BaseException:
        pass