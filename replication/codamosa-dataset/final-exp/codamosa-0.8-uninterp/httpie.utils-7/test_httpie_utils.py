# Automatically generated by Pynguin.
import httpie.utils as module_0

def test_case_0():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()

def test_case_1():
    dict_0 = {}
    str_0 = module_0.repr_dict(dict_0)

def test_case_2():
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    str_0 = 'dest'
    explicit_null_auth_1 = module_0.ExplicitNullAuth()
    var_0 = explicit_null_auth_1.__call__(str_0)

def test_case_3():
    str_0 = 'text.txt'
    var_0 = module_0.get_content_type(str_0)

def test_case_4():
    list_0 = []
    list_1 = module_0.get_expired_cookies(list_0)

def test_case_5():
    str_0 = 'JSESSIONID=C2065EBB17D6C0FE7D4023B1644D9F92; Path=/api/; HttpOnly; Secure'
    str_1 = 'Set-Cookie'
    str_2 = (str_1, str_0)
    str_3 = [str_2]
    list_0 = module_0.get_expired_cookies(str_3)

def test_case_6():
    str_0 = 'foo.png'
    var_0 = module_0.get_content_type(str_0)
    str_1 = 'foo.json'
    var_1 = module_0.get_content_type(str_1)
    str_2 = 'foo.txt'
    var_2 = module_0.get_content_type(str_2)
    str_3 = 'foo.txt.gz'
    var_3 = module_0.get_content_type(str_3)
    str_4 = 'foo.gz'
    var_4 = module_0.get_content_type(str_4)

def test_case_7():
    str_0 = 'set-cookie'
    str_1 = 'euconsent=foo; Max-Age=10'
    str_2 = (str_0, str_1)
    str_3 = (str_0, str_0)
    str_4 = [str_2, str_3]
    int_0 = 99981
    list_0 = module_0.get_expired_cookies(str_4, int_0)

def test_case_8():
    str_0 = 'set-cookie'
    str_1 = 'euconsent=foo; Max-Age=10'
    str_2 = (str_0, str_1)
    str_3 = "/e\t'OTGI~y%"
    str_4 = (str_3, str_0)
    str_5 = [str_2, str_4]
    int_0 = 100005
    list_0 = module_0.get_expired_cookies(str_5, int_0)

def test_case_9():
    float_0 = 1080.76
    var_0 = module_0.humanize_bytes(float_0)
    str_0 = '7\nO(Wd~}g}K"`!Au=3!2'
    var_1 = module_0.get_content_type(str_0)
    tuple_0 = ()
    explicit_null_auth_0 = module_0.ExplicitNullAuth()
    var_2 = explicit_null_auth_0.__call__(tuple_0)

def test_case_10():
    str_0 = 'set-cookie'
    str_1 = 'SESSION_ID="PsAjNg5IOW8="; expires=Tue, 15 Jan 2019 21:47:38 GMT; path=/'
    str_2 = (str_0, str_1)
    str_3 = [str_2]
    list_0 = module_0.get_expired_cookies(str_3)

def test_case_11():
    str_0 = 'set-cookie'
    str_1 = 'euconsent=foo; Max-Age=J0'
    str_2 = (str_0, str_1)
    str_3 = 'Set-Cookie'
    str_4 = (str_3, str_0)
    str_5 = [str_2, str_4]
    int_0 = 99989
    list_0 = module_0.get_expired_cookies(str_5, int_0)
    int_1 = 100005
    list_1 = module_0.get_expired_cookies(str_5, int_1)