# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        int_0 = None
        float_0 = -1148.529943
        dict_0 = {float_0: float_0}
        var_0 = module_0.append_match_flag(float_0, float_0, dict_0, int_0)
        bytes_0 = b'f\\\xba\xae\x0e\x95D.O?\xb7K\xa8+\x19e\xd7'
        str_0 = 'tyJ\n'
        set_0 = None
        var_1 = module_0.append_csv(bytes_0, str_0, set_0)
    except BaseException:
        pass

def test_case_1():
    try:
        bytes_0 = b'\x15\x14\xa0i\xb2\xe7\x12\xcd\xe4\xb30'
        str_0 = 'QBf'
        int_0 = 1090
        var_0 = module_0.append_match(bytes_0, str_0, int_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bool_0 = True
        str_0 = 'D]z'
        list_0 = []
        var_0 = module_0.append_wait(bool_0, str_0, list_0)
    except BaseException:
        pass

def test_case_3():
    try:
        str_0 = '-I'
        str_1 = 'filter'
        str_2 = 'INPUT'
        int_0 = 1
        str_3 = 'test rule'
        var_0 = dict(table=str_1, chain=str_2, rule_num=int_0, protocol=str_3, source=str_1, comment=str_3)
        var_1 = module_0.push_arguments(str_1, str_0, var_0)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '__main__'
        bool_0 = True
        bytes_0 = b'z\xe0\x12\xb1\xd1'
        var_0 = module_0.flush_table(str_0, bool_0, bytes_0)
    except BaseException:
        pass

def test_case_5():
    try:
        str_0 = '__main__'
        list_0 = []
        int_0 = 593
        var_0 = module_0.check_present(str_0, list_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        bytes_0 = b'L\x07\x15>\x005-\xc5'
        tuple_0 = None
        var_0 = module_0.append_rule(bytes_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_7():
    try:
        bool_0 = True
        set_0 = set()
        bytes_0 = b'|\ti#\xc7\xd52\xee\x82Hj\xd5\x7f|\xd6\xd2\xcd'
        var_0 = module_0.insert_rule(bool_0, set_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = ':#1|T])|%=7h~\x0c8]'
        str_1 = '%^~*e;RX'
        dict_0 = {str_0: str_0, str_1: str_0}
        var_0 = module_0.append_match_flag(str_0, str_1, str_1, dict_0)
        int_0 = 3934
        bytes_0 = None
        set_0 = set()
        tuple_0 = (int_0, bytes_0, set_0)
        var_1 = module_0.remove_rule(tuple_0, bytes_0, dict_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = 'pzImhX=*w{'
        float_0 = -842.0
        int_0 = -2869
        set_0 = {str_0, float_0, str_0, int_0}
        var_0 = module_0.set_chain_policy(int_0, set_0, set_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bytes_0 = b'\xc6\xa0\xed\xe7Q\x8dv\x9a'
        set_0 = None
        var_0 = module_0.get_iptables_version(bytes_0, set_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '/sbin/iptables'
        float_0 = 1270.17
        str_1 = '2LL'
        bytes_0 = b'L\x00\xdc\x8d\xcd\r\x11%\x02'
        dict_0 = {str_1: bytes_0, str_1: float_0}
        list_0 = [str_1, str_1, str_0]
        float_1 = None
        int_0 = 3285
        var_0 = module_0.append_csv(list_0, float_1, int_0)
        var_1 = module_0.append_match_flag(float_0, str_1, bytes_0, dict_0)
        str_2 = '-I'
        str_3 = 'filter'
        str_4 = '5'
        str_5 = 'tcp'
        str_6 = 'ACCEPT'
        var_2 = dict(table=str_3, chain=str_2, rule_num=str_4, protocol=str_5, destination_port=str_6, jump=str_6)
        var_3 = module_0.push_arguments(str_0, str_2, var_2)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = 'iptables'
        var_0 = None
        str_1 = 'filter'
        str_2 = 'i`nput'
        var_1 = dict(table=str_1, chain=str_2, policy=var_0)
        var_2 = module_0.get_chain_policy(str_0, var_0, var_1)
    except BaseException:
        pass

def test_case_13():
    try:
        str_0 = 'mZP'
        int_0 = 535000
        bytes_0 = b'\xa4\x8d\xe3\xcc\x1c'
        var_0 = module_0.append_jump(str_0, int_0, bytes_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = '^/.*|^[a-zA-Z].*|^[0-9].*'
        float_0 = -628.2265
        list_0 = [float_0, str_0, float_0, float_0]
        list_1 = [float_0, float_0]
        var_0 = module_0.append_param(str_0, float_0, list_0, list_1)
    except BaseException:
        pass

def test_case_15():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        str_0 = 'ansible.modules.iptables'
        bytes_0 = b"'m\xb5\x92H7\xf4;\xbe\x0b\xbc\xc3[\xc2"
        float_0 = -237.0
        tuple_0 = (list_0, float_0)
        tuple_1 = (tuple_0, str_0)
        bool_1 = False
        int_0 = 1789
        dict_0 = {int_0: bool_1}
        var_0 = module_0.append_wait(tuple_1, bool_1, dict_0)
        var_1 = module_0.set_chain_policy(list_0, bytes_0, bytes_0)
    except BaseException:
        pass

def test_case_16():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        str_0 = ':#1|T])|%=7h~\x0c8]'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.append_match_flag(str_0, str_0, str_0, dict_0)
        bytes_0 = None
        set_0 = set()
        var_1 = module_0.append_tcp_flags(set_0, list_0, bool_0)
        str_1 = '\'"!cXcb(wbG&NZF'
        var_2 = module_0.append_tcp_flags(set_0, str_1, dict_0)
        var_3 = module_0.append_tcp_flags(dict_0, bool_0, set_0)
        str_2 = 'K9e3>3\r0= 0fw6F|E'
        str_3 = 'role_path'
        var_4 = module_0.append_param(bytes_0, dict_0, str_3, str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '^/.*|^[a-zA-Z].*|^[0-9].*'
        bool_0 = False
        int_0 = 3144
        var_0 = module_0.append_param(str_0, str_0, bool_0, int_0)
    except BaseException:
        pass

def test_case_18():
    try:
        dict_0 = None
        list_0 = [dict_0, dict_0]
        bytes_0 = b'k\x19j_\x8a\xe97\x1a\xca\xbc\xb4\x07.\x99'
        float_0 = 1169.652
        tuple_0 = (list_0, float_0, list_0)
        var_0 = module_0.append_match(bytes_0, dict_0, tuple_0)
    except BaseException:
        pass

def test_case_19():
    try:
        tuple_0 = ()
        int_0 = 2722
        var_0 = module_0.append_jump(tuple_0, tuple_0, int_0)
        str_0 = '^/.*|^[a-zA-Z].*|^[0-9].'
        float_0 = -628.2265
        list_0 = [float_0, str_0, float_0, float_0]
        str_1 = 'nj,vZf;S,D(Q_a5'
        bool_0 = True
        tuple_1 = ()
        var_1 = module_0.append_param(bool_0, str_1, tuple_1, list_0)
    except BaseException:
        pass

def test_case_20():
    try:
        bool_0 = False
        list_0 = [bool_0, bool_0]
        str_0 = 'Invalid type supplied for source option, it must be a string'
        dict_0 = {str_0: str_0, str_0: str_0}
        var_0 = module_0.append_match_flag(str_0, str_0, str_0, dict_0)
        set_0 = set()
        var_1 = module_0.append_tcp_flags(set_0, list_0, set_0)
        bytes_0 = b'\xef\xb9\x19*\x86\xb3\xc8T\x97\xf4'
        str_1 = '!'
        bool_1 = None
        var_2 = module_0.append_param(bytes_0, str_1, str_1, bool_1)
    except BaseException:
        pass

def test_case_21():
    try:
        var_0 = []
        var_1 = None
        var_2 = module_0.append_tcp_flags(var_0, var_1, var_1)
        var_3 = []
        var_4 = {}
        var_5 = module_0.append_tcp_flags(var_3, var_4, var_1)
        str_0 = 'flags'
        var_6 = {str_0: var_1}
        var_7 = module_0.append_tcp_flags(var_4, var_6, var_1)
        var_8 = []
        str_1 = 'flags_set'
        var_9 = {str_1: var_1}
        var_10 = module_0.append_tcp_flags(var_8, var_9, var_1)
        var_11 = []
        var_12 = {str_0: var_1, str_1: var_1}
        var_13 = module_0.append_tcp_flags(var_11, var_12, var_1)
    except BaseException:
        pass

def test_case_22():
    try:
        var_0 = {}
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'policy'
        str_3 = 'filter'
        str_4 = 'ACCEPT'
        str_5 = {str_0: str_3, str_1: str_4, str_2: str_4}
        var_1 = module_0.set_chain_policy(str_0, var_0, str_5)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = '/sbin/iptables'
        float_0 = 1270.17
        str_1 = '2L`L'
        bytes_0 = b'LL\x00\xdc\x8d\xcd\r\x11%\x02'
        dict_0 = {str_1: bytes_0, str_1: float_0}
        var_0 = module_0.append_match_flag(float_0, str_1, bytes_0, dict_0)
        str_2 = '-I'
        str_3 = 'filter'
        str_4 = ''
        str_5 = 'tcp'
        str_6 = 'ACCEPT'
        var_1 = dict(table=str_3, chain=str_2, rule_num=str_4, protocol=str_5, destination_port=str_6, jump=str_6)
        var_2 = module_0.push_arguments(str_0, str_2, var_1)
    except BaseException:
        pass