# Automatically generated by Pynguin.
import tornado.httpclient as module_0
import tornado.httputil as module_1
import _io as module_2
import tornado.ioloop as module_3

def test_case_0():
    try:
        str_0 = 'YvlH'
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_0.fetch(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_1 = module_0.HTTPClient(h_t_t_p_client_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '?i\x0b?\n*|Z'
        str_1 = '{~VgAV'
        dict_0 = {}
        h_t_t_p_headers_0 = module_1.HTTPHeaders(**dict_0)
        float_0 = -3149.935
        int_0 = 1685
        dict_1 = {}
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_1, h_t_t_p_headers_0, str_1, str_0, float_0, int_0, str_0, dict_1, float_0, str_0, str_0, str_1, bool_0, bool_0)
        bytes_i_o_0 = module_2.BytesIO()
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()
        h_t_t_p_client_1 = module_0.HTTPClient()
        h_t_t_p_response_0 = h_t_t_p_client_1.fetch(h_t_t_p_request_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'm4KA[m8CnF%\t'
        float_0 = 12.270077231909209
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_request_0 = None
        int_0 = -1484
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, str_0, float_0, float_0)
        h_t_t_p_response_0.rethrow()
    except BaseException:
        pass

def test_case_4():
    try:
        module_0.main()
    except BaseException:
        pass

def test_case_5():
    try:
        module_0.main()
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'g+"jzi@\rg'
        int_0 = 365
        h_t_t_p_client_error_0 = module_0.HTTPClientError(int_0)
        list_0 = [str_0, str_0]
        h_t_t_p_client_0 = module_0.HTTPClient(list_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '?i\x0b?\n*|Z'
        str_1 = '{~VgAV'
        dict_0 = {}
        h_t_t_p_headers_0 = module_1.HTTPHeaders(**dict_0)
        float_0 = -3149.935
        int_0 = 1685
        dict_1 = {}
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_1, h_t_t_p_headers_0, str_1, str_0, float_0, int_0, str_0, dict_1, float_0, str_0, str_0, str_1, bool_0, bool_0)
        bytes_i_o_0 = module_2.BytesIO()
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, h_t_t_p_headers_0, bytes_i_o_0, str_0, bytes_i_o_0, float_0, float_0)
        str_2 = h_t_t_p_response_0.__repr__()
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()
        str_3 = 'B'
        h_t_t_p_response_1 = h_t_t_p_client_0.fetch(str_3)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '?i\x0b?\n*|Z'
        str_1 = '{~VgAV'
        dict_0 = {}
        h_t_t_p_headers_0 = module_1.HTTPHeaders(**dict_0)
        float_0 = -3149.935
        int_0 = 1685
        dict_1 = {str_0: float_0}
        bool_0 = True
        h_t_t_p_request_0 = module_0.HTTPRequest(str_0, str_1, h_t_t_p_headers_0, str_1, str_0, float_0, int_0, str_0, dict_1, float_0, str_0, str_0, str_1, bool_0, bool_0)
        bytes_i_o_0 = module_2.BytesIO()
        h_t_t_p_response_0 = module_0.HTTPResponse(h_t_t_p_request_0, int_0, h_t_t_p_headers_0, bytes_i_o_0, str_0, bytes_i_o_0, float_0, float_0)
        str_2 = h_t_t_p_response_0.__repr__()
        h_t_t_p_client_0 = module_0.HTTPClient()
        h_t_t_p_client_0.close()
        h_t_t_p_client_1 = module_0.HTTPClient()
        h_t_t_p_client_2 = module_0.HTTPClient()
        h_t_t_p_response_1 = h_t_t_p_client_1.fetch(h_t_t_p_request_0, **dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '?i\x0b?\n*|Z'
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        bool_0 = True
        list_0 = [str_0]
        async_h_t_t_p_client_0 = module_0.AsyncHTTPClient(*list_0)
        async_h_t_t_p_client_1 = async_h_t_t_p_client_0.__new__(i_o_loop_1, bool_0)
    except BaseException:
        pass