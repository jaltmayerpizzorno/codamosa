# Automatically generated by Pynguin.
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2
import tornado.ioloop as module_3

def test_case_0():
    try:
        str_0 = ' /\\?o[\x0c^LgJ\t'
        socket_0 = module_0.bind_unix_socket(str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        socket_0 = None
        bytes_0 = b'\tOr'
        callable_0 = module_0.add_accept_handler(socket_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_3():
    try:
        resolver_0 = module_0.Resolver()
        str_0 = 'Future[HTTPResponse]'
        int_0 = 661
        awaitable_0 = resolver_0.resolve(str_0, int_0)
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'SD@}GzC\x0c?#'
        int_0 = 497
        dict_0 = {}
        resolver_0 = module_0.Resolver(**dict_0)
        resolver_0.close()
        int_1 = 152
        list_0 = module_0.bind_sockets(int_0, str_0, int_1, int_1)
    except BaseException:
        pass

def test_case_5():
    try:
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        str_0 = 'Eo'
        int_0 = -2390
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_6():
    try:
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_7():
    try:
        default_executor_resolver_0 = module_0.DefaultExecutorResolver()
        dict_0 = None
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'kOU@1~8Sezb^<.S PGVp'
        int_0 = 698
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        dict_0 = {str_0: int_0}
        dict_1 = {}
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0, **dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = -167
        str_0 = None
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        dict_0 = {}
        str_0 = '/3VN<'
        int_0 = 1906
        list_0 = [int_0, dict_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        awaitable_0 = override_resolver_0.resolve(str_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'Fl}b3~B|_&60'
        dict_0 = {str_0: str_0}
        list_0 = [str_0, dict_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        override_resolver_0.close()
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 9999975
        list_0 = module_0.bind_sockets(int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'Encodes a username/password pair in the format used by HTTP auth.\n\n    The return value is a byte string in the form ``username:password``.\n\n    .. versionadded:: 5.1\n    '
        bool_0 = module_0.is_valid_ip(str_0)
    except BaseException:
        pass

def test_case_14():
    try:
        socket_0 = module_1.socket()
        str_0 = ''
        list_0 = []
        s_s_l_context_0 = module_2.SSLContext(*list_0)
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0, str_0)
        str_1 = "FdM('?c-p"
        resolver_0 = module_0.Resolver()
        bool_0 = module_0.is_valid_ip(str_1)
        default_executor_resolver_0 = module_0.DefaultExecutorResolver(*list_0)
        int_0 = 2275
        var_0 = socket_0.__repr__()
        list_1 = module_0.bind_sockets(int_0, str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'NXh+'
        socket_0 = module_0.bind_unix_socket(str_0)
        dict_0 = {}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        str_1 = "Bt']-~"
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0, str_1)
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        str_2 = '0'
        bool_0 = module_0.is_valid_ip(str_2)
        int_0 = -1964
        address_family_0 = None
        list_0 = module_0.bind_sockets(int_0, address_family_0)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'ssl_version'
        str_1 = 'certfile'
        str_2 = 'cert_reqs'
        str_3 = 'ca_certs'
        str_4 = 'ciphers'
        int_0 = 3
        int_1 = 2
        var_0 = {str_0: int_0, str_1: str_1, str_3: str_3, str_2: int_1, str_3: str_3, str_4: str_4}
        s_s_l_context_0 = module_0.ssl_options_to_context(var_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'NXh+'
        socket_0 = module_0.bind_unix_socket(str_0)
        dict_0 = {}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        str_1 = "Bt']-~"
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0, str_1)
        str_2 = '%00{/ZN'
        int_0 = -2157
        bool_0 = True
        address_family_0 = module_1.AddressFamily.AF_UNIX
        int_1 = None
        int_2 = 1573
        list_0 = module_0.bind_sockets(int_1, str_2, address_family_0, int_2, int_0, bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        str_0 = 'NXh+'
        socket_0 = module_0.bind_unix_socket(str_0)
        dict_1 = {}
        s_s_l_context_1 = module_0.ssl_options_to_context(dict_1)
        str_1 = 'Z\x0b\x0crooJypaa%'
        int_0 = None
        i_o_loop_0 = module_3.IOLoop()
        i_o_loop_1 = i_o_loop_0.instance()
        i_o_loop_2 = i_o_loop_1.instance()
        i_o_loop_3 = i_o_loop_2.instance()
        i_o_loop_4 = i_o_loop_3.instance()
        callable_0 = module_0.add_accept_handler(socket_0, i_o_loop_4)
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        str_2 = 'HOP7.fa4CM)rF8p'
        bool_0 = module_0.is_valid_ip(str_2)
        int_1 = 416
        list_0 = module_0.bind_sockets(int_0, str_1, int_1, bool_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = 'cert_reqs'
        str_1 = 'ca_certs'
        str_2 = 'ciphers'
        int_0 = 2
        var_0 = {str_2: int_0, str_0: str_0, str_1: str_1, str_0: int_0, str_1: str_1, str_2: str_2}
        s_s_l_context_0 = module_0.ssl_options_to_context(var_0)
    except BaseException:
        pass

def test_case_20():
    try:
        dict_0 = {}
        i_o_loop_0 = module_3.IOLoop(**dict_0)
        list_0 = [i_o_loop_0, i_o_loop_0, i_o_loop_0, i_o_loop_0]
        blocking_resolver_0 = module_0.BlockingResolver(**dict_0)
        blocking_resolver_0.initialize()
        executor_resolver_0 = module_0.ExecutorResolver()
        str_0 = 'tGx'
        int_0 = 0
        list_1 = executor_resolver_0.resolve(str_0, int_0)
        blocking_resolver_1 = module_0.BlockingResolver(*list_0)
    except BaseException:
        pass