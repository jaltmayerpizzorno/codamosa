# Automatically generated by Pynguin.
import ansible.plugins.filter.mathstuff as module_0

def test_case_0():
    pass

def test_case_1():
    list_0 = []
    str_0 = '\x0b>chjf=R>tAx2C'
    var_0 = module_0.intersect(list_0, list_0, str_0)

def test_case_2():
    float_0 = 2.718281828459045
    str_0 = '0q:sDj|?/0F6W^-z13;'
    var_0 = module_0.intersect(float_0, str_0, str_0)
    int_0 = -1928
    dict_0 = {}
    bool_0 = True
    bytes_0 = b'\x9b\x14\x8e\x15<\xd5\x9b\xa1#\x8d\xa9\xf3'
    var_1 = module_0.max(bytes_0, str_0)
    var_2 = module_0.intersect(int_0, dict_0, bool_0)

def test_case_3():
    int_0 = 100
    var_0 = module_0.logarithm(int_0)

def test_case_4():
    filter_module_0 = module_0.FilterModule()
    var_0 = filter_module_0.filters()

def test_case_5():
    str_0 = '=u1@8ILQ\r=H7$-N9\rBK'
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: str_0}
    bytes_0 = b'\x99\xb5\x81k@p?\x17\xfb\xc4\xe6L\x12\xcb\x8eTP'
    bytes_1 = b'\x1d\x1c\xbdU\xdc\xe3\xc1\x9f\xada\x17`\xab\xb5\x96\xfeq'
    tuple_0 = (str_0, bytes_1)
    tuple_1 = (bytes_0, tuple_0, bytes_1, dict_0)
    var_0 = module_0.intersect(list_0, dict_0, tuple_1)

def test_case_6():
    str_0 = 'hostname'
    str_1 = 'ip'
    str_2 = 'host&'
    str_3 = '10.0.0.1'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = 'host2'
    str_6 = '10.0.0.2'
    str_7 = {str_0: str_5, str_1: str_6}
    str_8 = 'host3'
    str_9 = '10.0.0.3'
    str_10 = {str_0: str_8, str_1: str_9}
    str_11 = [str_4, str_7, str_10]
    var_0 = module_0.rekey_on_member(str_11, str_1)
    var_1 = len(var_0)
    str_12 = '?(1#Ex-4l,54Ezbr5'
    dict_0 = {str_1: str_1, str_12: var_1}
    str_13 = ":iJ'I$ &"
    var_2 = module_0.difference(dict_0, str_13, dict_0)

def test_case_7():
    str_0 = 'hostname'
    str_1 = 'ip'
    str_2 = 'host&'
    str_3 = '10.0.0.1'
    str_4 = {str_0: str_2, str_1: str_3}
    str_5 = '10.0.0.2'
    str_6 = {str_0: str_0, str_1: str_5}
    str_7 = 'host3'
    str_8 = '10.0.0.3'
    str_9 = {str_0: str_7, str_1: str_8}
    str_10 = [str_4, str_6, str_9]
    var_0 = module_0.rekey_on_member(str_10, str_1)
    var_1 = len(var_0)

def test_case_8():
    str_0 = '=u1@8ILQ\r=H7$-N9\rBK'
    list_0 = [str_0, str_0, str_0]
    dict_0 = {str_0: str_0}
    bytes_0 = b'\x1d\x1c\xbdU\xdc\xe3\xc1\x9f\xada\x17`\xab\xb5\x96\xfeq'
    tuple_0 = (str_0, bytes_0)
    var_0 = module_0.intersect(list_0, dict_0, tuple_0)

def test_case_9():
    str_0 = '@\x0b$dyHOtF).@BFWC<\\{e'
    dict_0 = {}
    list_0 = [str_0, dict_0, str_0]
    var_0 = module_0.unique(dict_0, list_0)

def test_case_10():
    int_0 = 821
    list_0 = []
    bytes_0 = b'\x82\x1e{\xfd\x87\x85\xc6\x84\x9c\x7fe'
    bool_0 = False
    var_0 = module_0.unique(int_0, bytes_0, list_0, bool_0)

def test_case_11():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    str_0 = '(p;m LWW'
    str_1 = 'vN%9xukO:\tWb$'
    dict_0 = {str_0: bool_0, str_1: str_1}
    str_2 = 'lDT8HX2'
    var_0 = module_0.unique(bool_0, str_1)
    var_1 = module_0.max(list_0, str_2)
    int_0 = 766
    var_2 = module_0.human_readable(int_0, int_0)
    bytes_0 = b'\xf0\xf6\xe2\x95qE\xca\x83{>\xfedj\xa84n]\xf5'
    list_1 = [bytes_0, dict_0]
    bytes_1 = None
    tuple_0 = (bytes_1, bool_0, str_0)
    var_3 = module_0.difference(list_0, list_1, tuple_0)