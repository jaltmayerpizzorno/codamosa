# Automatically generated by Pynguin.
import tornado.auth as module_0

def test_case_0():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect()
    except BaseException:
        pass

def test_case_1():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        async_h_t_t_p_client_0 = open_id_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_2():
    try:
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin()
        o_auth_mixin_0 = module_0.OAuthMixin()
        str_0 = 'text/html; charset=UTF-8'
        str_1 = 'https://www.googleapis.com/oauth2/v1/userinfo'
        int_0 = 6
        twitter_mixin_0 = module_0.TwitterMixin()
        str_2 = 'p>v\\}Q["KMb9=n}WG(p'
        str_3 = 'PThBg:}u='
        dict_0 = {str_1: int_0, str_2: facebook_graph_mixin_0, str_3: str_3}
        dict_1 = {}
        any_0 = facebook_graph_mixin_0.facebook_request(str_0, dict_0, **dict_1)
        async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'I|BSKUF\\'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'k`Rtxla0a'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0, str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin()
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_6():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'H-.;r6/]lH5.gdq'
        optional_0 = None
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, optional_0, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'k`Rtxa0a'
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect(str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'k`Rtxla0a'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        list_0 = []
        str_1 = ',\rBa'
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, str_0, list_0, str_1)
    except BaseException:
        pass