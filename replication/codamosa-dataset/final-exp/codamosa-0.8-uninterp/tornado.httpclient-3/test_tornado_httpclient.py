# Automatically generated by Pynguin.
import tornado.httpclient as module_0

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_2():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_3():
    str_0 = 'http://example.com'
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0)

def test_case_4():
    int_0 = 3600
    float_0 = -706.0
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0, float_0)
    str_0 = h_t_t_p_client_error_0.__str__()

def test_case_5():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.sina.com.cn/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    h_t_t_p_client_0.close()
    int_0 = 609
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
    var_0 = h_t_t_p_response_0.body
    h_t_t_p_client_1 = module_0.HTTPClient()
    h_t_t_p_client_2 = module_0.HTTPClient()
    h_t_t_p_client_2.close()

def test_case_6():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.sina.com.cn/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)

def test_case_7():
    none_type_0 = None
    none_type_1 = None
    none_type_2 = None
    bytes_0 = b'\x10\xb9'
    str_0 = '__main__'
    dict_0 = {str_0: str_0, str_0: bytes_0, str_0: str_0, str_0: str_0}
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0, none_type_0, none_type_1, str_0, none_type_2, bytes_0, str_0, dict_0)
    int_0 = 4483
    dict_1 = None
    float_0 = -1732.01499
    h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, dict_1, float_0, str_0)
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_8():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.sina.com.cn/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    str_1 = h_t_t_p_response_0.__repr__()
    var_0 = h_t_t_p_response_0.body
    h_t_t_p_client_0.close()

def test_case_9():
    str_0 = 'http://example.com'
    h_t_t_p_client_0 = module_0.HTTPClient()
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    h_t_t_p_response_0.rethrow()
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0)

def test_case_10():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.sina.com.cn/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    var_0 = h_t_t_p_response_0.body

def test_case_11():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.sia.com.cn/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)