# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import socket as module_1
import tornado.netutil as module_2
import tornado.ioloop as module_3
import builtins as module_4
import datetime as module_5
import tornado.util as module_6
import _asyncio as module_7

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    str_0 = 'jlQ86]c;iO*'
    int_0 = -2112
    address_family_0 = module_1.AddressFamily.AF_UNIX
    dict_0 = {str_0: address_family_0}
    resolver_0 = module_2.Resolver()
    t_c_p_client_0 = module_0.TCPClient(resolver_0)
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, address_family_0, dict_0, int_0)

def test_case_3():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    t_c_p_client_0 = module_0.TCPClient()
    dict_0 = {i_o_loop_0: i_o_loop_0, i_o_loop_0: i_o_loop_0, t_c_p_client_0: t_c_p_client_0, i_o_loop_0: t_c_p_client_0}
    tuple_0 = (t_c_p_client_0, dict_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    bytearray_0 = module_4.bytearray()
    connector_0 = module_0._Connector(list_0, bytearray_0)
    tuple_1 = connector_0.split(list_0)
    i_o_loop_2 = i_o_loop_0.instance()
    time_0 = module_5.time()
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    connector_0.on_timeout()

def test_case_4():
    i_o_loop_0 = module_3.IOLoop()
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_0, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_timeout()

def test_case_5():
    i_o_loop_0 = module_3.IOLoop()
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_0, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_timeout()
    connector_0.on_connect_timeout()
    timedelta_0 = module_5.timedelta()
    future_0 = module_7.Future()

def test_case_6():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    callable_0 = None
    connector_0 = module_0._Connector(list_0, callable_0)
    connector_0.clear_timeouts()
    connector_0.on_timeout()

def test_case_7():
    i_o_loop_0 = module_3.IOLoop()
    str_0 = ',_L,-L/1/CrMnX'
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_0, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_timeout()
    dict_0 = {str_0: str_0, str_0: i_o_loop_0}
    optional_0 = None
    t_c_p_client_0 = module_0.TCPClient(optional_0)
    connector_0.on_connect_timeout()
    address_family_0 = module_1.AddressFamily.AF_NETBEUI
    timedelta_0 = module_5.timedelta()
    str_1 = ' B'
    tuple_1 = (timedelta_0, str_1, i_o_loop_0)
    future_0 = module_7.Future()
    connector_0.on_connect_done(dict_0, address_family_0, tuple_1, future_0)

def test_case_8():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    selectable_0 = module_3._Selectable()
    connector_0 = module_0._Connector(list_0, selectable_0)
    connector_0.clear_timeout()
    float_0 = -618.0
    timedelta_0 = module_5.timedelta()
    connector_0.set_timeout(float_0)
    connector_0.clear_timeouts()

def test_case_9():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    str_0 = ',_L,-L/1/CrMnX'
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_connect_timeout()
    connector_0.on_timeout()
    dict_0 = {str_0: str_0, str_0: i_o_loop_0}
    optional_0 = None
    t_c_p_client_0 = module_0.TCPClient(optional_0)
    tuple_1 = connector_0.split(list_0)
    address_family_0 = module_1.AddressFamily.AF_NETBEUI
    timedelta_0 = module_5.timedelta()
    str_1 = ' B'
    tuple_2 = (timedelta_0, str_1, i_o_loop_0)
    future_0 = module_7.Future()
    connector_0.on_connect_done(dict_0, address_family_0, tuple_2, future_0)

def test_case_10():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    str_0 = ',_L,-L/1/CrMnX'
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_connect_timeout()
    connector_0.on_timeout()
    dict_0 = {str_0: str_0, str_0: i_o_loop_0}
    optional_0 = None
    t_c_p_client_0 = module_0.TCPClient(optional_0)
    tuple_1 = connector_0.split(list_0)
    address_family_0 = module_1.AddressFamily.AF_NETBEUI
    timedelta_0 = module_5.timedelta()
    str_1 = ' B'
    connector_0.set_connect_timeout(timedelta_0)
    tuple_2 = (timedelta_0, str_1, i_o_loop_0)
    future_0 = module_7.Future()
    connector_0.on_connect_done(dict_0, address_family_0, tuple_2, future_0)

def test_case_11():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    str_0 = ',_L,-L/1/CrMnX'
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    list_0 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_0 = module_0._Connector(list_0, resolver_0)
    connector_0.on_timeout()
    dict_0 = {str_0: str_0, str_0: i_o_loop_0}
    t_c_p_client_0 = module_0.TCPClient(resolver_0)
    connector_0.on_connect_timeout()
    address_family_0 = module_1.AddressFamily.AF_NETBEUI
    connector_0.on_connect_timeout()
    timedelta_0 = module_5.timedelta()
    str_1 = ' B'
    tuple_1 = (timedelta_0, str_1, i_o_loop_0)
    future_0 = module_7.Future()
    connector_0.on_connect_done(dict_0, address_family_0, tuple_1, future_0)

def test_case_12():
    i_o_loop_0 = module_3.IOLoop()
    i_o_loop_1 = i_o_loop_0.instance()
    timeout_error_0 = module_6.TimeoutError()
    tuple_0 = (i_o_loop_1, timeout_error_0)
    executor_0 = None
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    selectable_0 = module_3._Selectable()
    connector_0 = module_0._Connector(list_0, selectable_0)
    connector_0.clear_timeout()
    list_1 = [tuple_0]
    resolver_0 = module_2.Resolver()
    connector_1 = module_0._Connector(list_1, resolver_0)
    connector_1.on_timeout()
    optional_0 = None
    float_0 = 1700.604947
    connector_0.set_connect_timeout(float_0)
    t_c_p_client_0 = module_0.TCPClient(optional_0)
    connector_1.on_connect_timeout()
    float_1 = -618.0
    tuple_1 = connector_1.split(list_1)
    timedelta_0 = module_5.timedelta()
    connector_0.set_timeout(float_1)
    str_0 = ' B'
    tuple_2 = (timedelta_0, str_0, i_o_loop_0)
    connector_0.clear_timeouts()
    future_0 = module_7.Future()
    address_family_0 = module_1.AddressFamily.AF_TIPC
    connector_1.on_connect_done(executor_0, address_family_0, tuple_2, future_0)