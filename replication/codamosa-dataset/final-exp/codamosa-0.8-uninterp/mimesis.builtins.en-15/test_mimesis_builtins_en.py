# Automatically generated by Pynguin.
import mimesis.builtins.en as module_0

def test_case_0():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()

def test_case_1():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    str_0 = u_s_a_spec_provider_0.tracking_number()

def test_case_2():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    str_0 = u_s_a_spec_provider_0.ssn()

def test_case_3():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    var_0 = u_s_a_spec_provider_0.personality()

def test_case_4():
    str_0 = "24T,54U:0j1'[s"
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    var_0 = u_s_a_spec_provider_0.personality(str_0)
    u_s_a_spec_provider_1 = module_0.USASpecProvider()
    str_1 = u_s_a_spec_provider_1.ssn()

def test_case_5():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    str_0 = 'rheti'
    var_0 = u_s_a_spec_provider_0.personality(str_0)