# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    list_0 = []
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_1():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    str_0 = module_0.repr_dict(dict_0)

def test_case_2():
    list_0 = []
    list_1 = module_0.get_expired_cookies(list_0)
    bool_0 = None
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    var_0 = explicit_null_auth_0.__call__(bool_0)

def test_case_3():
    str_0 = 'a.wav'
    var_0 = module_0.get_content_type(str_0)

def test_case_4():
    str_0 = 'PrXE_&Ie.ta'
    str_1 = 'x{L|GjYv3y!'
    tuple_0 = (str_0, str_1)
    list_0 = [tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_5():
    str_0 = 'a.wav'
    str_1 = '\t\x0cu2qL_!x;I'
    tuple_0 = (str_0, str_1)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    list_1 = module_0.get_expired_cookies(list_0, str_1)
    var_0 = module_0.get_content_type(str_0)

def test_case_6():
    dict_0 = {}
    str_0 = 'HbT]1W'
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0]
    explicit_null_auth_0 = module_0.ExplicitNullAuth(**dict_0)
    int_0 = 1220
    var_0 = module_0.humanize_bytes(int_0)
    bool_0 = False
    var_1 = explicit_null_auth_0.__call__(bool_0)
    list_1 = module_0.get_expired_cookies(list_0)
    dict_1 = {}
    str_1 = module_0.repr_dict(dict_1)
    float_0 = 610.0
    var_2 = module_0.humanize_bytes(float_0)
    str_2 = 'my8"wH)J>Z'
    var_3 = explicit_null_auth_0.__call__(str_2)
    list_2 = module_0.get_expired_cookies(list_0)

def test_case_7():
    str_0 = 'foo.pdf'
    var_0 = module_0.get_content_type(str_0)
    str_1 = 'foo.tar.gz'
    var_1 = module_0.get_content_type(str_1)
    str_2 = 'foo.png'
    var_2 = module_0.get_content_type(str_2)
    str_3 = 'foo.xlsx'
    var_3 = module_0.get_content_type(str_3)
    str_4 = 'foo.xls'
    var_4 = module_0.get_content_type(str_4)
    str_5 = 'foo.docx'
    var_5 = module_0.get_content_type(str_5)
    str_6 = 'foo.doc'
    var_6 = module_0.get_content_type(str_6)

def test_case_8():
    str_0 = 'Set-Cookie'
    str_1 = 'logged_in=no; Max-Age=0; expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/; Secure; HttpOnly'
    str_2 = (str_0, str_1)
    str_3 = [str_2]
    list_0 = module_0.get_expired_cookies(str_3)
    var_0 = type(list_0)
    str_4 = 'logged_in=no; Max-Age=-1; Path=/; Secure; HttpOnly'
    str_5 = (str_0, str_4)
    str_6 = [str_5]
    list_1 = module_0.get_expired_cookies(str_6)

def test_case_9():
    str_0 = 'Set-Cookie'
    str_1 = 'foo=bar'
    str_2 = (str_0, str_1)
    str_3 = 'lang=en-US; Max-Age=86400; path=/'
    str_4 = (str_0, str_3)
    str_5 = 'cookie_test=test; Domain=.example.com; Path=/; Secure; Expires=Sun, 15-May-2016 16:46:54 GMT; Max-Age=86400'
    str_6 = (str_0, str_5)
    str_7 = [str_2, str_4, str_6]
    int_0 = 1463336000
    list_0 = module_0.get_expired_cookies(str_7, int_0)