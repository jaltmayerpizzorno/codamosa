# Automatically generated by Pynguin.
import ansible.utils.hashing as module_0

def test_case_0():
    pass

def test_case_1():
    float_0 = None
    var_0 = module_0.md5s(float_0)

def test_case_2():
    tuple_0 = ()
    var_0 = module_0.secure_hash(tuple_0)

def test_case_3():
    bool_0 = False
    var_0 = module_0.md5(bool_0)

def test_case_4():
    str_0 = '/etc/passwd'
    var_0 = module_0.md5(str_0)

def test_case_5():
    str_0 = 'foo1'
    str_1 = 'w'
    var_0 = open(str_0, str_1)
    var_1 = var_0.close
    var_2 = module_0.md5(str_0)
    str_2 = 'result1:%s'
    var_3 = str_2 % var_2
    var_4 = print(var_3)

def test_case_6():
    str_0 = '/tmp'
    var_0 = module_0.md5(str_0)

def test_case_7():
    str_0 = '/bin/ls'
    var_0 = module_0.md5(str_0)