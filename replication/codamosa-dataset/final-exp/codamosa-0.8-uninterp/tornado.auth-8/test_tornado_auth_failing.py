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
        list_0 = []
        open_id_mixin_0 = module_0.OpenIdMixin(*list_0)
        async_h_t_t_p_client_0 = open_id_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = []
        str_0 = 'ziwVfGre\r#h*~Z;5Ps@='
        str_1 = '{Q{6Y?'
        str_2 = 'aL3~}'
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin()
        facebook_graph_mixin_1 = module_0.FacebookGraphMixin()
        optional_0 = facebook_graph_mixin_1.get_authenticated_user(str_0, str_1, str_0, str_2, facebook_graph_mixin_0)
        twitter_mixin_0 = module_0.TwitterMixin()
        dict_0 = {}
        o_auth_mixin_0 = module_0.OAuthMixin(*list_0, **dict_0)
        async_h_t_t_p_client_0 = o_auth_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_3():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'tDad\r<&J%{\t'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        str_0 = 'Ldj'
        o_auth2_mixin_0.authorize_redirect(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '3i>k|S5'
        str_1 = None
        str_2 = None
        facebook_graph_mixin_0 = module_0.FacebookGraphMixin()
        str_3 = "$W'g'NV<+(}Ii3?i"
        str_4 = '1tYY\\roAl)"'
        str_5 = 'Provides the errno from an Exception object.\n\n    There are cases that the errno attribute was not set so we pull\n    the errno out of the args but if someone instantiates an Exception\n    without any args you will get a tuple error. So this function\n    abstracts all that behavior to give you a safe way to get the\n    errno.\n    '
        none_type_0 = None
        optional_0 = facebook_graph_mixin_0.get_authenticated_user(str_3, str_4, str_5, str_2, none_type_0)
        optional_1 = facebook_graph_mixin_0.get_authenticated_user(str_0, str_1, str_2, str_1)
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'x*ON}'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        optional_0 = None
        str_1 = 'N(ptj]p@+"a_#HL?gC|'
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, optional_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        open_id_mixin_0 = module_0.OpenIdMixin()
        bytes_0 = b'\xb7\xc3\xe4\xaf\xad'
        open_id_mixin_0.authenticate_redirect(bytes_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'TY\nh,PZU_Y|=['
        str_1 = 'j$PjPP'
        str_2 = '.p'
        dict_0 = {str_1: str_1, str_1: str_2}
        str_3 = '6e'
        list_0 = []
        o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0)
        o_auth2_mixin_0.authorize_redirect(str_0, str_0, str_0, dict_0, str_3)
    except BaseException:
        pass