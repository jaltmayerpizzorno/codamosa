# Automatically generated by Pynguin.
import ansible.cli.adhoc as module_0

def test_case_0():
    try:
        bool_0 = True
        ad_hoc_c_l_i_0 = module_0.AdHocCLI(bool_0)
        var_0 = ad_hoc_c_l_i_0.init_parser()
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'NY'
        ad_hoc_c_l_i_0 = module_0.AdHocCLI(str_0)
        var_0 = ad_hoc_c_l_i_0.run()
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        ad_hoc_c_l_i_0 = module_0.AdHocCLI(bool_0)
        var_0 = ad_hoc_c_l_i_0.post_process_args(bool_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 485
        ad_hoc_c_l_i_0 = module_0.AdHocCLI(int_0)
        var_0 = ad_hoc_c_l_i_0.run()
    except BaseException:
        pass