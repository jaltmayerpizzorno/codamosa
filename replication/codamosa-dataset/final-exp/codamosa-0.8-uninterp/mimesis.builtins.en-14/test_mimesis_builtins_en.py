# Automatically generated by Pynguin.
import mimesis.builtins.en as module_0

def test_case_0():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()

def test_case_1():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    var_0 = u_s_a_spec_provider_0.personality()
    u_s_a_spec_provider_1 = module_0.USASpecProvider()
    str_0 = u_s_a_spec_provider_1.tracking_number()
    u_s_a_spec_provider_2 = module_0.USASpecProvider()

def test_case_2():
    bytes_0 = b'\xc0\xacOI\xd6\xc4m\x0fok\x13\xaa\xf7:\xc7'
    u_s_a_spec_provider_0 = module_0.USASpecProvider(bytes_0)
    str_0 = u_s_a_spec_provider_0.ssn()

def test_case_3():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    var_0 = u_s_a_spec_provider_0.personality()

def test_case_4():
    u_s_a_spec_provider_0 = module_0.USASpecProvider()
    str_0 = 'mbti'
    var_0 = u_s_a_spec_provider_0.personality(str_0)
    str_1 = 'rheti'
    var_1 = u_s_a_spec_provider_0.personality(str_1)