# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import ssl as module_1
import _io as module_2
import tornado.ioloop as module_3

def test_case_0():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_1 = module_0.HTTPClient()
        list_0 = []
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient(*list_0)
    except BaseException:
        pass

def test_case_1():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'DH9wd96pOPP'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'tornado.httpclient'
        str_1 = 'Already reading'
        int_0 = 339
        dict_0 = {}
        bool_0 = False
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0, str_0, str_1, int_0, str_1, dict_0, str_0, bool_0, str_1)
    except BaseException:
        pass

def test_case_3():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        module_0.main()
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = -878
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        module_0.main()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = ';n@:'
        dict_0 = {str_0: str_0}
        dict_1 = {str_0: dict_0, str_0: dict_0}
        s_s_l_context_0 = module_1.SSLContext(**dict_1)
        bytes_i_o_0 = module_2.BytesIO()
        bytes_0 = b'\xbd\x9b*\x15\xb8H+\xde\xba\xad\x1f\x94:\xa1'
        h_t_t_p_client_0 = module_0.HTTPClient(bytes_0)
    except BaseException:
        pass

def test_case_6():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        str_0 = 'http://www.google.com/'
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'url'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0)
        int_0 = -2131
        str_1 = 'error'
        str_2 = 'Not Found'
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_1, str_2)
        h_t_t_p_response_0.rethrow()
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'cx&IDQk$!Wd[6(W'
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_0)
        optional_0 = None
        h_t_t_p_client_0 = module_0.HTTPClient(optional_0)
        str_1 = 'set missing statement'
        str_2 = '!'
        str_3 = "Cl4i0r\n~&{|;'1S\\U.6"
        dict_0 = {str_0: str_1, str_1: h_t_t_p_client_0, str_2: h_t_t_p_request_0, str_3: str_1}
        h_t_t_p_client_1 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_1.fetch(h_t_t_p_request_0, **dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        i_o_loop_0 = module_3.IOLoop()
        bool_0 = True
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient()
        async_h_t_t_p_client_1 = module_0.AsyncHTTPClient()
        async_h_t_t_p_client_0.close()
        async_h_t_t_p_client_2 = module_0.AsyncHTTPClient()
        str_0 = 'VnNzb<[\r;pY<G\tl'
        future_0 = async_h_t_t_p_client_1.fetch(str_0)
    except BaseException:
        pass