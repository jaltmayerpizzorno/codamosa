# Automatically generated by Pynguin.
import tornado.simple_httpclient as module_0
import tornado.netutil as module_1
import tornado.tcpclient as module_2
import tornado.httputil as module_3
import tornado.httpclient as module_4

def test_case_0():
    try:
        str_0 = '#9Dh]-7'
        h_t_t_p_timeout_error_0 = module_0.HTTPTimeoutError(str_0)
        str_1 = h_t_t_p_timeout_error_0.__str__()
        str_2 = 'tornado.simple_httpclient'
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_2.TCPClient(resolver_0)
        optional_0 = None
        str_3 = 'E\x0c@fe1Q|K+wLa$7HR'
        h_t_t_p_headers_0 = module_3.HTTPHeaders()
        h_t_t_p_headers_1 = h_t_t_p_headers_0.copy()
        bool_0 = True
        int_0 = 300
        bool_1 = False
        str_4 = 'tornado.simple_httpclient'
        set_0 = set()
        h_t_t_p_request_0 = module_4.HTTPRequest(str_2, str_3, h_t_t_p_headers_1, str_3, bool_0, str_2, int_0, bool_0, str_3, bool_1, str_4, set_0)
        callable_0 = None
        int_1 = 307
        int_2 = 1930
        int_3 = None
        h_t_t_p_connection_0 = module_0._HTTPConnection(optional_0, h_t_t_p_request_0, t_c_p_client_0, callable_0, int_1, t_c_p_client_0, int_2, int_3)
    except BaseException:
        pass