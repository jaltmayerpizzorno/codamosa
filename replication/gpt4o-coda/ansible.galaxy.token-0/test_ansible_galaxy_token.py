# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    galaxy_token_0 = module_0.GalaxyToken()

def test_case_1():
    no_token_sentinel_0 = module_0.NoTokenSentinel()

def test_case_2():
    keycloak_token_0 = module_0.KeycloakToken()

def test_case_3():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_4():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.headers()

def test_case_5():
    float_0 = -3481.6
    basic_auth_token_0 = module_0.BasicAuthToken(float_0)
    int_0 = -537
    keycloak_token_0 = module_0.KeycloakToken(int_0)
    var_0 = basic_auth_token_0.get()

def test_case_6():
    int_0 = 15
    str_0 = '4\n05,;(,Pz%j]i'
    str_1 = 'An error occurred while calling ansible.utils.display.initialize_locale (%s). This may result in incorrectly calculated text widths that can cause Display to print incorrect line lengths'
    dict_0 = {str_0: int_0, str_1: str_1, str_0: int_0, str_1: str_1}
    str_2 = 'Zm|3" TKCn"*cA_plO\x0cb'
    dict_1 = {str_2: str_2, str_2: str_2, str_2: str_2}
    no_token_sentinel_0 = module_0.NoTokenSentinel(**dict_1)
    var_0 = no_token_sentinel_0.__new__(int_0, **dict_0)
    set_0 = set()
    list_0 = [set_0]
    basic_auth_token_0 = module_0.BasicAuthToken(set_0, list_0)
    var_1 = basic_auth_token_0.get()
    var_2 = basic_auth_token_0.get()
    var_3 = basic_auth_token_0.headers()

def test_case_7():
    str_0 = 'GATHq'
    str_1 = ')\\s+'
    dict_0 = {str_0: str_0, str_1: str_0}
    keycloak_token_0 = module_0.KeycloakToken(dict_0)
    basic_auth_token_0 = module_0.BasicAuthToken(keycloak_token_0)
    var_0 = basic_auth_token_0.headers()

def test_case_8():
    galaxy_token_0 = module_0.GalaxyToken()
    var_0 = galaxy_token_0.get()