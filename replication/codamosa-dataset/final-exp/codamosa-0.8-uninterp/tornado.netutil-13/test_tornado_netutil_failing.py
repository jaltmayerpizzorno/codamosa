# Automatically generated by Pynguin.
import tornado.netutil as module_0
import socket as module_1
import ssl as module_2

def test_case_0():
    try:
        str_0 = ',#DZfAn8xT\x0b+Y48U'
        int_0 = -1952
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        callable_0 = None
        callable_1 = module_0.add_accept_handler(socket_0, callable_0)
    except BaseException:
        pass

def test_case_1():
    try:
        executor_resolver_0 = module_0.ExecutorResolver()
    except BaseException:
        pass

def test_case_2():
    try:
        resolver_0 = module_0.Resolver()
        executor_resolver_0 = module_0.ExecutorResolver()
    except BaseException:
        pass

def test_case_3():
    try:
        resolver_0 = module_0.Resolver()
        resolver_0.close()
        int_0 = 1144
        address_family_0 = module_1.AddressFamily.AF_BLUETOOTH
        int_1 = -935
        list_0 = module_0.bind_sockets(int_1, address_family_0, int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'PuHfKA(p5m'
        int_0 = -369
        socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
        blocking_resolver_0 = module_0.BlockingResolver()
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '$,@H>6I>'
        list_0 = [str_0, str_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        override_resolver_0.close()
    except BaseException:
        pass

def test_case_6():
    try:
        socket_0 = None
        str_0 = 'P(d_/]L=LN'
        str_1 = "\x0b.ZBN8\n;EZ5|U'U\\zh"
        dict_0 = {str_0: socket_0, str_1: str_1}
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '7Ix"KI?\r_#9x!\'qD|kA.'
        int_0 = -1307
        address_family_0 = module_1.AddressFamily.AF_INET6
        resolver_0 = module_0.Resolver()
        awaitable_0 = resolver_0.resolve(str_0, int_0, address_family_0)
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_8():
    try:
        threaded_resolver_0 = module_0.ThreadedResolver()
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 8907
        list_0 = module_0.bind_sockets(int_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = '-FFD!A@TSD e(.i\nLJz'
        int_0 = -3000
        socket_0 = module_0.bind_unix_socket(str_0, int_0, int_0)
        s_s_l_context_0 = module_2.SSLContext()
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, s_s_l_context_0)
        list_0 = module_0.bind_sockets(int_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        resolver_0 = module_0.Resolver()
        str_0 = 'sz#8H'
        bool_0 = module_0.is_valid_ip(str_0)
        str_1 = None
        int_0 = 86400
        socket_0 = module_0.bind_unix_socket(str_1, int_0)
    except BaseException:
        pass

def test_case_12():
    try:
        resolver_0 = module_0.Resolver()
        str_0 = ' bQ=Cc2\x0bsU?c'
        resolver_0.close()
        str_1 = 'sz#8H'
        bool_0 = module_0.is_valid_ip(str_1)
        int_0 = 3761
        socket_0 = module_0.bind_unix_socket(str_0, int_0)
        list_0 = module_0.bind_sockets(int_0)
        str_2 = 'yU$q(gvr]Y,]OB,TcB'
        resolver_0.close()
        int_1 = 12
        awaitable_0 = resolver_0.resolve(str_2, int_1)
        resolver_0.close()
        str_3 = "Matches requests from host that is equal to application's default_host.\n    Always returns no match if ``X-Real-Ip`` header is present.\n    "
        bool_1 = module_0.is_valid_ip(str_3)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = None
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 3783
        address_family_0 = module_1.AddressFamily.AF_KEY
        bool_0 = True
        list_0 = module_0.bind_sockets(int_0, address_family_0, int_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_15():
    try:
        resolver_0 = module_0.Resolver()
        str_0 = ' bQ=Cc2\x0bsU?c'
        str_1 = ')Md5"Fl'
        int_0 = 1150
        address_family_0 = module_1.AddressFamily.AF_UNSPEC
        list_0 = [str_0, str_0]
        override_resolver_0 = module_0.OverrideResolver(*list_0)
        awaitable_0 = override_resolver_0.resolve(str_1, int_0, address_family_0)
    except BaseException:
        pass

def test_case_16():
    try:
        int_0 = 12297
        str_0 = ''
        list_0 = module_0.bind_sockets(int_0, str_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'K'
        address_family_0 = module_1.AddressFamily.AF_IRDA
        int_0 = -1629
        bool_0 = True
        list_0 = module_0.bind_sockets(int_0, str_0, address_family_0, int_0, int_0, bool_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'localhost'
        int_0 = None
        list_0 = module_0.bind_sockets(int_0, str_0)
        var_0 = print(list_0)
        bool_0 = True
        list_1 = module_0.bind_sockets(int_0, str_0, bool_0)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '-FFD!A@TSD e(.i\nLJz'
        s_s_l_context_0 = module_2.SSLContext()
        resolver_0 = module_0.Resolver()
        bool_0 = module_0.is_valid_ip(str_0)
        str_1 = 'ZxgC}~MJ+Y'
        int_0 = -2106
        awaitable_0 = resolver_0.resolve(str_1, int_0)
        str_2 = '/'
        socket_0 = module_0.bind_unix_socket(str_2)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = '3'
        dict_0 = {}
        str_1 = ' putters[%s]'
        bool_0 = module_0.is_valid_ip(str_1)
        int_0 = 1509
        socket_0 = module_0.bind_unix_socket(str_1, int_0)
        s_s_l_socket_0 = module_0.ssl_wrap_socket(socket_0, dict_0, str_0)
        bool_1 = module_0.is_valid_ip(str_0)
        s_s_l_context_0 = module_0.ssl_options_to_context(dict_0)
        int_1 = None
        str_2 = 'tCAFbng\x0c'
        int_2 = 219
        list_0 = []
        resolver_0 = module_0.Resolver(*list_0)
        awaitable_0 = resolver_0.resolve(str_2, int_2)
        list_1 = module_0.bind_sockets(int_1, str_0)
    except BaseException:
        pass