# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    pass

def test_case_1():
    str_0 = '%s'
    bytes_0 = None
    str_1 = 'ansible.modules.iptables'
    int_0 = 200
    var_0 = module_0.append_match_flag(str_0, bytes_0, str_1, int_0)

def test_case_2():
    bytes_0 = b'z\x19\xe1\x96\xe8IR'
    set_0 = {bytes_0}
    tuple_0 = (bytes_0, set_0)
    list_0 = [tuple_0]
    str_0 = 'F,izV]o$-|*bdOCVQa'
    bool_0 = True
    var_0 = module_0.append_match(list_0, str_0, bool_0)

def test_case_3():
    dict_0 = {}
    bytes_0 = b'~\x0e\xcb\xba\xed\xb6$\xe6\x0f\x80\xdf\xfe\rP\x02'
    float_0 = 453.986
    var_0 = module_0.append_param(dict_0, dict_0, bytes_0, float_0)
    bool_0 = False
    int_0 = 1827
    bool_1 = True
    str_0 = 'kZ\x0c&'
    complex_0 = None
    bytes_1 = b'\xf5e\x06V\xf4\x94\xa5\xf24FG\x95\xea'
    set_0 = set()
    tuple_0 = (set_0, bytes_1, int_0)
    var_1 = module_0.append_tcp_flags(tuple_0, tuple_0, complex_0)
    var_2 = module_0.append_jump(tuple_0, dict_0, bool_1)
    var_3 = module_0.main()
    var_4 = module_0.append_wait(bool_0, complex_0, bytes_1)
    tuple_1 = (float_0, str_0, bool_1)
    var_5 = module_0.append_match_flag(float_0, tuple_1, int_0, set_0)

def test_case_4():
    str_0 = None
    bool_0 = False
    complex_0 = None
    list_0 = []
    var_0 = module_0.append_match_flag(str_0, bool_0, complex_0, list_0)

def test_case_5():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    float_0 = 2068.6005
    var_0 = module_0.append_tcp_flags(bool_0, set_0, float_0)

def test_case_6():
    dict_0 = {}
    bytes_0 = b'~\x0e\xcb\xba\xed\xb6$\xe6\x0f\x80\xdf\xfe\rP\x02'
    float_0 = 453.986
    var_0 = module_0.append_param(dict_0, dict_0, bytes_0, float_0)
    str_0 = 'X-=z`XU*i)a%z`'
    tuple_0 = ()
    list_0 = None
    var_1 = module_0.append_jump(tuple_0, list_0, float_0)
    bool_0 = False
    list_1 = [bool_0, bool_0]
    str_1 = 'kZ\x0c&'
    tuple_1 = (float_0, str_1, bool_0)
    var_2 = module_0.append_match_flag(tuple_1, str_1, list_1, str_0)

def test_case_7():
    var_0 = []
    str_0 = 'match'
    str_1 = '--syn'
    bool_0 = True
    var_1 = module_0.append_match_flag(var_0, str_0, str_1, bool_0)
    str_2 = 'negate'
    var_2 = module_0.append_match_flag(var_0, str_2, str_1, bool_0)

def test_case_8():
    str_0 = 'iptables'
    str_1 = [str_0]
    str_2 = 'ACK'
    str_3 = 'RST'
    str_4 = [str_2, str_3]
    str_5 = 'SYN'
    str_6 = 'FIN'
    str_7 = [str_5, str_6]
    var_0 = dict(flags=str_4, flags_set=str_7)
    str_8 = '--tcp-flags'
    var_1 = module_0.append_tcp_flags(str_1, var_0, str_8)
    var_2 = module_0.append_tcp_flags(str_1, str_8, str_8)