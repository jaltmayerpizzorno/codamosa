# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.netutil as module_1
import ssl as module_2
import tornado.ioloop as module_3
import tornado.util as module_4
import socket as module_5
import _asyncio as module_6
import concurrent.futures._base as module_7

def test_case_0():
    try:
        list_0 = []
        float_0 = 1962.5165
        connector_0 = module_0._Connector(list_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        list_0 = [tuple_0]
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        connector_0 = module_0._Connector(list_0, t_c_p_client_0)
    except BaseException:
        pass

def test_case_2():
    try:
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        t_c_p_client_0.close()
        list_0 = None
        s_s_l_context_0 = module_2.SSLContext(*list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '.i_FN\r"yYHut'
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        t_c_p_client_1 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        callable_0 = None
        t_c_p_client_2 = module_0.TCPClient()
        t_c_p_client_2.close()
        connector_0 = module_0._Connector(list_0, callable_0)
        future_0 = connector_0.start()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '.i_FN\r"yYHut'
        i_o_loop_0 = module_3.IOLoop()
        t_c_p_client_0 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        callable_0 = None
        connector_0 = module_0._Connector(list_0, callable_0)
        connector_0.on_timeout()
        iterator_0 = None
        connector_0.clear_timeouts()
        connector_1 = module_0._Connector(list_0, callable_0)
        connector_1.try_connect(iterator_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '.i_FN\r"yYHut'
        i_o_loop_0 = module_3.IOLoop()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        callable_0 = None
        connector_0 = module_0._Connector(list_0, callable_0)
        address_family_0 = module_5.AddressFamily.AF_AX25
        float_0 = 1.0
        future_0 = module_6.Future()
        connector_0.on_connect_done(float_0, address_family_0, tuple_0, future_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '.i_FN\r"yYHut'
        int_0 = 404
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        t_c_p_client_1 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        callable_0 = None
        connector_0 = module_0._Connector(list_0, callable_0)
        timeout_error_1 = module_4.TimeoutError()
        connector_0.on_connect_timeout()
        timeout_error_2 = module_4.TimeoutError()
        connector_0.on_connect_timeout()
        i_o_loop_0.remove_handler(int_0)
        connector_1 = module_0._Connector(list_0, callable_0)
        connector_2 = module_0._Connector(list_0, callable_0)
        iterator_0 = None
        connector_2.try_connect(iterator_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '.i_FN\r"yYHut'
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        t_c_p_client_1 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        list_1 = []
        connector_0 = module_0._Connector(list_0, list_1)
        connector_0.close_streams()
        callable_0 = None
        connector_1 = module_0._Connector(list_0, callable_0)
        float_0 = None
        connector_1.set_timeout(float_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = '.i_FN\r"yYHut'
        t_c_p_client_0 = module_0.TCPClient()
        t_c_p_client_0.close()
        i_o_loop_0 = module_3.IOLoop()
        t_c_p_client_1 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        callable_0 = None
        connector_0 = module_0._Connector(list_0, callable_0)
        connector_0.clear_timeout()
        connector_0.close_streams()
        connector_1 = module_0._Connector(list_0, callable_0)
        list_1 = [tuple_0, tuple_0, tuple_0, tuple_0, tuple_0, tuple_0]
        connector_0.on_connect_timeout()
        timeout_error_1 = module_4.TimeoutError()
        connector_1.on_connect_timeout()
        connector_1.clear_timeouts()
        iterator_0 = None
        connector_2 = module_0._Connector(list_1, callable_0)
        connector_1.on_timeout()
        connector_3 = module_0._Connector(list_1, callable_0)
        connector_3.try_connect(iterator_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '.i_FN\r"yYHut'
        int_0 = 404
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        t_c_p_client_1 = module_0.TCPClient()
        float_0 = 1000.0
        str_1 = 'Resolver'
        tuple_0 = (str_1, t_c_p_client_0)
        float_1 = -1274.35744
        set_0 = set()
        tuple_1 = (float_1, set_0)
        list_0 = [tuple_0, tuple_0, tuple_1, tuple_1]
        str_2 = 'X,NGA(\t:\x0c^x$(wD/d5n'
        connector_0 = module_0._Connector(list_0, str_2)
        connector_0.set_timeout(float_0)
        timeout_error_0 = module_4.TimeoutError()
        tuple_2 = (timeout_error_0, str_0)
        list_1 = [tuple_2]
        connector_1 = module_0._Connector(list_1, i_o_loop_1)
        connector_1.on_timeout()
        list_2 = [tuple_2]
        list_3 = []
        connector_2 = module_0._Connector(list_2, list_3)
        connector_2.close_streams()
        callable_0 = None
        connector_3 = module_0._Connector(list_2, callable_0)
        address_family_0 = module_5.AddressFamily.AF_AX25
        float_2 = 1.0
        future_0 = module_6.Future()
        i_o_stream_0 = t_c_p_client_1.connect(str_0, int_0)
        connector_3.on_connect_done(float_2, address_family_0, tuple_2, future_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '.i_FN\r"yYHut'
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        t_c_p_client_0.close()
        i_o_loop_1 = i_o_loop_0.instance()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        connector_0 = module_0._Connector(list_0, i_o_loop_1)
        connector_0.on_timeout()
        list_1 = []
        connector_1 = module_0._Connector(list_0, list_1)
        connector_1.close_streams()
        connector_1.on_connect_timeout()
        callable_0 = None
        connector_2 = module_0._Connector(list_0, callable_0)
        executor_0 = module_7.Executor()
        i_o_loop_0.set_default_executor(executor_0)
        connector_1.close_streams()
        address_family_0 = module_5.AddressFamily.AF_AX25
        future_0 = module_6.Future()
        str_1 = 'Cross origin websockets not allowed'
        future_1 = None
        connector_1.on_connect_done(timeout_error_0, address_family_0, tuple_0, future_0)
        connector_0.on_connect_done(str_1, address_family_0, tuple_0, future_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '.i_FN\r"yYHut'
        t_c_p_client_0 = module_0.TCPClient()
        t_c_p_client_0.close()
        t_c_p_client_1 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        t_c_p_client_2 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0]
        connector_0 = module_0._Connector(list_0, i_o_loop_1)
        connector_0.on_timeout()
        list_1 = [tuple_0]
        list_2 = []
        connector_1 = module_0._Connector(list_1, list_2)
        connector_1.close_streams()
        connector_1.on_connect_timeout()
        callable_0 = None
        connector_2 = module_0._Connector(list_1, callable_0)
        float_0 = -4000.4
        connector_1.set_connect_timeout(float_0)
        connector_1.close_streams()
        address_family_0 = module_5.AddressFamily.AF_AX25
        connector_1.close_streams()
        future_0 = module_6.Future()
        str_1 = 'Cross origin websockets not allowed'
        connector_1.clear_timeouts()
        connector_2.on_connect_done(str_1, address_family_0, tuple_0, future_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '.i_FN\r"yYHut'
        int_0 = 404
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop()
        t_c_p_client_0.close()
        i_o_loop_1 = i_o_loop_0.instance()
        t_c_p_client_1 = module_0.TCPClient()
        timeout_error_0 = module_4.TimeoutError()
        tuple_0 = (timeout_error_0, str_0)
        list_0 = [tuple_0, tuple_0]
        list_1 = [list_0, i_o_loop_1, int_0]
        connector_0 = module_0._Connector(list_0, list_1)
        connector_0.clear_timeout()
        list_2 = [tuple_0]
        connector_1 = module_0._Connector(list_2, i_o_loop_1)
        connector_1.on_timeout()
        list_3 = [tuple_0]
        list_4 = []
        connector_2 = module_0._Connector(list_3, list_4)
        connector_2.close_streams()
        connector_2.on_connect_timeout()
        callable_0 = None
        connector_3 = module_0._Connector(list_3, callable_0)
        connector_2.close_streams()
        address_family_0 = module_5.AddressFamily.AF_INET
        float_0 = 471.343642
        connector_2.set_timeout(float_0)
        connector_2.close_streams()
        future_0 = module_6.Future()
        str_1 = 'xsrf_cookie_version'
        connector_2.clear_timeouts()
        connector_3.on_connect_done(str_1, address_family_0, tuple_0, future_0)
    except BaseException:
        pass