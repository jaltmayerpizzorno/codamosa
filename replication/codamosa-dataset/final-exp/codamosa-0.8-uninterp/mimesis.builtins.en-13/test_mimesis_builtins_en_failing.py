# Automatically generated by Pynguin.
import mimesis.builtins.en as module_0

def test_case_0():
    try:
        u_s_a_spec_provider_0 = module_0.USASpecProvider()
        str_0 = ''
        u_s_a_spec_provider_1 = module_0.USASpecProvider(str_0)
        str_1 = u_s_a_spec_provider_0.tracking_number(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '~hi\x0bO}swI)U'
        u_s_a_spec_provider_0 = module_0.USASpecProvider()
        u_s_a_spec_provider_1 = module_0.USASpecProvider(str_0)
        u_s_a_spec_provider_2 = module_0.USASpecProvider()
        str_1 = u_s_a_spec_provider_1.ssn()
        var_0 = u_s_a_spec_provider_2.personality()
        var_1 = u_s_a_spec_provider_1.personality()
        var_2 = u_s_a_spec_provider_1.personality()
        var_3 = u_s_a_spec_provider_1.personality()
        u_s_a_spec_provider_3 = module_0.USASpecProvider(str_0)
        str_2 = u_s_a_spec_provider_2.tracking_number()
        str_3 = u_s_a_spec_provider_3.tracking_number()
        str_4 = u_s_a_spec_provider_3.tracking_number()
        str_5 = u_s_a_spec_provider_3.tracking_number()
        var_4 = u_s_a_spec_provider_3.personality()
        str_6 = u_s_a_spec_provider_3.ssn()
        u_s_a_spec_provider_4 = module_0.USASpecProvider()
        var_5 = u_s_a_spec_provider_3.personality()
        str_7 = u_s_a_spec_provider_2.ssn()
        u_s_a_spec_provider_5 = module_0.USASpecProvider()
        str_8 = u_s_a_spec_provider_5.ssn()
        str_9 = u_s_a_spec_provider_1.ssn()
        u_s_a_spec_provider_6 = module_0.USASpecProvider(str_2)
        var_6 = u_s_a_spec_provider_4.personality()
        var_7 = u_s_a_spec_provider_3.personality(str_5)
        var_8 = u_s_a_spec_provider_2.personality()
        u_s_a_spec_provider_7 = module_0.USASpecProvider()
        str_10 = u_s_a_spec_provider_7.ssn()
        str_11 = '1(e-2=d'
        str_12 = u_s_a_spec_provider_4.tracking_number()
        str_13 = u_s_a_spec_provider_4.tracking_number(str_11)
    except BaseException:
        pass