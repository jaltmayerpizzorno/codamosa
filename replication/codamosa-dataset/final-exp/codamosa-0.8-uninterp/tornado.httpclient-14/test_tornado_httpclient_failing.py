# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import tornado.httputil as module_1
import builtins as module_2

def test_case_0():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'GF,QI0PZ1[tcZg1j!8q;'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'xR?Re'
        bool_0 = True
        bool_1 = True
        bool_2 = False
        bool_3 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_0, bool_0, bool_1, bool_1, bool_2, bool_3)
        str_1 = '+TPSjRl(Sk\\'
        str_2 = ' c1$z6^_'
        dict_0 = {str_1: bool_3, str_2: bool_3, str_0: h_t_t_p_request_0}
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(h_t_t_p_request_0, **dict_0)
    except BaseException:
        pass

def test_case_2():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'http://www.google.com/'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'xR?Re'
        bool_0 = True
        bool_1 = True
        bool_2 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_0, bool_0, bool_1, bool_1, bool_0, bool_2)
        str_1 = '+TPSjRl(Sk\\'
        str_2 = ' c1$z6^_'
        dict_0 = {str_1: bool_2, str_2: bool_2, str_0: h_t_t_p_request_0}
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(h_t_t_p_request_0, **dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '+Nc3a'
        dict_0 = {str_0: str_0}
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.__del__()
        h_t_t_p_client_0.__del__()
        list_0 = []
        bool_0 = True
        str_1 = 'i3^'
        dict_1 = {str_0: str_0, str_1: dict_0}
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, dict_0, str_0, str_0, list_0, bool_0, str_0, str_0, str_0, dict_1)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'v9>v8S)\r6'
        str_1 = 'Return any remaining buffered data not yet returned by decompress.\n\n        Also checks for errors such as truncated input.\n        No other methods may be called on this object after `flush`.\n        '
        dict_0 = {str_0: str_1}
        int_0 = 1478
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        h_t_t_p_headers_0 = module_1.HTTPHeaders(**dict_0)
        bool_0 = False
        str_2 = "\x0bD(\reY8u^P'.V}6$uz;y"
        float_0 = 1046.0
        h_t_t_p_request_0 = module_0.HTTPRequest(str_2, str_1, h_t_t_p_headers_0, str_2, float_0, float_0, float_0, str_0, str_0, bool_0, str_2)
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_2, str_1)
        h_t_t_p_response_0.rethrow()
    except BaseException:
        pass

def test_case_6():
    try:
        module_0.main()
    except BaseException:
        pass

def test_case_7():
    try:
        module_0.main()
    except BaseException:
        pass

def test_case_8():
    try:
        int_0 = 404
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        int_1 = -692
        str_0 = h_t_t_p_client_error_0.__str__()
        h_t_t_p_client_error_1 = module_0.HTTPClientError(int_1)
        str_1 = 'ao<yyaipq.'
        str_2 = '__main__'
        str_3 = '>T`rfOkzhnhGU?'
        h_t_t_p_client_error_2 = module_0.HTTPClientError(int_0, str_3)
        bool_0 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_3, str_1, bool_0, str_0, str_2)
        base_exception_0 = module_2.BaseException()
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_1, base_exception_0)
        str_4 = h_t_t_p_response_0.__repr__()
        str_5 = h_t_t_p_client_error_1.__str__()
        h_t_t_p_client_error_3 = module_0.HTTPClientError(int_0, str_3)
        str_6 = h_t_t_p_client_error_3.__str__()
        module_0.main()
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'q@Bs\\c[G1V$'
        h_t_t_p_client_0 = module_0.HTTPClient(str_0)
    except BaseException:
        pass