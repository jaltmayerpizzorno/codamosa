# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    pass

def test_case_1():
    no_token_sentinel_0 = module_0.NoTokenSentinel()

def test_case_2():
    keycloak_token_0 = module_0.KeycloakToken()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()

def test_case_4():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_5():
    str_0 = '<'
    galaxy_token_0 = module_0.GalaxyToken(str_0)
    var_0 = galaxy_token_0.get()

def test_case_6():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_7():
    float_0 = 0.001
    basic_auth_token_0 = module_0.BasicAuthToken(float_0)

def test_case_8():
    int_0 = -1389
    basic_auth_token_0 = module_0.BasicAuthToken(int_0)
    var_0 = basic_auth_token_0.headers()
    int_1 = 401
    no_token_sentinel_0 = module_0.NoTokenSentinel()
    var_1 = no_token_sentinel_0.__new__(int_1)
    var_2 = basic_auth_token_0.get()

def test_case_9():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.save()
    var_1 = galaxy_token_0.save()
    list_0 = [var_0, var_1, var_0]
    no_token_sentinel_0 = module_0.NoTokenSentinel(*list_0)
    var_2 = galaxy_token_0.set(no_token_sentinel_0)

def test_case_10():
    str_0 = 'distribution_major_version'
    str_1 = None
    keycloak_token_0 = module_0.KeycloakToken(str_1, str_0, str_0)
    dict_0 = None
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.set(dict_0)
    str_2 = 'p0a?S'
    set_0 = None
    str_3 = 'yA>0T17|8~(ct@;$`bP'
    bool_0 = False
    keycloak_token_1 = module_0.KeycloakToken(str_2, set_0, str_3, bool_0)
    var_1 = galaxy_token_0.set(dict_0)