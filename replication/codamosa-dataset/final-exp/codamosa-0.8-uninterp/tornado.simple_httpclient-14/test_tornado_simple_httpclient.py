# Automatically generated by Pynguin.
import tornado.simple_httpclient as module_0
import tornado.ioloop as module_1
import _asyncio as module_2
import tornado.httpclient as module_3
import tornado.tcpclient as module_4
import ssl as module_5
import tornado.httputil as module_6

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Z|2i{b;<Y'
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)

def test_case_2():
    str_0 = ',\\\rg~!'
    h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
    str_1 = h_t_t_p_timeout_error_0.__str__()

def test_case_3():
    str_0 = ''
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)

def test_case_4():
    str_0 = 'Z|2i{b;<Y'
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    str_1 = h_t_t_p_stream_closed_error_0.__str__()

def test_case_5():
    i_o_loop_0 = module_1.IOLoop()
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient()
    future_0 = module_2.Future()
    simple_async_h_t_t_p_client_1 = module_0.SimpleAsyncHTTPClient()

def test_case_6():
    i_o_loop_0 = module_1.IOLoop()
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient()
    bool_0 = False
    simple_async_h_t_t_p_client_1 = module_0.SimpleAsyncHTTPClient()
    str_0 = 'Test message'
    int_0 = -5358
    h_t_t_p_request_0 = module_3.HTTPRequest(str_0, str_0, int_0, str_0, str_0, str_0, bool_0)
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    callable_0 = None
    t_c_p_client_0 = module_4.TCPClient()
    int_1 = None
    h_t_t_p_connection_0 = module_0._HTTPConnection(simple_async_h_t_t_p_client_0, h_t_t_p_request_0, h_t_t_p_stream_closed_error_0, callable_0, int_0, t_c_p_client_0, int_1, int_0)
    h_t_t_p_connection_0.on_connection_close()

def test_case_7():
    i_o_loop_0 = module_1.IOLoop()
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient()
    str_0 = ';;HZ8HZVd!z3'
    future_0 = module_2.Future()
    h_t_t_p_stream_closed_error_0 = module_0.HTTPStreamClosedError(str_0)
    s_s_l_context_0 = module_5.SSLContext()
    str_1 = h_t_t_p_stream_closed_error_0.__str__()
    int_0 = 166
    dict_0 = {}
    int_1 = 2305
    optional_0 = None
    t_c_p_client_0 = None
    simple_async_h_t_t_p_client_0.initialize(int_0, dict_0, int_1, optional_0, t_c_p_client_0)
    simple_async_h_t_t_p_client_1 = module_0.SimpleAsyncHTTPClient()

def test_case_8():
    i_o_loop_0 = module_1.IOLoop()
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient()
    t_c_p_client_0 = module_4.TCPClient()
    simple_async_h_t_t_p_client_0.close()

def test_case_9():
    i_o_loop_0 = module_1.IOLoop()
    simple_async_h_t_t_p_client_0 = module_0.SimpleAsyncHTTPClient()
    str_0 = '2;;HZ8HZVd!z3'
    future_0 = module_2.Future()
    bool_0 = False
    t_c_p_client_0 = module_4.TCPClient()
    h_t_t_p_request_0 = module_3.HTTPRequest(str_0, future_0, str_0, str_0, bool_0, bool_0, str_0, str_0, t_c_p_client_0)
    list_0 = [i_o_loop_0, t_c_p_client_0, str_0]
    request_start_line_0 = module_6.RequestStartLine(*list_0)
    callable_0 = None
    simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)