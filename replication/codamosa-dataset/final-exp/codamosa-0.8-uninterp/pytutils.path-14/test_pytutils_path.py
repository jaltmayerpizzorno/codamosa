# Automatically generated by Pynguin.
import pytutils.path as module_0

def test_case_0():
    bytes_0 = b'\xe1\xd0/\x1f\xa0\xb9.\xeb\xea:\x04]\xd7\xe3t\x84'
    int_0 = 2136
    var_0 = module_0.join_each(bytes_0, int_0)

def test_case_1():
    str_0 = '/'
    str_1 = 'etc'
    str_2 = (str_0, str_1)
    var_0 = module_0.join_each(str_0, str_2)
    var_1 = list(var_0)