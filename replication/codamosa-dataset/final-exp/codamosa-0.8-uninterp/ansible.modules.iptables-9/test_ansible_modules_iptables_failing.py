# Automatically generated by Pynguin.
import ansible.modules.iptables as module_0

def test_case_0():
    try:
        int_0 = 8
        str_0 = 'PXQ@HHI{&t$=,vI+\x0c0P'
        tuple_0 = None
        var_0 = module_0.append_param(int_0, str_0, tuple_0, tuple_0)
    except BaseException:
        pass

def test_case_1():
    try:
        str_0 = 'match'
        str_1 = '--tcp-flags'
        bool_0 = False
        var_0 = module_0.append_match_flag(str_1, str_0, str_1, bool_0)
    except BaseException:
        pass

def test_case_2():
    try:
        int_0 = 173
        str_0 = ':f2!r c{h\x0b%qPC/g'
        bytes_0 = b's\x16\x99O\xd9`\x10\xd8*\xf0km'
        var_0 = module_0.append_match(int_0, str_0, bytes_0)
    except BaseException:
        pass

def test_case_3():
    try:
        int_0 = None
        str_0 = 'S\x0bqPZ<t\n^Gv\x0bff~J'
        str_1 = '(KR'
        var_0 = module_0.append_jump(int_0, str_0, str_1)
    except BaseException:
        pass

def test_case_4():
    try:
        str_0 = '\nkRSHs5j'
        float_0 = 1.5
        float_1 = 1649.04084
        var_0 = module_0.append_wait(str_0, float_0, float_1)
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
        int_0 = 1435
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
        set_0 = set()
        var_0 = module_0.get_chain_policy(int_0, dict_0, set_0)
    except BaseException:
        pass

def test_case_7():
    try:
        str_0 = '|/;$8 R\\Cm#/%hhXEV+d'
        str_1 = 'chain'
        bool_0 = True
        list_0 = [str_0]
        bytes_0 = b'?\x01dK\xfa\xbf\xfe\xb7'
        var_0 = module_0.append_match_flag(bool_0, str_1, list_0, bytes_0)
        str_2 = 'dBjnE\t1:,>P'
        float_0 = 192.19
        var_1 = module_0.check_present(str_2, float_0, bytes_0)
    except BaseException:
        pass

def test_case_8():
    try:
        str_0 = 'eay'
        bool_0 = True
        list_0 = [str_0, bool_0, str_0]
        bytes_0 = b'\x81\xb7\xb2fB\xc5\xff\xb4\xd2'
        var_0 = module_0.append_match_flag(bool_0, str_0, list_0, bytes_0)
        float_0 = 2524.97912
        str_1 = "P'6z+ h"
        var_1 = module_0.append_rule(list_0, float_0, str_1)
    except BaseException:
        pass

def test_case_9():
    try:
        int_0 = 8
        str_0 = 'PXQ@HHI{&t$=,vI+\x0c0P'
        tuple_0 = None
        int_1 = 400
        dict_0 = {str_0: tuple_0, str_0: int_1}
        bytes_0 = b'\xcb\xe1?\xd83M\xf4j\xa5\x0c\xa5F\x19\x19\x10\xb0\x1c\x9a\xf4'
        bool_0 = True
        var_0 = module_0.append_match_flag(int_1, dict_0, bytes_0, bool_0)
        var_1 = module_0.append_tcp_flags(int_0, str_0, str_0)
        float_0 = 3806.8088
        var_2 = module_0.insert_rule(float_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_10():
    try:
        str_0 = 'ansible.modules.iptables'
        bytes_0 = b'\xa9\xfe\xce\xdc'
        str_1 = '{Y/+Noe#T/J1'
        var_0 = module_0.remove_rule(str_0, bytes_0, str_1)
    except BaseException:
        pass

def test_case_11():
    try:
        str_0 = '|/;$8 RCm#/%hhzXEV+d'
        str_1 = 'chain'
        bool_0 = True
        list_0 = [str_0]
        bytes_0 = b'?dK\xfa\xbf\xfe'
        var_0 = module_0.append_match_flag(bool_0, str_1, list_0, bytes_0)
        dict_0 = {str_0: bytes_0, bytes_0: str_0, str_0: str_1}
        int_0 = 691
        var_1 = module_0.flush_table(dict_0, int_0, dict_0)
    except BaseException:
        pass

def test_case_12():
    try:
        str_0 = '__main__'
        bool_0 = None
        list_0 = []
        tuple_0 = ()
        var_0 = module_0.append_param(list_0, bool_0, tuple_0, tuple_0)
        dict_0 = {str_0: bool_0}
        var_1 = module_0.set_chain_policy(str_0, bool_0, dict_0)
    except BaseException:
        pass

def test_case_13():
    try:
        tuple_0 = ()
        bool_0 = None
        var_0 = module_0.get_iptables_version(tuple_0, bool_0)
    except BaseException:
        pass

def test_case_14():
    try:
        int_0 = 8
        str_0 = 'PXQ@HHI{&t$=,vI+\x0c0P'
        tuple_0 = None
        var_0 = module_0.append_tcp_flags(int_0, str_0, str_0)
        bytes_0 = b'\xd6d\xc0'
        int_1 = 576
        var_1 = module_0.append_csv(tuple_0, bytes_0, int_1)
    except BaseException:
        pass

def test_case_15():
    try:
        int_0 = 8
        str_0 = 'PXQ@HHI{&t$=,vI+\x0c0P'
        tuple_0 = None
        var_0 = module_0.append_tcp_flags(int_0, str_0, str_0)
        set_0 = {int_0}
        var_1 = module_0.append_match(set_0, tuple_0, tuple_0)
        str_1 = 'z!mUk\\'
        str_2 = '9#(Ouen0SI=Yky)q}eYR'
        str_3 = '~*'
        bool_0 = False
        var_2 = module_0.append_param(str_1, str_2, str_3, bool_0)
    except BaseException:
        pass

def test_case_16():
    try:
        var_0 = []
        str_0 = 'flags'
        str_1 = 'flags_set'
        str_2 = 'ACK'
        str_3 = 'RST'
        str_4 = 'SYN'
        str_5 = [str_2, str_3, str_4]
        str_6 = [str_5]
        str_7 = {str_0: str_5, str_1: str_6}
        var_1 = module_0.append_tcp_flags(var_0, str_7, str_2)
    except BaseException:
        pass

def test_case_17():
    try:
        str_0 = '-A'
        str_1 = 'table'
        str_2 = 'chain'
        str_3 = 'protocol'
        str_4 = 'rule_num'
        str_5 = 'source'
        str_6 = 'jump'
        str_7 = 'filter'
        str_8 = 'INPUT'
        var_0 = None
        str_9 = '127.0.0.1'
        str_10 = 'ACCEPT'
        var_1 = {str_1: str_7, str_2: str_8, str_3: str_3, str_4: var_0, str_5: str_9, str_6: str_10}
        var_2 = module_0.push_arguments(str_4, str_0, var_1)
    except BaseException:
        pass

def test_case_18():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = {str_0: str_1, str_1: str_1}
        var_0 = module_0.get_chain_policy(str_0, str_2, str_2)
    except BaseException:
        pass

def test_case_19():
    try:
        str_0 = '!/{yw4XqMjs+'
        bool_0 = True
        list_0 = [str_0]
        float_0 = -2849.877817
        list_1 = [float_0, list_0]
        var_0 = module_0.append_param(bool_0, list_0, float_0, list_1)
    except BaseException:
        pass

def test_case_20():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'this-chain-does-not-exist'
        str_3 = 'INPUT'
        int_0 = -1612
        list_0 = [str_2]
        bytes_0 = b'4&o\xb0@\x12I\x0e'
        var_0 = module_0.append_match_flag(int_0, int_0, list_0, bytes_0)
        str_4 = {str_0: str_2, str_1: str_3}
        ansible_module_0 = None
        dict_0 = {bytes_0: list_0}
        var_1 = module_0.flush_table(ansible_module_0, dict_0, str_4)
    except BaseException:
        pass

def test_case_21():
    try:
        str_0 = 'INPUT'
        str_1 = 'FORWARD'
        str_2 = '-I'
        str_3 = 'table'
        str_4 = 'chain'
        str_5 = 'action'
        str_6 = {str_3: str_0, str_4: str_1, str_5: str_2}
        str_7 = 'iptables'
        bool_0 = True
        var_0 = module_0.push_arguments(str_7, str_2, str_6, bool_0)
    except BaseException:
        pass

def test_case_22():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'protocol'
        str_3 = 'jump'
        str_4 = 'rule_num'
        str_5 = 'filter'
        str_6 = 'INPUT'
        str_7 = 'tcp'
        str_8 = 'ACCEPT'
        str_9 = '5'
        str_10 = {str_0: str_5, str_1: str_6, str_2: str_7, str_8: str_4, str_3: str_8, str_4: str_9}
        str_11 = 'iptables'
        str_12 = '-I'
        var_0 = module_0.push_arguments(str_11, str_12, str_10)
    except BaseException:
        pass

def test_case_23():
    try:
        str_0 = 'table'
        str_1 = 'chain'
        str_2 = 'protocol'
        str_3 = 'destination_port'
        str_4 = 'jump'
        str_5 = 'rule_num'
        str_6 = 'filter'
        str_7 = 'INPUT'
        str_8 = 'tcp'
        str_9 = '8080'
        str_10 = 'ACCEPT'
        str_11 = ''
        str_12 = {str_0: str_6, str_1: str_7, str_2: str_8, str_3: str_9, str_4: str_10, str_5: str_11}
        str_13 = 'iptables'
        str_14 = '-I'
        list_0 = None
        float_0 = 192.19
        list_1 = []
        str_15 = 'MJDRkz?ucqI'
        var_0 = module_0.append_match_flag(list_0, float_0, list_1, str_15)
        var_1 = module_0.push_arguments(str_13, str_14, str_12)
    except BaseException:
        pass

def test_case_24():
    try:
        str_0 = 'ansible.module_utils.basic'
        str_1 = 'IPTABLES'
        str_2 = 'iptables'
        str_3 = 'INPUT'
        str_4 = 'ACCEPT'
        var_0 = dict(chain=str_3, table=str_2, policy=str_4)
        var_1 = module_0.set_chain_policy(str_1, str_0, var_0)
    except BaseException:
        pass