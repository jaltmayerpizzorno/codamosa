# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import ssl as module_1
import tornado.ioloop as module_2
import tornado.netutil as module_3
import concurrent.futures._base as module_4
import _asyncio as module_5
import socket as module_6

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    t_c_p_client_0 = module_0.TCPClient()
    t_c_p_client_0.close()
    s_s_l_context_0 = module_1.SSLContext()

def test_case_3():
    int_0 = 355
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0, tuple_0]
    dict_0 = {}
    connector_0 = module_0._Connector(list_0, i_o_loop_0)
    connector_0.close_streams()
    connector_1 = module_0._Connector(list_0, dict_0)

def test_case_4():
    int_0 = 355
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    str_0 = '2mw<R^JAWg=lHYBo6'
    resolver_0 = module_3.Resolver()
    awaitable_0 = resolver_0.resolve(str_0, int_0)
    connector_0 = module_0._Connector(list_0, awaitable_0)
    connector_0.on_timeout()
    i_o_loop_1 = module_2.IOLoop()
    float_0 = 2147.8
    connector_0.set_timeout(float_0)

def test_case_5():
    float_0 = 0.0
    str_0 = 'afh3Y'
    int_0 = 306
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, str_0, float_0)
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0, tuple_0, tuple_0]
    str_1 = '2mw<R^JAWg=lHYBo6'
    int_1 = 399
    resolver_0 = module_3.Resolver()
    awaitable_0 = resolver_0.resolve(str_1, int_1)
    connector_0 = module_0._Connector(list_0, awaitable_0)
    connector_0.set_connect_timeout(float_0)
    i_o_loop_1 = module_2.IOLoop()
    future_0 = module_4.Future()
    callable_0 = None
    connector_1 = module_0._Connector(list_0, callable_0)
    float_1 = 0.0
    connector_1.set_timeout(float_1)

def test_case_6():
    int_0 = 355
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0]
    future_0 = module_5.Future()
    connector_0 = module_0._Connector(list_0, i_o_loop_0)
    connector_0.clear_timeout()

def test_case_7():
    int_0 = 355
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0, tuple_0]
    iterator_0 = None
    connector_0 = module_0._Connector(list_0, i_o_loop_0)
    connector_0.close_streams()
    connector_0.on_connect_timeout()
    address_family_0 = module_6.AddressFamily.AF_NETLINK
    future_0 = module_5.Future()
    callable_0 = None
    connector_1 = module_0._Connector(list_0, callable_0)
    connector_0.on_connect_done(iterator_0, address_family_0, tuple_0, future_0)

def test_case_8():
    int_0 = 355
    i_o_loop_0 = module_2.IOLoop()
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0, tuple_0]
    iterator_0 = None
    connector_0 = module_0._Connector(list_0, i_o_loop_0)
    connector_0.clear_timeout()
    connector_0.close_streams()
    connector_0.on_connect_timeout()
    address_family_0 = module_6.AddressFamily.AF_NETLINK
    connector_0.close_streams()
    future_0 = module_5.Future()
    s_s_l_context_0 = module_1.SSLContext()
    connector_1 = module_0._Connector(list_0, s_s_l_context_0)
    connector_0.on_timeout()
    connector_0.on_connect_done(iterator_0, address_family_0, tuple_0, future_0)

def test_case_9():
    str_0 = 'fh3Y'
    int_0 = 355
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_2.IOLoop()
    int_1 = 2748
    dict_0 = None
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_1, dict_0)
    tuple_0 = (i_o_loop_0, int_0)
    list_0 = [tuple_0]
    future_0 = module_5.Future()
    connector_0 = module_0._Connector(list_0, i_o_loop_0)
    float_0 = -208.267
    connector_0.set_timeout(float_0)
    connector_0.clear_timeout()
    connector_0.clear_timeout()
    connector_0.close_streams()
    connector_0.on_timeout()