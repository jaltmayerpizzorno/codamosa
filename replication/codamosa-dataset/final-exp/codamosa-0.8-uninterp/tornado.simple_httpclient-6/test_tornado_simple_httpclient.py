# Automatically generated by Pynguin.
import tornado.simple_httpclient as module_0
import tornado.ioloop as module_1
import tornado.httpclient as module_2
import tornado.tcpclient as module_3
import ssl as module_4

def test_case_0():
    pass

def test_case_1():
    str_0 = 'V-6ABf,G1.W\x0cQ\x0c>Xy'
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)

def test_case_2():
    str_0 = "z'z"
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
    str_1 = h_t_t_p_timeout_error_0.__str__()

def test_case_3():
    str_0 = 'uN~%z+|;9 '
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)

def test_case_4():
    str_0 = 'uN~%z+|;9 '
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    str_1 = h_t_t_p_stream_closed_error_0.__str__()

def test_case_5():
    h_t_t_p_headers_0 = None
    str_0 = 'n1CJkZk;O/foMI'
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    dict_0 = {str_0: str_0, str_0: str_0}
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_0.instance()
    i_o_loop_3 = i_o_loop_1.instance()
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    str_1 = '&XBA$@oK\nLyE!'
    simple_async_h_t_t_p_client_0.close()
    callable_0 = None
    str_2 = ''
    str_3 = '&@D-\x0bBPN\x0bl&-:!'
    str_4 = '91Sx'
    callable_1 = None
    bool_0 = False
    dict_1 = {str_1: simple_async_h_t_t_p_client_0, str_4: str_4, str_3: dict_0}
    h_t_t_p_request_0 = module_2.HTTPRequest(str_3, str_4, h_t_t_p_headers_0, str_1, str_2, str_4, str_2, str_1, str_4, callable_1, bool_0, dict_1)
    simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)
    t_c_p_client_0 = module_3.TCPClient()

def test_case_6():
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_1.instance()
    str_0 = 'zP:Dq'
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    int_0 = 609
    optional_0 = None
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    simple_async_h_t_t_p_client_0.initialize(int_0, optional_0)
    simple_async_h_t_t_p_client_1 = module_0.SimpleAsyncHTTPClient()

def test_case_7():
    h_t_t_p_headers_0 = None
    str_0 = 'The ``ssl_options`` keyword argument may either be an\n        `ssl.SSLContext` object or a dictionary of keywords arguments\n        for `ssl.wrap_socket`\n        '
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    dict_0 = {str_0: str_0, str_0: str_0}
    str_1 = h_t_t_p_stream_closed_error_0.__str__()
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_1.instance()
    str_2 = 'zP:Dq'
    h_t_t_p_stream_closed_error_1 = module_0.HTTPStreamClosedError(str_2)
    int_0 = 609
    optional_0 = None
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    simple_async_h_t_t_p_client_0.initialize(int_0, optional_0)
    s_s_l_context_0 = module_4.SSLContext()
    str_3 = '\nNfn\x0cK'
    dict_1 = {str_1: str_3, str_1: str_3, str_2: str_3, str_2: str_1}
    str_4 = 'O'
    dict_2 = {str_3: dict_0, str_4: optional_0, str_0: h_t_t_p_headers_0}
    simple_async_h_t_t_p_client_0.initialize(dict_1, int_0, dict_2, int_0)

def test_case_8():
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_1.instance()
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    simple_async_h_t_t_p_client_0.close()
    s_s_l_context_0 = module_4.SSLContext()

def test_case_9():
    str_0 = 'ct058Hc1` d%s0/n'
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    str_1 = h_t_t_p_stream_closed_error_0.__str__()
    h_t_t_p_headers_0 = None
    str_2 = 'n1CJkZk;O/foMI'
    h_t_t_p_stream_closed_error_1 = module_0.HTTPStreamClosedError(str_2)
    dict_0 = {str_2: str_2, str_2: str_2}
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_1.instance()
    i_o_loop_3 = i_o_loop_1.instance()
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    callable_0 = None
    str_3 = ''
    str_4 = '&@D-\x0bBPN\x0bl&-:!'
    str_5 = '91Sx'
    callable_1 = None
    bool_0 = True
    str_6 = '_3Wi;MX2}'
    dict_1 = {str_6: simple_async_h_t_t_p_client_0, str_5: str_5, str_4: dict_0}
    h_t_t_p_request_0 = module_2.HTTPRequest(str_4, str_5, h_t_t_p_headers_0, str_0, str_3, str_5, str_3, str_0, str_5, callable_1, bool_0, dict_1)
    simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)
    bytes_0 = b'\x057\x7f\x97\xea\xfe'
    int_0 = 1503
    t_c_p_client_0 = module_3.TCPClient()
    int_1 = -1049
    h_t_t_p_connection_0 = module_0._HTTPConnection(simple_async_h_t_t_p_client_0, h_t_t_p_request_0, list_0, callable_0, int_0, t_c_p_client_0, int_0, int_1)
    h_t_t_p_connection_0.data_received(bytes_0)

def test_case_10():
    str_0 = 'ct058Hc1` d%s0/n'
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    str_1 = h_t_t_p_stream_closed_error_0.__str__()
    str_2 = h_t_t_p_timeout_error_0.__str__()
    h_t_t_p_headers_0 = None
    str_3 = 'n1CJkZk;O/foMI'
    h_t_t_p_stream_closed_error_1 = module_0.HTTPStreamClosedError(str_3)
    dict_0 = {str_3: str_3, str_3: str_3}
    i_o_loop_0 = module_1.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    i_o_loop_2 = i_o_loop_1.instance()
    i_o_loop_3 = i_o_loop_1.instance()
    h_t_t_p_stream_closed_error_2 = module_0.HTTPStreamClosedError(str_3)
    list_0 = []
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient(*list_0)
    simple_async_h_t_t_p_client_0.close()
    simple_async_h_t_t_p_client_1 = module_0.SimpleAsyncHTTPClient(*list_0)
    callable_0 = None
    str_4 = 'ZZ\t[r9p:7O[|DWw4.4vr'
    str_5 = '&@D-\x0bBPN\x0bl&-:!'
    i_o_loop_1.initialize()
    str_6 = '91Sx'
    callable_1 = None
    bool_0 = False
    str_7 = '_3Wi;MX2}'
    dict_1 = {str_1: h_t_t_p_headers_0, str_7: simple_async_h_t_t_p_client_1, str_7: str_7, str_6: str_6, str_5: dict_0}
    h_t_t_p_request_0 = module_2.HTTPRequest(str_5, str_6, h_t_t_p_headers_0, str_0, str_4, str_6, str_4, str_0, str_6, callable_1, bool_0, dict_1)
    simple_async_h_t_t_p_client_1.fetch_impl(h_t_t_p_request_0, callable_0)
    bytes_0 = b'\x057\x7f\x97\xea\xfe'
    int_0 = 1500
    t_c_p_client_0 = module_3.TCPClient()
    int_1 = -1049
    h_t_t_p_connection_0 = module_0._HTTPConnection(simple_async_h_t_t_p_client_1, h_t_t_p_request_0, list_0, callable_0, int_0, t_c_p_client_0, int_0, int_1)
    h_t_t_p_connection_0.data_received(bytes_0)