# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.netutil as module_1
import socket as module_2
import datetime as module_3

def test_case_0():
    try:
        list_0 = []
        list_1 = [list_0]
        connector_0 = module_0._Connector(list_0, list_1)
    except BaseException:
        pass

def test_case_1():
    try:
        resolver_0 = module_1.Resolver()
        t_c_p_client_0 = module_0.TCPClient(resolver_0)
        t_c_p_client_0.close()
        str_0 = 'ResponseStartLine'
        int_0 = -2636
        address_family_0 = module_2.AddressFamily.AF_NETLINK
        i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, address_family_0, str_0, int_0)
        tuple_0 = ()
        list_0 = [tuple_0, tuple_0, tuple_0]
        dict_0 = {}
        timedelta_0 = module_3.timedelta(**dict_0)
        connector_0 = module_0._Connector(list_0, timedelta_0)
    except BaseException:
        pass