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
        var_0 = galaxy_token_0.set(galaxy_token_0)
    except BaseException:
        pass

def test_case_2():
    try:
        no_token_sentinel_0 = module_0.NoTokenSentinel()
        basic_auth_token_0 = module_0.BasicAuthToken(no_token_sentinel_0)
        dict_0 = None
        var_0 = basic_auth_token_0.get()
        galaxy_token_0 = module_0.GalaxyToken(dict_0)
        galaxy_token_1 = module_0.GalaxyToken()
        var_1 = galaxy_token_1.headers()
        dict_1 = {basic_auth_token_0: basic_auth_token_0}
        var_2 = basic_auth_token_0.get()
        var_3 = galaxy_token_1.set(dict_1)
    except BaseException:
        pass

def test_case_3():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.headers()
        basic_auth_token_0 = module_0.BasicAuthToken(galaxy_token_0)
        var_1 = basic_auth_token_0.headers()
        bytes_0 = b'\x9d\xed\x90\xdc\xe0'
        keycloak_token_0 = module_0.KeycloakToken(bytes_0)
        var_2 = keycloak_token_0.get()
    except BaseException:
        pass

def test_case_4():
    try:
        bytes_0 = b'<5k\xbe\x88'
        str_0 = ':&2'
        basic_auth_token_0 = module_0.BasicAuthToken(bytes_0, str_0)
        var_0 = basic_auth_token_0.get()
        galaxy_token_0 = module_0.GalaxyToken()
        var_1 = galaxy_token_0.headers()
        var_2 = galaxy_token_0.set(galaxy_token_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'test_access_token'
        str_1 = 'https://auth.example.com'
        bool_0 = False
        str_2 = 'test_client'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1, bool_0, str_2)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'dummy_access_token'
        str_1 = 'https://auth.exampe.com'
        bool_0 = True
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1, bool_0)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_7():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.headers()
    except BaseException:
        pass