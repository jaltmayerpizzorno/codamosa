# Automatically generated by Pynguin.
import tornado.netutil as module_0
import ssl as module_1
import socket as module_2

def test_case_0():
    try:
        int_0 = None
        list_0 = module_0.bind_sockets(int_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = '!j=n"5\tEt`9'
        int_0 = -1315
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        s_s_l_context_0 = module_1.SSLContext()
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '=*{7p'
        socket_0 = module_0.bind_unix_socket(str_0)
        address_family_0 = module_2.AddressFamily.AF_RDS
        tuple_0 = (address_family_0,)
        callable_0 = module_0.add_accept_handler(socket_0, tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_4():
    try:
        resolver_0 = module_0.Resolver()
        override_resolver_0 = module_0.OverrideResolver()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'K@A}79+TDp}NC'
        socket_0 = module_2.socket()
        dict_0 = {}
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0)
        dict_1 = {str_0: str_0}
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        override_resolver_0 = module_0.OverrideResolver(**dict_1)
    except BaseException:
        pass

def test_case_6():
    try:
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '.8\rk+Mq1S*V e'
        bool_0 = module_0.is_valid_ip(str_0)
    except BaseException:
        pass

def test_case_8():
    try:
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_9():
    try:
        s_s_l_context_0 = None
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '~B # \\4t<\n0\nl34gnc];'
        bool_0 = module_0.is_valid_ip(str_0)
        str_1 = 'xoT<"R.'
        dict_0 = {str_1: str_1}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'u] \rAU[]I'
        int_0 = -202
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        int_1 = 1943
        list_0 = module_0.bind_sockets(int_1, str_0, int_1)
    except BaseException:
        pass

def test_case_12():
    try:
        int_0 = 3000
        str_0 = ''
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = None
        int_0 = 825
        socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
    except BaseException:
        pass

def test_case_14():
    try:
        dict_0 = {}
        int_0 = 1566
        str_0 = 'v,(B2SJF%$'
        bool_0 = module_0.is_valid_ip(str_0)
        socket_0 = module_0.bind_unix_socket(str_0)
        s_s_l_context_0 = module_1.SSLContext()
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0)
        address_family_0 = None
        int_1 = -856
        int_2 = 836
        bool_1 = True
        list_0 = module_0.bind_sockets(int_2, str_0, address_family_0, int_0, int_1, bool_1)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = 'u] \rAU[]I'
        int_0 = -202
        str_1 = None
        bool_0 = module_0.is_valid_ip(str_1)
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        s_s_l_context_0 = module_1.SSLContext()
        s_s_l_context_1 = module_0.ssl_options_to_context(s_s_l_context_0)
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_1)
        str_2 = 'v,(B2SJF%$'
        bool_1 = module_0.is_valid_ip(str_2)
        socket_1 = module_0.bind_unix_socket(str_2)
        s_s_l_context_2 = module_1.SSLContext()
        s_s_l_socket_1 = module_0.ssl_wrap_socket(socket_1, s_s_l_context_2)
        int_1 = 5
        list_0 = module_0.bind_sockets(int_1)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = 'host'
        str_1 = '::ffff:127.0.0.1'
        str_2 = '%wj,gxr*lu]dOE*<'
        bool_0 = module_0.is_valid_ip(str_2)
        bool_1 = module_0.is_valid_ip(str_0)
        str_3 = 'v,(SF%$'
        bool_2 = module_0.is_valid_ip(str_3)
        bool_3 = module_0.is_valid_ip(str_1)
        dict_0 = {}
        executor_resolver_0 = module_0.ExecutorResolver(**dict_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'a{L\n'
        int_0 = 301
        address_family_0 = module_2.AddressFamily.AF_ALG
        bytes_0 = b'\xf5/\x88\xc87\x8ab\xa7\xc90s'
        bytes_1 = b'w\x96\xad\xc2i\xcc\xd9\xdd\xf7\xa4L'
        list_0 = [bytes_0, bytes_1]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        awaitable_0 = override_resolver_0.resolve(str_0, int_0, address_family_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = {}
        float_0 = None
        list_0 = [float_0, dict_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        override_resolver_0.close()
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = ')('
        bool_0 = module_0.is_valid_ip(str_0)
        str_1 = '.'
        int_0 = 2385
        socket_0 = module_0.bind_unix_socket(str_1, int_0)
    except BaseException:
        pass

def test_case_20():
    try:
        int_0 = 1566
        dict_0 = {}
        str_0 = 'P6$&,2whwO\\bgs'
        address_family_0 = module_2.AddressFamily.AF_QIPCRTR
        list_0 = [int_0, dict_0]
        dict_1 = {}
        override_resolver_0 = module_0.OverrideResolver(*list_0, **dict_1)
        awaitable_0 = override_resolver_0.resolve(str_0, int_0, address_family_0)
    except BaseException:
        pass