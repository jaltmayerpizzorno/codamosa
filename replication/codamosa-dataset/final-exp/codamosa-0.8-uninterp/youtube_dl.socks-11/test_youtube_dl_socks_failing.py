# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    try:
        socks4_error_0 = module_0.Socks4Error()
        socks4_error_1 = module_0.Socks4Error()
        int_0 = -1901
        socks4_command_0 = module_0.Socks4Command()
        float_0 = 1947.4
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.setproxy(int_0, socks4_command_0, float_0)
    except BaseException:
        pass

def test_case_1():
    try:
        sockssocket_0 = module_0.sockssocket()
        int_0 = 1876
        var_0 = sockssocket_0.connect(int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        socks5_auth_0 = module_0.Socks5Auth()
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect_ex(socks5_auth_0)
    except BaseException:
        pass

def test_case_3():
    try:
        sockssocket_0 = module_0.sockssocket()
        int_0 = 0
        var_0 = sockssocket_0.recvall(int_0)
        int_1 = 2
        var_1 = sockssocket_0.recvall(int_1)
    except BaseException:
        pass

def test_case_4():
    try:
        sockssocket_0 = module_0.sockssocket()
        int_0 = 0
        var_0 = sockssocket_0.recvall(int_0)
        bool_0 = False
        str_0 = '$SD__'
        list_0 = [bool_0]
        int_1 = 1275
        var_1 = sockssocket_0.setproxy(bool_0, str_0, str_0, list_0, int_1)
        int_2 = 1
        var_2 = sockssocket_0.recvall(int_2)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = False
        proxy_error_0 = module_0.ProxyError()
        socks5_command_0 = module_0.Socks5Command()
        sockssocket_0 = module_0.sockssocket()
        str_0 = '=k'
        dict_0 = {}
        proxy_type_0 = module_0.ProxyType(**dict_0)
        list_0 = [socks5_command_0, dict_0, bool_0]
        socks5_auth_0 = module_0.Socks5Auth()
        socks4_command_0 = module_0.Socks4Command(**dict_0)
        var_0 = sockssocket_0.setproxy(bool_0, list_0, socks5_auth_0, socks4_command_0, socks4_command_0)
        socks5_auth_1 = module_0.Socks5Auth(**dict_0)
        socks5_error_0 = module_0.Socks5Error(str_0)
        var_1 = sockssocket_0.recvall(bool_0)
        sockssocket_1 = module_0.sockssocket()
        sockssocket_2 = module_0.sockssocket()
        var_2 = sockssocket_0.connect(dict_0)
    except BaseException:
        pass