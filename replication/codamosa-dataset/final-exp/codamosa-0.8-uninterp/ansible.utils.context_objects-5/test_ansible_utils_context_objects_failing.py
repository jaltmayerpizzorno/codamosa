# Automatically generated by Pynguin.
import ansible.utils.context_objects as module_0

def test_case_0():
    try:
        int_0 = 588
        set_0 = {int_0}
        global_c_l_i_args_0 = module_0.GlobalCLIArgs(set_0)
        c_l_i_args_0 = module_0.CLIArgs(global_c_l_i_args_0)
        c_l_i_args_1 = module_0.CLIArgs(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'bC'
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        c_l_i_args_0 = module_0.CLIArgs(dict_0)
        bool_0 = True
        c_l_i_args_1 = module_0.CLIArgs(bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        c_l_i_args_0 = module_0.CLIArgs(list_0)
    except BaseException:
        pass