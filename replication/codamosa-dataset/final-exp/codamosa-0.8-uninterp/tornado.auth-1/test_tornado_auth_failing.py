# Automatically generated by Pynguin.
import tornado.auth as module_0

def test_case_0():
    try:
        str_0 = '{l\reTh'
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        str_0 = None
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin()
        any_0 = facebook_graph_mixin_0.facebook_request(str_0, **dict_0)
        open_id_mixin_0 = module_0.OpenIdMixin()
        async_h_t_t_p_client_0 = open_id_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        o_auth_mixin_0 = module_0.OAuthMixin(*list_0)
        async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_3():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect()
    except BaseException:
        pass

def test_case_4():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_5():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        dict_0 = open_id_mixin_0.get_authenticated_user()
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_6():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        list_0 = [o_auth2_mixin_0, o_auth2_mixin_0, o_auth2_mixin_0, o_auth2_mixin_0]
        auth_error_0 = module_0.AuthError(*list_0)
        o_auth2_mixin_0.authorize_redirect(auth_error_0)
    except BaseException:
        pass

def test_case_7():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        open_id_mixin_0 = module_0.OpenIdMixin()
        str_0 = 'I'
        str_1 = "Qi']8CE-x\\>\x0c <\n"
        str_2 = 'Z\x0b\tM7y%9l<'
        dict_0 = {}
        dict_1 = {str_0: o_auth2_mixin_0, str_1: str_1, str_2: dict_0}
        o_auth2_mixin_0.authorize_redirect(open_id_mixin_0, dict_1, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        open_id_mixin_0 = module_0.OpenIdMixin()
        str_0 = 'I'
        str_1 = '=k\tx'
        str_2 = 'O|c8dx\\\n&\\}i$'
        str_3 = ''
        dict_0 = {str_1: open_id_mixin_0, str_2: str_2, str_2: str_1, str_3: str_2}
        str_4 = 'Z5dF]x8GS'
        str_5 = 'qmTp"+\'~wuOf|G6wTG'
        dict_1 = {str_1: str_0, str_4: str_5}
        str_6 = 'a~'
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, dict_0, dict_1, str_6)
    except BaseException:
        pass