# Automatically generated by Pynguin.
import ansible.utils.hashing as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'SdBlE!S\x0b6G =fO3~!V|;'
    var_0 = module_0.md5s(str_0)

def test_case_2():
    float_0 = None
    var_0 = module_0.md5(float_0)

def test_case_3():
    str_0 = '/etc/passwd'
    var_0 = module_0.secure_hash(str_0)

def test_case_4():
    str_0 = '/dev/null'
    var_0 = module_0.secure_hash(str_0)

def test_case_5():
    str_0 = '/bin/bash'
    var_0 = module_0.md5(str_0)
    str_1 = '/bin/dne'
    var_1 = module_0.md5(str_1)
    bytes_0 = b'g"'
    var_2 = module_0.secure_hash(bytes_0)