# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.ioloop as module_1
import tornado.netutil as module_2
import concurrent.futures._base as module_3
import socket as module_4
import _asyncio as module_5

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    list_0 = []
    i_o_loop_0 = module_1.IOLoop(*list_0)
    resolver_0 = module_2.Resolver(*list_0)
    tuple_0 = (i_o_loop_0, resolver_0)
    list_1 = [tuple_0, tuple_0, tuple_0]
    str_0 = 'V} |\t"'
    connector_0 = module_0._Connector(list_1, str_0)
    connector_0.clear_timeouts()
    resolver_1 = module_2.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_1)

def test_case_3():
    t_c_p_client_0 = module_0.TCPClient()
    t_c_p_client_0.close()

def test_case_4():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_0)
    list_0 = [tuple_0]
    connector_0 = module_0._Connector(list_0, str_0)
    connector_0.on_connect_timeout()
    connector_1 = module_0._Connector(list_0, str_0)
    connector_1.on_timeout()

def test_case_5():
    list_0 = []
    i_o_loop_0 = module_1.IOLoop(*list_0)
    resolver_0 = module_2.Resolver(*list_0)
    tuple_0 = (i_o_loop_0, resolver_0)
    list_1 = [tuple_0, tuple_0, tuple_0]
    str_0 = 'V} |\t"'
    connector_0 = module_0._Connector(list_1, str_0)
    connector_0.close_streams()
    connector_0.clear_timeouts()
    resolver_1 = module_2.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_1)

def test_case_6():
    str_0 = 'Set connect timeout to IOloop'
    i_o_loop_0 = module_1.IOLoop()
    str_1 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_1)
    list_0 = [tuple_0]
    int_0 = 1498
    str_2 = 'A6l'
    str_3 = 'q'
    str_4 = None
    dict_0 = {str_2: str_2, str_3: str_1, str_4: i_o_loop_0}
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, dict_0, str_4)
    float_0 = -1620.43
    connector_0 = module_0._Connector(list_0, t_c_p_client_0)
    connector_0.set_timeout(float_0)

def test_case_7():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_0)
    list_0 = [tuple_0]
    connector_0 = module_0._Connector(list_0, str_0)
    connector_1 = module_0._Connector(list_0, str_0)
    connector_0.on_timeout()
    connector_1.clear_timeout()

def test_case_8():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_0)
    list_0 = [tuple_0]
    connector_0 = module_0._Connector(list_0, str_0)
    connector_0.on_connect_timeout()
    connector_1 = module_0._Connector(list_0, str_0)
    connector_1.on_timeout()
    connector_0.on_timeout()
    connector_1.clear_timeouts()

def test_case_9():
    str_0 = 'Set connect timeout to IOloop'
    i_o_loop_0 = module_1.IOLoop()
    tuple_0 = (i_o_loop_0, str_0)
    list_0 = [tuple_0]
    int_0 = 1498
    connector_0 = module_0._Connector(list_0, str_0)
    connector_0.on_connect_timeout()
    str_1 = 'q'
    str_2 = None
    float_0 = 1757.0
    connector_0.set_connect_timeout(float_0)
    dict_0 = {str_1: str_1, str_1: str_2, str_2: i_o_loop_0}
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, dict_0, str_2)
    connector_1 = module_0._Connector(list_0, str_0)
    connector_1.on_timeout()
    connector_0.on_timeout()
    connector_1.on_timeout()
    connector_1.clear_timeouts()
    connector_1.clear_timeout()
    callable_0 = None
    list_1 = [tuple_0, tuple_0]
    connector_2 = module_0._Connector(list_1, callable_0)
    callable_1 = None
    connector_3 = module_0._Connector(list_1, callable_1)

def test_case_10():
    str_0 = 'Set connect timeout to IOloop'
    i_o_loop_0 = module_1.IOLoop()
    str_1 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_1)
    list_0 = [tuple_0]
    int_0 = 1498
    connector_0 = module_0._Connector(list_0, str_0)
    connector_0.on_connect_timeout()
    str_2 = 'q'
    str_3 = None
    dict_0 = {str_1: str_1, str_2: str_1, str_3: i_o_loop_0}
    connector_0.on_connect_timeout()
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, dict_0, str_3)
    connector_1 = module_0._Connector(list_0, str_1)
    connector_1.on_timeout()
    connector_0.on_timeout()
    connector_1.on_timeout()
    connector_1.clear_timeouts()
    connector_1.clear_timeout()
    callable_0 = None
    list_1 = [tuple_0, tuple_0]
    connector_2 = module_0._Connector(list_1, callable_0)
    callable_1 = None
    connector_3 = module_0._Connector(list_1, callable_1)

def test_case_11():
    str_0 = 'S\nTU6?+Bxvj 2Vp!s'
    i_o_loop_0 = module_1.IOLoop()
    str_1 = 'L5a^_v+;'
    tuple_0 = (i_o_loop_0, str_1)
    list_0 = [tuple_0]
    connector_0 = module_0._Connector(list_0, str_0)
    connector_0.on_connect_timeout()
    future_0 = module_3.Future()
    address_family_0 = module_4.AddressFamily.AF_BLUETOOTH
    future_1 = module_5.Future()
    connector_0.on_connect_done(future_0, address_family_0, tuple_0, future_1)
    connector_1 = module_0._Connector(list_0, str_1)
    connector_1.on_timeout()
    connector_0.on_timeout()
    connector_1.clear_timeout()
    callable_0 = None
    connector_2 = module_0._Connector(list_0, callable_0)