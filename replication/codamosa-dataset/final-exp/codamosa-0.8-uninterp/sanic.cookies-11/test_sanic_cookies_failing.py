# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    try:
        int_0 = -417
        float_0 = 42.2
        cookie_jar_0 = module_0.CookieJar(float_0)
        var_0 = cookie_jar_0.__delitem__(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'N'
        bytes_0 = b'\x84\xd4\x95\x00\xa7\x95\x93FHU\x82DP\xd5'
        cookie_jar_0 = module_0.CookieJar(bytes_0)
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        float_0 = 743.5
        dict_0 = {}
        cookie_0 = module_0.Cookie(float_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'ih!1aCf>%'
        tuple_0 = ()
        cookie_jar_0 = module_0.CookieJar(tuple_0)
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'username'
        str_1 = 'user@example.com'
        cookie_0 = module_0.Cookie(str_0, str_1)
        bool_0 = False
        var_0 = cookie_0.encode(bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = 1447.642697
        cookie_jar_0 = module_0.CookieJar(float_0)
        str_0 = 'expires'
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'value'
        cookie_0 = module_0.Cookie(str_0, str_0)
        var_0 = str(cookie_0)
        var_1 = cookie_0.__str__()
        str_1 = 'key="value_with_no_legal_char"'
        cookie_jar_0 = None
        var_2 = cookie_0.__setitem__(str_1, cookie_jar_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'key'
        str_1 = 'value'
        cookie_0 = module_0.Cookie(str_0, str_1)
        str_2 = None
        cookie_1 = module_0.Cookie(str_0, str_2)
        var_0 = str(cookie_1)
        bool_0 = False
        int_0 = -2000
        cookie_jar_0 = module_0.CookieJar(int_0)
        var_1 = cookie_jar_0.__delitem__(bool_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'value'
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = '^'
        var_0 = cookie_0.__str__()
        var_1 = str(cookie_0)
        str_2 = 'expires'
        var_2 = cookie_0.__setitem__(str_2, str_1)
    except BaseException:
        pass