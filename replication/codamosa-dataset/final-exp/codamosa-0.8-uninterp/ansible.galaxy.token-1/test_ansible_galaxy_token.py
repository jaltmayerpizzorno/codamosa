# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()

def test_case_2():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_4():
    str_0 = None
    basic_auth_token_0 = module_0.BasicAuthToken(str_0)
    float_0 = 1199.867
    galaxy_token_0 = module_0.GalaxyToken(float_0)

def test_case_5():
    no_token_sentinel_0 = module_0.NoTokenSentinel()
    list_0 = [no_token_sentinel_0, no_token_sentinel_0]
    galaxy_token_0 = module_0.GalaxyToken(list_0)
    list_1 = [galaxy_token_0, galaxy_token_0, list_0, list_0]
    basic_auth_token_0 = module_0.BasicAuthToken(list_1)
    var_0 = basic_auth_token_0.get()

def test_case_6():
    int_0 = 600
    basic_auth_token_0 = module_0.BasicAuthToken(int_0)
    var_0 = basic_auth_token_0.get()
    galaxy_token_0 = module_0.GalaxyToken()
    var_1 = galaxy_token_0.get()
    var_2 = basic_auth_token_0.headers()
    dict_0 = None
    var_3 = galaxy_token_0.save()
    list_0 = [dict_0, dict_0]
    no_token_sentinel_0 = module_0.NoTokenSentinel(*list_0)

def test_case_7():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()