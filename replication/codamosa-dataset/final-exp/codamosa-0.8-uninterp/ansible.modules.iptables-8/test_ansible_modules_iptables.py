# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0
import ansible.module_utils.basic as module_1

def test_case_0():
    pass

def test_case_1():
    float_0 = -1063.789
    bytes_0 = b'\xbb\x12\x95\xdf\x87\x08\xe1e\xa9\xd5\xcc\xe6=|\xfa=\xc7\x861\xd8'
    list_0 = [float_0, bytes_0]
    str_0 = 'Cq`GyouH1;Ee=HDt'
    list_1 = []
    dict_0 = {}
    var_0 = module_0.append_param(list_0, str_0, list_1, dict_0)

def test_case_2():
    str_0 = 'iptables'
    str_1 = 'h&f19I ~'
    list_0 = [str_0, str_1]
    var_0 = module_0.append_tcp_flags(str_1, list_0, list_0)

def test_case_3():
    float_0 = -588.28
    str_0 = 'ansible.modules.iptables'
    bytes_0 = b'l\xa1\xd3\xb9.\\@\xbe,\xb0\xf0~'
    var_0 = module_0.append_match_flag(float_0, str_0, str_0, bytes_0)

def test_case_4():
    var_0 = module_0.main()

def test_case_5():
    str_0 = 'PREROUTING'
    bool_0 = True
    bytes_0 = b''
    var_0 = module_0.append_tcp_flags(bool_0, bytes_0, str_0)
    str_1 = '-I'
    str_2 = 'NOTRACK'
    var_1 = dict(table=str_0, chain=str_0, action=str_1, jump=str_2)
    str_3 = '-A'
    float_0 = 4838.0
    int_0 = 1061
    list_0 = []
    ansible_module_0 = module_1.AnsibleModule(int_0, list_0)
    int_1 = None
    ansible_module_1 = module_1.AnsibleModule(float_0, list_0, int_1, str_3)

def test_case_6():
    complex_0 = None
    dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
    bool_0 = True
    bytes_0 = b'\xb3:yQ\x0f\xb4\xa5#\xb6\xbcs\xcc\xc0h\x17&\xbd\xe9\x11\r'
    var_0 = module_0.append_param(complex_0, dict_0, bool_0, bytes_0)
    int_0 = -1306
    list_0 = None
    var_1 = module_0.append_match_flag(bytes_0, int_0, dict_0, list_0)

def test_case_7():
    str_0 = '--some-match'
    bool_0 = True
    var_0 = module_0.append_match_flag(bool_0, str_0, str_0, bool_0)
    var_1 = []
    str_1 = 'negate'
    var_2 = module_0.append_match_flag(var_1, str_1, str_0, bool_0)
    var_3 = []
    var_4 = None
    var_5 = module_0.append_match_flag(var_3, var_4, str_0, bool_0)
    bool_1 = False
    var_6 = []
    var_7 = module_0.append_match_flag(var_6, str_1, str_0, bool_1)

def test_case_8():
    var_0 = []
    str_0 = 'match'
    str_1 = '--some-match'
    bool_0 = True
    var_1 = module_0.append_match_flag(var_0, str_0, str_1, bool_0)
    var_2 = []
    str_2 = 'negate'
    var_3 = module_0.append_match_flag(var_2, str_2, str_1, bool_0)
    var_4 = []
    var_5 = None
    var_6 = module_0.append_match_flag(var_4, var_5, str_1, bool_0)
    var_7 = []
    bool_1 = False
    var_8 = module_0.append_match_flag(var_7, str_0, str_1, bool_1)
    var_9 = []
    var_10 = module_0.append_match_flag(var_9, str_2, str_1, bool_1)

def test_case_9():
    str_0 = 'URG'
    str_1 = 'J:5Y'
    var_0 = dict(flags=str_0, flags_set=str_0)
    var_1 = []
    var_2 = module_0.append_tcp_flags(var_1, var_0, str_1)
    str_2 = [str_0, str_0, str_0, str_0, str_0, str_1]
    var_3 = dict(flags=str_2, flags_set=str_0)