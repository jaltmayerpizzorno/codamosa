# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    pass

def test_case_1():
    socks4_error_0 = module_0.Socks4Error()

def test_case_2():
    int_0 = 3
    int_1 = 4
    invalid_version_error_0 = module_0.InvalidVersionError(int_0, int_1)

def test_case_3():
    sockssocket_0 = module_0.sockssocket()

def test_case_4():
    bool_0 = False
    sockssocket_0 = module_0.sockssocket()
    var_0 = sockssocket_0.recvall(bool_0)

def test_case_5():
    str_0 = '140.113.72.148'
    int_0 = 1234
    var_0 = (str_0, int_0)
    sockssocket_0 = module_0.sockssocket()
    var_1 = sockssocket_0.connect(var_0)
    bytes_0 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
    var_2 = len(bytes_0)
    var_3 = sockssocket_0.recvall(var_2)
    var_4 = sockssocket_0.close()
    sockssocket_1 = module_0.sockssocket()
    var_5 = sockssocket_1.connect(var_0)
    bytes_1 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
    var_6 = len(bytes_1)