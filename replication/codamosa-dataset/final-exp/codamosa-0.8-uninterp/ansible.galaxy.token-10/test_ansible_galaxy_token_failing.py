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
        set_0 = {galaxy_token_0, galaxy_token_0}
        var_0 = galaxy_token_0.set(set_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = ''
        bool_0 = True
        keycloak_token_0 = module_0.KeycloakToken(str_0, str_0, bool_0, str_0)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'https://sso.redhat.com/auth'
        str_1 = 'test-access-token'
        keycloak_token_0 = module_0.KeycloakToken(str_1, str_0)
        var_0 = keycloak_token_0.headers()
    except BaseException:
        pass