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
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.headers()
        galaxy_token_1 = module_0.GalaxyToken()
        str_0 = '!E^'
        str_1 = '\x0c9m\x0cwp(u`'
        var_1 = galaxy_token_1.headers()
        dict_0 = {str_0: galaxy_token_1, str_0: str_0, str_1: galaxy_token_1}
        set_0 = {str_0, str_1}
        no_token_sentinel_0 = module_0.NoTokenSentinel(**dict_0)
        var_2 = no_token_sentinel_0.__new__(set_0)
        float_0 = -2806.0
        bytes_0 = b''
        basic_auth_token_0 = module_0.BasicAuthToken(float_0, bytes_0)
        galaxy_token_2 = module_0.GalaxyToken()
        var_3 = galaxy_token_1.set(galaxy_token_2)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '&\nQFm\rb`HBid.+U;]'
        keycloak_token_0 = module_0.KeycloakToken(str_0)
        basic_auth_token_0 = module_0.BasicAuthToken(str_0)
        var_0 = basic_auth_token_0.headers()
        bool_0 = True
        var_1 = basic_auth_token_0.get()
        galaxy_token_0 = module_0.GalaxyToken(bool_0)
        var_2 = galaxy_token_0.get()
        galaxy_token_1 = module_0.GalaxyToken()
        var_3 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_4():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.get()
        list_0 = []
        no_token_sentinel_0 = module_0.NoTokenSentinel(*list_0)
        var_1 = galaxy_token_0.set(no_token_sentinel_0)
        var_2 = galaxy_token_0.set(galaxy_token_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'my_acess_toke'
        str_1 = 'http://example.com'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'abcdefg'
        str_1 = 'https://keycloak.example.com/auth/realms/redhat/protocol/openid-connect/token'
        bool_0 = True
        str_2 = 'cloud-services'
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_1, bool_0, str_2)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_7():
    try:
        galaxy_token_0 = module_0.GalaxyToken()
        var_0 = galaxy_token_0.get()
    except BaseException:
        pass