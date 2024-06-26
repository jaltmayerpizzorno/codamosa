# Automatically generated by Pynguin.
import youtube_dl.socks as module_0
import socket as module_1

def test_case_0():
    try:
        socks4_error_0 = module_0.Socks4Error()
        socks5_error_0 = module_0.Socks5Error(socks4_error_0)
        sockssocket_0 = None
        proxy_error_0 = module_0.ProxyError(sockssocket_0)
        socks5_command_0 = module_0.Socks5Command()
        bytes_0 = b'\x85\xf1\xd6\xea\x8d\xf7\x9a\x9f\x0f\xd5\x12\x93'
        invalid_version_error_0 = module_0.InvalidVersionError(bytes_0, socks5_command_0)
    except BaseException:
        pass

def test_case_1():
    try:
        sockssocket_0 = module_0.sockssocket()
        socks5_address_type_0 = module_0.Socks5AddressType()
        proxy_type_0 = module_0.ProxyType()
        socks5_error_0 = module_0.Socks5Error()
        tuple_0 = (sockssocket_0, socks5_error_0)
        str_0 = 'user28849593'
        var_0 = sockssocket_0.setproxy(socks5_address_type_0, proxy_type_0, tuple_0, str_0)
    except BaseException:
        pass

def test_case_2():
    try:
        tuple_0 = ()
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect_ex(tuple_0)
    except BaseException:
        pass

def test_case_3():
    try:
        proxy_0 = None
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect(proxy_0)
    except BaseException:
        pass

def test_case_4():
    try:
        int_0 = 614
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.recvall(int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        sockssocket_0 = module_0.sockssocket()
        socket_0 = module_1.socket()
        list_0 = [socket_0, sockssocket_0]
        proxy_error_0 = module_0.ProxyError(socket_0, list_0)
        int_0 = 8081
        str_0 = 'www.youtube.com'
        int_1 = 443
        var_0 = (str_0, int_1)
        var_1 = sockssocket_0.connect(var_0)
        var_2 = sockssocket_0.recvall(int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        proxy_error_0 = None
        bool_0 = False
        bool_1 = False
        float_0 = 1004.118682
        int_0 = -1459
        float_1 = -823.89491
        dict_0 = {proxy_error_0: int_0, int_0: proxy_error_0, bool_1: proxy_error_0, float_1: int_0}
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.setproxy(bool_0, bool_1, float_0, dict_0)
        invalid_version_error_0 = None
        var_1 = sockssocket_0.connect_ex(invalid_version_error_0)
    except BaseException:
        pass

def test_case_7():
    try:
        socks5_auth_0 = module_0.Socks5Auth()
        proxy_error_0 = module_0.ProxyError()
        list_0 = [socks5_auth_0, socks5_auth_0, socks5_auth_0]
        list_1 = []
        bool_0 = True
        socks5_error_0 = module_0.Socks5Error(bool_0)
        tuple_0 = (socks5_auth_0, list_0, list_1)
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect(tuple_0)
    except BaseException:
        pass

def test_case_8():
    try:
        proxy_type_0 = module_0.ProxyType()
        socks5_error_0 = module_0.Socks5Error(proxy_type_0)
        int_0 = -758
        invalid_version_error_0 = module_0.InvalidVersionError(int_0, int_0)
        socks5_command_0 = module_0.Socks5Command()
        socks5_error_1 = module_0.Socks5Error()
        dict_0 = {}
        sockssocket_0 = module_0.sockssocket(**dict_0)
        list_0 = []
        sockssocket_1 = module_0.sockssocket()
        str_0 = ''
        invalid_version_error_1 = None
        dict_1 = {socks5_command_0: invalid_version_error_1, sockssocket_0: list_0, str_0: socks5_error_0, socks5_error_0: proxy_type_0}
        var_0 = sockssocket_0.connect_ex(dict_1)
    except BaseException:
        pass

def test_case_9():
    try:
        sockssocket_0 = module_0.sockssocket()
        str_0 = 'www.youtube.com'
        int_0 = 443
        var_0 = (str_0, int_0)
        var_1 = sockssocket_0.connect(var_0)
        int_1 = 1024
        var_2 = sockssocket_0.recvall(int_1)
    except BaseException:
        pass