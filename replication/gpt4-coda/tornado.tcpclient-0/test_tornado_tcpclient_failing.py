# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.netutil as module_1

def test_case_0():
    try:
        list_0 = []
        str_0 = '.[4K'
        connector_0 = module_0._Connector(list_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        resolver_0 = module_1.Resolver()
        str_0 = None
        int_0 = 125
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        list_0 = []
        str_1 = '@.L[Xu$P9eM:z::qvV'
        tuple_0 = (str_1,)
        connector_0 = module_0._Connector(list_0, tuple_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = None
        str_0 = '`'
        tuple_0 = (int_0, str_0)
        list_0 = [tuple_0]
        list_1 = []
        resolver_0 = module_1.Resolver(*list_1)
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        resolver_0.close()
        t_c_p_client_0.close()
        bool_0 = True
        connector_0 = module_0._Connector(list_0, bool_0)
    except BaseException:
        pass