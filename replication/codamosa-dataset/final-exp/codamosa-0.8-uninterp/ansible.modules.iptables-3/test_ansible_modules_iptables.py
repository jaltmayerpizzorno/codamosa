# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0
import ansible.module_utils.compat.version as module_1

def test_case_0():
    pass

def test_case_1():
    bool_0 = True
    complex_0 = None
    str_0 = '%-8s %-15s %s'
    var_0 = module_0.append_wait(bool_0, complex_0, str_0)

def test_case_2():
    str_0 = '__main__'
    list_0 = [str_0, str_0]
    str_1 = '{!#]DC=T`!#Af5jr\nVb'
    int_0 = -4010
    set_0 = set()
    dict_0 = {str_1: set_0, str_1: int_0}
    var_0 = module_0.append_wait(list_0, dict_0, int_0)
    tuple_0 = (set_0,)
    var_1 = module_0.append_tcp_flags(tuple_0, str_1, tuple_0)

def test_case_3():
    var_0 = module_0.main()

def test_case_4():
    str_0 = 'iptmb7es'
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    float_0 = 1358.181961716743
    var_0 = module_0.append_tcp_flags(dict_0, str_0, float_0)

def test_case_5():
    float_0 = 904.989
    bool_0 = False
    str_0 = '__main__'
    list_0 = [str_0, str_0]
    var_0 = module_0.append_match(float_0, bool_0, list_0)
    str_1 = '[d\x0cc`1c\x0cD#,s?Z5'
    int_0 = -4010
    set_0 = set()
    dict_0 = {str_1: set_0, str_1: int_0}
    var_1 = module_0.append_wait(list_0, dict_0, int_0)
    tuple_0 = (set_0,)
    var_2 = module_0.append_tcp_flags(tuple_0, str_1, tuple_0)

def test_case_6():
    var_0 = []
    var_1 = None
    str_0 = '--test-param'
    bool_0 = False
    var_2 = module_0.append_param(var_0, var_1, str_0, bool_0)
    str_1 = 'TestParam'
    var_3 = module_0.append_param(var_0, str_1, str_0, bool_0)
    var_4 = []
    str_2 = 'TestParam1'
    str_3 = '!TestParam2'
    str_4 = [str_2, str_3]
    bool_1 = True
    var_5 = module_0.append_param(var_4, str_4, str_0, bool_1)

def test_case_7():
    var_0 = []
    var_1 = None
    str_0 = '--foo'
    bool_0 = True
    var_2 = module_0.append_match_flag(var_0, var_1, str_0, bool_0)
    var_3 = []
    str_1 = 'match'
    str_2 = '--foo'
    bool_1 = True
    var_4 = module_0.append_match_flag(var_3, str_1, str_2, bool_1)
    loose_version_0 = module_1.LooseVersion()

def test_case_8():
    str_0 = 'q'
    str_1 = [str_0, str_0]
    str_2 = 'flags'
    str_3 = 'flags_set'
    str_4 = 'ACK'
    str_5 = {str_2: str_4, str_3: str_2}
    str_6 = '--tcp-flags'
    var_0 = module_0.append_tcp_flags(str_1, str_5, str_6)

def test_case_9():
    str_0 = 'flags'
    str_1 = 'ACK'
    str_2 = 'RST'
    str_3 = 'SYN'
    str_4 = 'F,IN'
    str_5 = [str_1, str_2, str_3, str_4]
    str_6 = {str_0: str_0, str_2: str_5}
    str_7 = '--tcp-flags'
    var_0 = module_0.append_tcp_flags(str_0, str_6, str_7)