# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    pass

def test_case_1():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    str_0 = 'z=^`_\x0bs2\x0cUSb:K[Rd'
    var_0 = module_0.get_content_type(str_0)
    set_0 = set()
    dict_0 = {explicit_null_auth_0: set_0, var_0: explicit_null_auth_0, str_0: set_0, var_0: var_0}
    str_1 = module_0.repr_dict(dict_0)

def test_case_2():
    str_0 = ')/@&bj'
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    var_0 = explicit_null_auth_0.__call__(str_0)

def test_case_3():
    str_0 = '../README.md'
    var_0 = module_0.get_content_type(str_0)

def test_case_4():
    str_0 = '|a{0[<D`5'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_5():
    str_0 = 'd'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    float_0 = -4189.2786
    list_1 = module_0.get_expired_cookies(list_0, float_0)

def test_case_6():
    str_0 = '>"=?u)v8'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0)
    float_0 = 1709.6995
    var_0 = module_0.humanize_bytes(float_0)

def test_case_7():
    str_0 = 'Set-Cookie'
    str_1 = 'foo=bar; path=/; Max-Age=60'
    str_2 = (str_0, str_1)
    bool_0 = True
    var_0 = module_0.humanize_bytes(bool_0)
    str_3 = 'baz=qux; path=/; expires=Sun, 01 Jan 2018 00:00:00 GMT'
    str_4 = (str_0, str_3)
    str_5 = 'abc=def; path=/; expires=Sun, 01 Jan 1970 00:00:00 GMT'
    str_6 = '/3J'
    var_1 = module_0.get_content_type(str_6)
    str_7 = (str_0, str_5)
    str_8 = [str_2, str_4, str_7]
    int_0 = 0
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    list_0 = module_0.get_expired_cookies(str_8, int_0)

def test_case_8():
    str_0 = 'teBt.json'
    var_0 = module_0.get_content_type(str_0)

def test_case_9():
    str_0 = 'Set-Cookie'
    str_1 = 'foo=bar; path=/; Max-Age=60'
    str_2 = (str_0, str_1)
    str_3 = (str_0, str_1)
    str_4 = (str_0, str_0)
    str_5 = [str_2, str_3, str_4]
    int_0 = 0
    list_0 = module_0.get_expired_cookies(str_5, int_0)

def test_case_10():
    str_0 = 'Set-Cookie'
    str_1 = 'foo=bar; path=/; Max-Age=60'
    str_2 = (str_0, str_1)
    str_3 = 'baz=qux; path=/; expires=Sun, 01 Jan 2018 00:00:00 GMT'
    str_4 = (str_0, str_3)
    str_5 = 'abc=def; path=/; expires=Sun, 01 Jan 1970 00:00:00 GMT'
    str_6 = (str_0, str_5)
    str_7 = [str_2, str_4, str_6]
    int_0 = 0
    list_0 = module_0.get_expired_cookies(str_7, int_0)

def test_case_11():
    str_0 = 'index.html'
    var_0 = module_0.get_content_type(str_0)
    str_1 = 'index.html.gz'
    var_1 = module_0.get_content_type(str_1)

def test_case_12():
    str_0 = 'Set-Cookie'
    str_1 = 'foo=bar; path=/; Max-Age=<0'
    str_2 = (str_0, str_1)
    str_3 = 'baz=qux; path=/; expires=Sun, 01 Jan 2018 00:00:00 GMT'
    str_4 = (str_0, str_3)
    str_5 = '[)svK:T?x`"k'
    str_6 = '/3J'
    dict_0 = {str_4: str_3, str_5: str_1}
    str_7 = module_0.repr_dict(dict_0)
    var_0 = module_0.get_content_type(str_6)
    str_8 = (str_0, str_5)
    str_9 = [str_2, str_4, str_8]
    int_0 = 0
    list_0 = module_0.get_expired_cookies(str_9, int_0)