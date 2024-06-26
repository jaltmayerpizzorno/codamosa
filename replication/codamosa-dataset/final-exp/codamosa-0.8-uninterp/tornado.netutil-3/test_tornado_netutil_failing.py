# Automatically generated by Pynguin.
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

def test_case_0():
    try:
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_1():
    try:
        resolver_0 = module_0.Resolver()
        str_0 = ''
        resolver_0.close()
        int_0 = -1171
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        list_0 = [resolver_0, resolver_0, resolver_0]
        dict_0 = {}
        override_resolver_0 = module_0.OverrideResolver(*list_0, **dict_0)
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
        list_0 = []
        threaded_resolver_0 = module_0.ThreadedResolver(*list_0)
    except BaseException:
        pass

def test_case_4():
    try:
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        int_0 = -843
        str_0 = None
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'Resolver implementation using a `concurrent.futures.Executor`.\n\n    Use this instead of `ThreadedResolver` when you require additional\n    control over the executor being used.\n\n    The executor will be shut down when the resolver is closed unless\n    ``close_resolver=False``; use this if you want to reuse the same\n    executor elsewhere.\n\n    .. versionchanged:: 5.0\n       The ``io_loop`` argument (deprecated since version 4.1) has been removed.\n\n    .. deprecated:: 5.0\n       The default `Resolver` now uses `.IOLoop.run_in_executor`; use that instead\n       of this class.\n    '
        bool_0 = module_0.is_valid_ip(str_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = 'UN\ng\\fo@8$QO|u'
        str_1 = 'PM(`\rmyJ'
        bool_0 = False
        address_family_0 = module_1.AddressFamily.AF_IRDA
        dict_0 = {str_1: bool_0, str_1: address_family_0, str_0: str_1, str_0: str_1}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = 'UN\ng\\fo@8$QO|u'
        int_0 = -305
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        callable_0 = None
        callable_1 = module_0.add_accept_handler(socket_0, callable_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'G\\BLb7Jab~HZ>>\x0b~y\\'
        bool_0 = module_0.is_valid_ip(str_0)
        socket_0 = module_0.bind_unix_socket(str_0)
        dict_0 = None
        str_1 = '\\(B'
        var_0 = socket_0.detach()
        dict_1 = {str_1: dict_0}
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0, **dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 2083
        list_0 = module_0.bind_sockets(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        list_0 = []
        str_0 = ';H@5.\t%LZu,7TRAtF7V'
        dict_0 = {str_0: str_0}
        s_s_l_context_0 = module_2.SSLContext(*list_0, **dict_0)
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        bool_0 = module_0.is_valid_ip(str_0)
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        str_1 = ''
        bool_1 = module_0.is_valid_ip(str_1)
        resolver_0 = module_0.Resolver(**dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        list_0 = []
        str_0 = ';H@5.\t%LZu,7TRAtF7V'
        dict_0 = {str_0: str_0}
        s_s_l_context_0 = module_2.SSLContext(*list_0, **dict_0)
        int_0 = 805
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        list_1 = default_executor_resolver_0.resolve(str_0, int_0)
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        bool_0 = module_0.is_valid_ip(str_0)
        int_1 = 65536
        address_family_0 = module_1.AddressFamily.AF_BLUETOOTH
        list_2 = module_0.bind_sockets(int_1)
        str_1 = 'I&)c1)+]$$'
        list_3 = default_executor_resolver_0.resolve(str_1, int_1, address_family_0)
        int_2 = 1617
        socket_0 = module_0.bind_unix_socket(str_1, int_2)
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
        str_2 = '\\(B'
        resolver_0 = module_0.Resolver()
        address_family_1 = module_1.AddressFamily.AF_PPPOX
        bool_1 = True
        list_4 = module_0.bind_sockets(int_2, str_2, address_family_1, int_1, bool_1)
    except BaseException:
        pass

def test_case_12():
    try:
        list_0 = []
        str_0 = ';H@5.\t%LZu,7TRAtF7V'
        dict_0 = {str_0: str_0}
        s_s_l_context_0 = module_2.SSLContext(*list_0, **dict_0)
        int_0 = 805
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        list_1 = default_executor_resolver_0.resolve(str_0, int_0)
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        bool_0 = module_0.is_valid_ip(str_0)
        default_executor_resolver_1 = module_0.DefaultExecutorResolver()
        int_1 = 65536
        address_family_0 = module_1.AddressFamily.AF_BLUETOOTH
        list_2 = module_0.bind_sockets(int_1)
        str_1 = 'I&)c1)+]$$'
        list_3 = default_executor_resolver_1.resolve(str_1, int_1, address_family_0)
        str_2 = '4tDO'
        int_2 = 1649
        socket_0 = module_0.bind_unix_socket(str_2, int_2)
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
        str_3 = ''
        list_4 = module_0.bind_sockets(int_0, str_3, bool_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = '2'
        int_0 = 1310
        bool_0 = module_0.is_valid_ip(str_0)
        address_family_0 = module_1.AddressFamily.AF_BRIDGE
        list_0 = module_0.bind_sockets(int_0, address_family_0, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        resolver_0 = None
        dict_0 = {resolver_0: resolver_0, resolver_0: resolver_0, resolver_0: resolver_0}
        str_0 = 'queue not full, why are putters waiting?'
        int_0 = -2353
        address_family_0 = module_1.AddressFamily.AF_ROSE
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        list_0 = default_executor_resolver_0.resolve(str_0, int_0, address_family_0)
        int_1 = 394
        list_1 = [int_1, int_1]
        dict_1 = {}
        override_resolver_0 = module_0.OverrideResolver(*list_1, **dict_1)
        override_resolver_0.initialize(resolver_0, dict_0)
        str_1 = None
        address_family_1 = module_1.AddressFamily.AF_SECURITY
        awaitable_0 = override_resolver_0.resolve(str_1, int_1, address_family_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'X'
        list_0 = [str_0, str_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        override_resolver_0.close()
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'K7l)IBuQ\x0cDm6'
        int_0 = 805
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        list_0 = default_executor_resolver_0.resolve(str_0, int_0)
        bool_0 = module_0.is_valid_ip(str_0)
        default_executor_resolver_1 = module_0.DefaultExecutorResolver()
        int_1 = 65536
        address_family_0 = module_1.AddressFamily.AF_BLUETOOTH
        list_1 = module_0.bind_sockets(int_1)
        list_2 = default_executor_resolver_1.resolve(str_0, int_1, address_family_0)
        int_2 = 1625
        socket_0 = module_0.bind_unix_socket(str_0, int_2)
        str_1 = '3'
        bool_1 = False
        list_3 = module_0.bind_sockets(int_0, str_1, bool_1)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/dev/null'
        socket_0 = module_0.bind_unix_socket(str_0)
    except BaseException:
        pass