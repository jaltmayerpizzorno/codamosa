# Automatically generated by Pynguin.
import tornado.tcpclient as module_0
import tornado.ioloop as module_1
import tornado.gen as module_2
import concurrent.futures._base as module_3
import socket as module_4
import ssl as module_5

def test_case_0():
    pass

def test_case_1():
    t_c_p_client_0 = module_0.TCPClient()

def test_case_2():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    t_c_p_client_0.close()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_0)
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    float_0 = None
    connector_0 = module_0._Connector(list_1, float_0)
    connector_0.clear_timeouts()

def test_case_3():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '%a %b %d %H:%M:%S %Y'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    t_c_p_client_2 = module_0.TCPClient(list_1)
    str_2 = '|54~:*mJW\\X}cB6\r<q[\r'
    int_1 = -16
    connector_0 = module_0._Connector(list_1, t_c_p_client_2)
    connector_0.clear_timeouts()
    str_3 = "[|tkGy'$02&$rrf9"
    int_2 = -1155
    i_o_stream_1 = t_c_p_client_1.connect(str_3, int_2, int_2, str_3)
    t_c_p_client_2.close()
    int_3 = 3
    t_c_p_client_3 = module_0.TCPClient()
    i_o_stream_2 = t_c_p_client_3.connect(str_2, int_3, int_1, str_1)
    callable_1 = None
    connector_1 = module_0._Connector(list_1, callable_1)
    connector_2 = module_0._Connector(list_1, callable_1)
    connector_1.clear_timeout()
    connector_2.on_connect_timeout()
    str_4 = ''
    int_4 = 550
    i_o_stream_3 = t_c_p_client_2.connect(str_4, int_0, int_4)
    connector_2.close_streams()
    connector_0.on_timeout()

def test_case_4():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_0)
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    float_0 = None
    connector_0 = module_0._Connector(list_1, float_0)

def test_case_5():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2116
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '3*/<'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    callable_1 = None
    connector_0 = module_0._Connector(list_1, callable_1)
    connector_0.on_connect_timeout()

def test_case_6():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '3*/<'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    connector_0 = module_0._Connector(list_1, callable_0)
    connector_1 = module_0._Connector(list_1, callable_0)
    connector_1.on_timeout()

def test_case_7():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '3*/<'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    connector_0 = module_0._Connector(list_1, t_c_p_client_1)
    connector_0.clear_timeout()
    connector_0.on_timeout()

def test_case_8():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '3*/<'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_0.close()
    callable_0 = module_2.coroutine(tuple_0)
    t_c_p_client_0.close()
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    float_0 = -711.068418
    str_2 = 'code'
    int_1 = 2
    executor_0 = module_3.Executor()
    int_2 = -2925
    i_o_stream_1 = t_c_p_client_0.connect(str_2, int_1, executor_0, int_2, float_0)
    callable_1 = None
    connector_0 = module_0._Connector(list_1, callable_1)
    connector_0.set_connect_timeout(float_0)
    connector_0.on_timeout()

def test_case_9():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = 'ejAsvLKr"'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_0.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    float_0 = -711.068418
    str_2 = 'code'
    int_1 = 2
    executor_0 = module_3.Executor()
    i_o_stream_1 = t_c_p_client_1.connect(str_2, int_1, executor_0, int_0, float_0)
    connector_0 = module_0._Connector(list_1, i_o_stream_0)
    connector_0.on_connect_timeout()
    callable_1 = None
    connector_1 = module_0._Connector(list_1, callable_1)
    connector_0.clear_timeout()
    connector_0.on_timeout()

def test_case_10():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '%a %b %d %H:%M:%S %Y'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    int_1 = -3701
    i_o_stream_1 = t_c_p_client_0.connect(str_1, int_1, int_0, str_0)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    t_c_p_client_2 = module_0.TCPClient(list_1)
    connector_0 = module_0._Connector(list_1, t_c_p_client_2)
    connector_0.clear_timeouts()
    i_o_stream_2 = t_c_p_client_0.connect(str_0, int_0, int_0)
    str_2 = 'piRI\x0b7\r#{q!$pUP,'
    address_family_0 = module_4.AddressFamily.AF_NETBEUI
    i_o_stream_3 = t_c_p_client_2.connect(str_2, int_0, address_family_0)
    connector_0.on_timeout()
    float_0 = 1401.0
    connector_0.set_timeout(float_0)

def test_case_11():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '%a %b %d %H:%M:%S %Y'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    float_0 = None
    t_c_p_client_2 = module_0.TCPClient(list_1)
    int_1 = 0
    connector_0 = module_0._Connector(list_1, t_c_p_client_2)
    connector_0.clear_timeouts()
    str_2 = '&87`;\n_'
    address_family_0 = module_4.AddressFamily.AF_NETBEUI
    int_2 = 2828
    set_0 = {str_1, int_1, address_family_0}
    str_3 = 'T0oA'
    i_o_stream_1 = t_c_p_client_0.connect(str_3, int_1, str_0)
    i_o_stream_2 = t_c_p_client_0.connect(str_2, int_2, set_0, float_0)
    callable_1 = None
    connector_1 = module_0._Connector(list_1, callable_1)
    float_1 = -882.9
    connector_1.set_timeout(float_1)
    connector_1.clear_timeout()
    connector_1.close_streams()
    connector_2 = module_0._Connector(list_1, callable_1)
    connector_0.on_timeout()

def test_case_12():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    str_1 = '%a %b %d %H:%M:%S %Y'
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_1)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2]
    t_c_p_client_2 = module_0.TCPClient(list_1)
    s_s_l_context_0 = module_5.SSLContext()
    connector_0 = module_0._Connector(list_1, s_s_l_context_0)
    float_0 = 2704.25417
    connector_0.set_timeout(float_0)
    int_1 = 0
    connector_1 = module_0._Connector(list_1, s_s_l_context_0)
    connector_0.clear_timeouts()
    str_2 = '&87`;\n_'
    address_family_0 = module_4.AddressFamily.AF_PPPOX
    i_o_stream_1 = t_c_p_client_1.connect(str_1, int_1, address_family_0, str_2)
    connector_1.close_streams()

def test_case_13():
    t_c_p_client_0 = module_0.TCPClient()
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_1 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_1.connect(str_0, int_0, int_0, str_0)
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_0)
    t_c_p_client_2 = module_0.TCPClient()
    t_c_p_client_2.close()
    callable_0 = module_2.coroutine(tuple_0)
    list_0 = []
    tuple_1 = (list_0, list_0)
    tuple_2 = (callable_0, tuple_1)
    list_1 = [tuple_2, tuple_2]
    t_c_p_client_3 = module_0.TCPClient(list_1)
    float_0 = 0.3
    connector_0 = module_0._Connector(list_1, float_0)
    connector_1 = module_0._Connector(list_1, t_c_p_client_3)
    connector_1.clear_timeouts()
    float_1 = 753.91
    connector_1.set_connect_timeout(float_1)
    str_1 = '&87`;\n_'
    int_1 = 1812
    s_s_l_context_0 = module_5.SSLContext()
    none_type_0 = None
    i_o_stream_1 = t_c_p_client_2.connect(str_1, int_1, s_s_l_context_0, none_type_0)
    callable_1 = None
    list_2 = [tuple_2]
    connector_2 = module_0._Connector(list_2, callable_1)
    connector_1.clear_timeouts()
    connector_0.clear_timeout()
    connector_0.on_connect_timeout()
    connector_1.close_streams()
    connector_1.on_timeout()

def test_case_14():
    i_o_loop_0 = module_1.IOLoop()
    str_0 = 'Ff%A`'
    int_0 = 2105
    t_c_p_client_0 = module_0.TCPClient()
    i_o_stream_0 = t_c_p_client_0.connect(str_0, int_0, int_0, str_0)
    tuple_0 = (i_o_loop_0, i_o_stream_0, str_0)
    t_c_p_client_1 = module_0.TCPClient()
    t_c_p_client_1.close()
    callable_0 = module_2.coroutine(tuple_0)
    bool_0 = False
    address_family_0 = module_4.AddressFamily.AF_ATMSVC
    tuple_1 = ()
    future_0 = None
    dict_0 = {i_o_stream_0: callable_0, t_c_p_client_1: tuple_0}
    float_0 = None
    tuple_2 = (dict_0, float_0)
    list_0 = [tuple_2, tuple_2, tuple_2]
    connector_0 = module_0._Connector(list_0, dict_0)
    connector_0.on_connect_timeout()
    int_1 = 159
    i_o_stream_1 = t_c_p_client_0.connect(str_0, int_1, str_0)
    connector_0.on_connect_done(bool_0, address_family_0, tuple_1, future_0)