# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import ssl as module_1
import tornado.netutil as module_2
import tornado.ioloop as module_3
import socket as module_4
import _asyncio as module_5
import concurrent.futures._base as module_6

def test_case_0():
    try:
        list_0 = []
        str_0 = ''
        connector_0 = module_0._Connector(list_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        t_c_p_client_0 = module_0.TCPClient()
        t_c_p_client_0.close()
        t_c_p_client_0.close()
        t_c_p_client_0.close()
        str_0 = 'bxEcXR'
        list_0 = [str_0, str_0, str_0]
        s_s_l_context_0 = module_1.SSLContext(*list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'q]fw`lX+'
        dict_0 = {}
        resolver_0 = module_2.Resolver(**dict_0)
        int_0 = 2071
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop(**dict_0)
        tuple_0 = (dict_0, i_o_loop_0)
        list_0 = [tuple_0, tuple_0, tuple_0]
        bool_0 = True
        connector_0 = module_0._Connector(list_0, bool_0)
        connector_0.clear_timeouts()
        float_0 = 0.5
        future_0 = connector_0.start(float_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = 'q]fw`lX+'
        dict_0 = {}
        resolver_0 = module_2.Resolver(**dict_0)
        i_o_loop_0 = module_3.IOLoop(**dict_0)
        tuple_0 = (dict_0, i_o_loop_0)
        list_0 = [tuple_0, tuple_0, tuple_0]
        bool_0 = True
        connector_0 = module_0._Connector(list_0, bool_0)
        connector_0.clear_timeouts()
        address_family_0 = module_4.AddressFamily.AF_NETLINK
        connector_1 = module_0._Connector(list_0, address_family_0)
        connector_2 = module_0._Connector(list_0, str_0)
        connector_1.on_connect_timeout()
        future_0 = module_5.Future()
        connector_1.on_connect_done(address_family_0, address_family_0, tuple_0, future_0)
        iterator_0 = None
        address_family_1 = module_4.AddressFamily.AF_NETBEUI
        connector_2.on_connect_done(iterator_0, address_family_1, tuple_0, future_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'q]fw`lX+'
        dict_0 = {}
        resolver_0 = module_2.Resolver(**dict_0)
        t_c_p_client_0 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop(**dict_0)
        tuple_0 = (dict_0, i_o_loop_0)
        list_0 = [tuple_0, tuple_0, tuple_0]
        bool_0 = True
        t_c_p_client_0.close()
        connector_0 = module_0._Connector(list_0, bool_0)
        connector_0.clear_timeouts()
        address_family_0 = module_4.AddressFamily.AF_NETLINK
        connector_1 = module_0._Connector(list_0, address_family_0)
        connector_1.on_connect_timeout()
        connector_2 = module_0._Connector(list_0, str_0)
        connector_1.on_connect_timeout()
        address_family_1 = module_4.AddressFamily.AF_UNIX
        future_0 = module_5.Future()
        connector_1.on_connect_done(address_family_1, address_family_1, tuple_0, future_0)
        iterator_0 = None
        address_family_2 = module_4.AddressFamily.AF_NETBEUI
        connector_2.on_connect_done(iterator_0, address_family_2, tuple_0, future_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'q]fw`lX+'
        t_c_p_client_0 = module_0.TCPClient()
        str_1 = 'Unsupported header value %r'
        int_0 = -1029
        dict_0 = {str_1: str_0}
        i_o_stream_0 = t_c_p_client_0.connect(str_1, int_0, dict_0, int_0)
        dict_1 = {}
        resolver_0 = module_2.Resolver(**dict_1)
        int_1 = 2062
        awaitable_0 = resolver_0.resolve(str_0, int_1)
        t_c_p_client_1 = module_0.TCPClient()
        t_c_p_client_2 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop(**dict_1)
        tuple_0 = (dict_1, i_o_loop_0)
        list_0 = [tuple_0, tuple_0, tuple_0]
        bytes_0 = b'\xfc\x8f\xef\x80\xe0\x0c\xc4'
        connector_0 = module_0._Connector(list_0, bytes_0)
        connector_0.close_streams()
        bool_0 = False
        connector_1 = module_0._Connector(list_0, bool_0)
        tuple_1 = connector_1.split(list_0)
        connector_1.on_connect_timeout()
        t_c_p_client_0.close()
        connector_2 = module_0._Connector(list_0, bool_0)
        connector_2.clear_timeouts()
        str_2 = ''
        connector_2.clear_timeout()
        connector_1.on_timeout()
        connector_3 = module_0._Connector(list_0, str_2)
        connector_0.clear_timeout()
        list_1 = [tuple_0, tuple_0]
        address_family_0 = module_4.AddressFamily.AF_UNSPEC
        future_0 = module_5.Future()
        future_1 = module_6.Future()
        connector_4 = module_0._Connector(list_1, dict_1)
        connector_4.on_connect_done(future_1, address_family_0, tuple_0, future_0)
    except BaseException:
        pass

def test_case_6():
    try:
        t_c_p_client_0 = module_0.TCPClient()
        str_0 = 'Unsupported header value %r'
        dict_0 = {}
        resolver_0 = module_2.Resolver(**dict_0)
        int_0 = 50
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        int_1 = 2085
        awaitable_1 = resolver_0.resolve(str_0, int_1)
        t_c_p_client_1 = module_0.TCPClient()
        t_c_p_client_2 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop(**dict_0)
        tuple_0 = (dict_0, i_o_loop_0)
        list_0 = [tuple_0, tuple_0]
        bytes_0 = b'\xfc\x8f\xef\x80\xe0\x0c\xc4'
        connector_0 = module_0._Connector(list_0, bytes_0)
        float_0 = 3216.9
        connector_0.set_timeout(float_0)
        connector_0.close_streams()
        bool_0 = False
        connector_1 = module_0._Connector(list_0, bool_0)
        tuple_1 = connector_1.split(list_0)
        t_c_p_client_0.close()
        connector_2 = module_0._Connector(list_0, bool_0)
        connector_2.clear_timeouts()
        str_1 = ''
        connector_1.on_timeout()
        connector_3 = module_0._Connector(list_0, str_1)
        connector_0.clear_timeout()
        address_family_0 = module_4.AddressFamily.AF_UNSPEC
        future_0 = module_5.Future(**dict_0)
        connector_2.on_connect_done(awaitable_1, address_family_0, tuple_0, future_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'q]fw`lX+'
        t_c_p_client_0 = module_0.TCPClient()
        str_1 = 'Unsupported header value %r'
        int_0 = -1040
        dict_0 = {str_1: str_0}
        i_o_stream_0 = t_c_p_client_0.connect(str_1, int_0, dict_0, int_0)
        dict_1 = {}
        resolver_0 = module_2.Resolver(**dict_1)
        int_1 = 2046
        awaitable_0 = resolver_0.resolve(str_0, int_1)
        t_c_p_client_1 = module_0.TCPClient()
        t_c_p_client_2 = module_0.TCPClient()
        i_o_loop_0 = module_3.IOLoop(**dict_1)
        bytes_0 = b'\x10'
        tuple_0 = (i_o_loop_0, bytes_0)
        list_0 = [tuple_0, tuple_0]
        future_0 = module_6.Future()
        connector_0 = module_0._Connector(list_0, future_0)
        connector_0.on_connect_timeout()
        tuple_1 = (dict_1, i_o_loop_0)
        list_1 = [tuple_1, tuple_0, tuple_1]
        bytes_1 = b'\xfc\x8f\xef\x80\xe0\x0c\xc4'
        connector_1 = module_0._Connector(list_1, bytes_1)
        connector_1.close_streams()
        bool_0 = False
        connector_2 = module_0._Connector(list_1, bool_0)
        tuple_2 = connector_2.split(list_1)
        t_c_p_client_0.close()
        connector_3 = module_0._Connector(list_1, bool_0)
        connector_3.clear_timeouts()
        connector_2.on_timeout()
    except BaseException:
        pass