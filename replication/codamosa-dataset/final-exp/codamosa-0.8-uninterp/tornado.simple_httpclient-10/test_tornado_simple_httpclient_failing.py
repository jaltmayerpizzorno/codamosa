# Automatically generated by Pynguin.
import tornado.ioloop as module_0
import tornado.simple_httpclient as module_1
import tornado.httpclient as module_2
import concurrent.futures._base as module_3
import _asyncio as module_4
import ssl as module_5
import tornado.httputil as module_6
import tornado.netutil as module_7
import tornado.tcpclient as module_8

def test_case_0():
    try:
        i_o_loop_0 = module_0.IOLoop()
        simple_async_h_t_t_p_client_0 = module_1.SimpleAsyncHTTPClient()
        str_0 = 'k~}C@{y&$:TA'
        int_0 = -2927
        str_1 = None
        str_2 = 'Q4160?'
        str_3 = "ih=GIn'~OY7Sq}er#P"
        dict_0 = {str_1: str_1, str_2: str_0, str_3: str_3}
        simple_async_h_t_t_p_client_0.initialize(int_0, dict_0, int_0, int_0)
        h_t_t_p_timeout_error_0 = module_1.HTTPTimeoutError(str_0)
        i_o_loop_0.update_handler(int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        i_o_loop_0 = module_0.IOLoop()
        simple_async_h_t_t_p_client_0 = module_1.SimpleAsyncHTTPClient()
        str_0 = '4A(Dz=i-6]O#\r['
        h_t_t_p_timeout_error_0 = module_1.HTTPTimeoutError(str_0)
        str_1 = 'http://www.tornadoweb.org/enrstable/'
        str_2 = h_t_t_p_timeout_error_0.__str__()
        simple_async_h_t_t_p_client_0.close()
        float_0 = 0.1
        str_3 = '>'
        none_type_0 = None
        bool_0 = False
        h_t_t_p_request_0 = module_2.HTTPRequest(str_3, str_2, float_0, str_1, none_type_0, str_2, bool_0, str_1)
        callable_0 = None
        simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        i_o_loop_0 = module_0.IOLoop()
        simple_async_h_t_t_p_client_0 = module_1.SimpleAsyncHTTPClient()
        str_0 = "k~}C@{y&$:'A"
        str_1 = 'OA(Dz=i-V6]O#\r['
        str_2 = 'http://www.tornadoweb.org/enrstable/'
        h_t_t_p_timeout_error_0 = module_1.HTTPTimeoutError(str_2)
        str_3 = h_t_t_p_timeout_error_0.__str__()
        str_4 = '>'
        str_5 = 'Dv'
        bool_0 = False
        str_6 = '%d:%02d %s'
        set_0 = {simple_async_h_t_t_p_client_0, str_0, str_5, bool_0}
        str_7 = 'tornado.simple_httpclient'
        float_0 = 1000.0
        optional_0 = None
        var_0 = None
        h_t_t_p_request_0 = module_2.HTTPRequest(str_6, set_0, str_7, str_1, simple_async_h_t_t_p_client_0, float_0, str_4, optional_0, str_4, bool_0, bool_0, var_0)
        callable_0 = None
        simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)
    except BaseException:
        pass

def test_case_3():
    try:
        i_o_loop_0 = module_0.IOLoop()
        str_0 = 't0K)~Bg1"UNfr\n'
        h_t_t_p_timeout_error_0 = module_1.HTTPTimeoutError(str_0)
        str_1 = h_t_t_p_timeout_error_0.__str__()
        h_t_t_p_stream_closed_error_0 = module_1.HTTPStreamClosedError(str_0)
        list_0 = []
        i_o_loop_1 = module_0.IOLoop(*list_0)
        future_0 = module_3.Future()
        str_2 = '&;Wqfe|ot=M0b5w89C"G'
        list_1 = [str_2]
        i_o_loop_1.add_future(future_0, list_1)
        dict_0 = {}
        simple_async_h_t_t_p_client_0 = module_1.SimpleAsyncHTTPClient(*list_0, **dict_0)
        str_3 = 'k~}C@{y&$:TA'
        h_t_t_p_timeout_error_1 = module_1.HTTPTimeoutError(str_3)
        str_4 = 'http://www.tornadoweb.org/enrstable/'
        h_t_t_p_timeout_error_2 = module_1.HTTPTimeoutError(str_2)
        str_5 = h_t_t_p_timeout_error_2.__str__()
        simple_async_h_t_t_p_client_0.close()
        bool_0 = False
        future_1 = module_4.Future(*list_0)
        int_0 = 0
        dict_1 = {}
        simple_async_h_t_t_p_client_0.initialize(int_0, dict_1, int_0)
        str_6 = None
        float_0 = -4195.2
        selectable_0 = module_0._Selectable(**dict_0)
        s_s_l_context_0 = module_5.SSLContext()
        h_t_t_p_request_0 = module_2.HTTPRequest(str_6, str_5, future_1, str_6, float_0, str_4, selectable_0, str_4, str_5, bool_0, str_3, bool_0, s_s_l_context_0)
        callable_0 = None
        simple_async_h_t_t_p_client_0.fetch_impl(h_t_t_p_request_0, callable_0)
    except BaseException:
        pass

def test_case_4():
    try:
        i_o_loop_0 = module_0.IOLoop()
        simple_async_h_t_t_p_client_0 = module_1.SimpleAsyncHTTPClient()
        str_0 = 'k~}C@{y&$:TA'
        h_t_t_p_stream_closed_error_0 = module_1.HTTPStreamClosedError(str_0)
        str_1 = '4A(Dz=i-6]O#\r['
        h_t_t_p_timeout_error_0 = module_1.HTTPTimeoutError(str_1)
        str_2 = 'http://www.tornadoweb.org/enrstable/'
        str_3 = h_t_t_p_timeout_error_0.__str__()
        float_0 = 0.1
        str_4 = ''
        str_5 = '>'
        bytes_0 = b'BzW\x1a'
        str_6 = "Q|67W!C!%'^.\x0b/2!"
        h_t_t_p_headers_0 = module_6.HTTPHeaders()
        h_t_t_p_headers_1 = h_t_t_p_headers_0.copy()
        int_0 = -37
        bool_0 = False
        set_0 = set()
        h_t_t_p_request_0 = module_2.HTTPRequest(str_6, float_0, str_4, str_5, str_2, float_0, float_0, h_t_t_p_headers_1, int_0, bool_0, str_6, bool_0, str_5, set_0)
        str_7 = '+/\\E]_'
        dict_0 = {str_6: str_7}
        resolver_0 = module_7.Resolver()
        t_c_p_client_0 = module_8.TCPClient(resolver_0)
        int_1 = 10
        h_t_t_p_connection_0 = module_1._HTTPConnection(simple_async_h_t_t_p_client_0, h_t_t_p_request_0, h_t_t_p_stream_closed_error_0, dict_0, int_0, t_c_p_client_0, int_0, int_1)
        h_t_t_p_connection_0.data_received(bytes_0)
        h_t_t_p_connection_0.on_connection_close()
    except BaseException:
        pass