# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    no_token_sentinel_0 = module_0.NoTokenSentinel()

def test_case_2():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.save()

def test_case_4():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_5():
    list_0 = []
    basic_auth_token_0 = module_0.BasicAuthToken(list_0)

def test_case_6():
    int_0 = -868
    basic_auth_token_0 = module_0.BasicAuthToken(int_0)
    var_0 = basic_auth_token_0.get()

def test_case_7():
    float_0 = 4763.69373
    basic_auth_token_0 = module_0.BasicAuthToken(float_0)
    basic_auth_token_1 = module_0.BasicAuthToken(basic_auth_token_0)
    var_0 = basic_auth_token_1.headers()

def test_case_8():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()

def test_case_9():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()