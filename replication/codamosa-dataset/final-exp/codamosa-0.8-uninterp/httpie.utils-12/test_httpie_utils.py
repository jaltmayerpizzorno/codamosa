# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Set-Cookie'
    str_1 = 'cookie-nameN"cookie-value"; Path=/; Mx-Age=0'
    float_0 = -2560.245638
    dict_0 = {str_1: str_0, float_0: str_0, str_1: str_0, str_1: float_0}
    str_2 = module_0.repr_dict(dict_0)
    str_3 = (str_0, str_1)
    str_4 = [str_3]
    int_0 = 1561302290
    list_0 = module_0.get_expired_cookies(str_4, int_0)

def test_case_2():
    dict_0 = {}
    str_0 = module_0.repr_dict(dict_0)
    str_1 = ''
    str_2 = '\r5x?{E iI\x0b#'
    bool_0 = False
    var_0 = module_0.humanize_bytes(bool_0)
    list_0 = []
    list_1 = module_0.get_expired_cookies(list_0)
    tuple_0 = (str_2, str_1)
    list_2 = [tuple_0, tuple_0]
    float_0 = -1161.97
    list_3 = module_0.get_expired_cookies(list_2, float_0)
    explicit_null_auth_0 = module_0.ExplicitNullAuth()

def test_case_3():
    str_0 = 'qE,(%`QRkAJ#Ei#NH\x0b]:'
    dict_0 = {}
    explicit_null_auth_0 = module_0.ExplicitNullAuth(**dict_0)
    var_0 = explicit_null_auth_0.__call__(str_0)

def test_case_4():
    str_0 = 'Set-Cookie'
    str_1 = (str_0, str_0)
    str_2 = [str_1, str_1]
    int_0 = 1561302264
    list_0 = module_0.get_expired_cookies(str_2, int_0)

def test_case_5():
    str_0 = 'Set-Cookie'
    str_1 = 'cookiename="cookevlu"; Pth=/; x-Age=0'
    str_2 = (str_0, str_1)
    str_3 = [str_2, str_2]
    int_0 = 0
    list_0 = module_0.get_expired_cookies(str_3, int_0)

def test_case_6():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    dict_0 = {explicit_null_auth_0: explicit_null_auth_0, explicit_null_auth_0: explicit_null_auth_0}
    var_0 = explicit_null_auth_0.__call__(dict_0)
    str_0 = '`?K|QVd+tK>AO'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0]
    float_0 = 0.1
    list_1 = module_0.get_expired_cookies(list_0, float_0)

def test_case_7():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    dict_0 = {explicit_null_auth_0: explicit_null_auth_0, explicit_null_auth_0: explicit_null_auth_0}
    var_0 = explicit_null_auth_0.__call__(dict_0)
    str_0 = '`?K|QVd+tK>AO'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0]
    bool_0 = True
    var_1 = module_0.humanize_bytes(bool_0)
    float_0 = 0.1
    list_1 = module_0.get_expired_cookies(list_0, float_0)

def test_case_8():
    str_0 = 'example.txt.gz'
    str_1 = 'sxampld.txt.bz2'
    var_0 = module_0.get_content_type(str_1)
    str_2 = 'example.txt.xz'
    var_1 = module_0.get_content_type(str_2)
    var_2 = module_0.get_content_type(str_0)
    str_3 = 'example.txt.lzma'
    var_3 = module_0.get_content_type(str_3)
    str_4 = '-b'
    tuple_0 = (str_0, str_4)
    list_0 = [tuple_0, tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_9():
    str_0 = 'foo.txt'
    var_0 = module_0.get_content_type(str_0)
    str_1 = 'foo.html'
    var_1 = module_0.get_content_type(str_1)

def test_case_10():
    str_0 = 'Set-Cookie'
    str_1 = 'cookie-name="cookie-value"; Path=/; Max-Age=0'
    str_2 = (str_0, str_1)
    str_3 = [str_2, str_2]
    int_0 = 1561302264
    list_0 = module_0.get_expired_cookies(str_3, int_0)

def test_case_11():
    str_0 = 'Set-Cookie'
    str_1 = 'qookie-name="coBkie-valuer Path=/; Max-Age=i'
    str_2 = (str_0, str_1)
    str_3 = [str_2, str_2]
    int_0 = 1561302264
    list_0 = module_0.get_expired_cookies(str_3, int_0)