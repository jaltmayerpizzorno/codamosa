# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        bool_0 = True
        tuple_0 = (bool_0,)
        str_0 = 'CA|\x0b%Uk.'
        int_0 = 3101
        var_0 = module_0.append_param(tuple_0, str_0, tuple_0, int_0)
    except BaseException:
        pass

def test_case_1():
    try:
        dict_0 = None
        bytes_0 = b'w\r\x9d\xea\xcbk\xe3\x7f6L<i\xd8>\xe2\x1aR8'
        bool_0 = True
        dict_1 = {dict_0: bytes_0, dict_0: dict_0, bool_0: bool_0}
        list_0 = [dict_1]
        var_0 = module_0.append_csv(dict_1, list_0, list_0)
    except BaseException:
        pass

def test_case_2():
    try:
        bytes_0 = None
        str_0 = '__main__'
        dict_0 = {bytes_0: str_0, bytes_0: bytes_0, str_0: bytes_0}
        var_0 = module_0.append_jump(bytes_0, str_0, dict_0)
    except BaseException:
        pass

def test_case_3():
    try:
        list_0 = None
        set_0 = {list_0}
        list_1 = [set_0, set_0]
        var_0 = module_0.append_wait(list_0, set_0, list_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = ''
        var_0 = dict(table=str_0, chain=str_0, protocol=str_0, destination_port=str_0, jump=str_0, comment=str_0)
        var_1 = lambda x, **kw: str_0
        var_2 = module_0.check_present(str_0, str_0, var_0)
    except BaseException:
        pass

def test_case_5():
    try:
        bool_0 = True
        set_0 = {bool_0, bool_0, bool_0}
        int_0 = 127
        var_0 = module_0.check_present(bool_0, set_0, int_0)
    except BaseException:
        pass

def test_case_6():
    try:
        set_0 = None
        set_1 = {set_0}
        list_0 = [set_1]
        tuple_0 = (list_0,)
        float_0 = -2833.21537
        var_0 = module_0.append_rule(tuple_0, tuple_0, float_0)
    except BaseException:
        pass

def test_case_7():
    try:
        float_0 = 6121.0
        list_0 = [float_0]
        int_0 = 3101
        dict_0 = {float_0: list_0, float_0: int_0, float_0: int_0}
        int_1 = 632
        var_0 = module_0.append_match_flag(list_0, int_0, dict_0, int_1)
        str_0 = None
        str_1 = 'OH'
        var_1 = module_0.insert_rule(float_0, str_0, str_1)
    except BaseException:
        pass

def test_case_8():
    try:
        tuple_0 = ()
        bytes_0 = b'\xf6\x93\xfd\xc3\xb1+\xb0\xc0K\xdf'
        bool_0 = True
        var_0 = module_0.remove_rule(tuple_0, bytes_0, bool_0)
    except BaseException:
        pass

def test_case_9():
    try:
        str_0 = '/usr/bin/iptables'
        str_1 = ''
        str_2 = 'nat'
        str_3 = 'OUTPUT'
        var_0 = dict(table=str_2, chain=str_3)
        var_1 = module_0.flush_table(str_0, str_1, var_0)
    except BaseException:
        pass

def test_case_10():
    try:
        bool_0 = True
        float_0 = -1992.52837
        var_0 = module_0.set_chain_policy(bool_0, bool_0, float_0)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = 'eN'
        float_0 = -1438.65095
        float_1 = 145.0
        var_0 = module_0.get_chain_policy(str_0, float_0, float_1)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '"gF&y3&^kj\rp;Nt%MvIl'
        set_0 = {str_0, str_0}
        var_0 = module_0.get_iptables_version(str_0, set_0)
    except BaseException:
        pass

def test_case_13():
    try:
        dict_0 = {}
        bytes_0 = b'\xad'
        bool_0 = True
        list_0 = [bytes_0, bool_0]
        var_0 = module_0.append_match(bool_0, list_0, dict_0)
    except BaseException:
        pass

def test_case_14():
    try:
        str_0 = 'rGvI.y\tVL}0Eqnz{s$EZ'
        dict_0 = {str_0: str_0, str_0: str_0}
        list_0 = [dict_0]
        set_0 = None
        var_0 = module_0.append_match_flag(dict_0, str_0, list_0, set_0)
        float_0 = -2474.0
        bool_0 = True
        tuple_0 = ()
        bytes_0 = b'\n\xc0\x13\xb3\xd1\xe8l\x8c\xc4\xe9NF\xe1\xf0H\x83\xce'
        var_1 = module_0.append_wait(bool_0, tuple_0, bytes_0)
        str_1 = "T'm54U74VTrDO"
        list_1 = []
        str_2 = 'match'
        var_2 = module_0.append_csv(str_1, list_1, str_2)
        str_3 = '!'
        int_0 = 48
        var_3 = module_0.append_param(float_0, str_3, int_0, str_3)
    except BaseException:
        pass

def test_case_15():
    try:
        str_0 = '/sbin/iptables'
        str_1 = '5Wfitr'
        float_0 = -521.35112
        set_0 = set()
        var_0 = module_0.append_tcp_flags(float_0, set_0, set_0)
        str_2 = '}2Ms<*/'
        var_1 = None
        var_2 = dict(table=str_1, chain=str_0, protocol=str_2, destination_port=str_2, jump=var_1, comment=str_0)
        var_3 = lambda x, **kw: var_1
        var_4 = dict(run_command=var_3)
        var_5 = module_0.check_present(str_0, var_4, var_2)
    except BaseException:
        pass

def test_case_16():
    try:
        str_0 = '/sbin/iptables'
        str_1 = '-I'
        str_2 = 'chain'
        str_3 = 'rule_num'
        str_4 = 'table'
        str_5 = 'protocol'
        str_6 = 'jump'
        str_7 = 'tcp'
        str_8 = 'ipv4'
        str_9 = {str_2: str_6, str_3: str_8, str_4: str_8, str_5: str_7, str_8: str_6, str_6: str_1, str_6: str_8}
        var_0 = module_0.push_arguments(str_0, str_1, str_9)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '/sbin/iptable?'
        str_1 = '-I'
        str_2 = 'chain'
        str_3 = 'rule_num'
        str_4 = 'table'
        str_5 = 'protocol'
        str_6 = 'jump'
        str_7 = 'ip_version'
        str_8 = 'INPUT'
        str_9 = ''
        str_10 = 'filter'
        str_11 = 'tcp'
        str_12 = 'ACCEPT'
        str_13 = 'ipv'
        str_14 = {str_2: str_8, str_6: str_9, str_3: str_9, str_4: str_10, str_5: str_11, str_6: str_12, str_7: str_13}
        var_0 = module_0.push_arguments(str_0, str_1, str_14)
    except BaseException:
        pass