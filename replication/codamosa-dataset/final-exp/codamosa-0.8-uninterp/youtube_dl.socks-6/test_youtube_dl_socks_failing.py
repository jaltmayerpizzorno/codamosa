# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    try:
        bool_0 = None
        proxy_error_0 = module_0.ProxyError()
        invalid_version_error_0 = module_0.InvalidVersionError(bool_0, proxy_error_0)
    except BaseException:
        pass

def test_case_1():
    try:
        socks5_error_0 = module_0.Socks5Error()
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect_ex(socks5_error_0)
    except BaseException:
        pass

def test_case_2():
    try:
        list_0 = None
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = 1388361660
        sockssocket_0 = module_0.sockssocket()
        bool_0 = True
        socks4_error_0 = module_0.Socks4Error(int_0, bool_0)
        var_0 = sockssocket_0.connect_ex(socks4_error_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = None
        str_1 = 'g\nI{5%AC#`k;XtMp.)>B'
        str_2 = None
        dict_0 = {str_0: str_0, str_0: str_0, str_1: str_0, str_2: str_1}
        list_0 = [dict_0]
        float_0 = 3379.1
        int_0 = -2028
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.setproxy(list_0, float_0, int_0)
    except BaseException:
        pass

def test_case_5():
    try:
        sockssocket_0 = module_0.sockssocket()
        int_0 = 0
        var_0 = sockssocket_0.recvall(int_0)
        int_1 = 8
        var_1 = sockssocket_0.recvall(int_1)
    except BaseException:
        pass

def test_case_6():
    try:
        bool_0 = True
        proxy_error_0 = module_0.ProxyError()
        sockssocket_0 = module_0.sockssocket()
        socks5_error_0 = module_0.Socks5Error(bool_0)
        var_0 = sockssocket_0.connect(socks5_error_0)
    except BaseException:
        pass

def test_case_7():
    try:
        int_0 = 1388361660
        bool_0 = True
        invalid_version_error_0 = module_0.InvalidVersionError(int_0, bool_0)
        list_0 = [int_0, int_0, invalid_version_error_0]
        socks5_command_0 = module_0.Socks5Command(*list_0)
    except BaseException:
        pass

def test_case_8():
    try:
        bool_0 = True
        list_0 = []
        socks5_address_type_0 = module_0.Socks5AddressType(*list_0)
        proxy_error_0 = module_0.ProxyError()
        int_0 = 1388361660
        sockssocket_0 = module_0.sockssocket()
        bool_1 = False
        socks5_error_0 = module_0.Socks5Error(sockssocket_0)
        proxy_0 = None
        socks5_address_type_1 = module_0.Socks5AddressType()
        var_0 = sockssocket_0.setproxy(bool_0, socks5_error_0, proxy_0, socks5_address_type_1, int_0)
        sockssocket_1 = module_0.sockssocket()
        var_1 = sockssocket_0.recvall(bool_1)
        socks4_error_0 = module_0.Socks4Error(bool_0)
        var_2 = sockssocket_0.connect_ex(socks4_error_0)
    except BaseException:
        pass