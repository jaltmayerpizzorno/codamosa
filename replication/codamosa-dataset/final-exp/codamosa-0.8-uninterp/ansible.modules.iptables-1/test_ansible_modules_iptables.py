# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = 'SYN'
    str_1 = 'FIN'
    str_2 = [str_1, str_0, str_0, str_1]
    str_3 = '--tcp-flags'
    var_0 = module_0.append_tcp_flags(str_2, str_3, str_3)
    var_1 = print(str_1)

def test_case_2():
    complex_0 = None
    list_0 = [complex_0, complex_0, complex_0, complex_0]
    float_0 = 0.001
    str_0 = 'cl\x0b?]e])>N8%i<'
    tuple_0 = (list_0, str_0)
    var_0 = module_0.append_match_flag(list_0, float_0, str_0, tuple_0)

def test_case_3():
    bytes_0 = b'x\x15\xe7\xc2\xact\xf0\tL\x96\x039\x86\xce>\x915\x1b\xcf'
    tuple_0 = (bytes_0,)
    bool_0 = True
    dict_0 = {}
    int_0 = 2341
    var_0 = module_0.append_match(bool_0, dict_0, int_0)
    str_0 = None
    bytes_1 = b'\x1b\xf1\xc5^)}\x8c\xd3v\xe2z\x13\xda\xea\xb6J'
    var_1 = module_0.main()
    int_1 = 511
    bool_1 = False
    int_2 = 9000
    var_2 = module_0.append_csv(bool_1, int_2, int_1)
    tuple_1 = ()
    var_3 = module_0.append_tcp_flags(int_1, tuple_1, tuple_1)
    bool_2 = True
    var_4 = module_0.remove_rule(tuple_0, bool_2, bytes_0)
    bool_3 = False
    var_5 = module_0.append_tcp_flags(bool_3, str_0, bytes_1)
    int_3 = 5659
    str_1 = 'ansible.modules.iptables'
    float_0 = 2368.7789
    var_6 = module_0.append_csv(int_3, str_1, float_0)

def test_case_4():
    int_0 = -1183
    str_0 = 'Kbptj.TnW:*@5GnEw2,'
    dict_0 = None
    var_0 = module_0.append_tcp_flags(int_0, str_0, dict_0)
    bool_0 = True
    tuple_0 = ()
    bytes_0 = b'\n\xc0\x13\xb3\xd1\xe8l\x8c\xc4\xe9NF\xe1\xf0H\x83\xce'
    var_1 = module_0.append_wait(bool_0, tuple_0, bytes_0)

def test_case_5():
    var_0 = module_0.main()

def test_case_6():
    float_0 = -2474.0
    int_0 = -2106
    str_0 = 'ansible.legacy.file'
    dict_0 = None
    var_0 = module_0.append_tcp_flags(int_0, str_0, dict_0)
    dict_1 = {float_0: float_0, float_0: float_0}
    str_1 = "T'm54U74VTrDO"
    bytes_0 = b'\x1e\xfb\x14s'
    list_0 = []
    var_1 = module_0.append_jump(bytes_0, list_0, dict_1)
    list_1 = []
    str_2 = 'match'
    var_2 = module_0.append_csv(str_1, list_1, str_2)

def test_case_7():
    float_0 = -2474.0
    int_0 = -1183
    str_0 = 'Kbptj.TnW:*@5GnEw2,'
    dict_0 = None
    var_0 = module_0.append_tcp_flags(int_0, str_0, dict_0)
    dict_1 = {float_0: float_0, float_0: float_0}
    bool_0 = True
    tuple_0 = ()
    bytes_0 = b'\n\xc0\x13\xb3\xd1\xe8l\x8c\xc4\xe9NF\xe1\xf0H\x83\xce'
    var_1 = module_0.append_wait(bool_0, tuple_0, bytes_0)
    str_1 = "T'm54U74VTrDO"
    list_0 = [str_0, int_0, dict_1, dict_1]
    str_2 = '2fwL\r ?i0G'
    var_2 = module_0.append_match_flag(list_0, list_0, str_2, bool_0)
    list_1 = []
    str_3 = 'match'
    var_3 = module_0.append_csv(str_1, list_1, str_3)
    int_1 = 10
    bool_1 = True
    int_2 = -2263
    dict_2 = {int_0: str_1, var_2: int_1, float_0: int_2}
    var_4 = module_0.append_param(bool_1, tuple_0, tuple_0, dict_2)

def test_case_8():
    int_0 = -1183
    str_0 = 'Kbptj.TnW:*@5GnEw2,'
    dict_0 = None
    var_0 = module_0.append_tcp_flags(int_0, str_0, dict_0)
    bool_0 = False
    tuple_0 = ()
    bytes_0 = b'\n\xc0\x13\xb3\xd1\xe8l\x8c\xc4\xe9NF\xe1\xf0H\x83\xce'
    var_1 = module_0.append_wait(bool_0, tuple_0, bytes_0)
    str_1 = "T'm54U74VTrDO"
    list_0 = []
    str_2 = 'match'
    var_2 = module_0.append_csv(str_1, list_0, str_2)
    str_3 = '/_\\'
    tuple_1 = (dict_0, str_3)
    tuple_2 = None
    var_3 = module_0.append_param(tuple_1, dict_0, tuple_2, list_0)

def test_case_9():
    var_0 = []
    str_0 = 'match'
    str_1 = '--syn'
    bool_0 = True
    var_1 = module_0.append_match_flag(var_0, str_0, str_1, bool_0)
    var_2 = []
    str_2 = 'negate'
    var_3 = module_0.append_match_flag(var_2, str_2, str_1, bool_0)
    var_4 = []
    str_3 = 'invalid'
    var_5 = module_0.append_match_flag(var_4, str_3, str_1, bool_0)
    var_6 = []
    bool_1 = False
    var_7 = module_0.append_match_flag(var_6, str_3, str_1, bool_1)

def test_case_10():
    var_0 = []
    str_0 = 'ACK'
    str_1 = 'RST'
    str_2 = 'SYN'
    str_3 = 'FIN'
    str_4 = [str_0, str_1, str_2, str_3]
    var_1 = dict(flags=str_4, flags_set=str_1)
    str_5 = '--tcp-flags'
    var_2 = module_0.append_tcp_flags(var_0, var_1, str_5)
    var_3 = print(var_0)

def test_case_11():
    var_0 = []
    str_0 = 'match'
    str_1 = '--syn'
    bool_0 = True
    var_1 = module_0.append_match_flag(var_0, str_0, str_1, bool_0)
    var_2 = []
    str_2 = 'negate'
    var_3 = module_0.append_match_flag(var_2, str_2, str_1, bool_0)
    var_4 = []
    str_3 = 'invalid'
    var_5 = module_0.append_match_flag(var_4, str_3, str_1, bool_0)