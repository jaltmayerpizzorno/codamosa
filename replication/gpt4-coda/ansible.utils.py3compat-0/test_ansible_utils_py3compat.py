# Automatically generated by Pynguin.
import ansible.utils.py3compat as module_0

def test_case_0():
    text_environ_0 = module_0._TextEnviron()

def test_case_1():
    str_0 = 'C'
    text_environ_0 = module_0._TextEnviron(str_0)
    var_0 = text_environ_0.__iter__()

def test_case_2():
    bytes_0 = b'\x05+\xba\x051\xea\xd7\xb8\xb8-X\xdf\x1a'
    text_environ_0 = module_0._TextEnviron(bytes_0)
    var_0 = text_environ_0.__len__()

def test_case_3():
    bytes_0 = b'\xcd{I\xc3\xc0\xfbC0\x9e\xf0'
    bytes_1 = {bytes_0: bytes_0}
    text_environ_0 = module_0._TextEnviron(bytes_1)
    var_0 = text_environ_0[bytes_0]