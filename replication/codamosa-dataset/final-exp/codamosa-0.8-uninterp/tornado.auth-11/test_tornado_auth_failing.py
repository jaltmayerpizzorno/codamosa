# Automatically generated by Pynguin.
import tornado.auth as module_0
import tornado.httputil as module_1

def test_case_0():
    try:
        dict_0 = {}
        open_id_mixin_0 = module_0.OpenIdMixin(**dict_0)
        open_id_mixin_0.authenticate_redirect()
    except BaseException:
        pass

def test_case_1():
    try:
        twitter_mixin_0 = module_0.TwitterMixin()
        dict_0 = {}
        twitter_mixin_0.authenticate_redirect()
        str_0 = '5*|z\t-O9)Qs2'
        set_0 = set()
        dict_1 = {str_0: set_0}
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        any_0 = o_auth2_mixin_0.oauth2_request(str_0, **dict_1)
        open_id_mixin_0 = module_0.OpenIdMixin(**dict_0)
        async_h_t_t_p_client_0 = open_id_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_2():
    try:
        o_auth_mixin_0 = module_0.OAuthMixin()
        async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_3():
    try:
        dict_0 = {}
        open_id_mixin_0 = module_0.OpenIdMixin(**dict_0)
        str_0 = 'G\x0c5Lg"ul*zl1^x6RbZPp'
        o_auth2_mixin_0 = module_0.OAuth2Mixin(**dict_0)
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        list_0 = []
        h_t_t_p_headers_0 = module_1.HTTPHeaders(*list_0)
        bytes_0 = b'\x1fT\x1e\xdf\x18'
        bytes_1 = b'C\xacJ'
        list_1 = []
        str_0 = 'I|JMtGdeeV\r}'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(h_t_t_p_headers_0, bytes_0, bytes_1, list_1, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_6():
    try:
        o_auth_mixin_0 = module_0.OAuthMixin()
        o_auth_mixin_0.authorize_redirect()
        dict_0 = o_auth_mixin_0.get_authenticated_user()
        list_0 = []
        o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0)
        open_id_mixin_0 = module_0.OpenIdMixin()
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_7():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        str_0 = 'https://localhost'
        open_id_mixin_0.authenticate_redirect(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        h_t_t_p_headers_0 = module_1.HTTPHeaders()
        h_t_t_p_headers_1 = h_t_t_p_headers_0.copy()
        iterator_0 = h_t_t_p_headers_0.__iter__()
        str_0 = ''
        str_1 = 'filename'
        google_o_auth2_mixin_0 = module_0.GoogleOAuth2Mixin()
        dict_0 = google_o_auth2_mixin_0.get_authenticated_user(str_0, str_1)
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        str_2 = 'clear'
        dict_1 = {str_2: str_0, str_1: h_t_t_p_headers_0}
        o_auth2_mixin_0.authorize_redirect(str_1, str_1, str_0, dict_1)
    except BaseException:
        pass