# Automatically generated by Pynguin.
import tornado.netutil as module_0
import ssl as module_1
import socket as module_2
import tornado.ioloop as module_3
import _asyncio as module_4

def test_case_0():
    try:
        str_0 = ''
        int_0 = -2773
        list_0 = module_0.bind_sockets(int_0, str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'SERVER_NAME'
        socket_0 = module_0.bind_unix_socket(str_0)
        callable_0 = None
        callable_1 = module_0.add_accept_handler(socket_0, callable_0)
    except BaseException:
        pass

def test_case_2():
    try:
        resolver_0 = module_0.Resolver()
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '\r<GxYe&rX(%}C!vjH'
        str_1 = 'W\tRRU~=W7me>6nq+'
        str_2 = 'ymK3Y,uG&?s)i'
        dict_0 = {str_0: str_0, str_1: str_2}
        resolver_0 = module_0.Resolver(**dict_0)
    except BaseException:
        pass

def test_case_4():
    try:
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_5():
    try:
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_6():
    try:
        socket_0 = None
        s_s_l_context_0 = module_1.SSLContext()
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
    except BaseException:
        pass

def test_case_7():
    try:
        s_s_l_context_0 = None
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'QaDq0YX!7s`f'
        str_1 = '|&pX^4U'
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'QaDq0YX!7s`f'
        int_0 = 2086
        address_family_0 = module_2.AddressFamily.AF_WANPIPE
        bool_0 = True
        list_0 = module_0.bind_sockets(int_0, str_0, address_family_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = None
        int_0 = None
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        resolver_0 = module_0.Resolver()
        int_0 = 60
        list_0 = module_0.bind_sockets(int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        i_o_loop_0 = module_3.IOLoop()
        executor_resolver_0 = module_0.ExecutorResolver()
        executor_resolver_0.close()
        str_0 = None
        bool_0 = module_0.is_valid_ip(str_0)
        int_0 = 814
        int_1 = -541
        list_0 = module_0.bind_sockets(int_1, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '>:o`1f\x0b=jpBi\n@O'
        int_0 = -1036
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        bool_0 = True
        int_1 = -656
        address_family_0 = None
        list_0 = module_0.bind_sockets(int_0, str_0, address_family_0, int_0, int_1, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '>:o`1f\x0b=jpBi\n@O'
        int_0 = -1058
        dict_0 = {str_0: int_0, int_0: str_0, int_0: int_0, int_0: str_0}
        list_0 = [int_0, dict_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        override_resolver_0.close()
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'PVu@u1LGa5-usxMEBB`?'
        int_0 = 1686
        str_1 = '{Ib'
        str_2 = 'gMQa<V'
        dict_0 = {str_1: str_1, str_1: str_1, str_2: str_2}
        dict_1 = None
        list_0 = [dict_0, dict_1]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        awaitable_0 = override_resolver_0.resolve(str_0, int_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '>:o`1f\x0b=jpBi\n@O'
        int_0 = -1058
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        dict_0 = {}
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        address_family_0 = module_2.AddressFamily.AF_QIPCRTR
        awaitable_0 = resolver_0.resolve(str_0, int_0, address_family_0)
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        str_1 = 'Starts or resumes the generator, running until it reaches a\n        yield point that is not ready.\n        '
        bool_0 = module_0.is_valid_ip(str_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '>:o`1f\x0b=jpBi\n@O'
        int_0 = -1046
        int_1 = None
        address_family_0 = module_2.AddressFamily.AF_RDS
        resolver_0 = module_0.Resolver()
        awaitable_0 = resolver_0.resolve(str_0, int_1, address_family_0)
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        dict_0 = {}
        resolver_1 = module_0.Resolver()
        resolver_1.close()
        int_2 = 4014
        str_1 = '\x00'
        bool_0 = module_0.is_valid_ip(str_1)
        str_2 = "Ia|!G#QC=dpz\n'~+"
        awaitable_1 = resolver_1.resolve(str_2, int_2)
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        int_3 = 1411
        address_family_1 = module_2.AddressFamily.AF_UNSPEC
        list_0 = module_0.bind_sockets(int_3, address_family_1)
    except BaseException:
        pass

def test_case_18():
    try:
        int_0 = None
        str_0 = '1'
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_19():
    try:
        i_o_loop_0 = module_3.IOLoop()
        executor_resolver_0 = module_0.ExecutorResolver()
        int_0 = None
        str_0 = '1'
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_20():
    try:
        i_o_loop_0 = module_3.IOLoop()
        executor_resolver_0 = module_0.ExecutorResolver()
        executor_resolver_0.close()
        int_0 = None
        str_0 = '1'
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_21():
    try:
        i_o_loop_0 = module_3.IOLoop()
        threaded_resolver_0 = module_0.ThreadedResolver()
        threaded_resolver_0.initialize()
        executor_resolver_0 = module_0.ExecutorResolver()
        executor_resolver_0.close()
        dict_0 = {}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        s_s_l_context_1 = module_0.ssl_options_to_context(dict_0)
        s_s_l_context_2 = module_0.ssl_options_to_context(s_s_l_context_1)
        str_0 = '1'
        int_0 = 1395
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_22():
    try:
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_0.make_current()
        str_0 = ':('
        socket_0 = module_0.bind_unix_socket(str_0)
        future_0 = module_4.Future()
        callable_0 = module_0.add_accept_handler(socket_0, future_0)
        int_0 = 2
        executor_resolver_0 = module_0.ExecutorResolver()
        executor_resolver_0.close()
        str_1 = None
        bool_0 = module_0.is_valid_ip(str_1)
        dict_0 = {}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        s_s_l_context_1 = module_0.ssl_options_to_context(dict_0)
        str_2 = '1'
        int_1 = -541
        bool_1 = False
        executor_resolver_0.close()
        list_0 = module_0.bind_sockets(int_1, str_2, int_0, bool_1)
    except BaseException:
        pass

def test_case_23():
    try:
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_0.make_current()
        str_0 = ':('
        socket_0 = module_0.bind_unix_socket(str_0)
        future_0 = module_4.Future()
        executor_resolver_0 = module_0.ExecutorResolver()
        executor_resolver_0.close()
        str_1 = None
        bool_0 = module_0.is_valid_ip(str_1)
        int_0 = None
        dict_0 = {}
        str_2 = '1'
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        int_1 = 808
        bool_1 = module_0.is_valid_ip(str_2)
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        executor_resolver_0.close()
        executor_resolver_0.initialize(socket_0)
        list_0 = module_0.bind_sockets(int_0, str_2, int_1)
    except BaseException:
        pass

def test_case_24():
    try:
        i_o_loop_0 = module_3.IOLoop()
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        i_o_loop_0.make_current()
        list_0 = []
        executor_resolver_0 = module_0.ExecutorResolver(*list_0)
        str_0 = None
        int_0 = None
        list_1 = executor_resolver_0.resolve(str_0, int_0)
        str_1 = '.'
        str_2 = ',pz9w'
        int_1 = -3326
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        list_2 = default_executor_resolver_0.resolve(str_2, int_1)
        socket_0 = module_0.bind_unix_socket(str_1)
    except BaseException:
        pass