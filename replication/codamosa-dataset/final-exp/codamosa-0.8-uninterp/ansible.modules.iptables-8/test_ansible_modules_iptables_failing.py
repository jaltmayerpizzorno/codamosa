# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        bool_0 = False
        bytes_0 = b'\xb3:yQ\x0f\xb4\xa5#\xb6\xbcs\xcc\xc0h\x17&\xbd\xe9\x11\r'
        var_0 = module_0.append_param(complex_0, dict_0, bool_0, bytes_0)
        bool_1 = False
        bool_2 = True
        tuple_0 = (complex_0, bool_1, bool_2)
        str_0 = '8(K/3nCn$-`EI~S5;'
        var_1 = module_0.push_arguments(tuple_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x03G\x9e\x8e\xde\xde\xd2\xc0(\x9c'
        tuple_0 = None
        complex_0 = None
        list_0 = [complex_0]
        var_0 = module_0.append_csv(tuple_0, complex_0, list_0)
        str_0 = None
        bool_0 = False
        var_1 = module_0.set_chain_policy(str_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_2():
    try:
        str_0 = '5 9U \\%-tdVX'
        list_0 = [str_0, str_0, str_0, str_0]
        list_1 = [list_0, list_0, str_0, list_0]
        str_1 = 'zFr.ZhsU6/K\t['
        dict_0 = {str_1: str_1}
        tuple_0 = (dict_0,)
        bool_0 = False
        var_0 = module_0.append_param(list_1, str_1, tuple_0, bool_0)
        str_2 = '--reference'
        var_1 = module_0.append_match(str_0, list_0, str_2)
    except BaseException:
        pass

def test_case_3():
    try:
        bool_0 = True
        float_0 = 555.28616
        set_0 = {bool_0, bool_0, float_0}
        var_0 = module_0.append_jump(float_0, bool_0, set_0)
    except BaseException:
        pass

def test_case_4():
    try:
        set_0 = None
        str_0 = 'B7<|WRWi'
        float_0 = -351.3
        str_1 = 'hKy27+'
        str_2 = "Invalid value given for 'boot_time_command': %s."
        int_0 = None
        bytes_0 = b'\xb2\x06\x02\xa6I\x0c +\x88w'
        var_0 = module_0.append_match_flag(str_1, str_2, int_0, bytes_0)
        dict_0 = {float_0: str_0, float_0: set_0, str_0: str_0}
        list_0 = [dict_0, dict_0, dict_0, set_0]
        var_1 = module_0.append_wait(float_0, dict_0, list_0)
    except BaseException:
        pass

def test_case_5():
    try:
        float_0 = None
        var_0 = module_0.construct_rule(float_0)
    except BaseException:
        pass

def test_case_6():
    try:
        str_0 = '*}>7(-A G~9nf5'
        str_1 = '\r]UqL[JZ'
        var_0 = module_0.check_present(str_0, str_1, str_1)
    except BaseException:
        pass

def test_case_7():
    try:
        set_0 = set()
        int_0 = -187
        var_0 = module_0.append_rule(set_0, int_0, set_0)
    except BaseException:
        pass

def test_case_8():
    try:
        complex_0 = None
        dict_0 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        bool_0 = True
        bytes_0 = b'\xb3:yQ\x0f\xb4\xa5#\xb6\xbcs\xcc\xc0h\x17&\xbd\xe9\x11\r'
        var_0 = module_0.append_param(complex_0, dict_0, bool_0, bytes_0)
        str_0 = "Invalid value given for 'boot_time_command': %s."
        var_1 = module_0.insert_rule(str_0, dict_0, str_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'test'
        str_1 = 'module'
        str_2 = 'table'
        str_3 = 'chain'
        str_4 = 'rule_num'
        str_5 = {str_2: str_0, str_3: str_0, str_4: str_0}
        var_0 = module_0.remove_rule(str_0, str_1, str_5)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        int_0 = 10
        var_0 = module_0.flush_table(bool_0, int_0, int_0)
    except BaseException:
        pass

def test_case_11():
    try:
        var_0 = None
        str_0 = 'INPUT'
        str_1 = 'ipv4'
        var_1 = dict(chain=str_0, policy=str_1, table=str_0, ip_version=str_1, wait=var_0)
        var_2 = module_0.set_chain_policy(str_0, var_0, var_1)
    except BaseException:
        pass

def test_case_12():
    try:
        bytes_0 = b'<6E\x00k\xae\xbe\x10\xd4{\xb5\x85'
        str_0 = '\nN{F='
        int_0 = 83
        var_0 = module_0.get_chain_policy(bytes_0, str_0, int_0)
    except BaseException:
        pass

def test_case_13():
    try:
        bytes_0 = b'\xc3%\x0f#\xc1\xe1\xa8\x83\xca'
        list_0 = [bytes_0]
        str_0 = 'ansible.modules.iptables'
        bool_0 = False
        int_0 = -1062
        tuple_0 = (list_0, str_0, bool_0, int_0)
        var_0 = module_0.get_iptables_version(tuple_0, list_0)
    except BaseException:
        pass

def test_case_14():
    try:
        bytes_0 = None
        tuple_0 = (bytes_0,)
        int_0 = 1881
        var_0 = module_0.append_jump(tuple_0, bytes_0, int_0)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 2305
        bytes_0 = b''
        dict_0 = {}
        dict_1 = {bytes_0: dict_0, int_0: dict_0, int_0: int_0, bytes_0: int_0}
        str_0 = ''
        str_1 = 'cOdN{}lX{UjQq5,6j1,'
        bool_0 = True
        var_0 = module_0.append_match_flag(dict_1, str_0, str_1, bool_0)
        tuple_0 = ()
        float_0 = 4635.843106
        complex_0 = None
        dict_2 = {complex_0: complex_0, complex_0: complex_0, complex_0: complex_0}
        bool_1 = False
        bytes_1 = b'\x9a\xcd\xf3/\xb5_\xdc\xb7\xa9r\xa8TD\x03\x1c'
        var_1 = module_0.append_param(complex_0, dict_2, bool_1, bytes_1)
        float_1 = -458.1699
        var_2 = module_0.append_match(float_0, bool_1, float_1)
        var_3 = module_0.get_iptables_version(tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_16():
    try:
        set_0 = set()
        str_0 = '9\x0bmh4K#BpnsT}'
        var_0 = module_0.append_wait(set_0, set_0, str_0)
        int_0 = -3347
        tuple_0 = ()
        var_1 = module_0.append_csv(int_0, int_0, tuple_0)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = 'NOTRACK'
        var_0 = dict(table=str_0, chain=str_0, action=str_0, jump=str_0)
        str_1 = 'iptables'
        var_1 = module_0.push_arguments(str_1, str_0, var_0)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = '-I'
        str_1 = 'NOTRACK'
        var_0 = dict(table=str_0, chain=str_0, action=str_0, jump=str_1)
        str_2 = 'iptables'
        var_1 = module_0.push_arguments(str_2, str_0, var_0)
    except BaseException:
        pass