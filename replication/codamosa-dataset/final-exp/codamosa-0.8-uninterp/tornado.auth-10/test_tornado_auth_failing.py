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
        o_auth_mixin_0 = module_0.OAuthMixin()
        async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_3():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '=(BN[rwn&n'
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '=(BN[rwn&n'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'I,.z0rq^KTK=pE'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '=(BN[rwn&n'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        dict_0 = {str_0: o_auth2_mixin_0}
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '=(BN[rwn&n'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        list_0 = []
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin(*list_0)
        any_0 = facebook_graph_mixin_0.facebook_request(str_0)
        optional_0 = None
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, str_0, optional_0, str_0)
    except BaseException:
        pass