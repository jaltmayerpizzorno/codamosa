# Automatically generated by Pynguin.
import sanic.cookies as module_0

def test_case_0():
    try:
        str_0 = '\x0b<.\n8;%Ws|?AEA\x0cfSf'
        float_0 = -864.9
        cookie_jar_0 = module_0.CookieJar(float_0)
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'Sr'
        bool_0 = True
        cookie_jar_0 = module_0.CookieJar(bool_0)
        var_0 = cookie_jar_0.__delitem__(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'cund'
        cookie_0 = module_0.Cookie(str_0, str_0)
        var_0 = cookie_0.__str__()
        str_1 = 'expires'
        cookie_jar_0 = module_0.CookieJar(str_1)
        var_1 = cookie_jar_0.__delitem__(str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        float_0 = 1757.95
        cookie_jar_0 = module_0.CookieJar(float_0)
        str_0 = 'F#'
        str_1 = 'ggc/OQzxq&(]_k\x0bRB0'
        cookie_0 = module_0.Cookie(str_0, str_1)
        var_0 = cookie_0.encode(cookie_jar_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'chunked'
        cookie_0 = module_0.Cookie(str_0, str_0)
        var_0 = cookie_0.__str__()
        bytes_0 = b''
        bool_0 = True
        var_1 = cookie_0.__setitem__(bytes_0, bool_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'testcookie'
        str_1 = 'Banshee'
        cookie_0 = module_0.Cookie(str_0, str_1)
        str_2 = 'path'
        str_3 = '/'
        var_0 = cookie_0.__setitem__(str_2, str_3)
        str_4 = 'max-age'
        str_5 = '43200'
        var_1 = cookie_0.__setitem__(str_4, str_5)
        str_6 = 'expires'
        str_7 = 'Wed, 19-Aug-2021 05:34:28 GMT'
        var_2 = cookie_0.__setitem__(str_6, str_7)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'chunked'
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = 'max-age'
        var_0 = cookie_0.__setitem__(str_1, str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'hunked'
        str_1 = None
        cookie_0 = module_0.Cookie(str_0, str_1)
        var_0 = cookie_0.__str__()
        str_2 = 'max-age'
        var_1 = cookie_0.__setitem__(str_2, str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'Test_Cookie'
        cookie_0 = module_0.Cookie(str_0, str_0)
        str_1 = 'expires'
        var_0 = cookie_0.__setitem__(str_1, str_1)
    except BaseException:
        pass