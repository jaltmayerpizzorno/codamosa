# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import tornado.httputil as module_1
import tornado.ioloop as module_2

def test_case_0():
    pass

def test_case_1():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_2():
    h_t_t_p_client_0 = module_0.HTTPClient()

def test_case_3():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)

def test_case_4():
    str_0 = 'cx&IDQk$!Wd[6(W'
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0)

def test_case_5():
    int_0 = -822
    h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)

def test_case_6():
    h_t_t_p_client_0 = module_0.HTTPClient()
    h_t_t_p_client_0.close()

def test_case_7():
    str_0 = 'e\\fh,H"w\n'
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0)
    h_t_t_p_client_0 = module_0.HTTPClient()
    int_0 = 1896
    h_t_t_p_headers_0 = module_1.HTTPHeaders()
    h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, h_t_t_p_headers_0)
    str_1 = h_t_t_p_response_0.__repr__()

def test_case_8():
    str_0 = 'www.google.com'
    var_0 = None
    h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, var_0)
    int_0 = 200
    int_1 = 0
    h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, var_0, var_0, var_0, var_0, int_1)

def test_case_9():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    h_t_t_p_response_0.rethrow()
    h_t_t_p_response_0.rethrow()
    var_0 = h_t_t_p_response_0.body

def test_case_10():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    var_0 = h_t_t_p_response_0.body
    var_1 = print(h_t_t_p_response_0)
    h_t_t_p_client_0.close()

def test_case_11():
    h_t_t_p_client_0 = module_0.HTTPClient()
    str_0 = 'http://www.google.com/'
    h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    var_0 = h_t_t_p_response_0.body

def test_case_12():
    i_o_loop_0 = module_2.IOLoop()
    bool_0 = True
    async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
    async_h_t_t_p_client_1 = module_0.AsyncHTTPClient()
    async_h_t_t_p_client_0.close()
    async_h_t_t_p_client_2 = module_0.AsyncHTTPClient()
    async_h_t_t_p_client_1.close()