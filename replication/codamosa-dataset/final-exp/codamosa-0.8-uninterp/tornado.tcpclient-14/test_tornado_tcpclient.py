# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import ssl as module_1
import socket as module_2
import tornado.netutil as module_3
import tornado.ioloop as module_4
import concurrent.futures._base as module_5
import _asyncio as module_6
import datetime as module_7

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    t_c_p_client_0 = module_0.TCPClient()
    t_c_p_client_0.close()

def test_case_3():
    s_s_l_context_0 = module_1.SSLContext()
    str_0 = 't/\x0cmSOBfhGl=si{ X7'
    int_0 = 200
    address_family_0 = module_2.AddressFamily.AF_ECONET
    str_1 = 'cu(zc:]Aq#'
    int_1 = -229
    resolver_0 = module_3.Resolver()
    awaitable_0 = resolver_0.resolve(str_1, int_1)
    t_c_p_client_0 = module_0.TCPClient(awaitable_0)
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, address_family_0, str_0, int_0)
    t_c_p_client_0.close()
    str_2 = 'text/plain'
    int_2 = -3442
    t_c_p_client_1 = module_0.TCPClient()
    i_o_stream_1 = t_c_p_client_1.connect(str_2, int_2, int_1)

def test_case_4():
    i_o_loop_0 = module_4.IOLoop()
    str_0 = '\n7z'
    list_0 = []
    tuple_0 = (str_0, list_0)
    list_1 = [tuple_0, tuple_0, tuple_0, tuple_0]
    callable_0 = None
    connector_0 = module_0._Connector(list_1, callable_0)
    connector_0.clear_timeouts()

def test_case_5():
    i_o_loop_0 = module_4.IOLoop()
    str_0 = '\n7z'
    list_0 = []
    tuple_0 = (str_0, list_0)
    list_1 = [tuple_0, tuple_0, tuple_0, tuple_0]
    list_2 = []
    tuple_1 = (list_2, list_2)
    list_3 = [tuple_0, tuple_0, tuple_0]
    connector_0 = module_0._Connector(list_3, tuple_1)
    connector_0.on_connect_timeout()
    connector_1 = module_0._Connector(list_1, tuple_1)
    connector_1.clear_timeouts()
    bool_0 = False
    i_o_loop_0.close(bool_0)

def test_case_6():
    i_o_loop_0 = module_4.IOLoop()
    str_0 = 'o\nl'
    list_0 = []
    tuple_0 = (str_0, list_0)
    list_1 = [tuple_0, tuple_0, tuple_0]
    future_0 = module_5.Future()
    bytes_0 = b'6\xc3\xe3\xdfj\xacA}\x9cpM\xc5\x05\xf2n\xf1F\xe7\xd0='
    connector_0 = module_0._Connector(list_1, bytes_0)
    tuple_1 = connector_0.split(list_1)
    connector_0.clear_timeouts()
    connector_1 = module_0._Connector(list_1, future_0)
    connector_0.clear_timeout()
    connector_1.clear_timeouts()
    connector_0.on_connect_timeout()
    iterator_0 = None
    connector_1.on_timeout()
    future_1 = module_6.Future()
    address_family_0 = None
    connector_0.on_connect_done(iterator_0, address_family_0, tuple_0, future_1)

def test_case_7():
    i_o_loop_0 = module_4.IOLoop()
    str_0 = '[*/h'
    list_0 = []
    tuple_0 = (str_0, list_0)
    list_1 = [tuple_0, tuple_0]
    connector_0 = module_0._Connector(list_1, list_0)
    connector_0.clear_timeouts()
    str_1 = 'Z@tBX'
    bytes_0 = b'6\xc3\xe3\xdfj\xacA}\x9cpM\xc5\x05\xf2n\xf1F\xe7\xd0='
    connector_1 = module_0._Connector(list_1, bytes_0)
    tuple_1 = connector_1.split(list_1)
    connector_2 = module_0._Connector(list_1, str_1)
    float_0 = 20.0
    connector_2.set_timeout(float_0)
    connector_1.on_connect_timeout()
    connector_2.clear_timeout()
    str_2 = '\nlz'
    int_0 = None
    connector_1.on_connect_timeout()
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_2, int_0)
    timedelta_0 = module_7.timedelta(*list_0)
    connector_3 = module_0._Connector(list_1, timedelta_0)
    connector_3.on_timeout()
    future_0 = module_6.Future()

def test_case_8():
    i_o_loop_0 = module_4.IOLoop()
    str_0 = 'o\nl'
    list_0 = []
    tuple_0 = (str_0, list_0)
    list_1 = [tuple_0]
    future_0 = module_5.Future()
    str_1 = 'Z@tBX'
    bytes_0 = b'6\xc3\xe3\xdfj\xacA}\x9cpM\xc5\x05\xf2n\xf1F\xe7\xd0='
    connector_0 = module_0._Connector(list_1, bytes_0)
    tuple_1 = connector_0.split(list_1)
    connector_1 = module_0._Connector(list_1, str_1)
    connector_1.clear_timeouts()
    connector_1.clear_timeout()
    float_0 = 734.78571
    connector_0.set_timeout(float_0)
    connector_0.clear_timeouts()
    timedelta_0 = module_7.timedelta()
    connector_1.set_connect_timeout(timedelta_0)
    str_2 = '\nlz'
    connector_0.on_timeout()
    int_0 = None
    connector_0.on_connect_timeout()
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_2, int_0)
    future_1 = module_6.Future(*list_0)
    int_1 = 4183
    t_c_p_client_1 = module_0.TCPClient()
    i_o_stream_1 = t_c_p_client_1.connect(str_2, int_1, i_o_stream_0, int_0, timedelta_0)