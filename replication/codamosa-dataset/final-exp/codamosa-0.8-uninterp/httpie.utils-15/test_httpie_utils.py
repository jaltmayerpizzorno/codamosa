# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()

def test_case_1():
    bytes_0 = b'\x91\xcf\x8e'
    int_0 = 908
    float_0 = 587.898
    tuple_0 = (int_0, float_0, float_0)
    dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0, tuple_0: int_0}
    str_0 = module_0.repr_dict(dict_0)

def test_case_2():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    bytes_0 = b'\xcd#'
    var_0 = explicit_null_auth_0.__call__(bytes_0)
    dict_0 = {}
    str_0 = module_0.repr_dict(dict_0)
    var_1 = module_0.get_content_type(str_0)

def test_case_3():
    str_0 = 'filename.html'
    var_0 = module_0.get_content_type(str_0)
    var_1 = module_0.get_content_type(str_0)
    str_1 = 'filename.html.x'
    var_2 = module_0.get_content_type(str_1)

def test_case_4():
    list_0 = []
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_5():
    str_0 = 'Set-Cookie'
    str_1 = 'a=1; Path=/; Max-Age=2'
    str_2 = (str_0, str_1)
    str_3 = [str_2, str_2, str_2]
    int_0 = -3
    list_0 = module_0.get_expired_cookies(str_3, int_0)

def test_case_6():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    explicit_null_auth_1 = module_0.ExplicitNullAuth()
    bytes_0 = b'\xcd#'
    var_0 = explicit_null_auth_1.__call__(bytes_0)
    int_0 = 1073741824
    var_1 = module_0.humanize_bytes(int_0)
    str_0 = '7\t 4|m'
    var_2 = module_0.get_content_type(str_0)

def test_case_7():
    str_0 = 'Q;3 y'
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    int_0 = -1324
    var_0 = module_0.humanize_bytes(int_0)
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0)
    var_1 = explicit_null_auth_0.__call__(explicit_null_auth_0)
    bytes_0 = b'\xcd#'
    var_2 = explicit_null_auth_0.__call__(bytes_0)

def test_case_8():
    str_0 = 'foo.txt'
    var_0 = module_0.get_content_type(str_0)
    str_1 = 'foo.txt.gz'
    var_1 = module_0.get_content_type(str_1)
    str_2 = 'foo.txt.bz2'
    var_2 = module_0.get_content_type(str_2)

def test_case_9():
    str_0 = 'set-cookie'
    str_1 = 'session=.eJyrVkpVkpVslJQAQ7; Domain=mydomain.com; Expires=Sun, 07 Apr 2019 17:13:03 GMT; Max-Age=604800; Path=/'
    str_2 = (str_0, str_1)
    str_3 = 'country=US; Domain=mydomain.com; Expires=Sat, 06 Apr 2019 17:13:03 GMT; Max-Age=86400; Path=/'
    str_4 = (str_0, str_3)
    str_5 = [str_2, str_4]
    list_0 = module_0.get_expired_cookies(str_5)

def test_case_10():
    str_0 = '{X'
    str_1 = 'set-cookie'
    str_2 = (str_1, str_0)
    str_3 = [str_2]
    float_0 = 1517285308.362332
    list_0 = module_0.get_expired_cookies(str_3, float_0)
    list_1 = module_0.get_expired_cookies(str_3, float_0)