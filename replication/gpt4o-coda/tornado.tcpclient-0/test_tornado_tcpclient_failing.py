# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.netutil as module_1
import _asyncio as module_2

def test_case_0():
    try:
        tuple_0 = None
        list_0 = [tuple_0, tuple_0, tuple_0]
        bytes_0 = b':\xa7\xfa\xa2\x9b\x90y\x81\xb3\xeex*\xc9'
        list_1 = [tuple_0, list_0, bytes_0, tuple_0]
        connector_0 = module_0._Connector(list_0, list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        tuple_0 = None
        list_0 = [tuple_0, tuple_0, tuple_0]
        bytes_0 = b':\xa7\xfa\xa2\x9b\x90y\x81\xb3\xeex*\xc9'
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        t_c_p_client_0.close()
        list_1 = [tuple_0, list_0, bytes_0, tuple_0]
        connector_0 = module_0._Connector(list_0, list_1)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = 'Magyar'
        int_0 = 334
        t_c_p_client_0 = module_0.TCPClient()
        t_c_p_client_0.close()
        resolver_0 = module_1.Resolver()
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        future_0 = module_2.Future()
    except BaseException:
        pass