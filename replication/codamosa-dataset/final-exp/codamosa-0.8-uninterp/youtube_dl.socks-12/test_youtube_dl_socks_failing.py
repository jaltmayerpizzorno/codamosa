# Automatically generated by Pynguin.
import youtube_dl.socks as module_0

def test_case_0():
    try:
        socks4_command_0 = module_0.Socks4Command()
        sockssocket_0 = module_0.sockssocket()
        var_0 = sockssocket_0.connect(socks4_command_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = {}
        sockssocket_0 = module_0.sockssocket(**dict_0)
        var_0 = sockssocket_0.connect_ex(sockssocket_0)
    except BaseException:
        pass

def test_case_2():
    try:
        sockssocket_0 = module_0.sockssocket()
        dict_0 = {}
        sockssocket_1 = module_0.sockssocket(**dict_0)
        float_0 = -4743.94283
        bytes_0 = b"\x0b\x10\x14\x8213\xd9\xba\x97LM\xda\\\x82\xfd>\xc9'"
        set_0 = {float_0, bytes_0}
        var_0 = sockssocket_0.setproxy(float_0, bytes_0, set_0)
    except BaseException:
        pass

def test_case_3():
    try:
        sockssocket_0 = module_0.sockssocket()
        bool_0 = True
        int_0 = 0
        var_0 = sockssocket_0.recvall(int_0)
        var_1 = sockssocket_0.recvall(bool_0)
    except BaseException:
        pass