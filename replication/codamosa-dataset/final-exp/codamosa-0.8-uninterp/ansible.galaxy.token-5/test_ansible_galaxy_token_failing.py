# Automatically generated by Pynguin.
import ansible.galaxy.token as module_0

def test_case_0():
    try:
        keycloak_token_0 = module_0.KeycloakToken()
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_1():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        list_0 = [galaxy_token_0]
        var_0 = galaxy_token_0.set(list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        list_0 = [galaxy_token_0]
        tuple_0 = (list_0,)
        tuple_1 = (tuple_0,)
        str_0 = 'Q'
        basic_auth_token_0 = module_0.BasicAuthToken(str_0)
        basic_auth_token_1 = module_0.BasicAuthToken(list_0, tuple_1)
        basic_auth_token_2 = module_0.BasicAuthToken(list_0)
        var_0 = basic_auth_token_2.get()
        galaxy_token_1 = module_0.GalaxyToken()
        list_1 = [galaxy_token_1, galaxy_token_1]
        galaxy_token_2 = module_0.GalaxyToken()
        var_1 = basic_auth_token_2.headers()
        var_2 = galaxy_token_1.headers()
        var_3 = galaxy_token_1.set(list_1)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '`,%,Xo2NJviac@t'
        list_0 = [str_0, str_0, str_0]
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
        no_token_sentinel_0 = module_0.NoTokenSentinel(*list_0, **dict_0)
        dict_1 = {str_0: str_0, str_0: str_0, str_0: str_0}
        basic_auth_token_0 = module_0.BasicAuthToken(dict_1)
        var_0 = basic_auth_token_0.headers()
        galaxy_token_0 = module_0.GalaxyToken(basic_auth_token_0)
        galaxy_token_1 = module_0.GalaxyToken()
        var_1 = galaxy_token_1.headers()
        keycloak_token_0 = module_0.KeycloakToken(basic_auth_token_0)
        var_2 = galaxy_token_1.headers()
        galaxy_token_2 = module_0.GalaxyToken()
        var_3 = galaxy_token_2.set(no_token_sentinel_0)
        var_4 = galaxy_token_0.headers()
        var_5 = basic_auth_token_0.get()
        no_token_sentinel_1 = module_0.NoTokenSentinel(**dict_1)
        no_token_sentinel_2 = module_0.NoTokenSentinel(*list_0)
        var_6 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'abc'
        str_1 = 'https://example.com'
        bool_0 = False
        str_2 = 'example'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1, bool_0, str_2)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '12345'
        str_1 = 'http://foo.com'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1)
        var_0 = keycloak_token_0.get()
    except BaseException:
        pass