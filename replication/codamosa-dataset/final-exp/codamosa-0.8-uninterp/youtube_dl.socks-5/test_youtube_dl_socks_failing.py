# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    try:
        int_0 = -2728
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect(int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        float_0 = None
        proxy_type_0 = module_0.ProxyType()
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.setproxy(float_0, proxy_type_0, proxy_type_0)
    except BaseException:
        pass

def test_case_2():
    try:
        sockssocket_0 = module_0.sockssocket()
        sockssocket_1 = module_0.sockssocket()
        list_0 = [sockssocket_1, sockssocket_1]
        sockssocket_2 = module_0.sockssocket()
        var_0 = sockssocket_2.connect_ex(list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        socks5_error_0 = module_0.Socks5Error()
        int_0 = 4
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.recvall(int_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = 'izPG4e'
        proxy_error_0 = module_0.ProxyError()
        bool_0 = True
        socks5_error_0 = module_0.Socks5Error(bool_0)
        dict_0 = {str_0: proxy_error_0}
        socks5_address_type_0 = module_0.Socks5AddressType(**dict_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = 'network'
        int_0 = -2063
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.recvall(int_0)
        bool_0 = True
        bytes_0 = b'TMH\xfb\xc5\xe1\x7f'
        complex_0 = None
        var_1 = sockssocket_0.setproxy(bool_0, bytes_0, complex_0)
        str_1 = ':E"\'~\x0cL\t A3T&WSWu*o'
        str_2 = 'OpEC:=}\\LRy\x0c##Cv'
        str_3 = None
        dict_0 = {str_1: complex_0, str_0: str_0, str_2: sockssocket_0, str_3: int_0}
        var_2 = sockssocket_0.connect_ex(dict_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'\x00\x00\x00\x01\x00\x00\x00\x03'
        sockssocket_0 = module_0.sockssocket()
        str_0 = '8.8.8.8'
        int_0 = 53
        var_0 = (str_0, int_0)
        var_1 = sockssocket_0.connect(var_0)
        var_2 = len(bytes_0)
        var_3 = sockssocket_0.recvall(var_2)
    except BaseException:
        pass