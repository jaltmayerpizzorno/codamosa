# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'Od'
    socks5_address_type_0 = module_0.Socks5AddressType()
    socks4_error_0 = module_0.Socks4Error(str_0)

def test_case_2():
    socks5_error_0 = module_0.Socks5Error()

def test_case_3():
    int_0 = 2
    int_1 = 3
    invalid_version_error_0 = module_0.InvalidVersionError(int_0, int_1)

def test_case_4():
    sockssocket_0 = module_0.sockssocket()
    float_0 = -494.21079219340197
    var_0 = sockssocket_0.recvall(float_0)

def test_case_5():
    int_0 = -2063
    sockssocket_0 = module_0.sockssocket()
    var_0 = sockssocket_0.recvall(int_0)
    bool_0 = True
    bytes_0 = b'TMH\xfb\xc5\xe1\x7f'
    complex_0 = None
    var_1 = sockssocket_0.setproxy(bool_0, bytes_0, complex_0)
    socks5_address_type_0 = module_0.Socks5AddressType()
    socks5_address_type_1 = module_0.Socks5AddressType()