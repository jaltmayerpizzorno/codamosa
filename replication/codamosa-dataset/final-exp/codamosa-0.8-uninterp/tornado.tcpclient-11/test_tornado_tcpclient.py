# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.ioloop as module_1
import ssl as module_2
import tornado.netutil as module_3
import socket as module_4
import tornado.iostream as module_5

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    t_c_p_client_0 = module_0.TCPClient()
    t_c_p_client_0.close()

def test_case_3():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0, tuple_0]
    s_s_l_context_0 = module_2.SSLContext()
    connector_0 = module_0._Connector(list_0, s_s_l_context_0)
    connector_0.close_streams()

def test_case_4():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0]
    int_0 = 2901
    tuple_1 = i_o_loop_0.split_fd(int_0)
    connector_0 = module_0._Connector(list_0, tuple_1)
    connector_0.clear_timeout()
    connector_0.on_timeout()
    t_c_p_client_0.close()
    connector_0.clear_timeouts()

def test_case_5():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0, tuple_0]
    callable_0 = None
    connector_0 = module_0._Connector(list_0, callable_0)
    s_s_l_context_0 = module_2.SSLContext()
    connector_1 = module_0._Connector(list_0, callable_0)
    connector_2 = module_0._Connector(list_0, callable_0)
    connector_2.clear_timeout()

def test_case_6():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0, tuple_0]
    s_s_l_context_0 = module_2.SSLContext()
    set_0 = set()
    connector_0 = module_0._Connector(list_0, set_0)
    str_0 = 'K=!f6'
    connector_1 = module_0._Connector(list_0, str_0)
    float_0 = -358.1
    float_1 = 538.0
    connector_2 = module_0._Connector(list_0, float_1)
    connector_2.set_connect_timeout(float_0)

def test_case_7():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0]
    int_0 = 2901
    tuple_1 = (int_0, int_0)
    connector_0 = module_0._Connector(list_0, tuple_1)
    connector_0.clear_timeout()
    connector_0.on_timeout()
    t_c_p_client_0.close()
    connector_0.on_connect_timeout()
    connector_0.clear_timeouts()

def test_case_8():
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_0 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_0)
    list_0 = [tuple_0]
    int_0 = 2901
    tuple_1 = (int_0, int_0)
    connector_0 = module_0._Connector(list_0, tuple_1)
    connector_0.on_timeout()
    connector_0.clear_timeout()
    connector_0.on_timeout()
    t_c_p_client_0.close()
    float_0 = 1500.31001
    connector_0.set_connect_timeout(float_0)
    connector_0.set_timeout(float_0)
    connector_0.on_connect_timeout()
    t_c_p_client_0.close()
    connector_0.clear_timeouts()
    connector_0.set_connect_timeout(float_0)

def test_case_9():
    resolver_0 = module_3.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_0)
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_1 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_1)
    list_0 = [tuple_0]
    int_0 = 2901
    str_0 = 'pGw'
    dict_0 = {str_0: int_0, int_0: tuple_0, str_0: t_c_p_client_1}
    connector_0 = module_0._Connector(list_0, int_0)
    connector_1 = module_0._Connector(list_0, dict_0)
    connector_1.on_timeout()
    connector_0.on_connect_timeout()
    address_family_0 = module_4.AddressFamily.AF_INET
    tuple_1 = (int_0, int_0)
    connector_2 = module_0._Connector(list_0, tuple_1)
    connector_2.clear_timeouts()
    future_0 = None
    connector_3 = module_0._Connector(list_0, tuple_1)
    connector_0.on_connect_done(int_0, address_family_0, tuple_0, future_0)

def test_case_10():
    resolver_0 = module_3.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_0)
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_1 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_1)
    int_0 = 2901
    str_0 = 'pGw'
    float_0 = 5197.902
    tuple_1 = (int_0, float_0)
    list_0 = [tuple_0, tuple_0, tuple_1]
    int_1 = 5
    awaitable_0 = resolver_0.resolve(str_0, int_1)
    connector_0 = module_0._Connector(list_0, awaitable_0)
    callable_0 = None
    connector_1 = module_0._Connector(list_0, callable_0)
    connector_0.clear_timeouts()
    connector_2 = module_0._Connector(list_0, callable_0)

def test_case_11():
    resolver_0 = module_3.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_0)
    t_c_p_client_0.close()
    i_o_loop_0 = module_1.IOLoop()
    t_c_p_client_1 = module_0.TCPClient()
    tuple_0 = (i_o_loop_0, t_c_p_client_1)
    list_0 = [tuple_0]
    int_0 = 2901
    str_0 = 'w0WQ+'
    dict_0 = {str_0: int_0, int_0: tuple_0, str_0: t_c_p_client_1}
    connector_0 = module_0._Connector(list_0, int_0)
    connector_1 = module_0._Connector(list_0, dict_0)
    connector_1.on_timeout()
    connector_1.on_connect_timeout()
    float_0 = 2009.345561
    connector_0.set_timeout(float_0)
    connector_2 = module_0._Connector(list_0, i_o_loop_0)
    connector_2.clear_timeout()
    callable_0 = None
    connector_3 = module_0._Connector(list_0, callable_0)
    connector_0.clear_timeouts()
    iterator_0 = None
    socket_0 = module_4.socket()
    i_o_stream_0 = module_5.IOStream(socket_0)
    bytes_0 = None
    future_0 = i_o_stream_0.write(bytes_0)
    address_family_0 = module_4.AddressFamily.AF_UNSPEC
    connector_3.on_connect_done(iterator_0, address_family_0, tuple_0, future_0)
    connector_4 = module_0._Connector(list_0, callable_0)
    connector_2.on_connect_done(iterator_0, address_family_0, tuple_0, future_0)