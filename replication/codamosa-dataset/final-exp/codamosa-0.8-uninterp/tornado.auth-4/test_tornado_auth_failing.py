# Automatically generated by Pynguin.
import tornado.auth as module_0

def test_case_0():
    try:
        str_0 = '$'
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect(str_0)
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
        o_auth2_mixin_0.authorize_redirect()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'help'
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        o_auth2_mixin_0.authorize_redirect(str_0, str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        async_h_t_t_p_client_0 = o_auth2_mixin_0.get_auth_http_client()
    except BaseException:
        pass

def test_case_7():
    try:
        o_auth_mixin_0 = module_0.OAuthMixin()
        open_id_mixin_0 = module_0.OpenIdMixin()
        open_id_mixin_0.authenticate_redirect()
    except BaseException:
        pass

def test_case_8():
    try:
        o_auth2_mixin_0 = module_0.OAuth2Mixin()
        str_0 = 'U$upc^>{R/Y>Z'
        str_1 = ")[-6'fC=C"
        str_2 = 'L87.#5!g,07NE?BJeU!S'
        list_0 = [str_1, str_2]
        str_3 = "shouldn't happen: _handle_events without self._state"
        o_auth2_mixin_0.authorize_redirect(str_0, str_1, list_0, str_3)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = "WgP'd1~fy9U*)kj@fce"
        list_0 = []
        o_auth2_mixin_0 = module_0.OAuth2Mixin(*list_0)
        any_0 = o_auth2_mixin_0.oauth2_request(str_0)
        str_1 = 'help'
        optional_0 = None
        o_auth2_mixin_0.authorize_redirect(str_1, str_1, str_1, optional_0, str_0)
    except BaseException:
        pass