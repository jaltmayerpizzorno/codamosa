# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import tornado.httputil as module_1

def test_case_0():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = '6}od>dTsP*Copjz'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()
        module_0.main()
    except BaseException:
        pass

def test_case_2():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'https://www.google.com/'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_3():
    try:
        module_0.main()
    except BaseException:
        pass

def test_case_4():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'https://www.oogle.com/'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
        var_0 = h_t_t_p_response_0.body
        var_1 = print(var_0)
        h_t_t_p_response_0.rethrow()
        dict_0 = {str_0: h_t_t_p_client_0, h_t_t_p_client_0: h_t_t_p_response_0}
        h_t_t_p_client_1 = module_0.HTTPClient(dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '?>jv,O-Y902x0\x0cQu0%"'
        bool_0 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_0, bool_0, str_0, str_0, bool_0, bool_0, bool_0)
        str_1 = 'g\r=9j~h3jY\tJ'
        str_2 = '^n8jAmH\x0c/-M\x0c 2ibK'
        str_3 = '%kM!zD3)'
        dict_0 = {str_1: str_1, str_2: h_t_t_p_request_0, str_2: str_0, str_3: h_t_t_p_request_0}
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(h_t_t_p_request_0, **dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'https://www.oogle.com/'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
        var_0 = h_t_t_p_response_0.body
        int_0 = 1552
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        int_1 = 982
        h_t_t_p_client_error_1 = module_0.HTTPClientError(int_1, str_0)
        bytes_0 = b'\xa4<\x99A\x14\xb5i'
        float_0 = 1773.7801
        int_2 = 2749
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_0, bytes_0, float_0, int_2, bool_0)
        h_t_t_p_headers_0 = module_1.HTTPHeaders()
        str_1 = None
        dict_0 = {str_1: float_0}
        h_t_t_p_response_1 = module_0.HTTPResponse(h_t_t_p_request_0, int_2, h_t_t_p_headers_0, float_0, dict_0, str_0, float_0)
        h_t_t_p_response_1.rethrow()
    except BaseException:
        pass